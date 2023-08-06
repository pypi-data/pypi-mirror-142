# SuperTLD

![Flow_chart_of_SuperTLD](./overview.pdf)

SuperTLD is a novel method proposed to infer the hierarchical structure of TAD-like domains (TLDs) from RNA-associated interactions (RAIs). 
SuperTLD comprises the data imputation and hierarchical domain detection. 
SuperTLD supports RAI's asymmetric or symmetric contact map as input. 
Users can test the TAD inference potentiality from the integration of Hi-C and RAIs via SuperTAD.   
We also provide the scripts of evaluation performed in the paper.

## Requirements
* python3
* numpy
* pandas
* scipy
* SuperTAD v1.2 (https://github.com/deepomicslab/SuperTAD)

## Installation
Download SuperTLD by
```angular2html
pip install supertld
```

## Instructions
In this section, we show how to run SuperTLD with the example data.
### Data preparation 
The example data can be downloaded from the [zenode repository](https://zenodo.org/record/5501849#.YT3xwI4zaUk).
Download the example_data.zip and uncompress the example_data.zip into the directory of `./data`.

### Run SuperTLD

```angular2html
import supertld
import numpy as np

# 

ython main_pipeline.py -i [RAI_interaction_map] -w [workpath] -c [chrom] -r [resolution] --hic [hic_contact_map] -a [alpha] -A --bed [structure_protein_peaks] --bedgraph [H3K27me3/H3K36me3]
[RAI_interaction_map] - the file of interaction map constructed from RAIs
[workpath] - the path that saved all results
[chrom] - the chromosome of interaction map
[resolution] - the bin resolution, e.g. 100000 (bp)
[hic_contact_map] - the corresponding hic contact map (same cell line and chromosome)
[alpha] - the scaling factor for data integration, default: 1 (means without integration with Hi-C)
[structure_protein_peaks] - for evaluating the inferred TADs, e.g. CTCF peaks
[H3K27me3/H3K36me3] - for evaluating the inferred TADs
-A if given, SuperTAD-sparse will automatically determine the optimal value of alpha.
```
For an example, if the scaling factor alpha is defined by user, 
one can run `python main_pipeline.py -i ./data/iMARGI_chr22_RAI_matrix_100kb.txt -w ./test/ -c chr22 -r 100000 --hic ./data/HEK293T_chr22_100KR_matrix.txt -a [the_defined_alpha]` to infer the TADs.
If the scaling factor alpha is unknown, one can run `python main_pipeline.py -i ./data/iMARGI_chr22_RAI_matrix_100kb.txt -w ./test/ -c chr22 -r 100000 --hic ./data/HEK293T_chr22_100KR_matrix.txt -A 
--bed ./data/CTCF_ENCFF206AQV.bed --bedgraph ./data/H3K27ME3_hg38_GSM3907592.bedgraph ./data/H3K36me3_hg38_ENCSR910LIE.bedgraph` to find an optimal alpha and infer TADs.

All the derived contact maps are listed in `./test/all_fileList_Alpha*.txt`, 
the result of inferred TADs are suffixed with `.multi2D_AllH2_sparse.tsv`.  
### Evaluate the Results
We provide the scripts for evaluation, including the Pearson correlation coefficient (PCC) of distance decay, 
overlapping ratio (OR), normalized mutual information (NMI), CTCF fold change at boundaries, and percentage of histone H3 marks enriched TADs.
One can run `python main_evaluation.py -i ./test/all_fileList_Alpha*.txt -w ./test/ -c chr22 -r 100000
--hic ./data/HEK293T_chr22_100KR_matrix.txt --bed ./data/CTCF_ENCFF206AQV.bed --bedgraph ./data/H3K27ME3_hg38_GSM3907592.bedgraph ./data/H3K36me3_hg38_ENCSR910LIE.bedgraph`.
The `-i` is the file list output from SuperTAD-sparse. 

The output is saved in `./test/evaluation_AllResult_sparse.txt`. The first row is the result of Hi-C contact map, 
and the rest rows correspond to the file listed in `./test/evaluation_AllResult_sparse.txt`. The first column is the 
PCC of contact map (compared with Hi-C), the second column is the PCC of distance decay, the third and fourth column are OR and NMI respectively,
the fifth and sixth are the CTCF fold change and its pvalue, and the seventh column is the percentage of TADs enriched in H3* marks.

## Contact
Feel free to open an issue in Github or contact `yuwzhang7-c@my.cityu.edu.hk` if you have any problem in using SuperTAD-sparse.

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.

