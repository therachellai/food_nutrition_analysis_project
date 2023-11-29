import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def calculate_fitness_goal(df: pd.DataFrame) -> dict:
    """
    This function calculates the number of people recorded in the dataFrame who wants 
    to achieve each fitness goal.
    ------------------
    Parameters: 
    df: dataFrame provided
    ------------------
    Returns: dictionary with fitness goals as keys and respective number of people as values
    """
    
    total = len(df)
    lose_weight = df['Q5'].apply(lambda x: 'Lose weight' in x).sum() / total * 100
    gain_weight = df['Q5'].apply(lambda x: 'Gain weight' in x).sum() / total * 100
    maintain_weight = df['Q5'].apply(lambda x: 'Maintain weight' in x).sum() / total * 100
    gain_muscle = df['Q5'].apply(lambda x: 'Gain Muscle Mass' in x).sum() / total * 100
    build_strength = df['Q5'].apply(lambda x: 'Build strength' in x).sum() / total * 100
    build_stamina = df['Q5'].apply(lambda x: 'Build Stamina' in x).sum() / total * 100
    improve_health = df['Q5'].apply(lambda x: 'Improve General Health Level' in x).sum() / total * 100
    nothing = df['Q5'].apply(lambda x: 'Nothing, Just Goofing Around' in x).sum() / total * 100
    return {'Lose weight': lose_weight, 
            'Gain weight': gain_weight, 
            'Maintain weight': maintain_weight, 
            'Gain Muscle': gain_muscle, 
            'Build strength': build_strength, 
            'Build Stamina': build_stamina, 
            'Improve Health': improve_health, 
            'Nothing': nothing}

def plot_fitness_goal(df: pd.DataFrame) -> None:
    """
    This function plots the total number of people with each fitness goal.
    ------------------
    Parameters: 
    df: dataFrame provided
    ------------------
    Returns: None
    """
    
    data = calculate_fitness_goal(df)
    sorted_data = {k: v for k, v in sorted(data.items(), key=lambda item: item[1], reverse=True)}

    labels = list(sorted_data.keys())
    values = list(sorted_data.values())

    plt.figure(figsize=(14, 7))
    plt.bar(range(len(values)), values, tick_label=labels)
    plt.ylabel('Percentage (%)')
    plt.xlabel('Fitness Goals')
    plt.title('Percentage of Users with A Certain Fitness Goal')
    plt.xticks(range(len(values)), labels, rotation=30)
    plt.savefig('OUTPUTS/image1.png')
    plt.close()
    # from this function, we get that the general users go in this order: improve health, build strength, gain muscle, lose weight, 
    # build stamina, maintain weight, nothing, gain weight
    
def get_custom_order() -> str:
    return ['Improve Health', 'Build strength', 'Gain Muscle', 'Lose weight', 'Build Stamina', 'Maintain weight', 'Nothing', 'Gain weight']
    
