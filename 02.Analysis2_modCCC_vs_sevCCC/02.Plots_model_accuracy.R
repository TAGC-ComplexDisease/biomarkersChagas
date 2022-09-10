# 0. Load library
library(ggplot2)

# 1. Define all the models
algos <- c("DecisionTree", "SVM", "LogisticRegression", "RandomForest")

# 2. Prepare a table for all the results
dataPlot <- data.frame()

# 3. For each algo...
for(i in algos){
    # We read the data
    data <- read.table(paste("02.Analysis2_modCCC_vs_sevCCC/02.Feature_selection_machine_learning/MOD_SEV_", i, ".txt", sep = ""), sep = "\t", header = TRUE)
    # We rename the algo
    if(i == "DecisionTree"){
        myModel <- "Decision tree"
    }
    if(i == "SVM"){
        myModel <- "Linear SVM"
    }
    if(i == "LogisticRegression"){
        myModel <- "Logistic regression"
    }
    if(i == "RandomForest"){
        myModel <- "Random forest"
    } 
    # ... and for each number of features selected...
    for(y in 1:nrow(data)){
        # We create a temporary table with the model, the number of features, the mean and the standard deviation of accuracy between the k-fold runs
        tmp <- data.frame(Model = myModel,
                            NbFeatures = data[y,1],
                            Mean = mean(as.numeric(data[y, 2:ncol(data)])),
                            Sd = sd(as.numeric(data[y, 2:ncol(data)])))
        # And we merge those informations in a final table
        dataPlot <- rbind(dataPlot, tmp)
    }
}

# 4. Plot all the models and save the plot
p <- ggplot(dataPlot, aes(x=NbFeatures, y=Mean, fill = Model, color = Model)) + 
    geom_line() +
    geom_point(size = 0.5)+
    ylim(c(0,1.1)) +
    theme_classic() +
    xlab("Features number") +
    ylab("Accuracy mean (10-times CV)")

png("02.Analysis2_modCCC_vs_sevCCC/02.Feature_selection_machine_learning/MOD_vs_SEV_model_evaluation.png", res = 300, width = 8, height = 6, units = "in")
plot(p)
dev.off()
