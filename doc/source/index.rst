.. hocapontas documentation master file, created by
   sphinx-quickstart on Sun May 22 22:16:54 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.



hocapontas
==========

hocapontas is a small library built to provide an easy to use API when
developing 'life-assisting' applications in Python. Example areas where
hocapontas might be useful is when developing a CLI application for
managing your budget or a slackbot for planning and reminding your of
coming events. Just simple things, but simpler.


An Early Stage
~~~~~~~~~~~~~~

As of this early stage in development, hocapontas doesn't look like
much. It currently features a small task scheduler where task items
are made up of dictionaries to be easily passed on and manipulated in
which ever environment one desires.

For storing data persistantly, a plain text file is used and contains
just the task items, no users or other metadata exists yet. Future
versions will include adapter APIs for communication between proper
databases.


TODO
~~~~

* Database Adapter
  
  - Support for MongoDB  
  - Support for multiple users
    
* Reminder Module (upcoming events, nag about incomplete tasks, etc.)
* Budget Planning Module


Doc Contents:
~~~~~~~~~~~~~~

.. toctree::
   :maxdepth: 2

   install
   contribute
   scheduler
   
