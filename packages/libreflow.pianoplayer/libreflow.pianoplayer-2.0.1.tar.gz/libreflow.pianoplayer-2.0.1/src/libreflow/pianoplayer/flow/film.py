import os
import shutil
import re

from kabaret import flow
from kabaret.flow_entities.entities import Entity

from libreflow.utils.kabaret.flow_entities.entities import EntityView
from libreflow.baseflow.maputils import SimpleCreateAction
from libreflow.baseflow.file import CreateDefaultFilesAction
from libreflow.baseflow.departments import Department
from libreflow.baseflow.users import ToggleBookmarkAction

from .file import FileSystemMap
from .packaging import PackAction


class CreateDepartmentDefaultFilesAction(CreateDefaultFilesAction):

    _department = flow.Parent()

    def get_target_groups(self):
        return [self._department.name()]

    def get_file_map(self):
        return self._department.files


class Department(flow.Object):

    _short_name = flow.Param()

    toggle_bookmark = flow.Child(ToggleBookmarkAction)

    files = flow.Child(FileSystemMap).ui(
        expanded=True,
        action_submenus=True,
        items_action_submenus=True
    )

    create_default_files = flow.Child(CreateDepartmentDefaultFilesAction)
    
    def get_default_contextual_edits(self, context_name):
        if context_name == 'settings':
            return dict(
                department=self.name(),
                department_short_name=self._short_name.get() if self._short_name.get() is not None else self.name(),
            )


class CleanDepartment(Department):

    _short_name = flow.Param('cln')


class CompDepartment(Department):

    _short_name = flow.Param('comp')


class MiscDepartment(Department):

    pack = flow.Child(PackAction).ui(label='Create package')

    _short_name = flow.Param('misc')
    _label = flow.Param()

    def _fill_ui(self, ui):
        label = self._label.get()
        if label:
            ui['label'] = label


class ShotDepartments(flow.Object):

    misc        = flow.Child(MiscDepartment)
    clean       = flow.Child(CleanDepartment).ui(label='Clean-up')
    compositing = flow.Child(CompDepartment)


class Shot(Entity):

    ICON = ('icons.flow', 'shot')

    departments = flow.Child(ShotDepartments).ui(expanded=True)

    def get_default_contextual_edits(self, context_name):
        if context_name == 'settings':
            return dict(shot=self.name())


class Shots(EntityView):

    ICON = ('icons.flow', 'shot')

    create_shot = flow.Child(SimpleCreateAction)
    
    @classmethod
    def mapped_type(cls):
        return Shot
    
    def collection_name(self):
        mgr = self.root().project().get_entity_manager()
        return mgr.shots.collection_name()


class Sequence(Entity):

    ICON = ('icons.flow', 'sequence')

    shots = flow.Child(Shots).ui(
        expanded=True, 
        show_filter=True
    )

    def get_default_contextual_edits(self, context_name):
        if context_name == 'settings':
            return dict(sequence=self.name())


class Sequences(EntityView):

    ICON = ('icons.flow', 'sequence')

    create_sequence = flow.Child(SimpleCreateAction)
    
    @classmethod
    def mapped_type(cls):
        return Sequence
    
    def collection_name(self):
        mgr = self.root().project().get_entity_manager()
        return mgr.sequences.collection_name()


