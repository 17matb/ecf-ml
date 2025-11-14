import matplotlib.pyplot as plt
import pandas as pd
import questionary
import seaborn as sns

from src.data.loading import load


def explore_data():
    df: pd.DataFrame = load()

    print(f"-> Head:\n{df.head()}")
    print(f"\n-> Shape:\n{df.shape}")
    print(f"\n-> Basic stats:\n{df.describe()}")

    correlation_matrix = df.select_dtypes("number").corr()
    print(f"\n-> Correlation matrix:\n{correlation_matrix}")

    show_plots = questionary.confirm(
        "Would you like to see a few nice plots?",
        default=False,
    ).ask()

    if show_plots:
        sns.heatmap(
            correlation_matrix,
            annot=True,
            cmap="coolwarm",
        )
        plt.title("Correlation heatmap")
        plt.show()
