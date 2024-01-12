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
from dataclasses import dataclass


docs_query_jar_file = "qdocs.jar"
project_dir = "E:\Code\OvGU\Information Retrieval\Search Result Clustering"

cwd = os.getcwd()
docs_query_jar_file_path = os.path.join(cwd, "Preprocessing", docs_query_jar_file)
print(docs_query_jar_file_path)
jnius_config.set_classpath(docs_query_jar_file_path)

from jnius import autoclass

# Receiving query from user and calling java class function to retrieve relevant docs
QueryDocuments = autoclass("QueryDocuments")
DocumentPreprocessor = autoclass("DocumentPreprocessor")
qDoc = QueryDocuments()
docPreprocessor = DocumentPreprocessor()

def concat(tokens, divider = " "):
    res = ""
    for ti in tokens:
        res += ti + divider
    return res.strip()


query = input("Enter Query: ")
no_of_results = int(input("No of results expected: "))

json_result = qDoc.query(query, no_of_results)
result = json.loads(json_result)

# Preprocess retrieved relevant doc for Kmeans
preprocessed_docs = []
for ri in result:
    pp_doc = docPreprocessor.preprocess(ri["content"])
    pp_doc_list = [i for i in pp_doc]
    preprocessed_docs.append(concat(pp_doc_list))

# print(preprocessed_docs)

df = pd.DataFrame(result)
df["preprocessed"] = preprocessed_docs

# print(df)

# TF-IDF Vectorization
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(df["preprocessed"])

# print(tfidf_matrix.shape[0]) # no of docs

K = int(math.sqrt(len(df))) # No of clusters
clustering_model = KMeans(n_clusters = K, 
                          init = 'k-means++',
                          max_iter = 300, n_init = 10)
clustering_model.fit(tfidf_matrix)

clusters = [clustering_model.predict(tfidf_matrix[i])[0] for i in range(tfidf_matrix.shape[0])]
df["cluster"] = clusters

print(df)

final_cluster_res = {}
for cluster_i in range(K):
    docs = []
    fil_df = df[df["cluster"] == cluster_i]
    cluster_size = fil_df.shape[0]
    cluster_label = str(cluster_i)

    # iterate through docs belonging to cluster i
    for index in fil_df.index:
        
        doc_dict = {
            "doc_id" : int(fil_df["docId"][index]),
            "name" : fil_df["docName"][index],
            "content" : fil_df["content"][index]
        }

        print(type(fil_df["docId"][index]), type(fil_df["docName"][index]), type(fil_df["content"][index]))

        docs.append(doc_dict)

    res = {
        "label": cluster_label,
        "size": cluster_size,
        "documents": docs
    }

    print(type(cluster_label), type(cluster_size), type(docs))

    final_cluster_res[cluster_i] = res

print(final_cluster_res)

json_res = json.dumps(final_cluster_res, indent=4)
with open('cluster_res.json', 'w') as file:
    file.write(json_res)