class CreateShotPackagesAction(flow.Action):
    '''
    This action allows to package folders into existing shots.

    It uses the following parameters in the current site:
      - `package_source_dir`: location of the folders to pack
      - `package_target_dir`: location where each folder will
      be moved after packing

    A folder is packed as a tracked folder. The target shot
    name is extracted performing a match between the folder
    name and the regular expression `shot_name_regex`. Thus,
    only folders with names matching this parameter will be
    available for packing.

    Each package is requested toward all sites whose names are
    provided in the `target_sites` param of the current site.
    '''

    ICON = ('icons.gui', 'package')

    shot_name_regex = flow.Param('[^_]*_(c\d{3})_(s\d{3})').ui(editable=False, hidden=True)

    _default_department = flow.Param('misc').ui(editable=False, hidden=True)
    _default_pkg_name   = flow.Param('sources').ui(editable=False, hidden=True)

    _film = flow.Parent()

    def get_buttons(self):
        return ['Create packages', 'Cancel']
    
    def extract_shots_data(self):
        site = self.root().project().get_current_site()
        src_dir = site.package_source_dir.get()
        data = []

        if src_dir is not None:
            regex = self.shot_name_regex.get()
            
            for dir_name in sorted(next(os.walk(src_dir))[1]):
                m = re.search(regex, dir_name, re.IGNORECASE)

                if m is not None:
                    data.append({
                        'sequence': m.group(1).lower(),
                        'shot': m.group(2).lower(),
                        'name': dir_name,
                        'source_path': os.path.join(src_dir, dir_name).replace('\\', '/'),
                        'comment': None,
                        'default_comment': f'Packed from source folder {dir_name}'
                    })
        
        return data
    
    def _ensure_package_revision(self, sequence_name, shot_name, dept_name, package_name, comment):
        revision = None

        try:
            file_map = self.root().get_object(
                f'{self._film.oid()}/sequences/{sequence_name}/shots/{shot_name}/departments/{dept_name}/files'
            )
        except:
            pass
        else:
            if not file_map.has_folder(package_name):
                file_map.create_folder_action.folder_name.set(package_name)
                file_map.create_folder_action.tracked.set(True)
                file_map.create_folder_action.run('Create')
        
            revision = file_map[package_name].add_revision(comment=comment)
        
        return revision
    
    def _submit_upload(self, revision):
        current_site = self.root().project().get_current_site()
        job = current_site.get_queue().submit_job(
            job_type='Upload',
            init_status='WAITING',
            emitter_oid=revision.oid(),
            user=self.root().project().get_user_name(),
            studio=current_site.name(),
        )

        for site_name in current_site.target_sites.get():
            sites = self.root().project().get_working_sites()
            try:
                site = sites[site_name]
            except flow.exceptions.MappedNameError:
                continue
            else:
                site.get_queue().submit_job(
                    job_type='Download',
                    init_status='WAITING',
                    emitter_oid=revision.oid(),
                    user=self.root().project().get_user_name(),
                    studio=site_name,
                )
                revision.set_sync_status('Requested', site_name=site_name)

        self.root().project().get_sync_manager().process(job)
    
    def create_shot_packages(self, shots_data, dept_name=None, package_name=None):
        site = self.root().project().get_current_site()
        dst_dir = site.package_target_dir.get()

        if dept_name is None:
            dept_name = self._default_department.get()
        if package_name is None:
            package_name = self._default_pkg_name.get()

        for data in shots_data:
            sequence = data['sequence']
            shot = data['shot']
            source_folder = data['name']
            r = self._ensure_package_revision(sequence, shot, dept_name, package_name, data['comment'] or data['default_comment'])

            if r is not None:
                target_path = r.get_path()

                if os.path.exists(target_path):
                    shutil.rmtree(target_path)
                
                shutil.copytree(data['source_path'], target_path)
                print(f'{source_folder} :: Package created: {target_path}')
                self._submit_upload(r)
                print(f'{source_folder} :: Package uploaded')

                if dst_dir is not None:
                    shutil.move(data['source_path'], dst_dir)
                    print(f'{source_folder} :: Source folders moved to {dst_dir}')
            else:
                print(f'{source_folder} :: Shot does not exist in the project')
    
    def _fill_ui(self, ui):
        ui['custom_page'] = 'libreflow.pianoplayer.ui.packaging.CreateShotPackagesWidget'


class Film(Entity):

    ICON = ('icons.flow', 'film')

    sequences = flow.Child(Sequences).ui(
        expanded=True,
        show_filter=True
    )
    create_packages = flow.Child(CreateShotPackagesAction)
    
    def get_default_contextual_edits(self, context_name):
        if context_name == 'settings':
            return dict(film=self.name())


class Films(EntityView):

    ICON = ('icons.flow', 'film')

    create_film = flow.Child(SimpleCreateAction)

    @classmethod
    def mapped_type(cls):
        return Film
    
    def collection_name(self):
        return self.root().project().get_entity_manager().films.collection_name()
