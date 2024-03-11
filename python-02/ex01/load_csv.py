import pandas as pd


# function that loads a csv file into a pandas DataFrame
def load(path: str) -> pd.DataFrame:
    try:
        if not path.endswith(".csv"):
            print(f"File {path} is not a csv file")
            return None
        D_frame = pd.read_csv(path)
        # print("Loading dataset of dimensions", D_frame.shape)
        print(f"Loading dataset of dimensions {D_frame.shape}")
        return D_frame
    except FileNotFoundError:
        print(f"File {path} not found")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
