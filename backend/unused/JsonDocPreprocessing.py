import json
import os
import pandas as pd
import sys

if __name__ == "__main__":
    cwd = os.getcwd()
    processed_doc_json_file = "processed_docs.json"
    processed_doc_json_file_path = f"{cwd}\Preprocessing\{processed_doc_json_file}"
    
    if os.path.exists(processed_doc_json_file_path):
        processed_docs = None
        with open(processed_doc_json_file_path, 'r',encoding='utf-8') as file:
            processed_docs = json.load(file)
        
        if processed_docs == None or len(processed_docs) == 0:
            print(f"No processed document data found in {processed_doc_json_file_path}")
            sys.exit(0)
        
        df = pd.DataFrame(processed_docs)
        print(df)

        
        
    else:
        print(f"{processed_doc_json_file_path} doesn't exists")