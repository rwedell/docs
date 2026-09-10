import pandas as pd

df = pd.read_csv('https://gocarta.s3.us-east-2.amazonaws.com/public/data/tn_ng911_address_points/v1/data.csv')

df_zip = df[df["Zip_Code"] == 37406]

df_zip["Address"] = df_zip["AddNum_Pre"].astype("str") + ' ' + df_zip["Add_Number"].astype("str") + df_zip["AddNum_Suf"].astype("str") + df_zip["StNam_Full"].astype("str")

df_zip['Address'] = df_zip['Address'].str.replace('None', '', regex=False)

keep = ['Longitude', 'Latitude', 'Address']

df_zip = df_zip[keep]

df_zip.to_csv('df_zip.csv', index=False)