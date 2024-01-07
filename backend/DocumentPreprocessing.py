import os
import pandas as pd
from NltkPreprocessingSteps import NltkPreprocessingSteps


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
        
        print(f"Total Non-empty Documents Read: {len(documents)} / {len(docs_in_dir)}")
        data = {
            "filenames" : document_names,
            "text": documents
        }
        df = pd.DataFrame(data)
        txt_preproc = NltkPreprocessingSteps(df['text'])

        processed_text = \
            txt_preproc \
            .remove_html_tags()\
            .replace_diacritics()\
            .expand_contractions()\
            .remove_numbers()\
            .remove_punctuations_except_periods()\
            .lemmatize()\
            .remove_double_spaces()\
            .remove_all_punctuations()\
            .remove_stopwords()\
            .get_processed_text()
        
        print(processed_text)
        
        doc_ids = [i for i in range(1, len(documents)+1)]
        
        processed_df = pd.DataFrame({
            "doc_id": doc_ids,
            "filenames" : document_names,
            "text": processed_text
        })

        try:
            output_file_name = "pre_processed docs with id.xlsx"
            processed_df.to_excel(output_file_name, index=False)
            print(f"Documents Pre-processing result saved in {output_file_name}")
        except Exception as e:
            print(f"Exception in saving result in excel : {e}")

    else:
        print(f"Invalid dataset path {dataset_path}")