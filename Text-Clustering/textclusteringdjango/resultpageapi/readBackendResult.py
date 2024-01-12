import json
import os

os.chdir("E:\Code\OvGU\Information Retrieval\Search Result Clustering")
result_file = "cluster_result.json"
result_file_path = os.path.join(os.getcwd(), result_file)

def readResult():
    if os.path.exists(result_file_path):
        with open(result_file_path, 'r') as file:
            # Load the JSON data
            data = json.load(file)
            return data