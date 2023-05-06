.. GenBioX documentation master file, created by
   sphinx-quickstart on Sat May  6 14:07:00 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


.. image:: logo.png
   :height: 170px
   :width: 400px
   :class: logo-img
   :align: center

.. raw:: html

   <div style="height: 50px;"></div>




Welcome to GenBioX!
=======================
   
   
A Comprehensive Bioinformatics package for genome analysis.



The purpose of this package is to provide a set of tools and functionalities to perform a wide range of genome analysis tasks, including loading, quality control, preprocessing, and alignment of sequencing data.
It also includes tools to extract and filter annotations from GenBank files, perform sequence annotation, predict the functional effects of genetic variants, analyse gene expression and differential gene expression, and perform comparative genomics. 
The package provides visualisation tools to interpret the results of the analysis.
Overall, this package can be used for various genome analysis tasks in bioinformatics and genetics research.

Installation
-------------

To install GenBioX, you can use pip:

.. code-block:: bash

   pip install GenBioX

Getting started
----------------

To use GenBioX, start by importing it:

.. code-block:: python

   import GenBioX


To use Functions, start by importing different modules:

.. code-block:: python

  import GenBioX.data_preprocessing as dp 
  import GenBioX.statistical_analysis as sa
  import GenBioX.alignment as a
  import GenBioX.annotation as an
  import GenBioX.variant_analysis as va
  import GenBioX.gene_expression as ge
  import GenBioX.comparative_genomics as ca


You can then call any of the functions provided by the package. 
For example, to find the reverse complement of a DNA sequence:

.. code-block:: python

   seq = 'ATCGATCG'
   rev_comp = sa.reverse_complement(seq)
   print(rev_comp)

This will give output:

.. code-block:: none

   CGATCGAT



.. toctree::
   :maxdepth: 2
   :caption: Contents:

   data_preprocessing
   statistical_analysis
   alignment
   annotation
   variant_analysis
   gene_expression
   comparative_genomics


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

