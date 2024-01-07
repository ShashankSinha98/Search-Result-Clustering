import os
import pandas as pd

if __name__ == "__main__":
    documents = []
    document_names = []
    dataset_path = "big_dataset"
    if os.path.exists(dataset_path):
        docs_in_dir = os.listdir(dataset_path)
        for doc in docs_in_dir:
            if doc.endswith(".txt"):
                file_path = os.path.join(dataset_path, doc)
                with open(file_path, 'r', encoding='utf-8') as file_reader:
                    txt = file_reader.read()
                    if(len(txt) > 0):
                        documents.append(txt)
                        document_names.append(doc)
                    else:
                        print(f"{doc} is empty, not added in dataset")
        
        doc_ids = [i for i in range(1, len(documents)+1)]

        input_df = pd.DataFrame({
            "doc_id": doc_ids,
            "filenames" : document_names,
            "text": documents
        })

        try:
            output_file_name = "big dataset input docs.xlsx"
            input_df.to_excel(output_file_name, index=False)
            print(f"{len(documents)} Documents saved in {output_file_name}")
        except Exception as e:
            print(f"Exception in saving result in excel : {e}")