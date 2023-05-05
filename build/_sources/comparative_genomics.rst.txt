comparative genomics 
=====================

Perform comparative genomics to compare genomes across different species or strains


compare_genome_size
---------------------

 Compares the size of two genomes and reports the differences.

Usage:

.. code-block:: python

    import GenBioX.comparative_genomics as ca

    ca.compare_genome_size(genome1, genom)


identify_conserved_regions
---------------------------

Identifies conserved regions between two or more genomes

Usage:

.. code-block:: python

    ca.identify_conserved_regions(genomes)



pairwise_identity
-------------------

Calculates the pairwise identity between two sequences.

Usage:

.. code-block:: python

    ca.pairwise_identity(seq1, seq2, method='global')



phylogenetic_distance
----------------------

Calculates the phylogenetic distance between two genomes.

Usage:

.. code-block:: python

    ca.phylogenetic_distance(genome1, genome2)


