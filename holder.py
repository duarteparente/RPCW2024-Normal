import pandas as pd

df1 = pd.read_csv("data/Disease_Syntoms.csv")
df2 = pd.read_csv("data/Disease_Description.csv")
df3 = pd.read_csv("data/Disease_Treatment.csv")

previous_symptons = ["Fever", "Cough", "SoreThroat", "IncreasedThirst", "FrequentUrination", "Fatigue"]
new_symptoms = set()

previous_treatments = ["Rest", "Hydration", "AntiviralDrugs", "InsulinTherapy", "DietModification", "Exercise"]
new_treatments = set()

disease_description = {}

for _, row in df2.iterrows():
    disease = row['Disease'].strip().replace('(', '_').replace(')', '_')
    disease_description[disease] = row['Description']


disease_treatment = {}

for _, row in df3.iterrows():
    disease = row['Disease'].strip().replace('(', '_').replace(')', '_')

    if disease not in disease_treatment:
        disease_treatment[disease] = set()
    
    treatments = row[1:].dropna().tolist()

    for treatment in treatments:
        if treatment not in new_treatments and treatment not in previous_treatments:
            new_treatments.add(treatment)
        disease_treatment[disease].add(treatment)


disease_symptoms = {}

for _, row in df1.iterrows():
    disease = row['Disease'].strip().replace('(', '_').replace(')', '_')

    if disease not in disease_symptoms:
        disease_symptoms[disease] = set()

    symptoms = row[1:].dropna().tolist()

    for symptom in symptoms:
        if symptom not in previous_symptons:
            new_symptoms.add(symptom)
            disease_symptoms[disease].add(symptom)

for disease, symptoms in disease_symptoms.items():
    print(f":{disease.replace(' ', '-')} a :Disease ;")
    formatted_symptoms = ", ".join([f":{symptom.replace(' ', '').replace('(', '_').replace(')', '_')}" for symptom in symptoms])
    final = f'    :hasSymptom {formatted_symptoms} ;'
    
    if disease in disease_description:
        print(final)
        print(f'    :hasDescription "{disease_description[disease]}" .\n\n')
    else:
        final = final[:-1] + ". \n\n"
        print(final)

print("------------------------")

for treatment in new_treatments:
    print(f":{treatment.replace(' ', '').replace('(', '_').replace(')', '_')} a :Treatment .")