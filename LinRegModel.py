import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

"""
    THIS IS A ROUGH OUTLINE OF OUR LINEAR REGRESSION MODEL
    NOTHING IS SERIOUS YET!
    We are going to add more features
    Information is going to come from the website that has over 80'000 foods:
    I have searched one of my commonly purchased protein cookie and we are using the first
    nutrition score from their as our y value
    https://www.ewg.org/foodscores/products/888849006045-QuestProteinCookiePeanutButter/

Returns:
    _type_: dictionary of coefficients
"""

class LinearRegressionModel:
    def __init__(self, data):
        self.data = data

    def split_data(self, test_size=0.2, random_state=None):
        X = self.data[['Protein', 'Fat', 'Carbs', 'Trans Fat']]
        y = self.data['Healthy Score']
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=test_size, 
                                                                                random_state=random_state)

    def train_model(self):
        self.model = LinearRegression()
        self.model.fit(self.X_train, self.y_train)

    def evaluate_model(self):
        y_pred = self.model.predict(self.X_test)
        mse = mean_squared_error(self.y_test, y_pred)
        r2 = r2_score(self.y_test, y_pred)
        return mse, r2

    def get_coefficients(self):
        return {
            'Protein': self.model.coef_[0],
            'Fat': self.model.coef_[1],
            'Carbs': self.model.coef_[2],
            'Trans Fat': self.model.coef_[3],
            'Intercept': self.model.intercept_
        }

if __name__ == "__main__":
    # df is our dataFrame with features 'Protein', 'Fat', 'Carbs', 'Trans Fat', and a score to evaluate healthiness
    model = LinearRegressionModel(df)
    model.split_data(test_size=0.2, random_state=42)
    model.train_model()
    mse, r2 = model.evaluate_model()
    coefficients = model.get_coefficients()

    print(f"Mean Squared Error: {mse}")
    print(f"R-squared (R2) Score: {r2}")
    print("Model Coefficients:")
    for feature, coef in coefficients.items():
        print(f"{feature}: {coef}")
        
    # make predictions on new data