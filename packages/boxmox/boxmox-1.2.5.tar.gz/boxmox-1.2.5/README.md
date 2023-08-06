# BOXMOX

``boxmox`` is the Python wrapper for the chemical box model BOXMOX (a standalone
C/Fortran executable).

## Installation

### BOXMOX model needs to be installed

The BOXMOX chemical box model needs to be installed and the ``KPP_HOME`` environment variable has to be set. Download and instructions are our website at https://mbees.med.uni-augsburg.de/boxmodeling.

### Environment variable needs to be set

Additionally, ``boxmox`` needs a path to write temporary model results
to, given through the environment variable ``BOXMOX_WORK_PATH``. This directory needs to be accessible and writeable by the user. Set it in your environment, e.g., through:

```
export BOXMOX_WORK_PATH=/where/you/want/boxmox/to/write/stuff/to/
```

Remember to close the shell and log in again for these changes to take effect.

## Contributing

We are looking forward to receiving your [new issue report](https://mbees.med.uni-augsburg.de/gitlab/mbees/boxmox_pypackage/-/issues/new).

If you'd like to contribute source code directly, please [create a fork](https://mbees.med.uni-augsburg.de/gitlab/mbees/boxmox_pypackage),
make your changes and then [submit a merge request](https://mbees.med.uni-augsburg.de/gitlab/mbees/boxmox_pypackage/-/merge_requests/new) to the original project.

# Changelog

## 1.2.5 (2022-03-14)

- Release on PyPI

## 1.2.0 (2022-03-08) (not released)

- Updates to be compatible with BOXMOX 1.8

## 1.1.0 (2020-09-16)

- Python 3 compatible 

## 1.0.0 (2017-12-19)

- Peer-reviewed version to be published in Knote et al., GMD

## 0.1.0 (2017-08-12)

- Initial release
