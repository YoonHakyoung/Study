import pandas as pd

# 3개의 CSV 파일을 읽어옵니다.
df1 = pd.read_csv('cctv(num)_seoul.csv')
df2 = pd.read_csv('Roadside(num)_seoul.csv')
df3 = pd.read_csv('Children(num)_seoul.csv')
df4 = pd.read_csv('Alcol(num)_seoul.csv')
df5 = pd.read_csv('Bus(num)_seoul.csv')

# node_key을 기준으로 3개의 DataFrame을 병합합니다.
merged_df = pd.merge(df1, df2, on='node_key')
merged_df = pd.merge(merged_df, df3, on='node_key')
merged_df = pd.merge(merged_df, df4, on='node_key')
merged_df = pd.merge(merged_df, df5, on='node_key')

# 결과를 CSV 파일로 저장합니다.
merged_df.to_csv('weight_element_seoul.csv', index=False)