# Necessary Libraries
import pymysql
import streamlit as st
import pandas as pd

# Importing the accompanying Modules
import do_datafetch
import do_dataentry
import do_datanalysis
import do_visualization



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
    
#setting
st.set_page_config(layout="wide")

# style css
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Load and apply the CSS file
load_css("style.css")

#######TITLE####################
st.image("photos/header.png", use_container_width=True)
st.image("photos/about.png", use_container_width=True)
st.write("---")
####################### DATA ENTRY ###################



do_dataentry.inbound_entry()


do_dataentry.ounbound_entry()

#sidebar images
st.sidebar.image("photos/side1.png", use_container_width=True)
st.sidebar.image("photos/side2.png", use_container_width=True)
# Data Visualization
v_col1, v_col2 = st.columns(2)
try:
    with v_col1:
        do_visualization.pie_visual()
except:
    st.write("Visual not ready!!")    


try:
    
    with v_col2:
        do_visualization.daily_orders()
except:
    st.write("Visual Not Ready")


######### Display the inbound & outbound ##############
st.image("photos/outbound.png", use_container_width=True)
do_datafetch.display_outbound_data()

st.image("photos/inbound.png", use_container_width=True)
do_datafetch.display_inbound_data()

 
# Display the remaining materials
st.write("##")
st.image("photos/balance.png", use_container_width=True)
st.subheader("Available Packaging Materials:")

do_pm_balance = do_datanalysis.display_balance_data()
st.dataframe(do_pm_balance)

col1, col2, col3 = st.columns(3)
with col1:    
    
    st.write("##")
    st.markdown(f"(i)  :blue[**G Printers**] :  {do_pm_balance['b_g_printers'].values}")
    st.markdown(f"(i)  :blue[**ClearTapes**] :  {do_pm_balance['b_clear_tapes'].values}")
    st.write("##")
    st.markdown(f"(ii)  :blue[**BrandedTapes**] :  {do_pm_balance['b_branded_tapes'].values}")
    st.markdown(f"(v)  :red[**Cartons Small-size**] :  {do_pm_balance['b_carton_boxes_small'].values}")
    st.markdown(f"(vi)  :red[**Cartons Medium-size**] :  {do_pm_balance['b_carton_boxes_medium'].values}")

with col2:
    st.image("photos/centre.png", use_container_width=True)


with col3:
    
    st.write("##")
    st.markdown(f"(vii)  :red[**Cartons Large-size**] :  {do_pm_balance['b_carton_boxes_large'].values}")
    st.markdown(f"(viii) :blue[**Plastic Bags Small-size**] :  {do_pm_balance['b_plastic_bags_small'].values}")
    st.write("##")
    st.markdown(f"(ix) :green[**Plastic Bags Medium-size**] :  {do_pm_balance['b_plastic_bags_medium'].values}")
    st.markdown(f"(x) :blue[**90KGS Sucks**] :  {do_pm_balance['b_kg_90_suck'].values}")
    st.markdown(f"(xi)  :blue[**50KGS Sucks**] :  {do_pm_balance['b_kg_50_suck'].values}")

with st.expander("Finance Reviews:"):
    passcode1 = st.text_input("Passcode")
    if passcode1 == '114986bn':
            months = ['Current-Month', 'Last-Month']
            month = st.selectbox("Choose the Month you want to View Total Sales for ", months)
            if month == 'Current-Month':
                try:
                    st.write("Total Sales: ", do_datanalysis.Total_sales())
                except:
                    st.write("Could not fetch the data at the Moment!")    
                
            else:
                try:
                    st.write("Total Sales: ", do_datanalysis.last_Month_Total_sales())
                except:
                    st.write("Could not fetch the data at the Moment!")    
                

col11, col22, col33 = st.columns(3)
with col11:
    st.write("Note:  ")
    st.write('''To maximize in a packaging materials inventory, start by conducting a thorough assessment
              of your current stock levels and usage patterns. Implement a just-in-time inventory system like this to align 
             your purchases with comsumption rate, reducing excess stock and storage costs. Regularly review your 
             supplier agreements to ensure you’re getting the best pricing and consider consolidating orders to reduce much expenses. 
             Utilize inventory management software like this to track materials in real-time, enables you
              to anticipate shortages and avoid over-ordering. Finally, explore sustainable packaging options that
              can reduce costs and improve packaging standards, further enhancing your financial performance.


                                 ''')

with col22:
    do_visualization.cost_profit_vis()

try:
    with st.expander("View Trend"):
        do_visualization.daily_sale()
except:
    st.error("Sorry we could not fetch the Visual at the moment")        

with col33:
    st.subheader("Material Used Current Month")
    st.table(do_datanalysis.material_used_current_month())

# st.write("##")    
st.image("photos/footer.png", use_container_width=True)


