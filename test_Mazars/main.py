import pandas as pd
import numpy as np


df = pd.read_excel('toys.xlsx', header=None)


period = np.nan

column_names = ['POCORA', 'POCOBE', 'TOPBRACO', 'PORBCO', 'NOCOCPO', 'POSECO']

result = pd.DataFrame(columns=['Update', 'Period', 'Code', 'Label', 'Entity', 'Unit', 'Values'])


for i, row in df.iterrows():

    if pd.to_datetime(row[4], format='%Y.%m', errors='coerce') is not pd.NaT:
        period = row[4]

    elif pd.notnull(row[2]):

        entities = column_names
        values = row[5:11].values

        new_df = pd.DataFrame({
            'Update': pd.Timestamp.now().strftime('%Y/%m/%d'),
            'Period': period,
            'Code': row[2],
            'Label': row[3],
            'Entity': entities,
            'Unit': row[4],
            'Values': values
        })

        result = pd.concat([result, new_df], ignore_index=True)

result = result.dropna(subset=['Period'])

result = result[result['Code'] != 'Code']
result.to_excel('output.xlsx', index=False)
