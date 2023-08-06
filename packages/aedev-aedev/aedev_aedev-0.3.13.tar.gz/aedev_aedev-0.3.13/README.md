<!-- THIS FILE IS EXCLUSIVELY MAINTAINED by the project aedev.tpl_namespace_root V0.3.10 -->
# __aedev__ namespace-root project

aedev namespace-root: aedev namespace root, providing setup, development and documentation tools/templates for Python projects.


## aedev namespace root package use-cases

this project is maintaining the portions (modules and sub-packages) of the aedev namespace to:

* bulk refactor multiple portions of this namespace simultaneously using the [grm children actions](
https://aedev.readthedocs.io/en/latest/man/git_repo_manager.html "git_repo_manager manual")
* update and deploy common outsourced files, optionally generated from templates
* merge docstrings of all portions into a single combined and cross-linked documentation
* publish documentation via Sphinx onto [ReadTheDocs](https://aedev.readthedocs.io "aedev on RTD")

this namespace-root package is only needed for development tasks, so never add it to the installation requirements
file (requirements.txt) of a project.

to ensure the update and deployment of outsourced files generated from the templates provided by this root package via
the [git repository manager tool](https://github.com/aedev-group/aedev_git_repo_manager), add this root package to the
development requirements file (dev_requirements.txt) of a portion project of this namespace.


## installation

to use this root package first clone it to your local machine and then install it as editable package with `pip`::

   cd projects-parent-folder
   git clone https://gitlab.com/aedev-group
   pip install -e aedev_aedev


## namespace portions

the following 686 portions are currently included in this namespace:

* [aedev_setup_project](https://pypi.org/project/aedev_setup_project "aedev namespace portion aedev_setup_project")
* [aedev_tpl_project](https://pypi.org/project/aedev_tpl_project "aedev namespace portion aedev_tpl_project")
* [aedev_tpl_namespace_root](https://pypi.org/project/aedev_tpl_namespace_root "aedev namespace portion aedev_tpl_namespace_root")
* [aedev_tpl_app](https://pypi.org/project/aedev_tpl_app "aedev namespace portion aedev_tpl_app")
* [aedev_git_repo_manager](https://pypi.org/project/aedev_git_repo_manager "aedev namespace portion aedev_git_repo_manager")
* [aedev_setup_hook](https://pypi.org/project/aedev_setup_hook "aedev namespace portion aedev_setup_hook")
