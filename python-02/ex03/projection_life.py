from load_csv import load
import matplotlib.pyplot as plt

def conv_pop(population_str):
    if 'M' in population_str:
        return int(float(population_str.replace('M', '')) * 1e6)
    elif 'K' in population_str:
        return int(float(population_str.replace('K', '')) * 1e3)
    else:
        return int(population_str)

def main():
	income_data = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
	if income_data is None:
		return
	life_expectancy_data = load("life_expectancy_years.csv")

	income_1900 = {country: data['1900'] for country, data in income_data.items()}
	life_expectancy_1900 = {country: data['1900'] for country, data in life_expectancy_data.items()}

	countries = income_1900.keys() & life_expectancy_1900.keys()  # Intersection des pays dans les deux ensembles de données
	x_values = [conv_pop(income_1900[country]) for country in countries]
	y_values = [conv_pop(life_expectancy_1900[country]) for country in countries]

	plt.figure(figsize=(10, 6))
	plt.scatter(x_values, y_values, alpha=0.5)
	plt.title("Projection de l'espérance de vie en fonction du PNB en 1900")
	plt.xlabel("PNB par habitant (ajusté à l'inflation)")
	plt.ylabel("Espérance de vie (années)")
	plt.grid(True)

	plt.show()
     
if __name__ == "__main__":
    main()