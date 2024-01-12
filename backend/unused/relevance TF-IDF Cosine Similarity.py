import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from NltkPreprocessingSteps import NltkPreprocessingSteps
import os, sys

os.chdir("E:\Code\OvGU\Information Retrieval\Search Result Clustering")

preprocessed_doc_file_path = 'pre_processed docs with id.xlsx'  
original_doc_file_path = "big dataset input docs.xlsx"
preprocessed_doc_path_exist = os.path.exists(preprocessed_doc_file_path)
original_doc_path_exits = os.path.exists(original_doc_file_path)

if not preprocessed_doc_path_exist or not original_doc_path_exits:
    print(f"Document path doesn't exists: preprocessed_doc_path_exist- {preprocessed_doc_path_exist}, original_doc_path_exits: {original_doc_path_exits}")
    sys.exit(1)

ppdoc_df = pd.read_excel(preprocessed_doc_file_path)
odoc_df = pd.read_excel(original_doc_file_path)
query = input("Please Ente your Query: ")
query_dict = {
    "doc_id":-1,
    "filenames":"query",
    "text": query
}

query_df = pd.DataFrame(query_dict, index=[0])

# Preprocess query
txt_preproc = NltkPreprocessingSteps(query_df['text'])
processed_query = \
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

ppdoc_df.loc[len(ppdoc_df.index)] = [-1, "query", processed_query[0]]

# TF-IDF Vectorization
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(ppdoc_df["text"])

# Cosine Similarity
res = []
for i in range(tfidf_matrix.shape[0]-1):
    sim = cosine_similarity(tfidf_matrix[i], tfidf_matrix[-1])
    if sim > 0:
        res.append([sim, odoc_df.loc[i]])

# Displaying result
res.sort(key=lambda r: r[0], reverse=True)
print("Query: ",query, end="\n\n")

display_res_limit = 50 if len(res) > 10 else len(res)

for x in range(display_res_limit):
    print("Rank",(x+1))
    print("Sim: ",res[x][0])
    print("File name: ",res[x][1]["filenames"])
    print("Doc: ", res[x][1]["text"], end="\n\n")