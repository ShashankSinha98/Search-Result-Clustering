import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from NltkPreprocessingSteps import NltkPreprocessingSteps

# Load data from Excel sheet
excel_file_path = 'data.xlsx'  # Update with your file path
df = pd.read_excel(excel_file_path)

# Accept query string from the user
query = input("Enter your query: ")
txt_preproc = NltkPreprocessingSteps(query['text'])

processed_query = \
            txt_preproc \
            .remove_html_tags()\
            .replace_diacritics()\
            .expand_contractions()\
            .remove_numbers()\
            .fix_typos()\
            .remove_punctuations_except_periods()\
            .lemmatize()\
            .remove_double_spaces()\
            .remove_all_punctuations()\
            .remove_stopwords()\
            .get_processed_text()

# TF-IDF Vectorization
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(df['text'].append(pd.Series(processed_query)))

# Calculate cosine similarity
cosine_similarities = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1]).flatten()

# Get indices of top 50 similar documents
top_indices = cosine_similarities.argsort()[:-51:-1]

# Display the top 50 relevant documents
print("\nTop 50 Relevant Documents:")
for i, idx in enumerate(top_indices, 1):
    print(f"{i}. Document #{idx + 1} - Similarity: {cosine_similarities[idx]:.4f}")
    print(df['text'][idx])
    print("-" * 30)

