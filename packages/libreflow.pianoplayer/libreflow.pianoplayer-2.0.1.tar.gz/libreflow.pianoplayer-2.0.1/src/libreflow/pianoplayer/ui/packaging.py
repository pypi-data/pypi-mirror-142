from kabaret.app.ui.gui.widgets.flow.flow_view import CustomPageWidget, QtWidgets, QtCore, QtGui
from kabaret.app import resources

from ..resources.icons import gui as _


class ShotItem(QtWidgets.QTreeWidgetItem):
    
    def __init__(self, tree, shot):
        super(ShotItem, self).__init__(tree)
        self._tree = tree
        self._shot = None
        self.set_shot(shot)
    
    def set_shot(self, shot):
        self._shot = shot
        self._update()

    def _update(self):
        self.setText(0, self._shot['name'])
        self.setCheckState(0, QtCore.Qt.Unchecked)
    
    def is_selected(self):
        return self.checkState(0) == QtCore.Qt.Checked
    
    def to_dict(self):
        return self._shot


class ShotList(QtWidgets.QTreeWidget):
    
    def __init__(self, custom_widget, session):
        super(ShotList, self).__init__()
        self._custom_widget = custom_widget
        self.session = session

        self.setHeaderLabel('Source folders')
        self.header().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.header().setStretchLastSection(False)
        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        
        self.task_name_to_index = {}
        self.refresh()
    
    def sizeHint(self):
        return QtCore.QSize(300, 500)
    
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Space:
            for item in self.selectedItems():
                if item.checkState(0) == QtCore.Qt.Unchecked:
                    item.setCheckState(0, QtCore.Qt.Checked)
                else:
                    item.setCheckState(0, QtCore.Qt.Unchecked)
    
    def refresh(self):
        self.clear()

        shots_data = self._custom_widget.get_shots_data()

        for shot in shots_data:
            ShotItem(self, shot)


class CreateShotPackagesWidget(CustomPageWidget):

    def get_shots_data(self):
        return self.session.cmds.Flow.call(
            self.oid, 'extract_shots_data', [], {}
        )
    
    def create_packages(self, shots_data):
        self.session.cmds.Flow.call(
            self.oid, 'create_shot_packages', [shots_data], {}
        )

    def build(self):
        self.shot_list = ShotList(self, self.session)
        self.button_refresh = QtWidgets.QPushButton(
            QtGui.QIcon(resources.get_icon(('icons.gui', 'refresh'))), ''
        )
        self.button_refresh.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.button_refresh.setToolTip('Refresh list')
        self.checkbox_selectall = QtWidgets.QCheckBox('Select all')
        self.button_create = QtWidgets.QPushButton('Create packages')
        
        glo = QtWidgets.QGridLayout()
        glo.addWidget(self.shot_list, 0, 0, 1, 4)
        glo.addWidget(self.button_create, 1, 3)
        glo.addWidget(self.checkbox_selectall, 1, 1)
        glo.addWidget(self.button_refresh, 1, 0)
        glo.setSpacing(2)
        self.setLayout(glo)

        self.checkbox_selectall.stateChanged.connect(self.on_checkbox_state_changed)
        self.button_refresh.clicked.connect(self.on_refresh_button_clicked)
        self.button_create.clicked.connect(self.on_create_button_clicked)

    def on_create_button_clicked(self):
        data = []
        for i in range(self.shot_list.topLevelItemCount()):
            item = self.shot_list.topLevelItem(i)

            if item.is_selected():
                data.append(item.to_dict())
        
        self.create_packages(data)
        self.shot_list.refresh()
    
    def on_refresh_button_clicked(self):
        self.checkbox_selectall.setCheckState(QtCore.Qt.Unchecked)
        self.shot_list.refresh()
    
    def on_checkbox_state_changed(self, state):
        for i in range(self.shot_list.topLevelItemCount()):
            self.shot_list.topLevelItem(i).setCheckState(
                0, QtCore.Qt.CheckState(state)
            )
    
    def _close_view(self):
        self.parentWidget().page.view.close()
