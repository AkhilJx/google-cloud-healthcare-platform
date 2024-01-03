# ***********************************************************************************************************
"""" ******************* For viewing the contents of the data from table4 based on condition ******************* """
# ***********************************************************************************************************

import os
from google.cloud import bigquery

# ***********************************************************************************************************

# replace ******-******-******-************.json with ur credentials
credential_path = "C:/Users/AKHIL JX/Downloads/******-******-******-************.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

# ***********************************************************************************************************

# Construct a BigQuery client object.
client = bigquery.Client()

# ***********************************************************************************************************

# replace ******-******-******.dataset1.table4 with ur credentials
query = """
SELECT *
FROM `******-******-******.dataset1.table4` 
WHERE pactioner = "Dr. Mrs.Reena Mathews"
"""

# ***********************************************************************************************************

query_job = client.query(query)  # Make an API request.

# ***********************************************************************************************************

print("**************",query_job)
print("@@@@@@@@@@@@",type(query_job))
print("The query data:")

# ***********************************************************************************************************
i=0
for row in query_job:
    i+=1
    # Row values can be accessed by field name or index.
    # print("name={}, count={}".format(row[2], row["medications"]))
    # print(row[0],"\t",row[1],"\t",row[2],"\t",row[3],"\t",row[4],"\t",row[5],"\t",row[6])
    print(row)

print("size: ",i)
# ***********************************************************************************************************