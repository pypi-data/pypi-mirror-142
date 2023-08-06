##############
Installation
##############

************
MS Windows
************

-  **Sorry**

*****************
Apple MacOS/OSX
*****************

-  **Please consider using a fancy paid App**

*********
Linux
*********

-  Use python’s pip to `install locally <#pip>`__ for the user or ask
   ``pspman`` to do it.
-  *DO NOT INSTALL SYSTEMWIDE (ROOT)*.
-  You shouldn’t have to supply root previleges or user-password during
   installation.

Prerequisites
================

- Enable pango markup language in SwayWM configuration file
- Install an emoji font such as *google-noto-emoji-color-fonts*
- Install:

   - python3 (obviously)
   - gcc
   - linux-headers
   - sway (obviously)
   - systemd
   - nmcli (NetworkManager)
   - bluez
   - pass
   - wob
   - pulseaudio
   - light
   - waypipe
   - upower

pip
====
Preferred method

Install
--------

.. code:: sh

    pip install ppsi


Update
-------

.. code:: sh

    pip install -U ppsi


Uninstall
----------

.. code:: sh

    pip uninstall -y ppsi



`pspman <https://github.com/pradyparanjpe/pspman>`__
=====================================================

(Linux only)

For automated management: updates, etc


Install
--------

.. code:: sh

   pspman -s -i https://github.com/pradyparanjpe/ppsi.git



Update
-------

.. code:: sh

    pspman


*That's all.*


Uninstall
----------

Remove installation:

.. code:: sh

    pspman -s -d ppsi
