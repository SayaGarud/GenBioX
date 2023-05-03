variant analysis 
=====================

Prediction of the functional effects of genetic variants


variant_calling
-------------------

Identifies genetic variants such as SNPs, indels, and structural variations from sequencing data.


Usage:

.. code-block:: python

    import GenBioX.variant_analysis as va

    va.ariant_calling(input_bam, reference_genome, output_vcf)


variant_annotation
-------------------

Annotates genetic variants with information such as gene annotation, variant type, location, and allele frequency.

Usage:

.. code-block:: python

    va.variant_annotation(input_vcf, output_annovar_prefix, database)



variant_effect_prediction
--------------------------

Predicts the functional consequences of genetic variants using various tools such as SIFT, PolyPhen, and CADD.

Usage:

.. code-block:: python

    va.variant_effect_prediction(input_vcf, output_vcf, reference_genome)


splice_site_prediction
-----------------------

This function predicts the effect of variants on splicing by analyzing splice site sequences and motifs, which can help identify variants that may cause exon skipping or intron retention.

Usage:

.. code-block:: python

    va.splice_site_prediction(input_vcf, output_vcf, reference_genome):


phenotype_prediction
---------------------

predicts the effect of variants on phenotypes using various methods such as Mendelian randomization, polygenic risk scores, and machine learning models, which can help identify variants associated with specific diseases or traits.

Usage:

.. code-block:: python

    va.phenotype_prediction(variants, phenotypes)