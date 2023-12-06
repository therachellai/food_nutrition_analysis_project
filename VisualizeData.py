import streamlit as st
from PIL import Image
from CollectDataForTarget.CollectData import *
from Model.LinRegModel import *
from Model.DTRegressor import *
from Model.LangModel import *

def main():
    
    # Create a title for your app
    st.title("Food Nutrition Analyzer")
    st.write("Welcome to our streamlit dashboard that takes food nutrition analysis and recommendation to the next level")    
    st.title('Upload Photo')

    uploaded_file = st.file_uploader("Choose a photo...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Photo', use_column_width=True)
        
    if st.button('Analyze Food Label'):
        try:
            text_result = read_text(image)
            
            st.subheader('Extracted Text:')
            for text in text_result:
                st.write(text)  # Display the recognized text

        except Exception as e:
            st.error(f"Error: {e}")
                
    st.subheader('Extracted Info:')
    extracted_info = extract_info_from_text(text_result, 'meals')
    st.write(extracted_info)
    
    st.subheader('Organized Data for Analysis:')
    converted_df = convert_info_to_df(extracted_info)
    st.write(converted_df)
    
#############################

    st.title('Two Machine Learning Models')
    st.subheader('* We are choosing the model with ')

    # Using columns to display text side by side
    col1, col2 = st.columns(2)  # Split the layout into 2 columns
    
    with col1:
        st.header('Linear Model')
        data_for_model_training_raw = pd.read_csv('INPUTS/data_for_model_training.csv')
        data_for_model_training = convert_info_to_df_databse_lr(data_for_model_training_raw)
        data_for_model_training = data_for_model_training.dropna()
        linear_model = LinearRegressionModel(data_for_model_training)
        linear_model.split_data(test_size=0.2, random_state=42)
        linear_model.train_model()
        mse, r2 = linear_model.evaluate_model()
        coefficients = linear_model.get_coefficients()

        st.write("**Mean Squared Error**", f": {mse}")
        st.write("**R-squared (R2) Score**", f": {r2}")
        st.write("**Model Coefficients:**")
        for feature, coef in coefficients.items():
            st.write(f"{feature}: {coef}")
        
    with col2:
        data_for_model_training_raw = pd.read_csv('INPUTS/data_for_model_training.csv')
        data_for_model_training = convert_info_to_df_database_dt(data_for_model_training_raw)
        data_for_model_training = data_for_model_training.dropna()

        dt_model = DecisionTreeRegressorModel(data_for_model_training)
        dt_model.split_data(test_size=0.2, random_state=42)
        dt_model.train_model()
        mse, r2 = dt_model.evaluate_model()
        feature_importance = dt_model.get_feature_importance()

        st.header('Decision Tree Regressor')
        st.write("**Mean Squared Error**", f": {mse}")
        st.write("**R-squared (R2) Score**", f": {r2}")
        st.write("**Feature Importance:**")
        for feature, importance in zip(data_for_model_training.columns[1:], feature_importance):
            st.write(f"{feature}: {importance}")

    predicted_score = linear_model.model.predict(converted_df.drop('category', axis=1))[0]
    st.header('Estimated Score')
    st.subheader('From the Linear Regression Model:')
    st.write(f"*{predicted_score}*")

    ########################################################## 
    
    """ This is the space for implementing the language model """
    lang_model = LanguageModel()
    lang_score = lang_model.language_model_ingredients(uploaded_file)
    st.write(f"language_score: {lang_score}")
    
    ##########################################################
    
    if predicted_score <= 4:
        st.write('This food is great. Nice choice!')
    elif predicted_score <= 6 and predicted_score > 4:
        st.write('This food is fine. You can consume it as is. However, here are a few options:')
        category_value = converted_df['category'][0]
        recommendation_dataset = data_for_model_training[data_for_model_training['category'] == category_value]
        recommendation_dataset = recommendation_dataset.sort_values('Score', ascending=True)
        first_recommendation = recommendation_dataset.iloc[0]
        second_recommendation = recommendation_dataset.iloc[1]
        recommendations = [first_recommendation, second_recommendation]
        recommendations = [df for df in recommendations if df['Score'].max() < 6]
        for df in recommendations:
            st.write(df)
    else:
        st.write('This food is not good for your health. Please take a look at healthier options:')
        category_value = converted_df['category'][0]
        recommendation_dataset = data_for_model_training[data_for_model_training['category'] == category_value]
        recommendation_dataset = recommendation_dataset.sort_values('Score', ascending=True)
        first_recommendation = recommendation_dataset.iloc[0]
        second_recommendation = recommendation_dataset.iloc[1]
        recommendations = [first_recommendation, second_recommendation]
        recommendations = [df for df in recommendations if df['Score'].max() < 6]
        for df in recommendations:
            st.write(df)
    
if __name__ == '__main__':
    main()
