import time
import pandas as pd
import pyarrow.csv as pacsv
import requests

def display_iris():
    # Load the iris dataset

    url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/refs/heads/master/iris.csv"

    request = requests.get(url)

    if request.status_code == 200:
        with open("temp/iris.csv", "wb") as f:
            f.write(request.content)

        # Read the CSV file into a DataFrame

        s = time.perf_counter()
        df = pd.read_csv("temp/iris.csv")

        e = time.perf_counter()
        print(f"Function took {e - s:.4f} seconds to run.")

        print(df.head())

        s = time.perf_counter()
        pa_df = pacsv.read_csv("temp/iris.csv")
        e = time.perf_counter()
        print(f"Function took {e - s:.4f} seconds to run.")
        print(pa_df)
