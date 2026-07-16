import pandas as pd
import numpy as np


class InsightEngine:

    @staticmethod
    def generate(df, detected):

        insights = []

        sales = detected.get("sales")
        profit = detected.get("profit")
        category = detected.get("category")
        region = detected.get("region")
        customer = detected.get("customer")
        product = detected.get("product")
        date = detected.get("date")

        # Revenue

        if sales:

            total = df[sales].sum()

            avg = df[sales].mean()

            insights.append(
                f"Total Revenue : {total:,.2f}"
            )

            insights.append(
                f"Average Revenue : {avg:,.2f}"
            )

        # Profit

        if profit:

            p = df[profit].sum()

            insights.append(
                f"Total Profit : {p:,.2f}"
            )

        # Best Category

        if category and sales:

            best = (

                df.groupby(category)[sales]

                .sum()

                .sort_values(ascending=False)

                .head(1)

            )

            insights.append(

                f"Highest Revenue Category : {best.index[0]}"

            )

        # Best Region

        if region and sales:

            best = (

                df.groupby(region)[sales]

                .sum()

                .sort_values(ascending=False)

                .head(1)

            )

            insights.append(

                f"Top Region : {best.index[0]}"

            )

        # Top Customer

        if customer and sales:

            best = (

                df.groupby(customer)[sales]

                .sum()

                .sort_values(ascending=False)

                .head(1)

            )

            insights.append(

                f"Highest Paying Customer : {best.index[0]}"

            )

        # Top Product

        if product and sales:

            best = (

                df.groupby(product)[sales]

                .sum()

                .sort_values(ascending=False)

                .head(1)

            )

            insights.append(

                f"Best Selling Product : {best.index[0]}"

            )

        # Missing Values

        missing = df.isnull().sum().sum()

        if missing:

            insights.append(

                f"Dataset contains {missing} missing values."

            )

        # Duplicate Rows

        dup = df.duplicated().sum()

        if dup:

            insights.append(

                f"Dataset contains {dup} duplicate rows."

            )

        # Numeric Analysis

        numeric = df.select_dtypes(include=np.number)

        for col in numeric.columns:

            if numeric[col].std() > numeric[col].mean():

                insights.append(

                    f"{col} shows high variation."

                )

        # Date Trend

        if date and sales:

            temp = df.copy()

            temp[date] = pd.to_datetime(temp[date])

            temp["Month"] = temp[date].dt.to_period("M")

            monthly = (

                temp.groupby("Month")[sales]

                .sum()

            )

            if len(monthly) > 1:

                if monthly.iloc[-1] > monthly.iloc[0]:

                    insights.append(

                        "Revenue trend is increasing."

                    )

                else:

                    insights.append(

                        "Revenue trend is decreasing."

                    )

        return insights

    @staticmethod
    def executive_summary(insights):

        summary = ""

        for item in insights:

            summary += "• " + item + "\n"

        return summary

    @staticmethod
    def recommendations(detected):

        rec = []

        if detected.get("category"):

            rec.append(

                "Focus marketing on highest performing categories."

            )

        if detected.get("region"):

            rec.append(

                "Improve low-performing regions."

            )

        if detected.get("customer"):

            rec.append(

                "Create loyalty programs for top customers."

            )

        if detected.get("product"):

            rec.append(

                "Increase inventory for best-selling products."

            )

        rec.append(

            "Monitor KPIs weekly."

        )

        rec.append(

            "Review trends every month."

        )

        return rec