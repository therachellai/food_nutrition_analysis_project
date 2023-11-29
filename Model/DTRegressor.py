import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split


class DecisionTreeRegressorModel:
    def author():
        return ['Rachel Yu-Wei Lai']

    def __init__(self, data):
        self.data = data

    def split_data(self, test_size=0.2, random_state=None):
        X = self.data[['suga_to_total', 'fat_to_total', 'pro_to_total', 'carb_to_total', 'satu_to_total', 'tran_to_total']]
        y = self.data['Score']
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=test_size, 
                                                                                random_state=random_state)

    def train_model(self):
        self.model = DecisionTreeRegressor(random_state=42)
        self.model.fit(self.X_train, self.y_train)

    def evaluate_model(self):
        y_pred = self.model.predict(self.X_test)
        mse = mean_squared_error(self.y_test, y_pred)
        r2 = r2_score(self.y_test, y_pred)
        return mse, r2

    def get_feature_importance(self):
        return self.model.feature_importances_

def convert_info_to_df(df: pd.DataFrame)-> pd.DataFrame:
    columns = ['Name', 'suga_to_total', 'fat_to_total', 'pro_to_total', 'carb_to_total', 'satu_to_total', 'tran_to_total', 'Score', 'Category']  # Replace these with your column names
    nutrition = pd.DataFrame(columns=columns)
    nutrition['Name'] = df['Name']
    nutrition['Score'] = df['Score']
    nutrition['Category'] = df['Category']
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
    df = pd.read_csv('INPUTS/data_for_model_training.csv')
    df = convert_info_to_df(df)
    df = df.dropna()

    model = DecisionTreeRegressorModel(df)
    model.split_data(test_size=0.2, random_state=42)
    model.train_model()
    mse, r2 = model.evaluate_model()
    feature_importance = model.get_feature_importance()

    print(f"Mean Squared Error: {mse}")
    print(f"R-squared (R2) Score: {r2}")
    print("Feature Importance:")
    for feature, importance in zip(df.columns[1:], feature_importance):
        print(f"{feature}: {importance}")
    
    # this is for making predictions in new data
    # new_data = pd.read_csv('NEW_DATA.csv')    
    # predicted_scores = model.model.predict(new_data[['suga_to_total', 'fat_to_total', 'pro_to_total', 'carb_to_total', 'satu_to_total', 'tran_to_total']])   
    