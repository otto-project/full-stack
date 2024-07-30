import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error

for _ in range(601):
    # Read the data from the CSV file
    df = pd.read_csv("combined_reviews2.csv")

    # Convert height and weight columns to numeric
    df["height"] = pd.to_numeric(df["height"])
    df["weight"] = pd.to_numeric(df["weight"])

    # Encode the 'size' and 'size_comment' columns to numeric values
    size_label_encoder = LabelEncoder()
    df["size_encoded"] = size_label_encoder.fit_transform(df["size"])

    size_comment_label_encoder = LabelEncoder()
    df["size_comment_encoded"] = size_comment_label_encoder.fit_transform(
        df["size_comment"]
    )

    # Prepare the feature matrix and target vector
    X = df[["height", "weight"]]
    y = df["size_encoded"]

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Train the XGBoost model
    model = xgb.XGBRegressor(
        objective="reg:squarederror",
        n_estimators=100,
        learning_rate=0.1,
        max_depth=5,
        random_state=42,
    )
    model.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = model.predict(X_test)

    # Evaluate the model
    mse = mean_squared_error(y_test, y_pred)
    print(f"Mean Squared Error: {mse}")

    # Function to recommend size based on height and weight
    def recommend_size(
        height,
        weight,
        model,
        size_label_encoder,
        size_comment_label_encoder,
        df,
    ):
        size_encoded = model.predict(np.array([[height, weight]]))[0]
        size_label = size_label_encoder.inverse_transform([int(round(size_encoded))])[0]

        # Filter the dataset to find rows with the same predicted size
        filtered_df = df[df["size_encoded"] == int(round(size_encoded))]

        # Determine the most common size_comment for the predicted size
        most_common_size_comment = filtered_df["size_comment"].mode()[0]

        # Adjust the recommended size based on the most common size_comment
        if most_common_size_comment == "커요":
            if size_label == "S":
                return "S"
            elif size_label == "M":
                return "S"
            elif size_label == "L":
                return "M"
            elif size_label == "XL":
                return "L"
        elif most_common_size_comment == "보통이에요":
            return size_label
        elif most_common_size_comment == "작아요":
            if size_label == "S":
                return "M"
            elif size_label == "M":
                return "L"
            elif size_label == "L":
                return "XL"
            elif size_label == "XL":
                return "XL"

    # Example usage
    height_input = 163
    weight_input = 47

    recommended_size = recommend_size(
        height_input,
        weight_input,
        model,
        size_label_encoder,
        size_comment_label_encoder,
        df,
    )
    print(
        f"Recommended size for height {height_input} and weight {weight_input} is: {recommended_size}"
    )
