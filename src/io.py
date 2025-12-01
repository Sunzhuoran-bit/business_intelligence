"""
包含：
1. 从 data/raw/ 读取 .xlsx文件
2. 保存清洗后的数据到 data/processed/
"""

import os
import pandas as pd

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_raw_data(filename="数据分析岗位数据.xlsx"):
    path = os.path.join(PROJECT_ROOT,"data", "raw", filename)
    df = pd.read_excel(path)
    df = df.rename(columns={
        '职位': 'job',
        '公司名称': 'company_name',
        '地区': 'city',
        '公司类别': 'company_type',
        '公司规模': 'company_size',
        '行业类别': 'industry',
        '经验': 'experience',
        '学历': 'education',
        '人数': 'recruitment',
        '描述': 'description',
        '最低薪资': 'min_salary',
        '最高薪资': 'max_salary'
    })
    return df

def save_processed_data(df, filename="cleaned_dataset.xlsx"):
    path = os.path.join("data", "processed", filename)
    df.to_excel(path, index=False)
