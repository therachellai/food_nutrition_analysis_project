import os
import boto3
import time
import pandas as pd
from botocore.exceptions import NoCredentialsError
from dotenv import load_dotenv
import datetime




def author():
    """
    Returns:
       author name in list
    """
    return ['Simon Cheng-Wei Huang']

###########################################################

load_dotenv()

AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_DEFAULT_REGION = os.getenv("AWS_DEFAULT_REGION")

session = boto3.session.Session(
    region_name = AWS_DEFAULT_REGION,
    aws_access_key_id = AWS_ACCESS_KEY,
    aws_secret_access_key = AWS_SECRET_ACCESS_KEY
)

athena_client = session.client('athena')
s3_client = session.client('s3')

# Define your query and output location
query_string = "SELECT * FROM food_nutrition_analysis.food_nutrition_table LIMIT 10"
query_output_location = "s3://food-nutrition-analysis-5002/queries/"

def is_query_still_running(query_execution_id):
    """
    check if the query 
    ------------------
    Parameters: query_execution_id
    ------------------
    Returns: a boolean value, True means the query is still running, and if the query is done, it'll return False.
    """
    response = athena_client.get_query_execution(QueryExecutionId = query_execution_id)

    state = response['QueryExecution']['Status']['State']
    return state in ['QUEUED', 'RUNNING']

def response_to_df(response):
    """
    take a response from the athena query and turn it into a pandas dataframe
    ------------------
    Parameters: response from athena query
    ------------------
    Returns: a pandas dataframe
    """
    # Extract column names
    column_info = response['ResultSet']['ResultSetMetadata']['ColumnInfo']
    column_names = [col['Name'] for col in column_info]

    # Initialize a container for parsed rows
    parsed_rows = []

    # Skip the first row if it contains column headers
    start_index = 1 if response['ResultSet']['Rows'][0]['Data'][0]['VarCharValue'] in column_names else 0

    # Extract the rest of the rows
    for row in response['ResultSet']['Rows'][start_index:]:
        parsed_row = []
        for value in row["Data"]:
            if "VarCharValue" in value:
                parsed_row.append(value["VarCharValue"])
        
        parsed_rows.append(parsed_row)

    # Create DataFrame
    df = pd.DataFrame(parsed_rows, columns=column_names)
    return df

def query_from_athena(query = query_string):
    # Start the Athena query execution
    response = athena_client.start_query_execution(
        QueryString = query,
        QueryExecutionContext = {'Database': 'food_nutrition_analysis'},
        ResultConfiguration = {'OutputLocation': query_output_location}
    )

    # Get the query execution ID
    query_execution_id = response['QueryExecutionId']

    while is_query_still_running(query_execution_id):
        print("Query is still running...")
        time.sleep(5)

    # Get the query results (You may want to add waiting mechanism here to ensure the query has completed)
    result = athena_client.get_query_results(
        QueryExecutionId = query_execution_id
    )

    df = response_to_df(result)
    return df

def upload_food_nutrition_csv(file_path, bucket = "food-nutrition-analysis-5002", object_name = None):
    """
    upload files to s3
    ------------------
    Parameters: 
        - file_name: the local path of the file you want to upload
        - bucket: the bucket you want to store the data in.
        - object_name: what name do you wish the file be stored
    ------------------
    Returns: a boolean value. True means upload succeed, and False means upload failed
    """
    # If S3 object_name was not specified, use now time
    if object_name is None:
        object_name = datetime.now().isoformat()

    file_name = f"food_nutrition_csv/{object_name}"
    # Upload the file
    try:
        s3_client.upload_file(file_path, bucket, file_name)
    except NoCredentialsError:
        print("Credentials not available")
        return False
    return True
###########################################################

if __name__ == "__main__":
    print(query_from_athena())
    # if upload_food_nutrition_csv("./OUTPUTS/test1.csv", object_name="food_nutrition_csv/test1.csv"):
    #     result = query_from_athena()
    #     print(result)