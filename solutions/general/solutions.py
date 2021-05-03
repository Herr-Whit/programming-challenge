from solutions.general.src.DataFactory import FileDataFactory


def solve_weather_challenge():
    data_factory = FileDataFactory()
    ds = data_factory.load_data(r'.\src\main\resources\de\exxcellent\challenge\weather.csv')
    ds.create_absolute_difference_column('TDiff', ['MxT', 'MnT'])
    minimum_tdiff_row = ds.get_row_on_column_reduction('TDiff', min)
    return minimum_tdiff_row['Day'][0]


def solve_football_challenge():
    data_factory = FileDataFactory()
    ds = data_factory.load_data(r'.\src\main\resources\de\exxcellent\challenge\football.csv')
    ds.create_absolute_difference_column('GDiff', ['Goals', 'Goals Allowed'])
    minimum_tdiff_row = ds.get_row_on_column_reduction('GDiff', min)
    return minimum_tdiff_row['Team'][0]


def main():
    solve_football_challenge()


if __name__ == '__main__':
    main()
