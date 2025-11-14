import os
from pathlib import Path

import pandas as pd
import questionary

DATA_DIR = Path("data/raw")


def load() -> pd.DataFrame:
    data_files = os.listdir(DATA_DIR)
    choice = questionary.select(
        "What file would you like to load?",
        choices=[i for i in data_files],
    ).ask()
    df = pd.read_csv(Path(DATA_DIR / choice))
    return df
