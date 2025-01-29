from dotenv import load_dotenv
import os
import time
import pymssql
import csv

load_dotenv()

if __name__ == "__main__":
        
    HOST=os.getenv("HOST")
    DBUSER=os.getenv("DBUSER")
    DBPASSWORD = os.getenv("DBPASSWORD")
    DB=os.getenv("DB")

    conn = None
    print("Attempting to Connect")
    while conn is None:
        try:
            conn = pymssql.connect(
                host=HOST,
                user=DBUSER,
                password=DBPASSWORD,
                database=DB,
                encryption=None
            )
            print("Connected to {}".format(DB))
            break
        except pymssql.DatabaseError as err:
            print(str(err))
            time.sleep(1)
        except Exception as err:
            print(str(err))
            time.sleep(1)
    
    table_query = """
            SELECT name from sys.tables;
        """ 
    cursor = conn.cursor()
    cursor.execute(table_query)
    tables = cursor.fetchall()
    print("Found {} tables".format(len(tables) - 2))
    for table in tables:
        if table[0] not in ['SystemInfo', 'sysdiagrams']:
            csv_file_name = table[0] + '.csv'
            print("Generating {}".format(csv_file_name))
            output_path = os.path.join('CSV', csv_file_name)
            query = """
                SELECT * from {};
            """.format(table[0])
            cursor.execute(query)
            with open(output_path, 'w') as file:
                writer= csv.writer(file, quoting=csv.QUOTE_MINIMAL)
                writer.writerow(col[0] for col in cursor.description)
                writer.writerows(cursor)

    cursor.close()
    conn.close()
    print("Exiting")
    exit(0)