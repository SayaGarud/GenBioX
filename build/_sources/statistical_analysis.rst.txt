Statistical Analysis
=====================

The statistical_analysis module provides functions for statistical analysis of sequences.


calculate_gc_content
----------------------

calculates the GC content of a nucleotide sequence.

Usage:

.. code-block:: python

    gc_count = sa.calculate_gc_content(sequence)
    print(gc_count)    


count_nucleotides
------------------

counts the number of A, C, G, and T (or U) nucleotides in a nucleotide sequence.

Usage:

.. code-block:: python

    count = sa.count_nucleotides(sequence)
    print(count)


reverse_complement
-------------------

generates the reverse complement of a nucleotide sequence

Usage:

.. code-block:: python

    rev_comp = sa.reverse_complement(sequence)
    print(rev_comp)



translate
---------------

translates a nucleotide sequence into a protein sequence using the standard genetic code.

Usage:

.. code-block:: python

    seq = sa.translate(sequence)
    print(seq)