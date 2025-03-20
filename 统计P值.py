import pandas as pd

# 读取CSV文件
file_path = "D:/桌面/毕设/1-datafission/output/1001_lines/pval_boot.csv"# 请将此路径替换为你的CSV文件的实际路径
data = pd.read_csv(file_path, header=0, index_col=0)

# 获取OTU列表
otu_list = data.columns.tolist()

# 创建一个空列表来存储小于0.05的OTU对
results = []

# 创建一个计数器来统计p-value为0的OTU对
zero_pvalue_count = 0

# 遍历每个OTU对，检查它们的p值
for i in range(len(otu_list)):
    for j in range(i + 1, len(otu_list)):
        pvalue = data.iloc[i, j]
        if pvalue == 0:
            zero_pvalue_count += 1
        if pvalue < 0.05:
            results.append((otu_list[i], otu_list[j], pvalue))

# 打印结果
print("OTU对(小于0.05的p值):")
for otu1, otu2, pval in results:
    print(f"OTU1: {otu1}, OTU2: {otu2}, p-value: {pval}")

# 统计并打印有多少对OTU
num_pairs = len(results)
print(f"\n总共有 {num_pairs} 对OTU, 其p值小于0.05。")
print(f"\n总共有 {zero_pvalue_count} 对OTU, 其p值为0。")


#####两者相似程度
import pandas as pd
import numpy as np

# 读取数据，不包含列名
bootstrap_file_path = 'D:/桌面/毕设/1-datafission/output/1001_lines/pval_boot.csv'
datafission_file_path = 'D:/桌面/毕设/1-datafission/output/1001_lines/pval_df.csv'

# 读取数据到 DataFrame，跳过第一行（如果是非数值的行）
bootstrap_data = pd.read_csv(bootstrap_file_path, header=None, skiprows=1)
datafission_data = pd.read_csv(datafission_file_path, header=None, skiprows=1)

# 将所有数据转换为浮点数，强制转换时，将无法转换的值变为 NaN
bootstrap_data = bootstrap_data.apply(pd.to_numeric, errors='coerce')
datafission_data = datafission_data.apply(pd.to_numeric, errors='coerce')

# 获取矩阵的大小
n = bootstrap_data.shape[0]

# 生成 OTU 对的列表
otu_list = range(n)  # 假设 OTU 是从 0 到 n-1

# 提取 Bootstrap p 值的矩阵，并生成字典
bootstrap_dict = {}
for i in range(n):
    for j in range(i + 1, n):
        p_value = bootstrap_data.iloc[i, j]
        if not pd.isna(p_value):
            bootstrap_dict[(i, j)] = p_value

# 提取 Datafission p 值的矩阵，并生成字典
datafission_dict = {}
for i in range(n):
    for j in range(i + 1, n):
        p_value = datafission_data.iloc[i, j]
        if not pd.isna(p_value):
            datafission_dict[(i, j)] = p_value

# 设定显著性水平
significance_threshold = 0.05

# 比较 Datafission 显著的 OTU 对在 Bootstrap 方法中的显著性
correctly_predicted = 0
total_datafission_significant = 0

for otu_pair, p_value in datafission_dict.items():
    if p_value < significance_threshold:
        total_datafission_significant += 1
        if otu_pair in bootstrap_dict and bootstrap_dict[otu_pair] < significance_threshold:
            correctly_predicted += 1

# 输出结果
print(f"Datafission 方法中显著的 OTU 对总数: {total_datafission_significant}")
print(f"其中在 Bootstrap 方法中也显著的 OTU 对数: {correctly_predicted}")
print(f"Datafission 方法中显著的 OTU 对中，有 {correctly_predicted / total_datafission_significant:.2%} 在 Bootstrap 方法中也是显著的。")