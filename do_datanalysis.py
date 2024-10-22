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
    

    ############### Remaining Packaging Materials ################
# Function to fetch data from the "inbound" table
def fetch_balance_data():
    connection = connect_to_db()
    if connection is not None:
        try:
            with connection.cursor() as cursor:
                # SQL query to select all data from the "inbound" table
                query = """
              SELECT
                                    sum(i.g_printers) - (select sum(o.g_printers) from do_outbound o)  as b_g_printers,
                                    sum(i.clear_tapes) - (select sum(o.clear_tapes) from do_outbound o)  as b_clear_tapes,
                                    sum(i.branded_tapes) - (select sum(o.branded_tapes) from do_outbound o)  as b_branded_tapes,
                                    sum(i.plastic_bags_small) - (select sum(o.plastic_bags_small) from do_outbound o)  as b_plastic_bags_small,
                                    sum(i.carton_boxes_small) - (select sum(o.carton_boxes_small) from do_outbound o)  as b_carton_boxes_small,
                                    sum(i.carton_boxes_medium) - (select sum(o.carton_boxes_medium) from do_outbound o)  as b_carton_boxes_medium,
                                    sum(i.carton_boxes_large) - (select sum(o.carton_boxes_large) from do_outbound o)  as b_carton_boxes_large,
                                    sum(i.plastic_bags_medium) - (select sum(o.plastic_bags_medium) from do_outbound o)  as b_plastic_bags_medium,
                                    sum(i.kg_90_suck) - (select sum(o.kg_90_suck) from do_outbound o)  as b_kg_90_suck,
                                    sum(i.kg_50_suck) - (select sum(o.kg_50_suck) from do_outbound o)  as b_kg_50_suck
                                    FROM 
                                        do_inbound i;
                                                     """
                cursor.execute(query)
                
                # Fetch all the rows from the query result
                result = cursor.fetchall()

                column_names = [desc[0] for desc in cursor.description]

                # Combine column names with the data
                data_with_columns = [dict(zip(column_names, row)) for row in result]
                                
                # Close the connection
                connection.close()

                # Return the fetched data
                return data_with_columns
        except Exception as e:
            st.error(f"Error fetching data: {e}")
            return None
    else:
        print("no connection")

# Display data in the Streamlit app
def display_balance_data():
    data = fetch_balance_data()
    if data:
        return pd.DataFrame(data)
        
    else:
        st.write("No data available or unable to fetch data.")
