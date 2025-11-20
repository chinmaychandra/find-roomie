# roommate_matcher.py

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import NearestNeighbors

def get_roommate_matches(user_id, csv_path="Data.csv"):
    # -------------------------------
    # STEP 1: Load dataset
    # -------------------------------
    df = pd.read_csv(csv_path)

    # -------------------------------
    # STEP 2: Extract user row
    # -------------------------------
    if user_id not in df['id'].values:
        raise ValueError("User ID not found in dataset")

    user_row = df[df['id'] == user_id].iloc[0]

    # store fields
    user_age = user_row['age']
    user_gender = user_row['gender']
    user_location = user_row['location']

    # -------------------------------
    # STEP 3: Remove user row temporarily
    # -------------------------------
    df = df[df['id'] != user_id]

    # -------------------------------
    # STEP 4: Keep age ± 6, same gender, same location
    # -------------------------------
    df = df[
        (df['gender'] == user_gender) &
        (df['location'] == user_location) &
        (df['age'].between(user_age - 6, user_age + 6))
    ]

    # If no valid candidates → return empty list
    if df.empty:
        return []

    # -------------------------------
    # STEP 5: Drop name, mobile, email
    # -------------------------------
    df = df.drop(columns=["name", "mobile no.", "email address"])

    # Also drop them from the user's row for consistent encoding
    user_row_reduced = user_row.drop(labels=["name", "mobile no.", "email address"])

    # -------------------------------
    # STEP 6: Remove id AFTER saving it
    # -------------------------------
    candidate_ids = df["id"].tolist()
    df_no_id = df.drop(columns=["id"])
    user_no_id = user_row_reduced.drop(labels=["id"])

    # -------------------------------
    # STEP 7: Encode categorical columns
    # -------------------------------
    le = LabelEncoder()

    encoded_df = df_no_id.copy()
    encoded_user = user_no_id.copy()

    for col in encoded_df.columns:
        if encoded_df[col].dtype == "object":
            # Fit on combined data to avoid unseen labels
            combined = pd.concat([encoded_df[col], pd.Series([encoded_user[col]])])
            le.fit(combined)

            encoded_df[col] = le.transform(encoded_df[col])
            encoded_user[col] = le.transform([encoded_user[col]])[0]

    # -------------------------------
    # STEP 8: KNN - 10 closest matches
    # -------------------------------
    knn = NearestNeighbors(n_neighbors=min(10, len(encoded_df)), metric='euclidean')
    knn.fit(encoded_df)

    # Convert encoded_user into a DataFrame with same columns
    encoded_user_df = pd.DataFrame([encoded_user], columns=encoded_df.columns)

    distances, indices = knn.kneighbors(encoded_user_df)

    matched_ids = [candidate_ids[i] for i in indices[0]]
    return matched_ids

