import pandas as pd

def register_user(data):
    try:
        # Load existing profile.csv
        profile = pd.read_csv("profile.csv")

        # Check ID availability
        if str(data["id"]) in profile["id"].astype(str).values:
            return "exists"

        # Append to profile.csv
        new_profile_row = pd.DataFrame([{
            "id": data["id"],
            "password": data["password"]
        }])
        new_profile_row.to_csv("profile.csv", mode="a", index=False, header=False)

        # Append to Data.csv (complete user record)
        data_csv = pd.read_csv("Data.csv")

        new_data_row = pd.DataFrame([{
            "id": data["id"],
            "name": data["name"],
            "mobile no.": data["mobile"],
            "email address": data["email"],
            "age": data["age"],
            "gender": data["gender"],
            "location": data["location"],
            "specially-abled": data["abled"],
            "active-time": data["active"],
            "consumption habits": data["consumption"],
            "hygiene": data["hygiene"],
            "condition": data["condition"],
            "status": data["status"],
            "diet": data["diet"],
            "noise tolerance": data["noise"],
            "social preference": data["social"],
            "hobbies": data["hobbies"]
        }])

        new_data_row.to_csv("Data.csv", mode="a", index=False, header=False)

        return "success"

    except Exception as e:
        print("Error:", e)
        return "error"
