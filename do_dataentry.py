# Necessary Libraries
import pymysql
import streamlit as st
import pandas as pd




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
    


########################## Data Saving Function #######################
# Save inbound data to the database
def save_inbound_data(in_entry):
    connection = connect_to_db()
    if connection:
        try:
            with connection.cursor() as cursor:
                sql = """
                INSERT INTO do_inbound (indate, g_printers, clear_tapes, branded_tapes, plastic_bags_small, carton_boxes_small, 
                                     carton_boxes_medium, carton_boxes_large, plastic_bags_medium, kg_90_suck, kg_50_suck)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                cursor.execute(sql, (
                    in_entry['Inbounding Date'], in_entry["G Printers"], in_entry['ClearTapes'], in_entry["BrandedTapes"],
                    in_entry["Plastic Bags (Small)"], in_entry["Carton Boxes (Small)"], in_entry["Carton Boxes (Medium)"],
                    in_entry["Carton Boxes (Large)"], in_entry["Plastic Bags (Medium)"], in_entry["90KGS Suck"], 
                    in_entry["50KGS Suck"]
                ))
                connection.commit()
                st.success("Inbound data saved to database.")
        except Exception as e:
            st.error(f"Error saving inbound data: {e}")
        finally:
            connection.close()

# Save outbound data to the database
def save_outbound_data(out_entry):
    connection = connect_to_db()
    if connection:
        try:
            with connection.cursor() as cursor:
                sql = """
                INSERT INTO do_outbound (outdate, g_printers, clear_tapes, branded_tapes, plastic_bags_small, carton_boxes_small,
                                      carton_boxes_medium, carton_boxes_large, plastic_bags_medium, kg_90_suck, kg_50_suck, orders)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                cursor.execute(sql, (
                    out_entry['DATE'], out_entry["G Printers"], out_entry['ClearTapes'], out_entry["BrandedTapes"],
                    out_entry["Plastic Bags (Small)"], out_entry["Carton Boxes (Small)"], out_entry["Carton Boxes (Medium)"],
                    out_entry["Carton Boxes (Large)"], out_entry["Plastic Bags (Medium)"], out_entry["90KGS Suck"], 
                    out_entry["50KGS Suck"], out_entry["Orders"]
                ))
                connection.commit()
                st.success("Outbound data saved to database.")
        except Exception as e:
            st.error(f"Error saving outbound data: {e}")
        finally:
            connection.close()

# Saving the sales

def save_daily_sale(sale):
    connection = connect_to_db()
    if connection:
        try:
            with connection.cursor() as cursor:
                sql = """
                INSERT INTO sale_table (DATE, daily_sale, Orders)
                VALUES (%s, %s, %s)
                """
                cursor.execute(sql, (
                    sale['DATE'], sale["daily_sale"], sale['Orders']
                ))
                connection.commit()
        except Exception as e:
            st.error(f"Error saving outbound data: {e}")
        finally:
            connection.close()


########################## Sidebar data entry ######################
def inbound_entry():
    with st.sidebar.expander('INBOUND'):
        with st.form('entry form1', clear_on_submit=True):
            in_date = st.date_input("Inbounding Date", key='in_date')
            in_GP = st.number_input("G Printers", min_value=0,  step=1, key='in_GP')
            in_CT = st.number_input("ClearTapes", min_value=0, step=1, key='in_CT')
            in_BT = st.number_input("BrandedTapes", min_value=0, step=1, key='in_BT')
            #in_A5 = st.number_input("A5 Envelopes", min_value=0, step=1, key='in_A5')
            in_PB_S = st.number_input("Plastic Bags (Small)", min_value=0, step=1, key='in_PB_S')
            in_CTN_S = st.number_input("Carton Boxes (Small)", min_value=0, step=1, key='in_CTN_S')
            in_CTN_M = st.number_input("Carton Boxes (Medium)", min_value=0, step=1, key='in_CTN_M')
            in_CTN_L = st.number_input("Carton Boxes (Large)", min_value=0, step=1, key='in_CTN_L')
            in_PB_M = st.number_input("Plastic Bags (Medium)", min_value=0, step=1, key='in_PB_M')
            in_KG90 = st.number_input("90KGS Suck", min_value=0, step=1, key='in_KG90')
            in_KG50 = st.number_input("50KGS Suck", min_value=0, step=1, key='in_KG50')            
            submitted1 = st.form_submit_button("Save Inbound")
            # Example for saving inbound data
            if submitted1:
                in_entry = {
                    'Inbounding Date': in_date, "G Printers": in_GP, 'ClearTapes': in_CT, "BrandedTapes": in_BT, 
                    "Plastic Bags (Small)": in_PB_S, "Carton Boxes (Small)": in_CTN_S, "Carton Boxes (Medium)": in_CTN_M,
                    "Carton Boxes (Large)": in_CTN_L, "Plastic Bags (Medium)": in_PB_M, "90KGS Suck": in_KG90,
                    "50KGS Suck": in_KG50
                }
                
                save_inbound_data(in_entry)






def ounbound_entry():
    with st.sidebar.expander('OUTBOUND'):
        with st.form('entry form2', clear_on_submit=True):        
            DT = st.date_input("DATE", key='DT')
            GP = st.number_input("G Printers", min_value=0, step=1, key='GP')
            CT = st.number_input("ClearTapes", min_value=0, step=1, key='CT')
            BT = st.number_input("BrandedTapes", min_value=0, step=1, key='BT')
            #A5 = st.number_input("A5 Envelopes", min_value=0, step=1, key='A5')
            PB_S = st.number_input("Plastic Bags (Small)", min_value=0, step=1, key='PB_S')
            CTN_S = st.number_input("Carton Boxes (Small)", min_value=0, step=1, key='CTN_S')
            CTN_M = st.number_input("Carton Boxes (Medium)", min_value=0, step=1, key='CTN_M')
            CTN_L = st.number_input("Carton Boxes (Large)", min_value=0, step=1,key='CTN_L')
            PB_M = st.number_input("Plastic Bags (Medium)", min_value=0, step=1, key='PB_M')
            PB_L = st.number_input("90KGS Suck", min_value=0, step=1, key='PB_L')
            KG50 = st.number_input("50KGS Suck", min_value=0, step=1, key='KG50')
            ODRS = st.number_input("Orders", min_value=0, step=1, key='odrs')
            submitted2 = st.form_submit_button("Save Outbound")
            

            
            

            if submitted2:
                tt_amount = (CT*99)+(BT*220)+(PB_S*6)+(CTN_S*20)+(CTN_M*40)+(CTN_L*72)+(PB_M*13)+(PB_L*33)+(KG50*25)
                price = {
                    'DATE' : DT, 'daily_sale' : tt_amount, 'Orders':ODRS
                     }
                out_entry = {
                    'DATE': DT, "G Printers": GP, 'ClearTapes': CT, "BrandedTapes": BT, "Plastic Bags (Small)": PB_S, 
                    "Carton Boxes (Small)": CTN_S, "Carton Boxes (Medium)": CTN_M, "Carton Boxes (Large)": CTN_L,
                    "Plastic Bags (Medium)": PB_M, "90KGS Suck": PB_L, "50KGS Suck": KG50, "Orders": ODRS
                }
                save_daily_sale(price)
                save_outbound_data(out_entry)
