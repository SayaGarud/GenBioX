Annotation 
=====================

Extract, Filter and Search annotations from GenBank file


extract_annotations
---------------------

Usage:

.. code-block:: python

    annotations = an.extract_annotations('ann.gb')
    print(annotations)


filter_annotations
--------------------

Usage:

.. code-block:: python

    fiter_dict = {'product': 'hypothetical protein'}
    fa = an.filter_annotations(annotations, fiter_dict)
    print(fa)


search_annotations
-------------------

Usage:

.. code-block:: python

   query = "aminoglycoside"
   sa = an.search_annotations(annotations, query)
   print(sa) 


extract_locations
-------------------
Extracts Gene Names names and Locations as a pandas dataframe 

Usage:

.. code-block:: python

   loc = an.extract_locations('test.gb')
   print(loc)


visualize_annotations
----------------------

Usage:

.. code-block:: python

   an.visualize_annotations('test.gb')