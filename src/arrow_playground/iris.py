import time
import pandas as pd
import io
import requests

def display_iris():
    # Load the iris dataset

    url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/refs/heads/master/iris.csv"

    request = requests.get(url)

    if request.status_code == 200:

        # Read the CSV file into a DataFrame

        s = time.perf_counter()
        df = pd.read_csv(io.BytesIO(request.content))

        e = time.perf_counter()
        print(f"Function took {e - s:.4f} seconds to run.")
        return df


def test_display_iris():
    # Test the display_iris function
    df = display_iris()

    assert df is not None
    # Check if the DataFrame is not empty
    assert not df.empty, "DataFrame is empty"
    # Check if the DataFrame has the expected number of columns
    assert df.shape[1] == 5, "DataFrame does not have 5 columns"
    # Check if the DataFrame has the expected column names
    assert list(df.columns) == ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"], "DataFrame does not have the expected column names"