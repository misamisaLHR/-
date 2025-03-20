# Load necessary packages
if (!require(MASS)) install.packages("MASS", dependencies=TRUE)
library(MASS)

# Data
txt_file <- "D:/桌面/毕设/1-datafission/output/1001_lines/1001_lines.txt" 
otu_data <- read.table(txt_file, header = TRUE, sep = "\t", row.names = 1)
dim(otu_data)

dataset1 <- matrix(NA, nrow = nrow(otu_data), ncol = ncol(otu_data))
dataset2 <- matrix(NA, nrow = nrow(otu_data), ncol = ncol(otu_data))

# 步骤 3: 生成新的数据集
for (i in 1:ncol(otu_data)) {
  # 获取每个 OTU 样本的丰度
  X <- otu_data[, i]
  
  for (j in 1:length(X)) {
    z <- X[j]
    
    # Gamma 分布的参数
    alpha <- 1 + z
    beta <- 2  # 因为 B = 2, 我们设置 rate 为 2
    
    # 从 Gamma 分布中生成 X
    X_simulated <- rgamma(1, shape = alpha, rate = beta)
    
    # 使用生成的 X 生成 B 个泊松数据点
    new_Z <- rpois(2, lambda = X_simulated)
    
    # 将生成的数据点分配到两个新的数据集中
    dataset1[j, i] <- new_Z[1]
    dataset2[j, i] <- new_Z[2]
  }
}

# 将数据矩阵转换为数据框
dataset1 <- as.data.frame(dataset1)
dataset2 <- as.data.frame(dataset2)

# 步骤 4: 保存生成的数据集
write.csv(dataset1, file = 'D:/桌面/毕设/1-datafission/output/1001_lines/dataset1.csv', quote = FALSE, row.names = TRUE)
write.csv(dataset2, file = 'D:/桌面/毕设/1-datafission/output/1001_lines/dataset2.csv', quote = FALSE, row.names = TRUE)

cat("Datasets have been generated and saved as CSV files.\n")