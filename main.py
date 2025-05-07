import numpy as np
import pyarrow as pa
import pandas as pd

def display_pyarrow():
    random_numbers = np.random.randint(1, 100, size=10)

    # Create a PyArrow array from the NumPy array
    arrow_array = pa.array(random_numbers)

    print("NumPy array:", random_numbers)
    print("PyArrow array:", arrow_array)

    arrow_string = pa.array(
        [
            "Hello",
            "World",
            "from",
            "PyArrow",
            "and",
            "NumPy",
            "Python",
            "rocks",
            "!",
            "123",
        ]
    )

    arrow_table = pa.table({"numbers": arrow_array, "strings": arrow_string})

    print("PyArrow table:")
    print(arrow_table)


def display_pandas():

    random_numbers = np.random.randint(1, 100, size=10)

    # Create a Pandas DataFrame from the NumPy array
    df = pd.DataFrame({"numbers": random_numbers})

    df["strings"] = [
        "Hello",
        "World",
        "from",
        "Pandas",
        "and",
        "NumPy",
        "Python",
        "rocks",
        "!",
        "123",
    ]

    print("Pandas DataFrame with strings:")
    print(df)


def main():
    display_pyarrow()
    display_pandas()


if __name__ == "__main__":
    main()
