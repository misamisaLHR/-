if (!require(Matrix)) install.packages("Matrix", dependencies=TRUE)
library(Matrix)

original_corr <- read.csv("C:/Users/mandrake/Desktop/科研/aaaaa毕业设计aaaa/数据/cor_exp1.csv", row.names = 1)
pseudo1_corr <- read.csv("C:/Users/mandrake/Desktop/科研/aaaaa毕业设计aaaa/数据/cor_exp_DF_1.csv", row.names = 1)
pseudo2_corr <- read.csv("C:/Users/mandrake/Desktop/科研/aaaaa毕业设计aaaa/数据/cor_exp_DF_2.csv", row.names = 1)

pseudo_corr <- (pseudo1_corr + pseudo2_corr) / 2

original_corr_matrix <- as.matrix(original_corr)
pseudo_corr_matrix <- as.matrix(pseudo_corr)

mean_pseudo <- mean(pseudo_corr_matrix)
sd_pseudo <- sd(pseudo_corr_matrix)
z_scores <- (original_corr_matrix - mean_pseudo) / sd_pseudo

# 步骤 3: 计算 p-value
# 转换 z-scores 为 p-values
p_values <- 2 * pnorm(-abs(z_scores))  # 双尾检验

# 将 p-value 写入 CSV 文件
write.csv(p_values, file = 'C:/Users/mandrake/Desktop/科研/aaaaa毕业设计aaaa/数据/p_values.csv', quote = FALSE, row.names = TRUE)

cat("P-values have been calculated and saved as CSV files.\n")