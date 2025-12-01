"""
包含：
1. 用中位数填充缺失值（待定）
2. 保存清洗后的数据到 data/processed/
"""

def fill_salary_missing(df):
    df["min_salary"] = df["min_salary"].fillna(df["min_salary"].median())
    df["max_salary"] = df["max_salary"].fillna(df["max_salary"].median())
    return df