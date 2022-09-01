## Article information

Title : Blood DNA methylation marks discriminate Chagas cardiomyopathy disease clinical forms

Authors : Pauline Brochet1, Barbara Ianni2, João PS Nunes1,2,3,4, Amanda F Frade2,3,4, Priscila C Teixeira2,3,4, Charles Mady5, Ludmila RP Ferreira6, Andreia Kuramoto2, Cristina W Pissetti7, Bruno Saba8, Darlan DS Cândido2,3,4, Fabrício Dias9, Marcelo Sampaio8, José A Marin-Neto9, Abílio Fragata8, Ricardo CF Zaniratto2, Sergio Siqueira10, Giselle DL Peixoto10, Vagner OC Rigaud2, Paula Buck11, Rafael R Almeida2,3,4, Hui Tzu Lin-Wang8, André Schmidt9, Martino Martinelli10, Mario H Hirata12, Eduardo Donadi9, Virmondes Rodrigues Junior7, Alexandre C Pereira11, Jorge Kalil2,3,4, Lionel Spinelli1,13,c, Edecio Cunha-Neto2,3,4,c,*, Christophe Chevillard1,c,*.

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

This GitHub repository contains the python scripts as well as conda environment to reproduce the analysis performed on *Blood DNA methylation marks discriminate Chagas cardiomyopathy disease clinical forms* paper [DOI].



## Description of the datasets

One methylation dataset was 


All those data are available at [GEO].



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



### Documentation




```
