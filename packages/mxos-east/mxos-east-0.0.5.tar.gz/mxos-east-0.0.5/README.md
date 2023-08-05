This is the MXOS meta tool, ``east``.

https://www.mxchip.com

Installation
------------

Using pip:

``pip3 install mxos-east``

(Use ``pip3 uninstall mxos-east`` to uninstall it.)

Basic Usage
-----------

Build ``demos/helloworld`` and flash APP image into EMC3080.

``east build -m emc3080 demos/helloworld -f APP``

Additional Commands
-------------------

East has multiple sub-commands. 

For a list of available commands, run ``east -h``. Get help on a
command with ``east <command> -h``.
