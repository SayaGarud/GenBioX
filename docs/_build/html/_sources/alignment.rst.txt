Alignment 
============

Perform sequence alignment to a reference genome or to other sequences in a database


align
--------

Aligns a given sequence to a reference genome using a specified alignment algorithm.


Usage:

.. code-block:: python

    import GenBioX.alignment as a

    a.align(seq, ref, algorithm='global')


read_alignment
------------------

Maps high-throughput sequencing reads to a reference genome to identify their genomic location and alignment quality.

Usage:

.. code-block:: python

    a.read_alignment(reads, reference_genome)


pairwise_alignment
-------------------

performs pairwise_alignment of two sequences 

Usage:

.. code-block:: python

    a.pairwise_alignment("seq.fasta", "seq2.fasta")
    


merge_alignment
-------------------

Merges two sequence alignments to produce a single alignment.


Usage:

.. code-block:: python

    a.merge_alignments(aln1, aln2)


evaluate_alignment_quality
---------------------------

Evaluates the quality of a sequence alignment based on various metrics such as coverage, accuracy, and gap distribution.

Usage:

.. code-block:: python

    aln_quality = a.evaluate_alignment_quality(alignment)
    print(aln_quality)


extract_conserved_regions
--------------------------

Extracts conserved regions from a multiple sequence alignment.

Usage:

.. code-block:: python

    conserved_regions = a.extract_conserved_regions(alignment)
    print(conserved_regions)