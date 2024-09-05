import pandas as pd
import re
import json

df = pd.read_csv('A_Z_medicines_dataset_of_India.csv')
df.dropna()

def clean_string(string):
    string = string.lower()
    string = string.replace(" ","")
    string = re.sub(r'[^a-zA-Z0-9]', '', string)

    return string

def get_salt(df,med,exact_match=False):
    
    clean_med = clean_string(med)
    
    df['clean_name'] = df['name'].apply(clean_string)
    
    if exact_match:
        filtered_df = df[df['clean_name'] == clean_med]
    else:
        filtered_df = df[df['name'].str.contains(med, case=False, na=False)]
    
    if filtered_df.empty:
        return None
    
    return filtered_df.iloc[0]['short_composition1']


medicine_name_1 = 'paracetamol Tablet' 
medicine_name_2 = 'ganaton total Capsule sr'
composition_1 = get_salt(df, medicine_name_1, exact_match=True)
composition_2 = get_salt(df, medicine_name_2, exact_match=True)
print(f"The composition for {medicine_name_1} is: {composition_1}")
print(f"The composition for {medicine_name_2} is: {composition_2}")

