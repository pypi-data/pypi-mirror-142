# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html)[^1].

<!---
Types of changes

- Added for new features.
- Changed for changes in existing functionality.
- Deprecated for soon-to-be removed features.
- Removed for now removed features.
- Fixed for any bug fixes.
- Security in case of vulnerabilities.

-->

## [Unreleased]

## [2.0.2] - 2022-03-13

### Added

* Prettier labels for sequences, shots and departments
* Search flow views, which allow to browse project indexed entries. This feature relies on the search module included in Libreflow, which makes use of a MongoDB for entry indexation. Thus, the feature can be enabled giving the session the URI configuration string of this database. If not provided, flow views revert to their default behaviour.

## [2.0.1] - 2022-03-13

### Added

* An option to pack directories into existing shots.
* An option to create packages, based on predefined templates.
* Register runners required to:
  - edit AfterEffects scenes (`AfterEffects`)
  - render image sequences (`AfterEffectsRender`)
  - mark rendered images (`MarkSequenceRunner`)

### Fixed

* Error raising when the home page *Sequences* button was clicked

## [2.0.0] - 2022-02-08

Define a flow up and ready to use.