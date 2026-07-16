import pandas as pd
import numpy as np


class DataCleaner:

    @staticmethod
    def remove_duplicates(df):
        return df.drop_duplicates()

    @staticmethod
    def remove_empty_rows(df):
        return df.dropna(how="all")

    @staticmethod
    def remove_empty_columns(df):
        return df.dropna(axis=1, how="all")

    @staticmethod
    def fill_missing(df):

        df = df.copy()

        for col in df.columns:

            if pd.api.types.is_numeric_dtype(df[col]):
                df[col] = df[col].fillna(df[col].median())

            elif pd.api.types.is_datetime64_any_dtype(df[col]):
                df[col] = df[col].fillna(method="ffill")

            else:
                mode = df[col].mode()

                if len(mode) > 0:
                    df[col] = df[col].fillna(mode[0])

        return df

    @staticmethod
    def convert_dates(df):

        df = df.copy()

        for col in df.columns:

            try:
                converted = pd.to_datetime(df[col])

                if converted.notna().sum() > len(df) * 0.7:
                    df[col] = converted

            except:
                pass

        return df

    @staticmethod
    def clean(df):

        df = DataCleaner.remove_duplicates(df)

        df = DataCleaner.remove_empty_rows(df)

        df = DataCleaner.remove_empty_columns(df)

        df = DataCleaner.fill_missing(df)

        df = DataCleaner.convert_dates(df)

        return df