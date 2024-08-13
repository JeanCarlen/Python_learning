from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def conv_pop(population_str):
    if 'M' in population_str:
        return int(float(population_str.replace('M', '')) * 1e6)
    elif 'K' in population_str:
        return int(float(population_str.replace('K', '')) * 1e3)
    else:
        return int(population_str)

def format_value(value):
    if value >= 1e6:
        return f"{value / 1e6:.1f}M"
    elif value >= 1e3:
        return f"{value / 1e3:.1f}K"
    else:
        return str(int(value))

def main():
	income_data = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
	if income_data is None:
		return

	life_expectancy_data = load("life_expectancy_years.csv")
	if life_expectancy_data is None:
		return

	income_1900 = income_data[['country', '1900']].rename(columns={'1900': 'GDP per capita'})
	income_1900['GDP per capita'] = income_1900['GDP per capita'].apply(format_value)

	life_expectancy_1900 = life_expectancy_data[['country', '1900']].rename(columns={'1900': 'Life Expectancy'})

	# Fusionner les deux DataFrames sur la colonne 'country'
	merged_df = pd.merge(income_1900, life_expectancy_1900, on='country')
    
	
    # Supprimer les lignes avec des valeurs manquantes
	merged_df = merged_df.dropna(subset=['GDP per capita', 'Life Expectancy'])
	# Conversion de la colonne 'GDP per capita' si nécessaire
	merged_df['GDP per capita'] = merged_df['GDP per capita'].apply(conv_pop)

	print(income_1900['GDP per capita'].max())

	plt.figure(figsize=(12, 6))
	plt.scatter(merged_df['GDP per capita'], merged_df['Life Expectancy'], color='blue')

	# Définir les positions des ticks et leurs labels
	tick_positions = list(range(300, 1001, 100)) + list(range(1000, 10001, 1000))
	tick_labels = ['300','','','','','','','','1k','','','','','','','','','10k']

	# Appliquer les ticks à l'axe X avec rotation pour améliorer la lisibilité
	plt.xticks(ticks=tick_positions, labels=tick_labels, ha='right')

	plt.xlim([0, 12000])

	plt.title("1900")
	plt.xlabel("Gross domestic product")
	plt.ylabel("Life expectancy")
	
	plt.grid(False)

	plt.show()

if __name__ == "__main__":
    main()