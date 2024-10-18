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
    
##############################################Fetching data############################################

# Function to fetch data from the "inbound" table
def fetch_inbound_data():
    connection = connect_to_db()
    if connection is not None:
        try:
            with connection.cursor() as cursor:
                # SQL query to select all data from the "inbound" table
                query = "SELECT * FROM do_inbound;"
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
def display_inbound_data():
    data = fetch_inbound_data()
    if data:
        df_inbound = pd.DataFrame(data)
        # Assuming the 'inbound' table has these columns: id, item_name, quantity, date_received
        
        st.table(df_inbound.tail(3))
    else:
        st.write("No data available or unable to fetch data.")




 # Function to fetch data from the "outbound" table
def fetch_outbound_data():
    connection = connect_to_db()
    if connection is not None:
        try:
            with connection.cursor() as cursor:
                # SQL query to select all data from the "inbound" table
                query = "SELECT * FROM do_outbound;"
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
def display_outbound_data():
    data = fetch_outbound_data()
    if data:
        df_outbound = pd.DataFrame(data)
        # Assuming the 'inbound' table has these columns: id, item_name, quantity, date_received
        
        st.table(df_outbound.tail(3))
    else:
        st.write("No data available or unable to fetch data.")
