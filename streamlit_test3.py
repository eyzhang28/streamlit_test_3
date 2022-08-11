import streamlit as st
import pandas as pd
import numpy as np
import tabula as tb
import glob, os
import pdfplumber

st.title('Test')

DATE_COLUMN = 'date/time'

notice = st.selectbox(
     'What notice is this file?',
     ('First Notice', 'Second Notice', 'Final Notice'))

st.write('Please upload the proofs in the first uploader and the State Contact Shet in the second uploader')

proofs_data = st.file_uploader("Upload Proofs PDF", type=["pdf"])
state_data = st.file_uploader("Upload the State Contact Info Sheet")
print_data = st.file_uploader("Upload Print Files", type=["csv"])

total_lines = []
def string_cleaning(s):
    try:
        s = s.replace(" ", "")
        s = s.lower()
    except:
        pass
    return s
def string_stripping(s):
    try:
        s = s.strip()
    except:
        pass
    return s
def xa_cleaning(s):
    try:
        s = s.replace('\n', ' ')
        s = s.replace('\xad', '-')
        s = s.replace('\xa0', ' ')
    except:
        pass
    return s
def compare_dict(df6, proofs_dictionary):
    if (proofs_dictionary['Form Identification'] == 'BLS 3023 - Industry Verification Form'):
        st.write('Right Form Identification')
    else:
        st.write('Wrong Identification')
    if (proofs_dictionary['OMB Clearance Information'] == 'O.M.B. No. 1220-0032'):
        st.write('Right OMB info')
    else:
        st.write('Wrong OMB info')
    if (string_cleaning(df6['State Agency Name (50 char)'].iloc[0]) == string_cleaning(proofs_dictionary['State Agency Name'])):
        st.write('Same State Agency Name')
        if (df6['Abbreviation'].iloc[0] == proofs_dictionary['Abbreviation']):
            st.write('Same Abbreviation')
        else:
            st.write('Different Abbreviation')
        if (string_cleaning(df6['Department Name (50 char)'].iloc[0]) == string_cleaning(proofs_dictionary['Department Name'])):
            st.write('Same Department Name')
        else:
            st.write('Different Department Name')
        if (string_cleaning(df6['Return Address'].iloc[0]) == string_cleaning(proofs_dictionary['Return Address'])):
            st.write('Same Return Address')
        else:
            st.write('Different Return Address')
        if (string_cleaning(df6['Return Address Line 2'].iloc[0]) == xa_cleaning(string_cleaning(proofs_dictionary['Return Address Line 2']))):
            st.write('Same Return Address 2')
        else:
            st.write('Different Return Address 2')
        if (df6['Return Address Zip Code'].iloc[0] == proofs_dictionary['Return Address Zip Code']):
            st.write('Same Return Zip Code')
        else:
            st.write('Different Return Zip Code')
        if (df6['Phone Number'].iloc[0] == proofs_dictionary['Phone Number']):
            st.write('Same Phone Number')
        else:
            st.write('Different Phone Number')
        if (df6['Print (Y/N)'].iloc[0] == proofs_dictionary['Print Email']):
            if (df6['Print (Y/N)'].iloc[0] == 'N'):
                st.write('Same Email')
            else:
                if (df6['Email Address to be printed on ARS Letters'].iloc[0] == proofs_dictionary['Email']):
                    st.write('Same Email')
                else:
                    st.write('Different Email')
    else:
        st.write('Different State Agency Name')
    if (df6['BMA_Area_Code_1'].iloc[0] == proofs_dictionary['BA_ZIP_5']):
        st.write('Same ZIP 5')
    else:
        st.write('Different ZIP 5')
    if (df6['BMA_Area_Code_2'].iloc[0] == proofs_dictionary['BA_ZIP_4']):
        st.write('Same ZIP 4')
    else:
        st.write('Different ZIP 4')
    if (df6['State Agency Name'].iloc[0] == proofs_dictionary['the State Agency Name 1']):
        st.write('Same the State Agency Name 1')
    else:
        st.write('Different the State Agency Name 1')
    if (df6['State Agency Name'].iloc[0] == proofs_dictionary['the State Agency Name 2']):
        st.write('Same the State Agency Name 2')
    else:
        st.write('Different the State Agency Name 2')
    if (string_stripping(df6['BMA_City'].iloc[0]) == proofs_dictionary['BA_City']):
        st.write('Same BMA City')
    else:
        st.write('Different BMA City')
    if (string_stripping(df6['BMA_State'].iloc[0]) == proofs_dictionary['BA_State']):
        st.write('Same BMA State')
    else:
        st.write('Different BMA State')
    if (df6['Mandatory (Y or N only)'].iloc[0] == proofs_dictionary['Is_Mandatory']):
        st.write('Same Mandatory Status')
    else:
        st.write('Different Mandatory Status')
    if (df6['Mandatory (Y or N only)'].iloc[0] == 'Y'):
        if (df6['State Law (Mandatory Only)'].iloc[0] == xa_cleaning(proofs_dictionary['State_Law'])):
            st.write('Same State Law')
        else:
            st.write('Different State Law')
    if (df6['Print Spanish Instructions link?'].iloc[0] == proofs_dictionary['spanish_link']):
        st.write('Same Spanish Link')
    else:
        st.write('Different Spanish Link')
    if (string_stripping(df6['Mail_Address_1'].iloc[0]) == proofs_dictionary['BA_Address_1']):
        st.write('Same Mail Address 1')
    else:
        st.write('Different Mail Address 1')
    if (string_stripping(df6['Mail_Address_2'].iloc[0]) == ''):
        df6['Mail_Address_2'].iloc[0] = 'Empty'
    if (string_stripping(df6['Mail_Address_2'].iloc[0]) == proofs_dictionary['BA_Address_2']):
        st.write('Same Mail Address 2')
    else:
        if (string_stripping(df6['Trade_Name'].iloc[0]) == proofs_dictionary['BA_Address_2']):
            st.write('Same Mail Address 2')
        else:
            st.write('Different Mail Address 2')
    if (string_stripping(df6['Legal_Name'].iloc[0]) == ''):
        df6['Legal_Name'].iloc[0] = 'Empty'
    if (string_stripping(df6['Legal_Name'].iloc[0]) == proofs_dictionary['Legal_Name']):
        st.write('Same Legal Name')
    else:
        if (string_stripping(df6['Trade_Name'].iloc[0]) == proofs_dictionary['Legal_Name']):
            st.write('Same Legal Name')
        else:
            st.write('Different Legal Name')
    if (string_stripping(df6['Trade_Name'].iloc[0]) == ''):
        df6['Trade_Name'].iloc[0] = 'Empty'
    if (string_stripping(df6['Trade_Name'].iloc[0]) == proofs_dictionary['Trade_Name']):
        st.write('Same Trade Name')
    else:
        if (string_stripping(df6['Trade_Name'].iloc[0]) == proofs_dictionary['Legal_Name']):
            st.write('Same Trade Name')
        else:
            if (string_stripping(df6['Mail_Address_2'].iloc[0]) == proofs_dictionary['Trade_Name']):
                st.write('Same Trade Name')
            else:
                st.write('Different Trade Name')
