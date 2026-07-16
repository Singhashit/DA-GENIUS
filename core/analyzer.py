import pandas as pd
import numpy as np


class DataAnalyzer:

    @staticmethod
    def dataset_summary(df):

        rows = df.shape[0]
        cols = df.shape[1]

        missing = int(df.isnull().sum().sum())
        duplicates = int(df.duplicated().sum())

        memory = round(df.memory_usage(deep=True).sum() / 1024**2, 2)

        numeric = len(df.select_dtypes(include=np.number).columns)

        categorical = len(df.select_dtypes(include="object").columns)

        datetime = len(df.select_dtypes(include="datetime").columns)

        return {
            "Rows": rows,
            "Columns": cols,
            "Missing": missing,
            "Duplicates": duplicates,
            "Memory": memory,
            "Numeric": numeric,
            "Categorical": categorical,
            "Datetime": datetime
        }


    @staticmethod
    def quality_score(df):

        score = 100

        missing_percent = (df.isnull().sum().sum()) / (df.shape[0] * df.shape[1])

        duplicate_percent = df.duplicated().sum() / max(df.shape[0], 1)

        score -= missing_percent * 40
        score -= duplicate_percent * 30

        score = max(0, min(100, round(score, 1)))

        return score


    @staticmethod
    def missing_table(df):

        table = pd.DataFrame({

            "Column": df.columns,

            "Missing Values": df.isnull().sum().values,

            "Percentage": (
                df.isnull().sum().values /
                len(df) * 100
            ).round(2)

        })

        return table.sort_values(
            "Missing Values",
            ascending=False
        )


    @staticmethod
    def datatype_table(df):

        return pd.DataFrame({

            "Column": df.columns,

            "Data Type": df.dtypes.astype(str),

            "Unique Values": df.nunique(),

            "Null Values": df.isnull().sum()

        })


    @staticmethod
    def recommendations(df):

        rec = []

        if df.isnull().sum().sum() > 0:
            rec.append("Fill missing values.")

        if df.duplicated().sum() > 0:
            rec.append("Remove duplicate rows.")

        if len(df.select_dtypes(include="object").columns) > 0:
            rec.append("Encode categorical columns if needed.")

        if len(df.select_dtypes(include="datetime").columns) == 0:
            rec.append("Check for date columns.")

        if len(rec) == 0:
            rec.append("Dataset looks clean.")

        return rec