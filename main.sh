#!/bin/sh

# This script run all the steps performed on "Blood DNA methylation marks discriminate Chagas cardiomyopathy disease clinical forms" paper analysis


# Download the raw data from GEO database

wget https://ftp.ncbi.nlm.nih.gov/geo/series/GSE191nnn/GSE191082/suppl/GSE191082_Normalized_data_Blood.txt.gz
gunzip GSE191082_Normalized_data_Blood.txt.gz
mv GSE191082_Normalized_data_Blood.txt.gz 00.Data/


##############################################################
# Analysis 1 : Asymptomatic VS Chagas Chronic Cardiomyopathy #
##############################################################

# 1. Feature selection according to beta value
mkdir -p 01.Analysis1_ASY_vs_CCC/01.Feature_selection_percent_methylation
Rscript 01.Analysis1_ASY_vs_CCC/01.Feature_selection.R 

# 2. Train machine learning models and select features
mkdir -p 01.Analysis1_ASY_vs_CCC/02.Feature_selection_machine_learning
python3 01.Analysis1_ASY_vs_CCC/02.Feature_selection_machine_learning.py
Rscript 01.Analysis1_ASY_vs_CCC/02.Plots_model_accuracy.R

# 3. Model optimization and test on validation cohort
mkdir -p 01.Analysis1_ASY_vs_CCC/03.Model_evaluation_optimization
python3 01.Analysis1_ASY_vs_CCC/03.Model_evaluation_optimization.py

###########################################
# Analysis 2 : Moderate CCC VS Severe CCC #
###########################################

# 1. Feature selection according to beta value
mkdir -p 02.Analysis2_modCCC_vs_sevCCC/01.Feature_selection_percent_methylation
Rscript 02.Analysis2_modCCC_vs_sevCCC/01.Feature_selection.R 

# 2. Train machine learning models and select features
mkdir -p 02.Analysis2_modCCC_vs_sevCCC/02.Feature_selection_machine_learning
python3 02.Analysis2_modCCC_vs_sevCCC/02.Feature_selection_machine_learning.py
Rscript 02.Analysis2_modCCC_vs_sevCCC/02.Plots_model_accuracy.R

# 3. Model optimization and test on validation cohort

mkdir -p 02.Analysis2_modCCC_vs_sevCCC/03.Model_evaluation_optimization
python3 02.Analysis2_modCCC_vs_sevCCC/03.Model_evaluation_optimization.py
