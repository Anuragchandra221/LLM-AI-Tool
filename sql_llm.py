secret_key = "AIzaSyDyRXZPsuPLB3PH_6DN4ZI6A-ZMeTu1eCM"

from langchain_google_genai import GoogleGenerativeAI
 
llm = GoogleGenerativeAI(model="models/text-bison-001",google_api_key=secret_key, temperature=0.2)

from langchain_community.utilities import SQLDatabase

username = "root"
localhost = "localhost"
password = "root"
port = 3306
database = "atliq_tshirts"
db = SQLDatabase.from_uri(f"mysql+pymysql://{username}:{password}@{localhost}/{database}", sample_rows_in_table_info=3)
print(db.table_info)

from langchain_experimental.sql import SQLDatabaseChain

db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)
db_chain("How many tshirts are there?")
