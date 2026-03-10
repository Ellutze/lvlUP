Development
===========

Describe contributions and any unit testing.

Unit Testing
------------

Unit testing not part of the template yet. Not quite that standardised.


Use Cases
---------

Examples for users.



Versions tracking
-----------------
The vesion system uses standar python approch consisting of 3 numbers e.g. 1.2.3, major.minor.patch.

Before pushing/merging to main the appropriate command from the below has to be run.

.. code-block:: bash

	bump2version.exe bumpversion patch
	
	bump2version.exe bumpversion minor
	
	bump2version.exe bumpversion major
	
Tags should be pushed as follows

.. code-block:: bash

	git push origin branch_name --tags 
	
	
To Do List
----------

The TODO's below should be specific. It should be clear what needs to be done to clear the TODO. These are included in the text throughtout the documentation, and automatically gathered here for complete list. This includes missing aspects of documentation, missing code functionality, missing checks...

.. todolist::