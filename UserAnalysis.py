import matplotlib.pyplot as plt
import pandas as pd

def calculate_fitness_goal(df):
    
    total = len(df)
    lose_weight = df['Q5'].apply(lambda x: 'Lose weight' in x).sum()
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

def plot_fitness_goal(df):
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
    
def get_custom_order():
    return ['Improve Health', 'Build strength', 'Gain Muscle', 'Lose weight', 'Build Stamina', 'Maintain weight', 'Nothing', 'Gain weight']
    
def plot_fitness_goal_by_gender(df):
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

    plt.xlabel('Goals')
    plt.ylabel('Values')
    plt.title('Comparison of Goals Between Female and Male')

    plt.xticks([i + bar_width / 2 for i in x], custom_order, rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.savefig('OUTPUTS/image2.png')
    plt.close()

if __name__ == "__main__":
    survey_data = pd.read_csv('INPUTS/survey_data.csv')
    calculate_fitness_goal(survey_data)
    plot_fitness_goal(survey_data)
    plot_fitness_goal_by_gender(survey_data)