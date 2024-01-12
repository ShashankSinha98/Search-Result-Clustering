import os
from pathlib import Path
import json

import jnius_config
file_path = os.path.join( Path(__file__).parent.absolute().parent.absolute(),"Search Result Clustering","Preprocessing", "qdocs.jar")
print("FP: ",file_path)


jnius_config.set_classpath(file_path)
#jnius_config.add_classpath("E:\Code\OvGU\Information Retrieval\Search Result Clustering\Preprocessing\qdocs_lib\*")

from jnius import autoclass

QueryDocuments = autoclass("QueryDocuments")
qDoc = QueryDocuments()

user_continue = True

while user_continue:
    query = input("Enter Query: ")
    no_of_results = int(input("No of results expected: "))
    json_result = qDoc.query(query, no_of_results)
    result = json.loads(json_result)
    for ri in result:
        print(ri)
    
    user_continue = bool(input("Continue(True/False)?: "))

