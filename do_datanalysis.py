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


def fetch_total_quantities():
    connection = connect_to_db()
    if connection is not None:
        try:
            with connection.cursor() as cursor:
                # SQL query to select all data from the "inbound" table
                query = """
              
                            SELECT 
                                (SUM(g_printers) + SUM(clear_tapes) + SUM(branded_tapes) + SUM(plastic_bags_small)
                                + SUM(carton_boxes_small) + SUM(carton_boxes_medium) + SUM(carton_boxes_large) + SUM(plastic_bags_medium) 
                                + SUM(kg_90_suck)+ SUM(kg_50_suck) ) AS Materials,
                                sum(Orders) AS Orders
                            FROM do_outbound
                            WHERE MONTH(outdate) = MONTH(CURDATE())
                            AND YEAR(outdate) = YEAR(CURDATE());

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
                return pd.DataFrame(data_with_columns)
        except Exception as e:
            st.error(f"Error in getting total data: {e}")
            return None
    else:
        print("no connection")


#fetching data date and orders processed
def daily_orders():
    connection = connect_to_db()
    if connection is not None:
        try:
            with connection.cursor() as cursor:
                # SQL query to select all data from the "inbound" table
                query = """
              
                          SELECT 
                                    outdate, Orders
                                FROM
                                    do_outbound
                                WHERE
                                    MONTH(outdate) = MONTH(CURDATE())
                                        AND YEAR(outdate) = YEAR(CURDATE());

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
                return pd.DataFrame(data_with_columns)
        except Exception as e:
            st.error(f"Error in getting total data: {e}")
            return None
    else:
        print("no connection")


# Total Sale

def Total_sales():
    connection = connect_to_db()
    if connection is not None:
        try:
            with connection.cursor() as cursor:
                # SQL query to select all data from the "inbound" table
                query = """
              
                           SELECT 
                                                SUM(clear_tapes) * (SELECT 
                                                        clear_tapes
                                                    FROM
                                                        selling_price) + SUM(branded_tapes) * (SELECT 
                                                        branded_tapes
                                                    FROM
                                                        selling_price) + SUM(plastic_bags_small) * (SELECT 
                                                        plastic_bags_small
                                                    FROM
                                                        selling_price) + SUM(carton_boxes_small) * (SELECT 
                                                        carton_boxes_small
                                                    FROM
                                                        selling_price) + SUM(carton_boxes_medium) * (SELECT 
                                                        carton_boxes_medium
                                                    FROM
                                                        selling_price) + SUM(carton_boxes_large) * (SELECT 
                                                        carton_boxes_large
                                                    FROM
                                                        selling_price) + SUM(plastic_bags_medium) * (SELECT 
                                                        plastic_bags_medium
                                                    FROM
                                                        selling_price) + SUM(kg_90_suck) * (SELECT 
                                                        kg_90_suck
                                                    FROM
                                                        selling_price) + SUM(kg_50_suck) * (SELECT 
                                                        kg_50_suck
                                                    FROM
                                                        selling_price) AS total_sale
                                            FROM
                                                do_outbound
                                                WHERE
                                                    MONTH(outdate) = MONTH(CURDATE())
                                                        AND YEAR(outdate) = YEAR(CURDATE());

                                                     """
                cursor.execute(query)
                
                # Fetch all the rows from the query result
                result = cursor.fetchall()
       
                # Close the connection
                connection.close()

                # Return the fetched data
                return int(result[0][0])
        except Exception as e:
            st.error(f"Error in getting total data: {e}")
            return None
    else:
        print("no connection")


def last_Month_Total_sales():
    connection = connect_to_db()
    if connection is not None:
        try:
            with connection.cursor() as cursor:
                # SQL query to select all data from the "inbound" table
                query = """
              
                           SELECT 
                                                SUM(clear_tapes) * (SELECT 
                                                        clear_tapes
                                                    FROM
                                                        selling_price) + SUM(branded_tapes) * (SELECT 
                                                        branded_tapes
                                                    FROM
                                                        selling_price) + SUM(plastic_bags_small) * (SELECT 
                                                        plastic_bags_small
                                                    FROM
                                                        selling_price) + SUM(carton_boxes_small) * (SELECT 
                                                        carton_boxes_small
                                                    FROM
                                                        selling_price) + SUM(carton_boxes_medium) * (SELECT 
                                                        carton_boxes_medium
                                                    FROM
                                                        selling_price) + SUM(carton_boxes_large) * (SELECT 
                                                        carton_boxes_large
                                                    FROM
                                                        selling_price) + SUM(plastic_bags_medium) * (SELECT 
                                                        plastic_bags_medium
                                                    FROM
                                                        selling_price) + SUM(kg_90_suck) * (SELECT 
                                                        kg_90_suck
                                                    FROM
                                                        selling_price) + SUM(kg_50_suck) * (SELECT 
                                                        kg_50_suck
                                                    FROM
                                                        selling_price) AS total_sale
                                            FROM
                                                do_outbound
                                            WHERE
                                              outdate >= DATE_FORMAT(CURDATE() - INTERVAL 1 MONTH, '%Y-%m-01')
                                                      AND outdate < DATE_FORMAT(CURDATE(), '%Y-%m-01');

                                                     """
                cursor.execute(query)
                
                # Fetch all the rows from the query result
                result = cursor.fetchall()
       
                # Close the connection
                connection.close()

                # Return the fetched data
                return int(result[0][0])
        except Exception as e:
            st.error(f"Error in getting total data: {e}")
            return None
    else:
        print("no connection")



