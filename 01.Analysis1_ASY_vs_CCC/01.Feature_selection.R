# 1. Load library
require(data.table)

# 2. Read data
    # 2.1. Raw data
data <- fread("00.Data/GSE191082_Normalized_data_Blood.txt", sep = "\t")
data <- data.frame(data)
rownames(data) <- as.character(data$ID_REF)
data$ID_REF <- NULL
    # 2.2. Samples informations
phenoTable <- read.table("00.Data/phenoTable.txt",sep = "\t", header = TRUE)

# 3. Split raw data in train and test cohort
train <- data[,as.character(phenoTable$ID[phenoTable$Cohorte == "Train"])]
test <- data[,as.character(phenoTable$ID[phenoTable$Cohorte == "Test"])]

# 4. Keep CpGs with at list 10 percent of methylation difference on train dataset between case and control
asy <- as.character(phenoTable$ID[phenoTable$Phenotype == "ASY"])
ccc <- as.character(phenoTable$ID[phenoTable$Phenotype != "ASY"])

train$MeanASY <- rowMeans(train[,colnames(train) %in% asy])
train$MeanCCC <- rowMeans(train[,colnames(train) %in% ccc])

train$deltaBeta <- train$MeanCCC - train$MeanASY
train <- train[which(abs(train$deltaBeta) >= 0.1),]
train$deltaBeta <- train$MeanCCC <- train$MeanASY <- NULL

# 5. Prepare test cohort
test <- test[rownames(train),]

# 6. Prepare table for machine learning application
    # 6.1. Train
train <- data.frame(t(train))
train$Phenotype <- ifelse(rownames(train) %in% asy, 0, 1)
    # 6.2. Test
test <- data.frame(t(test))
test$Phenotype <- ifelse(rownames(test) %in% asy, 0, 1)

# 7. Write tables
write.table(train, "01.Analysis1_ASY_vs_CCC/01.Feature_selection_percent_methylation/ASY_vs_CCC_train.txt", sep = "\t", row.names=FALSE)
write.table(test, "01.Analysis1_ASY_vs_CCC/01.Feature_selection_percent_methylation/ASY_vs_CCC_test.txt", sep = "\t", row.names=FALSE)
