###################
USER-CONFIGURATION
###################

Configuration file format may be

  - `yaml <https://yaml.org/spec/>`__
  - `toml <https://toml.io/en/>`__
  - `conf <https://docs.python.org/3/library/configparser.html>`__

- Copy `ppsi.yml <ppsi/server/config/ppsi.yml>`__ to ``${HOME}/.config/sway/ppsi.yml``
- Copy `pspbar.yml <ppsi/pspbar/config/pspbar.yml>`__ to ``${HOME}/.config/sway/pspbar.yml``

.. note::

   pip generally installs packages in /home/.local/lib

.. code:: sh

   cp "${HOME}/.local/lib/python$(python --version | awk '{print $2}' | cut -d '.' -f 1,2)/site-packages/ppsi/server/config/ppsi.yml" "${HOME}/.config/sway/ppsi.yml"
   cp "${HOME}/.local/lib/python$(python --version | awk '{print $2}' | cut -d '.' -f 1,2)/site-packages/ppsi/pspbar/config/pspbar.yml" "${HOME}/.config/sway/pspbar.yml"

- If ppsi somehow got installed system-wide, use the following instead

.. code:: sh

   cp "/usr/local/lib/python$(python --version | awk '{print $2}' | cut -d '.' -f 1,2)/site-packages/ppsi/server/config/ppsi.yml" "${HOME}/.config/sway/ppsi.yml"
   cp "/usr/local/lib/python$(python --version | awk '{print $2}' | cut -d '.' -f 1,2)/site-packages/ppsi/pspbar/config/pspbar.yml" "${HOME}/.config/sway/pspbar.yml"

.. warning::

   Installation of ppsi system-wide  **is strongly discouraged**

- modify them suitably

********************************
Configuration Handling
********************************

Configuration is handled by `xdgpspconf <https://pradyparanjpe.gitlab.io/xdgpspconf/>`__

*********************
Configuration format
*********************

ppsi.yml
=============

3 yaml objects
--------------------
1. primary keybinding:

   .. code:: yaml

      key-primary: $mod+Shift+Return

2. workspaces:

   .. code:: yaml

      workspaces:
      - index:
        - 1
        name: WWW
        primary: firefox
        bind:
        - key: $mod+Shift+g
          exec: google-chrome
        assignments:
          ^Firefox$: wayland

      - index:
        - 2
        name: GNU
        primary: emacsclient -c -a=""
        assignments:
          ^Emacs$: xorg
        bind: []

      - index:
        - F1
        - F2
        - F3
        - F4
        - F5
        name: REMOTE
        primary: ppsi remote
        bind: []
        assignments: {}

3. remote:

   .. code:: yaml

      remote:
        hosts:
        - localhost
        - www.example.com

        users:
        - root
        - guest


pspbar.yml
-----------------
.. code:: yaml

   update: 1  # seconds after which, bar is updated
   slow: 10  # multiple of "update" that gives the period of slow-updating segments
   time:
     active: true  # bool ?show this segment
     full: true  # bool
     fmt24: "%x %X"  # strfmt  (# date --help)
     fmt12: "%x %R"  # strfmt

   battery:
     active: true  # bool
     suspend: 2.5  # float%
     critical: 5  # float%
     minimal: 10  # float%
     low: 20  # float%
     green: 75  # float%
     yellow: 50  # float%
     red: 25  # float%
     display: time  # {time,percent,null}

   cpu:
     active: True  # bool

   temperature:
     active: true  # bool
     fire: 80  # float degrees Celsius
     orange: 70  # float degrees Celsius
     yellow: 60  # float degrees Celsius
     hot: 50  # float degrees Celsius
     warm: 40  # float degrees Celsius

   ram:
     active: true  # bool
     red: 80  # float%
     orange: 66  # float%
     yellow: 50  # float%

   network:
     active: true  # bool

   uname:
     active: true  # bool

   load:
     active: true  # bool
     red: 100  # float%
     orange: 80  # float%
     yellow: 60  # float%
