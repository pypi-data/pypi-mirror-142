***************
PPSI Server
***************

PPSI server daemon ``ppsid`` must be called at the end of sway config

.. code::

   exec --no-startup-id ppsid &

The server maintains a list of all socket communications that it received at ``"${SWAYROOT:-${XDG_CONFIG_HOME:-${HOME}/.config}}/.ppsi.log"``

The server opens a unix socket to accepts communications at ``"${XDG_RUNTIME_HOME:-/run/user/${UID}}/sway/ppsi.sock"``.

PPSID auto-applies following keybindings:
  - $mod+tab: `ppsi workspace latest`
  - $mod+Shift+Tab: `ppsi workspace oldest`
  - $mod+Ctrl+Tab: `ppsi workspace reverse`
