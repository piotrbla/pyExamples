import pandas as pd


def test_birds():
    bird_data = pd.read_csv("bird_tracking.csv")
    # bird_data.info()
    print(bird_data.head())


if __name__ == '__main__':
    test_birds()