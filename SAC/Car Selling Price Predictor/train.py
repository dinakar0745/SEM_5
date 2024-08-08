import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib
from sklearn.metrics import r2_score

# Load the dataset
data = pd.read_csv('car_prices_dataset.csv')

# Features and target variable
X = data[['Age', 'Mileage']]
y = data['Selling Price']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)

# Accuracy
accuracy = r2_score(y_test, y_pred)
print(f"Model accuracy (R² score): {accuracy:.2f}")


# Save the trained model to a file
joblib.dump(model, 'car_price_model.pkl')

print("Model trained and saved as car_price_model.pkl")
