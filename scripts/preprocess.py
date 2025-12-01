import pandas as pd
import numpy as np
import os
from src.io import load_raw_data, save_processed_data

df = load_raw_data()
print(df.head(2))

