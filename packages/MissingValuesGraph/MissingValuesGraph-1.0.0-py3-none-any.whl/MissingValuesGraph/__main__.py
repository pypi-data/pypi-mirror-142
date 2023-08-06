import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


class MissingValues:
    def __init__(self, data):
        self.data = data

    def findMissingValues(self):
        values = (self.data.isna().sum()).sort_values(ascending=False)
        percent = (self.data.isna().sum() / len(self.data) * 100).sort_values(ascending=False)
        df_na = pd.concat([values, percent], axis=1)
        df_na = df_na.rename(columns={0: 'Values', 1: 'Percentage'})

        #         Draw plot
        fig, ax = plt.subplots(figsize=(10, 8), dpi=70)
        ax.vlines(x=df_na.index, ymin=0, ymax=df_na.Percentage, color='firebrick', alpha=0.7, linewidth=2)
        ax.scatter(x=df_na.index, y=df_na.Percentage, s=75, color='firebrick', alpha=0.7)

        # Title, Label, Ticks and Ylim
        ax.set_title('Lollipop Chart for Missing values', fontdict={'size': 22})
        ax.set_ylabel('Percentage')
        ax.set_xticks(df_na.index)
        ax.set_xticklabels(df_na.index, rotation=60, fontdict={'horizontalalignment': 'right', 'size': 12})
        ax.set_ylim(0, 30)

        # Annotate
        for row in df_na.itertuples():
            ax.text(row.Index, row.Percentage + .5, s=round(row.Percentage, 2), horizontalalignment='center',
                    verticalalignment='bottom', fontsize=14)

        plt.figure(figsize=(12, 5))
        sns.heatmap(self.data.isnull(), cmap='cool')
        plt.title('Null Values in each feature of Dataset')
        plt.show()

