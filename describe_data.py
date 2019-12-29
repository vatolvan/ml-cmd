from pprint import pprint

def display_data(data):
    pprint(data.head())
    pprint(data.describe())

    print("\nCorrelation matrix: ")
    pprint(data.corr())

    input("Press Enter to continue...")
