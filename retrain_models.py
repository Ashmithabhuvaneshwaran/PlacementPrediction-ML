import numpy as np
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import preprocessing

print("Training Placement Prediction Model...")
try:
    # Load data
    df = pd.read_csv('Placement_Prediction_data.csv', index_col=0)
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    df.fillna(0, inplace=True)
    
    # Prepare features and target
    x = df.drop(['StudentId', 'PlacementStatus'], axis=1)
    y = df['PlacementStatus']
    
    # Encode categorical variables
    le = preprocessing.LabelEncoder()
    if 'Internship' in x.columns:
        x['Internship'] = le.fit_transform(x['Internship'])
    if 'Hackathon' in x.columns:
        x['Hackathon'] = le.fit_transform(x['Hackathon'])
    
    # Train model
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=100)
    classify = RandomForestClassifier(n_estimators=100, criterion="entropy")
    classify.fit(x_train, y_train)
    
    # Evaluate
    from sklearn.metrics import accuracy_score
    ypred = classify.predict(x_test)
    accuracy = accuracy_score(ypred, y_test)
    print(f"Placement Model Accuracy: {accuracy}")
    
    # Save model
    joblib.dump(classify, 'model.pkl')
    print("Placement Model saved successfully!")
except Exception as e:
    print(f"Error training placement model: {e}")
    import traceback
    traceback.print_exc()

print("\nTraining Salary Prediction Model...")
try:
    # Load salary data
    df_salary = pd.read_csv('Salary_prediction_data.csv', index_col=0)
    df_salary = df_salary.loc[:, ~df_salary.columns.str.contains('^Unnamed')]
    df_salary.fillna(0, inplace=True)
    
    # Prepare features and target - drop StudentId AND salary
    x_sal = df_salary.drop(['StudentId', 'salary'], axis=1)
    y_sal = df_salary['salary']
    
    # Encode categorical variables
    le2 = preprocessing.LabelEncoder()
    if 'Internship' in x_sal.columns:
        x_sal['Internship'] = le2.fit_transform(x_sal['Internship'])
    if 'Hackathon' in x_sal.columns:
        x_sal['Hackathon'] = le2.fit_transform(x_sal['Hackathon'])
    if 'PlacementStatus' in x_sal.columns:
        x_sal['PlacementStatus'] = le2.fit_transform(x_sal['PlacementStatus'])
    
    # Train model
    x_train_sal, x_test_sal, y_train_sal, y_test_sal = train_test_split(x_sal, y_sal, test_size=0.3, random_state=100)
    classify_sal = RandomForestClassifier(n_estimators=100, criterion="entropy")
    classify_sal.fit(x_train_sal, y_train_sal)
    
    # Evaluate
    ypred_sal = classify_sal.predict(x_test_sal)
    accuracy_sal = accuracy_score(ypred_sal, y_test_sal)
    print(f"Salary Model Accuracy: {accuracy_sal}")
    
    # Save model
    joblib.dump(classify_sal, 'model1.pkl')
    print("Salary Model saved successfully!")
except Exception as e:
    print(f"Error training salary model: {e}")
    import traceback
    traceback.print_exc()

print("\nModels trained and saved with current sklearn version!")