if st.button("Run Script"):
    df = pd.read_csv(print_data)
    df2 = pd.read_excel(state_data)
    df2 = df2.drop([2,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,43,44,45])
    df2_transposed = df2.T
    df3 = df2_transposed.reset_index(drop = True)
    df3.columns = df3.iloc[1]
    df3 = df3.drop([0,1])
    df3 = df3.rename(columns = {'FIPS': 'Abbreviation_list'})
    df4 = pd.merge(df3, df, on = 'Abbreviation_list', how = 'outer')
    df4 = df4.iloc[:-2 , :]
    for i in range(1, 5, 2):
        proofs_dictionary = {}
        with pdfplumber.open(proofs_data) as pdf:
            page = pdf.pages[i-1]
            output = page.extract_text()
            output = xa_cleaning(output)
        WEB_ID = output[output.index('WEB ID:') + 8: output.index('WEB ID: ') + 20]
        PSWD = output[output.index('PASSWORD:') + 10: output.index('PASSWORD:') + 18]
        df4 = df4[df4['Web_ID'].notna()]
        df5 = df4[df4['Web_ID'].str.contains(WEB_ID)]
        df6 = df5[df5['Password'].str.contains(PSWD)]
        df6['Form Identification'] = 'BLS 3023 - Industry Verification Form'
        df6['OMB_Clearance_Information'] = 'O.M.B. No. 1220-0032'
        df6 = df6.reset_index(drop = True)
        file = 'C:/Users/zhang_e/Downloads/proofs_NVS_1.pdf'
        data = tb.read_pdf(file, area = (150, 400, 180, 600), pages = i)
        if (notice == 'Second Notice'):
            if (data[0].columns[0] == 'SECOND NOTICE'):
                st.write("Correct Notice")
            else:
                st.write("Incorrect Notice")
        elif (notice == 'Third Notice'):
            if (data[0].columns[0] == 'THIRD NOTICE'):
                st.write("Correct Notice")
            else:
                st.write("Incorrect Notice")
        else:
            if (data == []):
                st.write("Correct Notice")
            else:
                st.write("Incorrect Notice")
            
        data = tb.read_pdf(file, area = (23, 52, 144, 333), pages = i)
        if (df6['State Agency Name (50 char)'].iloc[0].lower().strip() == data[0].columns[0].lower().strip()):
            proofs_dictionary['State Agency Name'] = data[0].columns[0]
            if (pd.isnull(df6['Return Address Line 2'].iloc[0]) and pd.isnull(df6['Department Name (50 char)'].iloc[0])):
                proofs_dictionary['Department Name'] = "Empty"
                proofs_dictionary['Return Address'] = data[0].iloc[0][0]
                proofs_dictionary['Return Address Line 2'] = "Empty"
                proofs_dictionary['City'] = data[0].iloc[1][0][0:data[0].iloc[1][0].index(',')]
                proofs_dictionary['Abbreviation'] = data[0].iloc[1][0][data[0].iloc[1][0].index(',') + 2:data[0].iloc[1][0].index(',') + 4]
                zip_codes = data[0].iloc[1][0][data[0].iloc[1][0].index(',') + 6:]
                zip_codes = xa_cleaning(zip_codes)
                proofs_dictionary['Return Address Zip Code'] = zip_codes
                proofs_dictionary['Phone Number'] = xa_cleaning(data[0].iloc[2][0][7:])
            if (pd.isnull(df6['Return Address Line 2'].iloc[0]) and not pd.isnull(df6['Department Name (50 char)'].iloc[0])):
                proofs_dictionary['Department Name'] = xa_cleaning(data[0].iloc[0][0])
                proofs_dictionary['Return Address'] = data[0].iloc[1][0]
                proofs_dictionary['Return Address Line 2'] = "Empty"
                proofs_dictionary['City'] = data[0].iloc[2][0][0:data[0].iloc[2][0].index(',')]
                proofs_dictionary['Abbreviation'] = data[0].iloc[2][0][data[0].iloc[2][0].index(',') + 2:data[0].iloc[2][0].index(',') + 4]
                zip_codes = data[0].iloc[2][0][data[0].iloc[2][0].index(',') + 6:]
                zip_codes = xa_cleaning(zip_codes)
                proofs_dictionary['Return Address Zip Code'] = zip_codes
                proofs_dictionary['Phone Number'] = xa_cleaning(data[0].iloc[3][0][7:])
            if (not pd.isnull(df6['Return Address Line 2'].iloc[0]) and pd.isnull(df6['Department Name (50 char)'].iloc[0])):
                proofs_dictionary['Department Name'] = "Empty"
                proofs_dictionary['Return Address'] = data[0].iloc[0][0]
                proofs_dictionary['Return Address Line 2'] = data[0].iloc[1][0]
                proofs_dictionary['City'] = data[0].iloc[2][0][0:data[0].iloc[2][0].index(',')]
                proofs_dictionary['Abbreviation'] = data[0].iloc[2][0][data[0].iloc[2][0].index(',') + 2:data[0].iloc[2][0].index(',') + 4]
                zip_codes = data[0].iloc[2][0][data[0].iloc[2][0].index(',') + 6:]
                zip_codes = xa_cleaning(zip_codes)
                proofs_dictionary['Return Address Zip Code'] = zip_codes
                proofs_dictionary['Phone Number'] = xa_cleaning(data[0].iloc[3][0][7:])
            if (not pd.isnull(df6['Return Address Line 2'].iloc[0]) and not pd.isnull(df6['Department Name (50 char)'].iloc[0])):
                proofs_dictionary['Department Name'] = xa_cleaning(data[0].iloc[0][0])
                proofs_dictionary['Return Address'] = data[0].iloc[1][0]
                proofs_dictionary['Return Address Line 2'] = data[0].iloc[2][0]
                proofs_dictionary['City'] = data[0].iloc[3][0][0:data[0].iloc[3][0].index(',')]
                proofs_dictionary['Abbreviation'] = data[0].iloc[3][0][data[0].iloc[3][0].index(',') + 2:data[0].iloc[3][0].index(',') + 4]
                zip_codes = data[0].iloc[3][0][data[0].iloc[3][0].index(',') + 6:]
                zip_codes = xa_cleaning(zip_codes)
                proofs_dictionary['Return Address Zip Code'] = zip_codes
                proofs_dictionary['Phone Number'] = xa_cleaning(data[0].iloc[4][0][7:])
            if (df6['Print (Y/N)'].iloc[0] == 'Y'):
                proofs_dictionary['Print Email'] = 'Y'
                proofs_dictionary['Email'] = xa_cleaning(data[0].iloc[len(data[0])-1][0][7:])
            else:
                proofs_dictionary['Print Email'] = 'N'
                proofs_dictionary['Email'] = "Empty"
                if (data[0].iloc[len(data[0])-1][0][0:6] == 'Email:'):
                    proofs_dictionary['Email'] = "Extra Email"
        else:
            proofs_dictionary['State Agency Name'] = 'Empty'
            
        mandatory_data = tb.read_pdf(file, area = (130, 420, 150, 590), pages = i)
        if (mandatory_data == []):
            proofs_dictionary['Is_Mandatory'] = 'N'
            proofs_dictionary['State_Law'] = 'Empty'
        elif (mandatory_data[0].columns[0] == 'MANDATORY'):
            proofs_dictionary['Is_Mandatory'] = 'Y'
            proofs_dictionary['State_Law'] = output[output.index('in accordance with') + 19: output.index('and is authorized') - 1]
    
        proofs_dictionary['U.I.'] = output[output.index('U.I. Number:') + 12: output.index('U.I. Number:') + 23]
        
        new_data = tb.read_pdf(file, area = (115, 80, 250, 400), pages = i)
        test_df = new_data[0]
        if (len(test_df) == 6):
            proofs_dictionary['Legal_Name'] = xa_cleaning(test_df.iat[0,0])
            proofs_dictionary['Trade_Name'] = xa_cleaning(test_df.iat[1,0])
            proofs_dictionary['BA_Address_1'] = test_df.iat[3,0]
            proofs_dictionary['BA_Address_2'] = test_df.iat[2,0]
            proofs_dictionary['BA_City'] = test_df.iat[4,0][0:test_df.iat[4,0].index(',')]
            proofs_dictionary['BA_State'] = test_df.iat[4,0][test_df.iat[4,0].index(',') + 2:test_df.iat[4,0].index(',') + 4]
            proofs_dictionary['BA_ZIP'] = xa_cleaning(test_df.iat[4,0][test_df.iat[4,0].index(',') + 6:])
        if (len(test_df) == 4):
            proofs_dictionary['Legal_Name'] = xa_cleaning(test_df.iat[0,0])
            proofs_dictionary['Trade_Name'] = "Empty"
            proofs_dictionary['BA_Address_1'] = test_df.iat[1,0]
            proofs_dictionary['BA_Address_2'] = "Empty"
            proofs_dictionary['BA_City'] = test_df.iat[2,0][0:test_df.iat[2,0].index(',')]
            proofs_dictionary['BA_State'] = test_df.iat[2,0][test_df.iat[2,0].index(',') + 2:test_df.iat[2,0].index(',') + 4]
            proofs_dictionary['BA_ZIP'] = xa_cleaning(test_df.iat[2,0][test_df.iat[2,0].index(',') + 6:])
        if (len(test_df) == 5):
            proofs_dictionary['Legal_Name'] = xa_cleaning(test_df.iat[0,0])
            proofs_dictionary['Trade_Name'] = xa_cleaning(test_df.iat[1,0])
            proofs_dictionary['BA_Address_1'] = test_df.iat[2,0]
            proofs_dictionary['BA_Address_2'] = test_df.iat[1,0]
            proofs_dictionary['BA_City'] = test_df.iat[3,0][0:test_df.iat[3,0].index(',')]
            proofs_dictionary['BA_State'] = test_df.iat[3,0][test_df.iat[3,0].index(',') + 2:test_df.iat[3,0].index(',') + 4]
            proofs_dictionary['BA_ZIP'] = xa_cleaning(test_df.iat[3,0][test_df.iat[3,0].index(',') + 6:])
        spanish_data = tb.read_pdf(file, area = (720, 310, 750, 530), pages = i)
        if (spanish_data == []):
            proofs_dictionary['spanish_link'] = 'N'
        elif (spanish_data[0].columns[0] == 'En Español: www.bls.gov/respondents/ars/espanol.pdf'):
            proofs_dictionary['spanish_link'] = 'Y'
        code_data = tb.read_pdf(file, area = (70, 380, 110, 550), pages = i)
        if code_data == []:
            proofs_dictionary['Form Identification'] = 'Empty'
        else:
            proofs_dictionary['Form Identification'] = code_data[0].columns[0]
        if 'approved with' in output:
            proofs_dictionary['OMB Clearance Information'] = output[output.index('approved with') + 14: output.index('approved with') + 34]
        else:
            proofs_dictionary['OMB Clearance Information'] = 'Empty'
        if 'Every three years' and 'and the U.S. Bureau of Labor' in output:
            proofs_dictionary['the State Agency Name 1'] = output[output.index('Every three years') + 19:output.index('and the U.S. Bureau of Labor') - 1]
        else:
            proofs_dictionary['the State Agency Name 1'] = 'Empty'
        if 'The information collected by' and 'and BLS will' in output:
            proofs_dictionary['the State Agency Name 2'] = output[output.index('The information collected by') + 29:output.index('and BLS will') - 1]
        else:
            proofs_dictionary['the State Agency Name 2'] = 'Empty'
        if '-' in proofs_dictionary['BA_ZIP']:
            proofs_dictionary['BA_ZIP_5'] = proofs_dictionary['BA_ZIP'][0:5]
            proofs_dictionary['BA_ZIP_4'] = proofs_dictionary['BA_ZIP'][6:10]
        else:
            proofs_dictionary['BA_ZIP_5'] = proofs_dictionary['BA_ZIP']
            proofs_dictionary['BA_ZIP_4'] = 'Empty'
        df6 = df6.fillna('Empty')
        st.write(i)
        compare_dict(df6, proofs_dictionary)
        st.write('_____________________________')
