gene expression 
=================

performs gene expression analysis 

read_gene_expression_file
-----------------------------

reading gene expression file and converting it into dataframe for further analysis 

Usage:

.. code-block:: python

    expression_data = ge.read_gene_expression_file('mouseretina.txt')
    print(expression_data)


gene_expression_normalization
-----------------------------

This function normalizes raw gene expression data to remove technical variations and biases, which can affect downstream analysis.

Usage:

.. code-block:: python
    
    ge.gene_expression_normalization(expression_data, method='quantile')


get_group_labels
------------------

Get Group Labels For differential_gene_expression_analysis

Usage:

.. code-block:: python
    
    group_labels = ge.get_group_labels(norm)


differential_gene_expression_analysis
-------------------------------------

This function performs differential gene expression analysis to identify genes that are differentially expressed between two or more conditions or group_labels

Usage:

.. code-block:: python

    ge.differential_gene_expression_analysis(expression_data, group_labels)



gene_expression_quantification
-------------------------------

This function quantifies gene expression levels using various methods such as RPKM, TPM, or FPKM, which can be used as input for downstream analysis.

Usage:

.. code-block:: python

    ge.gene_expression_quantification(counts_matrix, lengths)



gene_expression_correlation
---------------------------

This function calculates the correlation between gene expression levels and various phenotypic or clinical variables, such as disease status, age, or gender, which can help identify potential biomarkers or therapeutic targets.

Usage:

.. code-block:: python

    ge.gene_expression_correlation(expression_data, clinical_data)


