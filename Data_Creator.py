#data creator program simply run it, and it will create a data file of 10000 entries as datanew.csv

import csv
import random

# Male and Female Indian names
male_names = [
    "aarav", "vivaan", "aditya", "arjun", "aryan", "kabir", "om", "rahul", "rohan", "deepak",
    "amit", "vijay", "suresh", "manish", "gopal", "prateek", "ankit", "ravi", "karan", "sumit",
    "rajat", "abhishek", "tarun", "alok", "mohit", "shyam", "dinesh", "pankaj", "sandeep",
    "harshit", "varun", "arvind", "saurabh", "vivek", "ashish", "chetan", "naveen", "kiran", "manoj",
    "prashant", "nitin", "arun", "devesh", "rajesh", "puneet", "akshay", "harsh", "yash", "gaurav",
    "rakesh", "siddharth", "lalit", "sachin", "devansh", "amrit", "harpreet", "jaspreet", "gurpreet",
    "mandeep", "karandeep", "sukhmeet", "baljeet", "rajdeep", "farhan", "imtiaz", "salman", "amir",
    "rehman", "ramesh", "mahesh", "ganesh", "dilip", "narayan", "subhash", "rajan", "bala", "murali",
    "vignesh", "ashwin", "vinay", "tejas", "nitesh", "chirag", "adnan", "raunak", "anurag", "prem",
    "mukesh", "amitabh", "rajiv", "mahendra", "dev", "kunal", "parth", "jay", "charan", "deva", "mohan"
]

female_names = [
    "aanya", "siya", "advika", "ananya", "isha", "pari", "saanvi", "navya", "diya", "meera",
    "anjali", "neha", "pooja", "riya", "nikita", "swati", "shreya", "aarti", "tanya", "mansi",
    "ruchi", "sonali", "nisha", "priya", "sakshi", "pallavi", "divya", "sneha", "bhavna", "komal",
    "isha", "kavya", "muskan", "zoya", "tanvi", "radhika", "payal", "shruti", "aishwarya", "pragya",
    "sana", "nida", "afreen", "ayesha", "ramya", "keerthi", "sindhu", "nirmala", "lavanya", "sushma",
    "jyoti", "usha", "vidya", "reema", "rekha", "alisha", "geeta", "sarita", "neelam", "anjum",
    "fatima", "lata", "seema", "kamini", "nirmala", "poornima", "indu", "meenakshi", "madhu", "shobha",
    "vandana", "anjana", "sunita", "meenakshi", "bimla", "pushpa", "usha", "hema", "savita", "sangeeta",
    "parul", "usha", "tina", "prerna", "reshma", "radha", "geetha", "lavina", "varsha", "simran",
    "laxmi", "karishma", "poonam", "bhavya", "sonam", "anjana", "sejal", "veena", "urvashi", "anjum"
]

# Other categories
locations = ["mumbai", "delhi", "bangalore", "hyderabad", "ahmedabad", "chennai", "kolkata", "pune", "patna", "jaipur"]
active_time = ["morning-time", "night-owl", "humming bird"]
consumption = ["only drinks", "only smokes", "both", "none"]
hygiene = ["dr. sanitizer", "deo defender", "forgotten toothbrush"]
conditions = ["none", "thyroid", "diabetes", "obesity", "alzheimer’s", "migraine", "asthma"]
status = ["student", "working", "travelling"]
diet_types = ["vegetarian", "vegan", "non-vegetarian", "eggetarian"]
noise = ["quite", "moderate", "rock"]
social = ["introvert", "extrovert", "ambivert"]
hobbies = [
    "reading", "gardening", "playing a musical instrument", "painting", "cooking/baking",
    "hiking", "photography", "writing", "learning a new language", "video games"
]

headers = [
    "id", "name", "mobile no.", "email address", "age", "gender", "location", "specially-abled",
    "active-time", "consumption habits", "hygiene", "condition", "status", "diet",
    "noise tolerance", "social preference", "hobbies"
]

def random_mobile():
    return str(random.randint(6000000000, 9999999999))

def random_email(name):
    domains = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com"]
    return f"{name}{random.randint(1,999)}@{random.choice(domains)}"

data = []

for i in range(1, 10001):
    gender_prob = random.random()

    # Assign name and gender realistically
    if gender_prob < 0.48:
        name = random.choice(male_names)
        gender = "male"
    elif gender_prob < 0.96:
        name = random.choice(female_names)
        gender = "female"
    else:
        name = random.choice(male_names + female_names)
        gender = "others"

    # Specially-abled ratio 1 in 20
    specially_abled = "yes" if random.randint(1, 20) == 1 else "no"

    # Condition: 70% "none"
    condition = "none" if random.random() < 0.7 else random.choice(conditions[1:])

    # Diet: 3 in 4 vegetarian
    diet = "vegetarian" if random.random() < 0.75 else random.choice(diet_types[1:])

    row = [
        i,  # unique id
        name,
        random_mobile(),
        random_email(name),
        random.randint(16, 65),
        gender,
        random.choice(locations),
        specially_abled,
        random.choice(active_time),
        random.choice(consumption),
        random.choice(hygiene),
        condition,
        random.choice(status),
        diet,
        random.choice(noise),
        random.choice(social),
        random.choice(hobbies)
    ]
    data.append(row)

# Save to CSV
with open("Datanew.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(data)

print("✅ Dataset 'roommate_dataset.csv' created successfully with realistic distributions and unique IDs.")
