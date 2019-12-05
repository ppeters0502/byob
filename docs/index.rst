Build Your Own Botnet (BYOB)
============================


Guide
^^^^^

.. toctree::
   :maxdepth: 2

   modules
   requirements

README
======

BYOB (Build Your Own Botnet)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Disclaimer: This project should be used for authorized testing or educational purposes only.

BYOB is an open-source project that provides a framework for security researchers and developers 
to build and operate a basic botnet to deepen their understanding of the sophisticated malware 
that infects millions of devices every year and spawns modern botnets, in order to improve their 
ability to develop counter-measures against these threats. 

It is designed to allow developers to easily implement their own code and add cool new
features *without* having to write a **RAT** (Remote Administration Tool) or a
**C2** (Command & Control server) from scratch.

*The RAT's key feature is that arbitrary code/files can be remotely loaded into memory
from the C2 and executed on the target machine without writing anything to the disk.*

Supports Python 2 & 3.

Client
^^^^^^
*Generate fully-undetectable clients with staged payloads, remote imports, and unlimited post-exploitation modules*

1) Remote Imports: remotely import third-party packages from the server without writing them 
to the disk or downloading/installing them

2) Nothing Written To The Disk: clients never write anything to the disk - not even temporary files (zero IO
system calls are made) because remote imports allow arbitrary code to be 
dynamically loaded into memory and directly imported into the currently running 
process

3) Zero Dependencies (Not Even Python Itself)__: client runs with just the python standard library, remotely imports any non-standard
packages/modules from the server, and can be compiled with a standalone python 
interpreter into a portable binary executable formatted for any platform/architecture,
allowing it to run on anything, even when Python itself is missing on the target host

4) Add New Features With Just 1 Click: any python script, module, or package you copy to the `./byob/modules/` directory
automatically becomes remotely importable & directly usable by every client while 
your command & control server is running

5) Write Your Own Modules: a basic module template is provided in `./byob/modules/` directory to make writing
your own modules a straight-forward, hassle-free process

6) Run Unlimited Modules Without Bloating File Size: use remote imports to add unlimited features without adding a single byte to the
client's file size 

7) Fully Updatable: each client will periodically check the server for new content available for
remote import, and will dynamically update its in-memory resources
if anything has been added/removed

8) Platform Independent: everything is written in Python (a platform-agnostic language) and the clients
generated can optionally be compiled into a portable executable (*Windows*) or
bundled into a standalone application (*macOS*)

9) Bypass Firewalls: clients connect to the command & control server via reverse TCP connections, which
will bypass most firewalls because the default filter configurations primarily
block incoming connections

10) Counter-Measure Against Antivirus: avoids being analyzed by antivirus by blocking processes with names of known antivirus
products from spawning

11) Encrypt Payloads To Prevent Analysis: the main client payload is encrypted with a random 256-bit key which exists solely
in the payload stager which is generated along with it

12) Prevent Reverse-Engineering: by default, clients will abort execution if a virtual machine or sandbox is detected

Server
^^^^^^
*Command & control server with persistent database and console*

1) Console-Based User-Interface: streamlined console interface for controlling client host machines remotely via
reverse TCP shells which provide direct terminal access to the client host machines

2) Persistent SQLite Database: lightweight database that stores identifying information about client host machines,
allowing reverse TCP shell sessions to persist through disconnections of arbitrary
duration and enabling long-term reconnaissance

3) Client-Server Architecture: all python packages/modules installed locally are automatically made available for clients 
to remotely import without writing them to the disk of the target machines, allowing clients to use modules which require
packages not installed on the target machines

Core
^^^^
*Core framework modules used by the generator and the server*

1) Utilities (`byob.core.util`): miscellaneous utility functions that are used by many modules

2) Security (`byob.core.security`): Diffie-Hellman IKE & 3 encryption modes (AES-256-OCB, AES-256-CBC, XOR-128)

3) Loaders (`byob.core.loaders`): remotely import any package/module/scripts from the server

4) Payloads (`byob.core.payloads`): reverse TCP shell designed to remotely import dependencies, packages & modules

5) Stagers (`byob.core.stagers`): generate unique payload stagers to prevent analysis & detection   

6) Generators (`byob.core.generators`): functions which all dynamically generate code for the client generator

7) Database (`byob.core.database`): handles interaction between command & control server and the SQLite database

8) Handler (`byob.core.handler`): HTTP POST request handler for remote file uploads to the server



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