def plot_fitness_goal_by_gender(df: pd.DataFrame) -> None:
    """
    This function plots the total number of people in each gender with each fitness goal.
    ------------------
    Parameters: 
    df: dataFrame provided
    ------------------
    Returns: None
    """
    
    female = df[df['Q2'] == 'Female']
    male = df[df['Q2'] == 'Male']
    data_female = calculate_fitness_goal(female)
    data_male = calculate_fitness_goal(male)
    custom_order = get_custom_order()
    female_sorted = [data_female[key] for key in custom_order]
    male_sorted = [data_male[key] for key in custom_order]
    bar_width = 0.35
    x = range(len(female_sorted))
    
    plt.bar(x, female_sorted, width=bar_width, label='Female')
    plt.bar([i + bar_width for i in x], male_sorted, width=bar_width, label='Male')

    plt.xlabel('Fitness Goals')
    plt.ylabel('Percentage (%)')
    plt.title('Comparison of Goals Between Female and Male')

    plt.xticks([i + bar_width / 2 for i in x], custom_order, rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.savefig('OUTPUTS/image2.png')
    plt.close()
    
def plot_fitness_goal_by_age(df: pd.DataFrame) -> None:
    """
    This function plots the total number of people in each age group with each fitness goal.
    ------------------
    Parameters: 
    df: dataFrame provided
    ------------------
    Returns: None
    """
    
    early_twenties = calculate_fitness_goal(df[df['Q1'] == '21-25'])
    late_twenties = calculate_fitness_goal(df[df['Q1'] == '26-30'])
    early_thirties = calculate_fitness_goal(df[df['Q1'] == '31-35'])
    late_thirties = calculate_fitness_goal(df[df['Q1'] == '36-40'])
    early_forties = calculate_fitness_goal(df[df['Q1'] == '41-45'])
    late_forties = calculate_fitness_goal(df[df['Q1'] == '46-50'])
    beyond = calculate_fitness_goal(df[df['Q1'] == 'Over 51'])
    
    custom_order = ['Improve Health', 'Build strength', 'Gain Muscle', 'Lose weight', 'Build Stamina', 'Maintain weight', 'Nothing', 'Gain weight']

    age_data = {
    '21-25': early_twenties,
    '26-30': late_twenties,
    '31-35': early_thirties,
    '36-40': late_thirties,
    '41-45': early_forties,
    '46-50': late_forties,
    'Over 51': beyond
    }
    bar_width = 0.1
    x = range(len(custom_order))

    for age_group, data in age_data.items():
        values = [data[key] for key in custom_order]
        plt.bar([i + bar_width * (list(age_data.keys()).index(age_group)) for i in x], values, width=bar_width, label=age_group)

    plt.xlabel('Fitness Goals')
    plt.ylabel('Percentage (%)')
    plt.title('Comparison of Goals Among Different Age Groups')

    plt.xticks([i + bar_width * (len(age_data) / 2) for i in x], custom_order, rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.savefig('OUTPUTS/image3.png')
    plt.close()
    
def plot_fitness_goal_by_fitness_level(df: pd.DataFrame) -> None:
    """
    This function plots the total number of people in each fitness level with each fitness goal.
    ------------------
    Parameters: 
    df: dataFrame provided
    ------------------
    Returns: None
    """
    
    first = calculate_fitness_goal(df[df['Q3'] == 1])
    second = calculate_fitness_goal(df[df['Q3'] == 2])
    third = calculate_fitness_goal(df[df['Q3'] == 3])
    fourth = calculate_fitness_goal(df[df['Q3'] == 4])
    fifth = calculate_fitness_goal(df[df['Q3'] == 5])
    
    custom_order = ['Improve Health', 'Build strength', 'Gain Muscle', 'Lose weight', 'Build Stamina', 'Maintain weight', 'Nothing', 'Gain weight']

    fitness_data = {
    '1': first,
    '2': second,
    '3': third,
    '4': fourth,
    '5': fifth,
    }
    bar_width = 0.1
    x = range(len(custom_order))

    for fitness_group, data in fitness_data.items():
        values = [data[key] for key in custom_order]
        plt.bar([i + bar_width * (list(fitness_data.keys()).index(fitness_group)) for i in x], values, width=bar_width, label=fitness_group)

    plt.xlabel('Fitness Levels')
    plt.ylabel('Percentage (%)')
    plt.title('Comparison of Goals Among Different Fitness Levels')

    plt.xticks([i + bar_width * (len(fitness_data) / 2) for i in x], custom_order, rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.savefig('OUTPUTS/image4.png')
    plt.close()

def plot_fitness_goals_by_user_profiles(df: pd.DataFrame) -> None:
    """
    This function plots everything about fitness goals in relation to user profiles.
    ------------------
    Parameters: 
    df: dataFrame provided
    ------------------
    Returns: None
    """
    plot_fitness_goal(df)
    plot_fitness_goal_by_gender(df)
    plot_fitness_goal_by_age(df)
    plot_fitness_goal_by_fitness_level(df)

#############################################################################################

def calculate_improvement_in_satisfaction(df: pd.DataFrame) -> pd.DataFrame:
    """
    This function calculate people's change in % in their confidence in their own 
    ability to make wise food choices before and after using our recommendaiton system.
    ------------------
    Parameters: 
    df: dataFrame provided
    ------------------
    Returns: None
    """
    
    def calculate_improvement(satisfaction):
        if pd.notna(satisfaction):
            values = list(map(float, satisfaction.split(',')))
            if len(values) == 2 and values[0] != 0:
                return (values[1] / values[0] - 1) * 100
        return None
        
    df['Improvement in Satisfaction %'] = df['Q9'].apply(calculate_improvement)
    return df

def plot_improvement_in_satisfaction_by_fitness_level(df: pd.DataFrame) -> None:
    """
    This function plots people's change in confidence in each fitness level.
    ------------------
    Parameters: 
    df: dataFrame provided
    ------------------
    Returns: None
    """
    fitness_order = [1, 2, 3, 4, 5]

    plt.figure(figsize=(10, 6))
    plt.ylim(0, 200)
    sns.boxplot(x='Q3', y='Improvement in Satisfaction %', data=df, order=fitness_order)
    plt.title("Improvement in User's Confidence to Make Wise Food Choices in % Among Different Fitness Levels")
    plt.xlabel('Fitness Level')
    plt.savefig('OUTPUTS/image5.png')
    plt.close()
    

if __name__ == "__main__":
    survey_data = pd.read_csv('INPUTS/survey_data.csv')
    survey_data = calculate_improvement_in_satisfaction(survey_data)
    plot_fitness_goals_by_user_profiles(survey_data)
    plot_improvement_in_satisfaction_by_fitness_level(survey_data)