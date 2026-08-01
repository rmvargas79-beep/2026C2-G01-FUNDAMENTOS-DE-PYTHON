import kagglehub
from kagglehub import KaggleDatasetAdapter

file_path = "twitchdata.csv"

try:
    df = kagglehub.dataset_load(
        KaggleDatasetAdapter.PANDAS,
        "aayushmishra1512/twitchdata",
        file_path
    )

    print("Primeros 5 registros:")
    print(df.head())

except Exception as error:
    print("Ocurrió un error:")
    print(type(error).__name__)
    print(error)