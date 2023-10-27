# Food Nutrition Analysis Project

## Nutritional Information

Smart food labeling provides a comprehensive breakdown of the nutritional information associated with the food product. The AI system scrutinizes the extracted text to ascertain the quantities of macronutrients (such as carbohydrates, proteins, and fats), micronutrients (including vitamins and minerals), and the total caloric content. This information is presented in a user-friendly format, allowing consumers to make informed decisions regarding their dietary choices.

## Ingredient Analysis (Customizable User Profile Later)

A core aspect of smart food labeling is the meticulous analysis of the ingredients employed in food products. The AI system scrutinizes the extracted ingredients list, cross-referencing it against an extensive database of recognized ingredients. This analysis aids in identifying specific components, including allergens, additives, preservatives, or artificial sweeteners that may be present in the product. This level of transparency empowers consumers to quickly ascertain whether a product aligns with their dietary needs or restrictions.

## How to Run

1. Create folders named "OUTPUTS" and "INPUTS" (unless they are already there).
2. Store the interested image in the "INPUTS" folder
3. pip install easyOCR      # for OCR
4. pip install tabula
5. pip install pandas       # for data analysis
6. pip install pillow       # for converting image to pdf
7. pip install scikit-learn     # for training machine learning models
8. pip install openai       # for LM
9. pip install streamlit    # for visualization

## How This Will Go Down
1. Ingredient Side:
    1.1 Take the ingredient list photo of the food we are interested in, and run LangModel.py on it.
    1.2 This will show GPT's rating of the food based on the ingredient list
2. Nutrition Side
    2.1 Gather lots of food label pictures from the website (https://www.ewg.org/foodscores/products/888849006045-QuestProteinCookiePeanutButter/) or in person
    2.2 Run them through ReadImage.py to get text, which in the same file, can have its info extracted and put
        into a single-row dataFrame. Using the same file, add another column of "score", which can be found on
        the website.
    2.3 Run CleanData on all the df entries from the pdf to concatenate them to a large df
    2.4 Run LinRegModel (and possibly other models in the future) using the df we have gotten from the previous step.
        Test model accuracy and efficiency. Finetune it. Then make predictions.
3. Putting It Together
    3.1 Conduct user centered research on our own time
    3.2 Run VisualizeData, which uses the streamlit framework to visualize data we have collected from users and 
        the models
        (streamlit run VisualizeData.py)

# Clean Code and Logistics

1. Please add your name to the author() method or implement a new one if it is something you are working on.
2. Please always include a doc string and time cast for new functions