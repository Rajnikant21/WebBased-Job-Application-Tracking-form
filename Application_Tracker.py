import streamlit as st
import pandas as pd
st.title("Job Application Data Entry")

# Create input fields for Date, Role, Company, Location, and Company Website
date_of_application = st.date_input("Date of Application")
role = st.text_input("Role")
company = st.text_input("Company")
location = st.text_input("Location")
company_website = st.text_input("Company Website")

# Create a button to submit the data
if st.button("Submit"):
    # Store the data in a DataFrame or another data structure
    data = {'Date of Application': [date_of_application],
            'Role': [role],
            'Company': [company],
            'Location': [location],
            'Company Website': [company_website]}

    df = pd.DataFrame(data)

    # Append the data to a CSV file or a database
    df.to_csv('job_applications.csv', mode='a', header=False, index=False)

    # Display a success message
    st.success("Data submitted successfully!")
