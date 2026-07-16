import pandas as pd
import streamlit as st


class DataLoader:

    @staticmethod
    def load_file(uploaded_file):

        if uploaded_file is None:
            return None

        filename = uploaded_file.name.lower()

        try:

            if filename.endswith(".csv"):
                df = pd.read_csv(uploaded_file)

            elif filename.endswith(".xlsx") or filename.endswith(".xls"):
                df = pd.read_excel(uploaded_file)

            else:
                st.error("Unsupported file type.")
                return None

            return df

        except Exception as e:
            st.error(f"Error loading file: {e}")
            return None