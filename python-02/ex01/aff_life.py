from load_csv import load
import matplotlib.pyplot as plt


# function that displays the life expectancy of Switzerland over the years
# on a graph
def main():
    # load the dataset
    file_path = "life_expectancy_years.csv"
    data = load(file_path)
    if data is None:
        return
    switzerland_data = data[data['country'] == 'Switzerland']
    years = switzerland_data.columns[1:]
    life_expectancy = switzerland_data.values[0][1:]
    # print(switzerland_data)
    # plot the data
    plt.plot(years, life_expectancy)
    plt.title("Switzerland's life expectancy Projections")
    plt.xlabel("Year")
    plt.xticks(years[::40])
    plt.ylabel('Life Expectancy')
    plt.ylim(25, 95)  # Set y-axis limits
    plt.yticks(range(30, 91, 10))  # Set y-axis ticks
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
