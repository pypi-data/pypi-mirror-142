#########
PPSI
#########

*********
Gist
*********

Source Code Repository
=======================

|source| `Repository <https://gitlab.com/pradyparanjpe/ppsi.git>`__

|pages| `Documentation <https://pradyparanjpe.gitlab.io/ppsi>`__

Badges
======

|Pipeline|  |Coverage|  |PyPi Version|  |PyPi Format|  |PyPi Pyversion|


************
Description
************

A person-python-sway interface

What does it do
===============


provides a python interface for:

- workspace-specific keybindings for

  - workspace's default app: triggered by ``$mod+Shift+Return``
  - workspace-specific customizable apps

- remote [ssh/waypipe]
- password-manager [pass]
- wifi [nmcli]
- bluetooth [bluez]
- reboot [systemd]
- poweroff [systemd]
- volume [pactl] with feedback
- brightness [ light] with feedback

- a customizable pspbar (an info-bar) showing:

  - Workload (only if heavy)
  - OS Name
  - Network Speeds
  - Current IP (interactive)
  - RAM Usage
  - CPU Usage
  - Core Temperature
  - Battery (interactive)
  - Time (interactive)


.. |Pipeline| image:: https://gitlab.com/pradyparanjpe/ppsi/badges/master/pipeline.svg

.. |source| image:: https://about.gitlab.com/images/press/logo/svg/gitlab-icon-rgb.svg
   :width: 50
   :target: https://gitlab.com/pradyparanjpe/ppsi.git

.. |pages| image:: https://about.gitlab.com/images/press/logo/svg/gitlab-logo-gray-stacked-rgb.svg
   :width: 50
   :target: https://pradyparanjpe.gitlab.io/ppsi

.. |PyPi Version| image:: https://img.shields.io/pypi/v/ppsi
   :target: https://pypi.org/project/ppsi/
   :alt: PyPI - version

.. |PyPi Format| image:: https://img.shields.io/pypi/format/ppsi
   :target: https://pypi.org/project/ppsi/
   :alt: PyPI - format

.. |PyPi Pyversion| image:: https://img.shields.io/pypi/pyversions/ppsi
   :target: https://pypi.org/project/ppsi/
   :alt: PyPi - pyversion

.. |Coverage| image:: https://gitlab.com/pradyparanjpe/ppsi/badges/master/coverage.svg?skip_ignored=true
