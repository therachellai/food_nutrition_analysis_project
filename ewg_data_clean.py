import pandas as pd
import re


def author():
    """
    Returns:
       author name in list
    """
    return ['Mingjun Shen']


def parse_and_convert(value):
    match = re.match(r'<?(\d+(\.\d+)?)\s*(\D+)', str(value).replace(' ', ''))
    if match:
        number, _, unit = match.groups()
        unit_mapping = {
            'g': 1,
            'mg': 0.001,
            'q': 1,
            '[g, g]': 1,
            'g*': 1,
            'g,': 1,
            '%': 1,
        }
        if unit.lower() in unit_mapping:
            return float(number) * unit_mapping[unit.lower()]
    elif str(value).replace('<', '').isdigit():
        return str(value).replace('<', '')
    else:
        return "Invalid Data"


def rename(df):
    df = df[['uid', 'name', 'score', 'Calories', 'Total Fat', 'Total Carbs', 'Protein', 'Saturated Fat', 'Trans Fat',
             'Cholesterol', 'Sodium', 'Added Sugar Ingredients:', 'Dietary Fiber', 'Sugars', ]]
    df.set_axis(
        ['uid', 'name', 'score', 'Calories', 'Total Fat', 'Total Carbohydrate', 'Protein', 'Saturated Fat', 'Trans Fat',
         'Cholesterol', 'Sodium', 'Added Sugar', 'Dietary Fiber', 'Sugars'], axis=1, inplace=True)
    return df


def del_invalid(df):
    all_columns = df.columns
    for column in all_columns:
        df = df[~(df[column] == 'Invalid Data')]
    return df


def check_type(df):
    df[['score', 'Calories', 'Total Fat', 'Total Carbohydrate', 'Protein', 'Saturated Fat', 'Trans Fat', 'Cholesterol',
        'Sodium', 'Dietary Fiber', 'Sugars']] = df[
        ['score', 'Calories', 'Total Fat', 'Total Carbohydrate', 'Protein', 'Saturated Fat', 'Trans Fat', 'Cholesterol',
         'Sodium', 'Dietary Fiber', 'Sugars']].astype(float)
    return df


if __name__ == "__main__":
    df = pd.read_csv('ewg/ewg_crawl/ewg_data_raw.csv')
    df = rename(df)
    df.fillna('0', inplace=True)
    df[['Total Fat', 'Total Carbohydrate', 'Protein', 'Saturated Fat', 'Trans Fat', 'Cholesterol', 'Sodium',
        'Dietary Fiber', 'Sugars']] = df[
        ['Total Fat', 'Total Carbohydrate', 'Protein', 'Saturated Fat', 'Trans Fat', 'Cholesterol', 'Sodium',
         'Dietary Fiber', 'Sugars']].applymap(parse_and_convert)

    df = del_invalid(df)
    df = check_type(df)
    df.to_csv('ewg/ewg_crawl/ewg_data_clean_1107.csv', index=False)
