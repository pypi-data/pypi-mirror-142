from typing import List, Union, TypeVar
import treefiles as tf
import pandas as pd

T = TypeVar("T", bound="MySuperDF")


class MySuperDF(pd.DataFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @classmethod
    def from_csv(cls, *args, **kwargs):
        return cls(pd.read_csv(*args, **kwargs))

    @property
    def filter_numeric(self):
        return filter_df(self, 'float64')

    @property
    def filter_bool(self):
        return filter_df(self, 'bool')

    @property
    def filter_object(self):
        return filter_df(self, 'object')

    @property
    def filling_rate(self) -> T:
        results = pd.DataFrame(columns=['missing_values', 'filling_rate'])

        #  Count of rows
        nb_rows = self.shape[0]

        # for each feature
        for column in self.columns:

            # Count of the values on each column
            values_count = self[column].count()

            # Computing missing values
            missing_values = nb_rows - values_count

            # Computing filling rates
            filling_rate = values_count / nb_rows

            # Adding a row in the results' dataframe
            results.loc[column] = [missing_values, filling_rate]

        # Sorting the features by number of missing_values
        return MySuperDF(results.dropna(subset=['filling_rate']))


def filter_df(df, selected_type:Union[str, List[str]]) -> T:
    my_data = []
    for i, j in zip(df.dtypes, df.columns):
        if i in tf.get_iterable(selected_type):
            my_data.append(j)
    return MySuperDF(df[my_data])

