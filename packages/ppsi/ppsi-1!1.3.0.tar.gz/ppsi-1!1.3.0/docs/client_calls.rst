*******************
CLIENT CALLS
*******************
.. note::

   Unless otherwise stated, interactive actions are handled by
   `launcher_menus <https://github.com/pradyparanjpe/launcher-menus.git>`__.

Help
======

Display help message about command.

.. code:: sh

   ppsi --help

   ppsi -h

   ppsi help

For help about a subcommand ``sub``

.. code:: sh

   ppsi sub -h

Remote connection
======================

SSH

Remote connection details are handled interactively. PPSID temporarily
remembers the remote machines that were contacted untill a restart.

.. code:: sh

   ppsi remote

Passwords
==============

`PASS <http://www.passwordstore.org/>`__

Recall and generate passwords.

.. code:: sh

   ppsi pass

Wifi
========

`NMCLI <https://wiki.gnome.org/Projects/NetworkManager>`__

Discovers available wifi networks, connects to selected network. Prompts
password if needed.

.. code:: sh

   ppsi wifi

Bluetooth
==============

`BLUEZ <http://www.bluez.org/>`__

Same as wifi, but for bluetooth

.. code:: sh

   ppsi bluetooth

Sway Window Manager Workspaces
=======================================

`SWAYMSG <https://swaywm.org/>`__

Back to Latest
--------------------

Performs action similar to swaymsg back_and_forth Switches to the latest
workspace

.. code:: sh

   ppsi workspace latest

Jump to Oldest
----------------------

Allows cycling through all workspaces in an order from the the oldest to
the latest

Especially usefull after the order of workspaces has been reversed

.. code:: sh

   ppsi workspace oldest

Reverse workspace order
-------------------------

Reverse the registered order of workspaces so that the oldest workspace
becomes the latest.

.. code:: sh

   ppsi workspace reverse

Update
---------

Update a workspace action (new, switch, cycle, etc)

Called automatically after workspace action through ``ppsi client``

.. code:: sh

   ppsi workspace update

Volume
===========

`PULSEAUDIO <https://www.freedesktop.org/wiki/Software/PulseAudio/>`__

Adjust volume of the currently active channel and show visible feedback
using `wob <https://github.com/francma/wob>`__

Increase
-----------

Increase volume by ``change``\ % ``change`` defaults to 2

.. code:: sh

   ppsi vol + [change]

   ppsi vol up [change]

Decrease
---------------

Decrease volume by ``change``\ % ``change`` defaults to 2

.. code:: sh

   ppsi vol - [change]

   ppsi vol down [change]

Mute
--------

Mute the channel

.. code:: sh

   ppsi vol 0

   ppsi vol mute

Brightness
===============

`LIGHT <https://haikarainen.github.io/light/>`__

Same as ``Volume`` other than the option ``mute``

.. code:: sh

   ppsi light {+,-,up,down} [change]

System
===========

`SYSTEMD <https://systemd.io/>`__

System calls

Suspend
-----------

Suspend session

.. code:: sh

   ppsi system suspend

Poweroff
------------

Poweroff session

.. code:: sh

   ppsi system poweroff

Reboot
----------

Reboot session

.. code:: sh

   ppsi system reboot

Reboot to UEFI
---------------------

Reboot the system with a request to open UEFI (BIOS)

.. code:: sh

   ppsi system bios_reboot

PPSI Daemon Communication
===============================

Communicate with ppsid.

.. code:: sh

   ppsi comm [reload|quit]

.. note::

   This feature doesn't work currently
   Instead, use:
.. code:: sh

   killall wob; killall ppsid; nohup ppsid >/dev/null 2>&1 & disown


****************
sway config
****************

Client calls may be bound in sway config as follows:

.. code::

    bindsym e exec killall ppsid, exit
    bindsym s exec --no-startup-id ppsi system suspend, mode "default"
    bindsym Shift+s exec --no-startup-id ppsi system poweroff, mode "default"
    bindsym r exec --no-startup-id ppsi system reboot, mode "default"
    bindsym Shift+r exec --no-startup-id ppsi system bios_reboot, mode "default"
    bindsym $mod+End exec --no-startup-id ppsi wifi
    bindsym $mod+Home exec --no-startup-id ppsi bluetooth
    bindsym $mod+Shift+P exec ppsi pass
    bindsym --locked XF86AudioRaiseVolume exec --no-startup-id ppsi vol +
    bindsym --locked XF86AudioLowerVolume exec --no-startup-id ppsi vol -
    bindsym --locked XF86AudioMute exec --no-startup-id ppsi vol 0
    bindsym --locked XF86MonBrightnessUp exec --no-startup-id ppsi light +
    bindsym --locked XF86MonBrightnessDown exec --no-startup-id ppsi light -
