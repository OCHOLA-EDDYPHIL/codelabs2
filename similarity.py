"""
This module contains the functions to calculate the similarity between males and females
"""
import pandas as pd
import transformers
transformers.utils.hub.default_timeout = 60  # Set timeout to 60 seconds
import json
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer


def split_names(df):
    # Ensure that 'Gender' and 'Student Name' columns exist
    if 'Gender' not in df.columns or 'Student Name' not in df.columns:
        raise ValueError("DataFrame must contain 'Gender' and 'Student Name' columns")

    # Split male and female names
    male_names = df[df['Gender'] == 'M']['Student Name'].tolist()
    female_names = df[df['Gender'] == 'F']['Student Name'].tolist()
    return male_names, female_names


def compute_similarity(male_names, female_names, output_path, threshold=0.5):
    # Load the LaBSE model
    model = SentenceTransformer('sentence-Transformer/LaBSE')
    results = []

    # Compute embeddings for male and female names
    male_embeddings = model.encode(male_names, convert_to_tensor=True)
    female_embeddings = model.encode(female_names, convert_to_tensor=True)

    # Compute cosine similarity matrix
    similarity_matrix = cosine_similarity(male_embeddings.cpu(), female_embeddings.cpu())

    for i, male_name in enumerate(male_names):
        for j, female_name in enumerate(female_names):
            similarity_score = similarity_matrix[i][j]
            if similarity_score >= threshold:
                results.append({
                    'male_name': male_name,
                    'female_name': female_name,
                    'similarity_score': similarity_score
                })

    # Save results
    with open(output_path / 'similarity_results.json', 'w') as f:
        json.dump(results, f, indent=4)
    print(f"Similarity results saved to {output_path / 'similarity_results.json'}")
