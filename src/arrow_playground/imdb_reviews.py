import requests
import io
import pandas as pd
import time



def display_imdb_reviews():

    url = "https://raw.githubusercontent.com/SkyThonk/Movie-Reviews-Sentiment-Analysis/refs/heads/master/dataset/IMDB%20Dataset.csv"

    r = requests.get(url)

    if r.status_code == 200:

        content = io.BytesIO(r.content)

        s = time.perf_counter()
        _ = pd.read_csv(content, encoding="utf-8", engine='pyarrow')
        print(f"Function took {time.perf_counter() - s:.4f} seconds to run.")

        # s = time.perf_counter()
        # df = pd.read_csv(content)
        # print(f"Function took {time.perf_counter() - s:.4f} seconds to run.")
