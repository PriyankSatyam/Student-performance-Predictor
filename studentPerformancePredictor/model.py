import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load dataset
data = pd.read_csv("students.csv")

# Convert categorical to numeric
data = pd.get_dummies(data)

# Features and target
X = data.drop("math score", axis=1)
y = data["math score"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Prediction function
def predict_score(input_data):
    input_df = pd.DataFrame([input_data])
    input_df = pd.get_dummies(input_df)

    # Align columns with training data
    input_df = input_df.reindex(columns=X.columns, fill_value=0)

    prediction = model.predict(input_df)
    return round(prediction[0], 2)