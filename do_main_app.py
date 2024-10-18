# Necessary Libraries
import pymysql
import streamlit as st
import pandas as pd

# Importing the accompanying Modules
import do_datafetch
import do_dataentry
import do_datanalysis



# RDS connection parameters
db_host = 'dilagaininventory-do-do-user-18043894-0.g.db.ondigitalocean.com'
db_user = 'doadmin'
db_password = 'AVNS_C2Ahmu-89xG7YG1QhNJ'
db_name = 'do_inventory_db'
db_port = 25060
# Connect to the database
def connect_to_db():
    try:
        connection = pymysql.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_name,
            port=db_port
        )
        return connection
    except Exception as e:
        st.error(f"Error connecting to database: {e}")
        return None

st.markdown(
    """
    <style>
    body {
        background-color: #e52020;
    }
    </style>
    """,
    unsafe_allow_html=True
)
###############TITLE####################
st.image("Images/header.png", use_column_width=True)

####################### DATA ENTRY ###################



do_dataentry.inbound_entry()


do_dataentry.ounbound_entry()



######### Display the inbound & outbound ##############
st.image("Images/outbound.png", use_column_width=True)
do_datafetch.display_outbound_data()

st.image("Images/inbound.png", use_column_width=True)
do_datafetch.display_inbound_data()

 
# Display the remaining materials
st.write("##")
st.image("Images/balance.png", use_column_width=True)
st.subheader("Available Packaging Materials:")
do_pm_balance = pd.read_csv("do_pm_balance.csv")
col1, col2, col3 = st.columns(3)
with col1:    
    
    st.markdown(f"(i)  :blue[**G Printers**] :  {do_pm_balance['b_g_printers'].values}")
    st.markdown(f"(i)  :blue[**ClearTapes**] :  {do_pm_balance['b_clear_tapes'].values}")
    st.markdown(f"(ii)  :blue[**BrandedTapes**] :  {do_pm_balance['b_branded_tapes'].values}")
    st.markdown(f"(v)  :red[**Cartons Small-size**] :  {do_pm_balance['b_carton_boxes_small'].values}")
    

with col2:
    st.image("Images/centre.png")

with col3:
    st.markdown(f"(vi)  :red[**Cartons Medium-size**] :  {do_pm_balance['b_carton_boxes_medium'].values}")
    st.markdown(f"(vii)  :red[**Cartons Large-size**] :  {do_pm_balance['b_carton_boxes_large'].values}")
    st.markdown(f"(viii) :violet[**Plastic Bags Small-size**] :  {do_pm_balance['b_plastic_bags_small'].values}")
    st.markdown(f"(ix) :green[**Plastic Bags Medium-size**] :  {do_pm_balance['b_plastic_bags_medium'].values}")
    st.markdown(f"(x) :violet[**90KGS Sucks**] :  {do_pm_balance['b_kg_90_suck'].values}")
    st.markdown(f"(xi)  :violet[**50KGS Sucks**] :  {do_pm_balance['b_kg_50_suck'].values}")

st.write("##")    
st.image("Images/footer.png", use_column_width=True)

