import pandas as pd

def validate_credentials(user_id, password):
    try:
        df = pd.read_csv("profile.csv")

        # convert everything to str so comparison is safe
        df["id"] = df["id"].astype(str)
        df["password"] = df["password"].astype(str)

        # check match
        match = df[(df["id"] == str(user_id)) & (df["password"] == str(password))]

        return not match.empty
    except Exception as e:
        print("Error:", e)
        return False
