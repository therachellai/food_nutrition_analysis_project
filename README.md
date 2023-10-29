# Food Nutrition Analysis Project

## Nutritional Information

Smart food labeling provides a comprehensive breakdown of the nutritional information associated with the food product. The AI system scrutinizes the extracted text to ascertain the quantities of macronutrients (such as carbohydrates, proteins, and fats), micronutrients (including vitamins and minerals), and the total caloric content. This information is presented in a user-friendly format, allowing consumers to make informed decisions regarding their dietary choices.

## Ingredient Analysis (Customizable User Profile Later)

A core aspect of smart food labeling is the meticulous analysis of the ingredients employed in food products. The AI system scrutinizes the extracted ingredients list, cross-referencing it against an extensive database of recognized ingredients. This analysis aids in identifying specific components, including allergens, additives, preservatives, or artificial sweeteners that may be present in the product. This level of transparency empowers consumers to quickly ascertain whether a product aligns with their dietary needs or restrictions.

## How to install virtual environments
1. Install Anaconda/miniconda
2. If creating VM for the first time
'''conda env create -f environment.yml'''
3. Activate VM:
'''conda activate food_nutrition_analysis'''
4. Every time you install a package, you are OBLIGED to update environment.yml:
First, google whether condas has this package; if so,  use conda to install 
'conda install xxx', if not, install pip in your conda, and use the path to your pip (for example, mine is '/Users/rachellai/miniconda3/envs/food_nutrition_analysis/bin/pip') install to install the package
5. Update environment.yml
'''conda env export | grep -v "^prefix: " > environment.yml'''
6. if a conda env already exists, update existing conda env from updated yml: 
'''
conda activate {myenv}
conda env update --file environment.yml --prune
'''
7. If you want to exit the VM:
'''conda deactivate'''

## How to Run

1. Create folders named "OUTPUTS" and "INPUTS" (unless they are already there).
2. Store the interested image in the "INPUTS" folder

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