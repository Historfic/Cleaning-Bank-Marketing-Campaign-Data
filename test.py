import pandas as pd
import numpy as np

# Start coding here...

df = pd.read_csv('bank_marketing.csv')


df = df.dropna()

#Client DataFrame
client_columns = ['client_id', 'age', 'job', 'marital', 'education', 'credit_default', 'mortgage']
client = df[client_columns].copy()

#Convert

client['job'] = client['job'].str.replace('.', '_')
client['education'] = client['job'].str.replace('.', '_').replace("unknown", np.NaN)
client['credit_default'] = client['credit_default'].apply(lambda x: True if x == 'yes' else False)
client['mortgage'] = client['mortgage'].apply(lambda x: True if x == 'yes' else False)


# Campaign DataFrame
campaign_columns = ["client_id",
               "number_contacts",
               "contact_duration",
               "previous_campaign_contacts",
               "previous_outcome",
               "campaign_outcome"]
campaign = df[campaign_columns].copy()


# Convert the previous_outcome and campaign_outcome to Boolean
campaign['previous_outcome'] = campaign['previous_outcome'].apply(lambda x: True if x == 'success' else False)
campaign['campaign_outcome'] = campaign['campaign_outcome'].apply(lambda x: True if x == 'yes' else False)

# Create a Month Mapping using dictionary for keys and values
month_mapping = {'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6, 'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12}


df['year'] = 2022

df['month'] = df['month'].map(month_mapping)

df['date_str'] = df['year'].astype(str) + '-' + df['month'].astype(str) + '-' + df['day'].astype(str)

campaign['last_contact_date'] = pd.to_datetime(df['date_str'], format='%Y-%m-%d')

#campaign.to_csv("campaign.csv", index=False)



# Economics DataFrame

economics_columns = ['client_id', 'cons_price_idx', 'euribor_three_months']

economics = df[economics_columns].copy()

campaign.to_csv("economics.csv", index=False)