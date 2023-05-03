
Data Preprocessing
===================

The data_preprocessing module provides functions for Loading sequence files, Quality control & Preprocessing of the sequences from sequencing data.


read_fasta
---------------

Reads a FASTA file and returns a dictionary containing the sequence IDs as keys and the corresponding sequences as values.

Usage:

.. code-block:: python

    import GenBioX.data_preprocessing as dp

    # Load sequencing data
    seq = dp.read_fasta("sequencing_data.fasta")

    # Print the sequence
    print(seq)


fetch_seq
---------------

Retrieves a sequence from a public sequence database (such as NCBI) using its accession number.

Usage:

.. code-block:: python

    # Load sequencing data
    seq = dp.fetch_seq(database, accession_number)

    # Print the sequence
    print(seq)


read_vcf
---------------

Reads vcf file and returns a DataFrame with the variant data

Usage:

.. code-block:: python

    # Load data
    data = dp.read_vcf(vcf_path)
    print(data)


fasta_quality_check
--------------------

performs quality check on a sequence 

Usage:

.. code-block:: python

    # Load data
    data = dp.fasta_quality_check(sequences, min_length=50, max_length=1000000)
    print(data)


filter_low_quality_reads
-------------------------

Remove reads with low overall quality scores or with too many low-quality bases.

Usage:

.. code-block:: python

    # Load data
    data = dp.filter_low_quality_reads(quality_scores, min_avg_score=20, max_low_quality_bases=5)
    print(data)


quality_scores
---------------

Calculate the quality scores for each base in a sequencing read, typically represented as a Phred score.

Usage:

.. code-block:: python

    # Load data
    data = dp.quality_scores(seq)
    print(data)


trim_adapters
---------------

dentify and remove adapter sequences that may have been introduced during library preparation.

Usage:

.. code-block:: python

    # Load data
    data = dp.trim_adapters(sequence, adapter='AGATCGGAAGAGCACACGTCTGAACTCCAGTCAC')
    print(data)


remove_duplicates
-------------------

Identify and remove duplicate reads that may have been introduced during PCR amplification.

Usage:

.. code-block:: python

    # Load data
    data = dp.remove_duplicates(seq)
    print(data)


filter_contaminants
--------------------

Identify and remove reads that match known contaminant sequences, such as those from bacterial or viral genomes.

Usage:

.. code-block:: python

    # Load data
    data = dp.filter_contaminants(seq, contaminants)
    print(data)


visualise_quality_metrics
-------------------------

Generate plots and summary statistics to assess the quality of sequencing data, such as per-base quality scores and read length distributions.

Usage:

.. code-block:: python

    # Load data
    data = dp.visualise_quality_metrics(sequences, quality_scores)