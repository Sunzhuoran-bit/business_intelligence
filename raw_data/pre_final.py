import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# -------------------------
# 1. 继承上一步数据和处理函数
# -------------------------
df = pd.read_csv('tetuan_processed_v3.csv')

def replace_outliers_iqr(series):
    """
    使用 IQR 方法将异常值替换为上下限
    """
    Q1 = series.quantile(0.25)
    Q3 = series.quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    # 替换异常值
    series_clipped = series.copy()
    series_clipped[series_clipped < lower_bound] = lower_bound
    series_clipped[series_clipped > upper_bound] = upper_bound
    return series_clipped

# 3. 处理 X2 和 X3 的异常值
print("--- 异常值处理 ---")
df['X2'] = replace_outliers_iqr(df['X2'])
df['X3'] = replace_outliers_iqr(df['X3'])
print("X2 和 X3 异常值已使用 IQR 上下限进行替代。")


# -----------------------------------------------
# 4. 数据标准化：消除量纲差异
# -----------------------------------------------
# 确定需要进行标准化的数值型特征
# 排除日期/时间、目标变量 Y (如果存在) 和已是分类变量的特征 (如 X4_Binary, X5_Cat)
# 假设 X1 是日期类型 (或者已无用)，Y 是目标变量
numerical_features = ['X2', 'X3', 'X5_Log']

features_to_scale = ['X2', 'X3', 'X5_Log']

# 初始化标准化器
scaler = StandardScaler()

print("\n--- 数据标准化 (Standardization) ---")
# 对指定的特征进行标准化
df[features_to_scale] = scaler.fit_transform(df[features_to_scale])
print(f"特征 {features_to_scale} 已标准化 (均值=0, 方差=1)。")


# -----------------------------------------------
# 5. 划分数据集：训练集、验证集、测试集
# -----------------------------------------------
# 目标：60% 训练集, 20% 验证集, 20% 测试集
# 步骤1: 先将数据分为 80% 训练+验证集 和 20% 测试集
df_train_val, df_test = train_test_split(
    df, test_size=0.2, random_state=42, shuffle=False
) # 假设是时间序列数据，使用 shuffle=False，如果不是，请删除 shuffle=False

# 步骤2: 将 80% 的训练+验证集按 3:1 的比例 (即 60% vs 20%) 分为训练集和验证集
# 验证集占 df_train_val 的比例为 0.2 / 0.8 = 0.25
df_train, df_val = train_test_split(
    df_train_val, test_size=0.25, random_state=42, shuffle=False
) # 同样假设时间序列，使用 shuffle=False

# 打印划分结果
print("\n--- 数据集划分结果 ---")
print(f"总样本数: {len(df)}")
print(f"训练集 (Train, 60%): {len(df_train)} 条数据")
print(f"验证集 (Validation, 20%): {len(df_val)} 条数据")
print(f"测试集 (Test, 20%): {len(df_test)} 条数据")


# -----------------------------------------------
# 6. 保存处理后的数据集
# -----------------------------------------------
df_train.to_csv('tetuan_train.csv', index=False)
df_val.to_csv('tetuan_validation.csv', index=False)
df_test.to_csv('tetuan_test.csv', index=False)

print("\n--- 数据保存完成 ---")
print("训练集已保存至: tetuan_train.csv")
print("验证集已保存至: tetuan_validation.csv")
print("测试集已保存至: tetuan_test.csv")