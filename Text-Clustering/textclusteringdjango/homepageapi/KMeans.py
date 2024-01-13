# Import all libs
import os
import json
from typing import Any
import jnius_config
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import math
import numpy as np

docs_query_jar_file = "qdocs.jar" # This jar must be inside Search Result Clustering/Preprocessing/ 
project_dir = "E:\Code\OvGU\Information Retrieval\Search Result Clustering" # Replace with your project root dir

os.chdir(project_dir)
cwd = os.getcwd()
docs_query_jar_file_path = os.path.join(cwd, "Preprocessing", docs_query_jar_file)
print(docs_query_jar_file_path)

jnius_config.set_classpath(docs_query_jar_file_path)

from jnius import autoclass

# Receiving query from user and calling java class function to retrieve relevant docs
QueryDocuments = autoclass("QueryDocuments")
DocumentPreprocessor = autoclass("DocumentPreprocessor")
queryDocs = QueryDocuments()
docPreprocessor = DocumentPreprocessor()


def queryCluster(query: str, no_of_results: int = 50, K: int = 7, save_result: bool=False) -> str:
    # Run query to lucene and fetch relevant docs in json
    json_result = queryDocs.query(query, no_of_results)
    result = json.loads(json_result)

    # Preprocess retrieved relevant doc for Kmeans
    preprocessed_docs = []
    for ri in result:
        pp_doc = docPreprocessor.preprocess(ri["content"])
        pp_doc_list = [i for i in pp_doc]
        preprocessed_docs.append(concat(pp_doc_list))

    df = pd.DataFrame(result)
    df["preprocessed"] = preprocessed_docs

    # TF-IDF Vectorization
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(df["preprocessed"])

    # K Means
    #K = int(math.sqrt(len(df))) # No of clusters
    clustering_model = KMeans(n_clusters = K, 
                            init = 'k-means++',
                            max_iter = 300, n_init = 10)
    clustering_model.fit(tfidf_matrix)

    # Add cluster values in dataframe
    clusters = [clustering_model.predict(tfidf_matrix[i])[0] for i in range(tfidf_matrix.shape[0])]
    df["cluster"] = clusters


    # Generate final json result for frontend
    final_cluster_res = []
    for cluster_i in range(K):
        docs = []
        fil_df = df[df["cluster"] == cluster_i]
        cluster_size = fil_df.shape[0]
        cluster_label = str(cluster_i+1)

        # iterate through docs belonging to cluster i
        for index in fil_df.index:
            
            doc_dict = {
                "doc_id" : int(fil_df["docId"][index]),
                "name" : fil_df["docName"][index],
                "content" : fil_df["content"][index]
            }

            docs.append(doc_dict)

        res = {
            "label": "Cluster: "+cluster_label,
            "size": cluster_size,
            "documents": docs
        }

        final_cluster_res.append(res)

    json_res = json.dumps(final_cluster_res, indent=4)

    if save_result:
        with open('cluster_result.json', 'w') as file:
            file.write(json_res)

    return json_res


def concat(tokens, divider = " "):
    res = ""
    for ti in tokens:
        res += ti + divider
    return res.strip()


# if __name__ =="__main__":
#     while int(input("Continue (1/0)?: ")) != 0:
#         # Ask for inputs from user
#         query = input("Enter Query: ")
#         no_of_results = int(input("No of results expected: "))
        
#         json_res = queryCluster(query, no_of_results, True)
#         print(json_res)

