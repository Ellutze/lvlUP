# LVLUP 0.0.0


NOTHING WORKS YET, UNDER INITIAL DEVELOPMENT, BARE WITH ME xD


This repo maintains all the objects and functions needed for DnD5e character sheet maintanance.

.. code-block:: bash

    git clone https://github.com/Ellutze/LVLUP

Documentation is prepared to be built after cloning, if you don't have Sphinx install it as follows in your Python env:

.. code-block:: bash

    pip install sphinx

After cloning the repository, run the following command in "docs/" sub-folder:

.. code-block:: bash
    
    make html

and then open the docs at docs/build/html/index.html.





Notes (once resolved this will go to readme):

1. no "class" parent of "subclass", if subclass is selected at later levels user is just meant to pick placeholder "subclass", as it won't affect low level leveling anyway (this means repetition in early levels for multiple sub-classes ...)