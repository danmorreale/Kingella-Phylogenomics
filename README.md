# Acquisition, co-option, and duplication of the rtx toxin system and the emergence of virulence in Kingella
Data associated with the manuscript "Acquisition, co-option, and duplication of the rtx toxin system and the emergence of virulence in Kingella" by Morreale et al.

## File Guide
This project includes several folders with additonal data and resources used in the analysis of this work. 

### Directory:
- Fig1_genus_tree
  - Figure1B.txt : Newick formatted tree corresponding to figure 1B, following annotation in IToL.
  - RAxML_bipartitions.Genus_tree_KWGREF_FINAL : RAxML output file for this tree with bootstrap information.
  - RAxML_bipartitionsBranchLabels.Genus_tree_KWGREF_FINAL : RAxML output file for this tree containing branch information.
  - RAxML_info.Genus_tree_KWGREF_FINAL : RAxML log file for this tree. 
- Fig2_K._negevensis
  - AA267_contig32.gb
  - BB331_contig1_735174_755141.gb
  - BB526_contig1_76751_96918.gb
  - CC132_contig4_185563_205598.gb
  - CC443_contig1_934713_954880.gb
  - CC505b_contig13.gb
  - D2292_contig1_1133462_1155857.gb
  - D7641_contig1_979923_1000057.gb
  - EPA014_contig1_744079_764246.gbk
  - KWG1_locus1_284426_303662.gb
  - KWG1_locus2_96316_107334.gb
  - PED555_contig1_233397_43194.gbk
  - PVC1712_contig6_22672_37546.gb
  - SW416_contig1_959893_979928.gb
  </br></br> **NOTE:** Each file in this directory is Genbank formatted genomic regions for the RTX systems in K. negevensis. These were used as input for Fig 2 along with EasyFig. The file names include the Strain name, contig of interest, genomic coordinates.
- Kingella_metadata_tree
  - NEWICK formatted tree associated with figure 3.
- Scripts:
  - amrbatch.sh
  - collect_from_ffn.py
  - dnds.py
  - Easyfig.py
  - from_cat.py
  - getfilenames.py
  - phylo_converter.sh
  - prokka.sh
  - roary_plotter.py
  </br></br> **NOTE:** Each file in this directory is a small batch script generated during analysis. Not all analyses were included in the final manuscript.
- Tree_Congruency
  - Alignment:
   </br> **This directory includes the original alignments used as input for quantifying tree congruency.**</br></br>
  - Results:
   </br> **This directory inlcudes the IQTree files generated during statistical analyses of tree congruency.**</br></br>
- Fig4_data
  - Basolateral_CFU_Isogenic_16HBE_transwell_data.txt : Basolateral CFU counts generated for isogenic strains in the 16HBE model system.
  - Rat_survival_data_KK03.txt : Rat survival data associated with isogenic strain i.p. infection.
  - TEER_Isogenic_16HBE_transwell_data.txt : Transepithelial electric resistance measurements for isogenic strains in the 16HBE model system.
- FigS2_data
  - Basolateral_CFU_Isogenic_16HBE_transwell_data.txt : Basolateral CFU counts generated for PYKK081 isogenic strains in the 16HBE model system.
  - Rat_survival_data_PYKK081.txt : Rat survival data associated with isogenic strain i.p. infection.
  - TEER_Isogenic_16HBE_transwell_data.txt : Transepithelial electric resistance measurements for PYKK081 isogenic strains in the 16HBE model system.

Each directory contains several files that pertain to the analysis or figure. Please don't hesitate to contact us if there are any issues.
