import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import joblib

# Load the dataset
file_path = 'students_placement.xlsx'
df = pd.read_excel(file_path)

# Separate features and target
X = df[['cgpa', 'iq', 'profile_score']]
y = df['placed']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train the logistic regression model
model = LogisticRegression()
model.fit(X_train_scaled, y_train)

# Save the model using joblib
joblib.dump(model, 'logistic_model.joblib')
joblib.dump(scaler, 'scaler.joblib')
