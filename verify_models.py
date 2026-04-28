import joblib
import pandas as pd
import numpy as np

print("=" * 60)
print("MODEL VERIFICATION SCRIPT")
print("=" * 60)

# Load models
try:
    model = joblib.load('model.pkl')
    model1 = joblib.load('model1.pkl')
    print("✓ Models loaded successfully")
except Exception as e:
    print(f"✗ Error loading models: {e}")
    exit(1)

# Check model properties
print(f"\nPlacement Model:")
print(f"  - Expected features: {model.n_features_in_}")
print(f"  - Feature names: {model.feature_names_in_ if hasattr(model, 'feature_names_in_') else 'Not available'}")

print(f"\nSalary Model:")
print(f"  - Expected features: {model1.n_features_in_}")
print(f"  - Feature names: {model1.feature_names_in_ if hasattr(model1, 'feature_names_in_') else 'Not available'}")

# Load training data to verify
df = pd.read_csv('Placement_Prediction_data.csv', index_col=0)
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
print(f"\nPlacement Data Features ({len(df.columns)} total):")
for i, col in enumerate(df.columns, 1):
    print(f"  {i}. {col}")

df_salary = pd.read_csv('Salary_prediction_data.csv', index_col=0)
df_salary = df_salary.loc[:, ~df_salary.columns.str.contains('^Unnamed')]
print(f"\nSalary Data Features ({len(df_salary.columns)} total):")
for i, col in enumerate(df_salary.columns, 1):
    print(f"  {i}. {col}")

# Test with example data
print("\n" + "=" * 60)
print("EXAMPLE INPUT FOR APP")
print("=" * 60)

example_input = {
    'name': 'John Doe',
    'cgpa': '8.5',
    'projects': '3',
    'workshops': '2',
    'mini_projects': '2',
    'skills': 'Python,Java,ML',  # Count of comma-separated = 3 skills
    'communication_skills': '4.0',
    'internship': 'Yes',  # Will be encoded to 1
    'hackathon': 'Yes',   # Will be encoded to 1
    'tw_percentage': '80',  # 12th percentage
    'te_percentage': '85',  # 10th percentage
    'backlogs': '0'
}

print("\nExample JSON/Form Input:")
for key, value in example_input.items():
    print(f"  {key}: {value}")

# Create feature array as the app would
from sklearn import preprocessing

print("\n" + "=" * 60)
print("FEATURE ARRAY GENERATION")
print("=" * 60)

# Count skills
skills_list = example_input['skills'].split(',')
skill_count = len(skills_list)
print(f"Skills count: {skill_count}")

# Prepare placement prediction input
arr = np.array([
    float(example_input['cgpa']),
    float(example_input['projects']),
    float(example_input['workshops']),
    float(example_input['mini_projects']),
    skill_count,
    float(example_input['communication_skills']),
    1.0 if example_input['internship'].lower() == 'yes' else 0.0,
    1.0 if example_input['hackathon'].lower() == 'yes' else 0.0,
    float(example_input['tw_percentage']),
    float(example_input['te_percentage']),
    float(example_input['backlogs'])
])

print(f"\nPlacement Input Array ({len(arr)} features):")
print(f"  {arr}")

# Test placement prediction
try:
    placement_result = model.predict([arr])
    print(f"\nPlacement Prediction: {placement_result[0]}")
except Exception as e:
    print(f"\n✗ Placement Prediction Error: {e}")

# Prepare salary prediction input
placement_status = 1 if placement_result[0] == 'Placed' else 0
arr_salary = np.append(arr, placement_status)

print(f"\nSalary Input Array ({len(arr_salary)} features):")
print(f"  {arr_salary}")

# Test salary prediction
try:
    salary_result = model1.predict([arr_salary])
    print(f"\nSalary Prediction: ₹{int(salary_result[0]):,}")
except Exception as e:
    print(f"\n✗ Salary Prediction Error: {e}")

print("\n" + "=" * 60)
