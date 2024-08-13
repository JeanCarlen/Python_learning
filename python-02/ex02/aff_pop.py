from load_csv import load
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


def conv_pop(population_str):
    if 'M' in population_str:
        return int(float(population_str.replace('M', '')) * 1e6)
    elif 'K' in population_str:
        return int(float(population_str.replace('K', '')) * 1e3)
    else:
        return int(population_str)


def main():
    # load the dataset
    file_path = "population_total.csv"
    data = load(file_path)
    if data is None:
        return
    switzerland_data = data[data['country'] == 'Switzerland']
    france_data = data[data['country'] == 'France']

    years = [int(col) for col in france_data.columns[1:]]
# Convert the population data to actual numbers
    s_population = [conv_pop(pop) for pop in switzerland_data.values[0][1:]]
    f_population = [conv_pop(pop) for pop in france_data.values[0][1:]]


    plt.plot(years, f_population, label='France', color='blue')
    plt.plot(years, s_population, label='Switzerland', color='red')
    plt.title("Population Projections")
    plt.xlabel("Year")
    plt.xlim(1780, 2070)
    plt.xticks(range(1800, 2041, 40))
    plt.ylabel("Population")
    plt.ylim(0, 70e6)
    plt.yticks([i * 1e6 for i in range(20, 61, 20)])
    formatter = ticker.FuncFormatter(lambda x, pos: f'{int(x / 1e6)}M')
    plt.gca().yaxis.set_major_formatter(formatter)
    plt.legend(title=" ", title_fontsize='8', loc='lower right')
    # plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