# Total and Total profit
def cost_profit():
    connection = connect_to_db()
    if connection is not None:
        try:
            with connection.cursor() as cursor:
                # SQL query to select all data from the "inbound" table
                query = """
              
                                                    SELECT 
                            SUM(clear_tapes) * (SELECT 
                                    clear_tapes
                                FROM
                                    buying_price) + SUM(branded_tapes) * (SELECT 
                                    branded_tapes
                                FROM
                                    buying_price) + SUM(plastic_bags_small) * (SELECT 
                                    plastic_bags_small
                                FROM
                                    buying_price) + SUM(carton_boxes_small) * (SELECT 
                                    carton_boxes_small
                                FROM
                                    buying_price) + SUM(carton_boxes_medium) * (SELECT 
                                    carton_boxes_medium
                                FROM
                                    buying_price) + SUM(carton_boxes_large) * (SELECT 
                                    carton_boxes_large
                                FROM
                                    buying_price) + SUM(plastic_bags_medium) * (SELECT 
                                    plastic_bags_medium
                                FROM
                                    buying_price) + SUM(kg_90_suck) * (SELECT 
                                    kg_90_suck
                                FROM
                                    buying_price) + SUM(kg_50_suck) * (SELECT 
                                    kg_50_suck
                                FROM
                                    buying_price) AS total_cost,
                                    
                                    SUM(clear_tapes) * (SELECT 
                                    clear_tapes
                                FROM
                                    profit) + SUM(branded_tapes) * (SELECT 
                                    branded_tapes
                                FROM
                                    profit) + SUM(plastic_bags_small) * (SELECT 
                                    plastic_bags_small
                                FROM
                                    profit) + SUM(carton_boxes_small) * (SELECT 
                                    carton_boxes_small
                                FROM
                                    profit) + SUM(carton_boxes_medium) * (SELECT 
                                    carton_boxes_medium
                                FROM
                                    profit) + SUM(carton_boxes_large) * (SELECT 
                                    carton_boxes_large
                                FROM
                                    profit) + SUM(plastic_bags_medium) * (SELECT 
                                    plastic_bags_medium
                                FROM
                                    profit) + SUM(kg_90_suck) * (SELECT 
                                    kg_90_suck
                                FROM
                                    profit) + SUM(kg_50_suck) * (SELECT 
                                    kg_50_suck
                                FROM
                                    profit) AS total_profit
                        FROM
                            do_outbound
                            WHERE
                                MONTH(outdate) = MONTH(CURDATE())
                                    AND YEAR(outdate) = YEAR(CURDATE());
 

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
                return pd.DataFrame(data_with_columns)
        except Exception as e:
            st.error(f"Error in getting total data: {e}")
            return None
    else:
        print("no connection")



# Total Materials used in the current month
def material_used_current_month():
    connection = connect_to_db()
    if connection is not None:
        try:
            with connection.cursor() as cursor:
                # SQL query to select all data from the "inbound" table
                query = """
              
                   SELECT
                                    sum(o.g_printers)  as used_g_printers,
                                    sum(o.clear_tapes)  as used_clear_tapes,
                                    sum(o.branded_tapes)   as used_branded_tapes,
                                    sum(o.plastic_bags_small)  as used_plastic_bags_small,
                                    sum(o.carton_boxes_small)   as used_carton_boxes_small,
                                    sum(o.carton_boxes_medium)  as used_carton_boxes_medium,
                                    sum(o.carton_boxes_large)  as used_carton_boxes_large,
                                    sum(o.plastic_bags_medium)   as used_plastic_bags_medium,
                                    sum(o.kg_90_suck)   as used_kg_90_suck,
                                    sum(o.kg_50_suck) as used_kg_50_suck
                                    FROM 
                                        do_outbound o
                                         WHERE
    MONTH(outdate) = MONTH(CURDATE())
        AND YEAR(outdate) = YEAR(CURDATE());
 

                                                     """
                cursor.execute(query)
                
                # Fetch all the rows from the query result
                result = cursor.fetchall()

                column_names = [desc[0] for desc in cursor.description]

                # Combine column names with the data
                data_with_columns = [dict(zip(column_names, row)) for row in result]
                                
                # Close the connection
                connection.close()
                
                df = (pd.DataFrame(data_with_columns)).T
                df.index.name = "Material Identifier"
                column_names_m = ["Total Used"]
                df.columns = column_names_m

                # Return the fetched data
                return df
        except Exception as e:
            st.error(f"Error in getting total data: {e}")
            return None
    else:
        print("no connection")