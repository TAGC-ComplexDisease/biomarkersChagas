## Article information

Title : Blood DNA methylation marks discriminate Chagas cardiomyopathy disease clinical forms

Authors : Pauline Brochet(1), Barbara Ianni(2, João PS Nunes(1,2,3,4), Amanda F Frade(2,3,4), Priscila C Teixeira(2,3,4), Charles Mady(5), Ludmila RP Ferreira(6), Andreia Kuramoto(2), Cristina W Pissetti(7), Bruno Saba(8), Darlan DS Cândido(2,3,4), Fabrício Dias(9), Marcelo Sampaio(8), José A Marin-Neto(9), Abílio Fragata(8), Ricardo CF Zaniratto(2), Sergio Siqueira(10), Giselle DL Peixoto(10), Vagner OC Rigaud(2), Paula Buck(11), Rafael R Almeida(2,3,4), Hui Tzu Lin-Wang(8), André Schmidt(9), Martino Martinelli(10), Mario H Hirata(12), Eduardo Donadi(9), Virmondes Rodrigues Junior(7), Alexandre C Pereira(11), Jorge Kalil(2,3,4), Lionel Spinelli(1,13),c, Edecio Cunha-Neto(2,3,4,c,*), Christophe Chevillard(1,c,*).

* Authors had an equal contribution. 
c corresponding authors 

 
Affiliations: 

1. INSERM, UMR_1090, Aix Marseille Université, TAGC Theories and Approaches of Genomic Complexity, Institut MarMaRa, Marseille, France.

2. Laboratory of Immunology, Heart Institute (InCor), University of São Paulo, School of Medicine, São Paulo, Brazil.

3. Division of Clinical Immunology and Allergy, University of São Paulo, School of Medicine, São Paulo, Brazil.

4. Instituto Nacional de Ciência e Tecnologia, INCT, iii- Institute for Investigation in Immunology, São Paulo, Brazil.

5. Myocardiopathies and Aortic Diseases Unit, Heart Institute (InCor), School of Medicine, University of São Paulo, São Paulo, Brazil.

6. RNA Systems Biology Laboratory (RSBL), Departamento de Morfologia, Instituto de Ciências Biológicas, Universidade Federal de Minas Gerais, Belo Horizonte, Minas Gerais, Brazil.

7. Laboratory of Immunology, Universidade Federal Do Triângulo Mineiro (UFTM), Uberaba, Brazil.

8. Laboratório de Investigação Molecular em Cardiologia, Instituto de Cardiologia Dante Pazzanese (IDPC), São Paulo, Brazil.

9. School of Medicine of Ribeirão Preto (FMRP), University of São Paulo, Ribeirão Preto, Brazil.

10. Pacemaker Clinic, Heart Institute (InCor), School of Medicine, University of São Paulo, São Paulo, Brazil.

11. Heart Institute (InCor), School of Medicine, University of São Paulo, São Paulo, São Paulo, Brazil.

12. Department of Clinical and Toxicological Analyses, Faculty of Pharmaceutical Sciences, University of São Paulo (USP), São Paulo, Brazil.

13. Aix Marseille Université, CNRS, INSERM, Centre d'Immunologie de Marseille-Luminy, Marseille, France.

 

c Correspondence: 

Christophe Chevillard : christophe.chevillard@univ-amu.fr

Edecio Cunha-Neto : edecunha@gmail.com

Lionel Spinelli : lionel.spinelli@univ-amu.fr



Abstract :


Chagas disease, caused by the protozoan Trypanosoma cruzi, is an endemic parasitic disease of Latin America, affecting 7 million people. Although most patients are asymptomatic, 30% develop complications, including the often-fatal Chronic Chagasic Cardiomyopathy (CCC). The pathogenic process remains poorly understood. 

Based on bulk RNA-seq and whole genome DNA methylation data, we investigated the genetic and epigenetic deregulations present in the moderate and severe stages of CCC. Based on heart tissue gene expression profile, we had identified 1407 differentially expressed transcripts (DEGs) specific from CCC patients. A tissue DNA methylation analysis done on the same tissue has permitted the identification of 92 regulatory Differentially Methylated Regions (DMR) localized in the promoter of DEGs. An in-depth study of the transcription factors binding sites (TFBS) in the DMRs corroborated the importance of TFBS’s DNA methylation for gene expression in CCC myocardium. TBX21, RUNX3 and EBF1 are the transcription factors whose binding motif appears to be affected by DNA methylation in the largest number of genes. 

By combining both transcriptomic and methylomic analysis on heart tissue, and methylomic analysis on blood, 4 biological processes affected by severe CCC have been identified, including immune response, ion transport, cardiac muscle processes and nervous system. An additional study on blood methylation of moderate CCC samples put forward the importance of ion transport and nervous system in the development of the disease.



## Goal of the repository

This GitHub repository contains the python scripts as well as conda environment to reproduce the analysis performed on *Blood DNA methylation marks discriminate Chagas cardiomyopathy disease clinical forms* paper (DOI : https://doi.org/10.3389/fimmu.2022.958200).



## Description of the dataset

The dataset contains methylation levels (delta beta value) of 138 samples (48 asymptomatic, 46 moderate CCC and 44 severe CCC). It is available at GEO  (accession number : GSE191082).



## System requirement and dependencies

All the analysis has been done on a Linux system using Conda environment.



## Environment preparation

In order to prepare the environment for analysis execution, it is required to:

1. Clone the current GitHub repository and set the `WORKING_DIR` environment variable
2. Create the conda environment. 

This section provides additional information for each of these steps.
 


### Clone the GitHub repository

Use you favorite method to clone this repository in a chosen folder (see [GitHub documentation](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository) for more information). This will create a folder called `EpiChagas` containing all the code and documentation. 

Then, set an environment variable called `WORKING_DIR` with a value set to the path to this folder. For instance, if you cloned the repository in `/home/user/workspace`, then the `WORKING_DIR` variable needs be set to `/home/user/workspace/biomarkersChagas`.

**On Linux:**

```
export WORKING_DIR=/home/user/workspace/biomarkersChagas
```
 


### Create the conda environment

Go to the Github repertoire, and create the environement from the yml :

```
conda env create --name biomarkers --file=00.Data/Conda_environment.yml
```


### Run the analysis

In a Linux terminal, activate the conda environment :

```
source activate biomarkers
```

Then run the script :

```
sh main.sh
```

The raw files will be download automatically, and the analysis results will be created in the 01 or 02 folders, depending on the analysis.
