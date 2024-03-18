import os
import pandas as pd
import re

# Define the data cleaning function
def data_cleaning(raw_data):
    # Convert raw_data to DataFrame format
    df = pd.DataFrame(raw_data)

    # Replacing or deleting null values
    df = df.fillna(0)   # CHECK
    df = df.drop(df.columns[5:], axis=1)

    # Column headers making
    df.columns = df.iloc[0]
    df = df.drop(index=0)
    df = df.rename(columns={df.columns[0]: "Product code"})
    
    pattern_product = r'["\']'
    df['Product label'] = df['Product label'].apply(lambda x: re.sub(pattern_product,'',x))

    # Unpivoted the table
    un_data = pd.melt(df, id_vars=['Product code', 'Product label'], var_name="Countries_Years", value_name="Transaction_values")
    un_data['Transaction_values'] = pd.to_numeric(un_data['Transaction_values'])
    # Creating year column
    pattern3 = r'(\d+(\.\d+)?)'
    un_data["Year"] = un_data['Countries_Years'].apply(lambda x: re.search(pattern3, x, re.IGNORECASE).group() if re.search(pattern3, x, re.IGNORECASE) else None)
    # Creating Country1 column
    pattern = r'^([^\']+)'
    un_data['Country1'] = un_data['Countries_Years'].apply(lambda x: re.search(pattern, x).group(1) if re.search(pattern, x) else None).astype(str)

    # Creating Country2 column
    pattern1 = r'exports to ([^\-]+)'
    def extract_C_Name(text):
        uygunluq = re.search(pattern1, text)
        if uygunluq:
            return uygunluq.group(1)
        else:
            return None
    un_data['Country2'] = un_data['Countries_Years'].apply(extract_C_Name)
    un_data['Country2'] = un_data['Country2'].astype(str)

    # Creating import/export column
    pattern5= r'import|export'
    un_data["Import/Export"] = un_data['Countries_Years'].apply(lambda x: re.search(pattern5, x, re.IGNORECASE).group() if re.search(pattern5, x, re.IGNORECASE) else None)
    un_data = un_data.drop(columns="Countries_Years")
    return un_data

# Folder path containing the files
folder_path = r"C:\Users\S.S\Desktop\Exportfiles"

# Get a list of all files in the directory
file_names = os.listdir(folder_path)

# Iterate over each file in the directory
cleaned_data_list = []
for file_name in file_names:
    file_path = os.path.join(folder_path, file_name)
    with open(file_path, encoding='utf-8') as file:  # Specify the encoding here
        raw_data = []
        for line in file:
            # Strip the line of leading/trailing whitespace and split it by tabs
            d = line.strip().split('\t')
            # Append the list of components to the data list
            raw_data.append(d)
    cleaned_data = data_cleaning(raw_data)  # Call the data_cleaning function
    cleaned_data_list.append(cleaned_data)

# Concatenate all cleaned data into a single DataFrame
# Concatenate all cleaned data into a single DataFrame
end_data = pd.concat(cleaned_data_list, ignore_index=True)
end_data.to_csv('DATA1.csv')  # Write the DataFrame to a CSV file
