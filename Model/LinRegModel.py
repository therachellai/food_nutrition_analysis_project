import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

"""
    Linear Regression Model

Returns:
    _type_: dictionary of coefficients
"""

class LinearRegressionModel:
    def author():
        """
        Returns:
        author name in list
        """
        return ['Rachel Yu-Wei Lai']

    def __init__(self, data):
        self.data = data

    def split_data(self, test_size=0.2, random_state=None):
        X = self.data[['suga_to_total', 'fat_to_total', 'pro_to_total', 'carb_to_total', 'satu_to_total', 'tran_to_total']]
        y = self.data['Score']
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
            'suga_to_total': self.model.coef_[0],
            'fat_to_total': self.model.coef_[1],
            'pro_to_total': self.model.coef_[2],
            'carb_to_total': self.model.coef_[3],
            'satu_to_total': self.model.coef_[4],
            'satu_to_total': self.model.coef_[5],
            'Intercept': self.model.intercept_
        }
    def predict_new_data(self, new_data):
        suga_to_total = round(new_data['Added Sugar'] * 4 / new_data['Calories'], 4)
        fat_to_total = round(new_data['Total Fat'] * 9 / new_data['Calories'], 4)
        pro_to_total = round(new_data['Protein'] * 4 / new_data['Calories'], 4)
        carb_to_total = round(new_data['Total Carbohydrate'] * 4 / new_data['Calories'], 4)
        satu_to_total = round(new_data['Saturated Fat'] * 9 / new_data['Calories'], 4)
        tran_to_total = round(new_data['Trans Fat'] * 9 / new_data['Calories'], 4)

        new_data_features = [[suga_to_total, fat_to_total, pro_to_total, carb_to_total, satu_to_total, tran_to_total]]
        predicted_score = self.model.predict(new_data_features)
        return predicted_score[0]
        
def convert_info_to_df_databse_lr(df: pd.DataFrame)-> pd.DataFrame:
    columns = ['category', 'suga_to_total', 'fat_to_total', 'pro_to_total', 'carb_to_total', 'satu_to_total', 'tran_to_total', 'Score', 'category']  # Replace these with your column names
    nutrition = pd.DataFrame(columns=columns)
    nutrition['Name'] = df['Name']
    nutrition['Score'] = df['Score']
    nutrition['category'] = df['Category']
    # Calories from Added Sugar vs Total Calories
    nutrition['suga_to_total'] = round(df['Added Sugar'] * 4 / df['Calories'], 4)
    # Calories from Fat vs Total Calories
    nutrition['fat_to_total'] = round(df['Total Fat'] * 9 / df['Calories'], 4)
    # Calories from Protein vs Total Calories
    nutrition['pro_to_total'] = round(df['Protein'] * 4 / df['Calories'], 4)
    # Calories from Carbohydrates vs Total Calories
    nutrition['carb_to_total'] = round(df['Total Carbohydrate'] * 4 / df['Calories'], 4)
    # Calories from Saturated Fat vs Total Calories
    nutrition['satu_to_total'] = round(df['Saturated Fat'] * 9 / df['Calories'], 4)
    # Calories from Trans Fat vs Total Calories
    nutrition['tran_to_total'] = round(df['Trans Fat'] * 9 / df['Calories'], 4)
    return nutrition


if __name__ == "__main__":
    # df is our dataFrame with features 'Protein', 'Fat', 'Carbs', 'Trans Fat', and a score to evaluate healthiness
    df = pd.read_csv('INPUTS/data_for_model_training.csv')
    print(df)
    df = convert_info_to_df_databse_lr(df)
    print(df)
    df = df.dropna()
    print(df)
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
    # new_data = pd.read_csv('NEW_DATA.csv')
    # predicted_scores = model.predict_new_data(new_data)