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

Predicts the functional consequences of genetic variants

Usage:

.. code-block:: python

    va.variant_effect_prediction(input_vcf, output_vcf, reference_genome)


splice_site_prediction
-----------------------

predicts the effect of variants on splicing by analyzing splice site sequences and motifs

Usage:

.. code-block:: python

    va.splice_site_prediction(input_vcf, output_vcf, reference_genome):


phenotype_prediction
---------------------

predicts the effect of variants on phenotypes 

Usage:

.. code-block:: python

    va.phenotype_prediction(variants, phenotypes)