import os
import pandas as pd

if __name__ == "__main__":
    documents = []
    dataset_path = "dataset_hanan"
    if os.path.exists(dataset_path):
        docs_in_dir = os.listdir(dataset_path)
        for doc in docs_in_dir:
            if doc.endswith(".txt"):
                file_path = os.path.join(dataset_path, doc)
                with open(file_path, 'r', encoding='utf-8') as file_reader:
                    documents.append(file_reader.read())
        
        input_df = pd.DataFrame({
            "filenames" : docs_in_dir,
            "text": documents
        })

        try:
            output_file_name = "input docs.xlsx"
            input_df.to_excel(output_file_name, index=False)
            print(f"Documents saved in {output_file_name}")
        except Exception as e:
            print(f"Exception in saving result in excel : {e}")