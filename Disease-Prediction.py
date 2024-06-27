import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input
from sklearn.metrics import accuracy_score

# Load data
df = pd.read_csv("heartCorrected.csv", sep=";")
print(df.columns)
# Prepare data
# Convert categorical variables to dummy variables
X = pd.get_dummies(df.drop(["HeartDisease"], axis=1), drop_first=True)
y = df["HeartDisease"]

# Normalize the data
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Build the model
model = Sequential()
model.add(Input(shape=(X_train.shape[1],)))
model.add(Dense(units=32, activation="relu"))
model.add(Dense(units=64, activation="relu"))
model.add(Dense(units=1, activation="sigmoid"))

# Compile the model
model.compile(loss="binary_crossentropy", optimizer="sgd", metrics=["accuracy"])

# Train the model
model.fit(X_train, y_train, epochs=300, batch_size=18, validation_data=(X_test, y_test))

# Predict and evaluate the model
y_hat = model.predict(X_test)
y_hat_classes = (y_hat > 0.5).astype(int).flatten()

# Calculate accuracy
accuracy = accuracy_score(y_test, y_hat_classes)
print(f"Accuracy: {accuracy}")

# Print actual vs predicted for each sample in the test set
comparison = pd.DataFrame({"Actual": y_test, "Predicted": y_hat_classes})

for index, row in comparison.iterrows():
    print(f"Actual: {row['Actual']}, Predicted: {row['Predicted']}")

print(model.predict())
