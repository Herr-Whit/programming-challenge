from solutions.general.src.DataFactory import FileDataFactory


def solve_weather_challenge():
    data_factory = FileDataFactory()
    ds = data_factory.load_data(r'.\src\main\resources\de\exxcellent\challenge\weather.csv')
    ds.create_difference_column('TDiff', ['MxT', 'MnT'])
    maximum_tdiff_row = ds.get_row_on_column_max('TDiff')
    return maximum_tdiff_row['Day'][0]

