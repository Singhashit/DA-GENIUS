from core.theme import set_page
from core.ui import hero
from core.metrics import show_metrics
from core.cards import feature_cards

import streamlit as st

set_page()

hero()

st.divider()

show_metrics()

st.divider()

st.header("✨ Platform Features")

feature_cards()

st.divider()

st.header("Technology Stack")

st.write(
"""
- Python
- Pandas
- NumPy
- Plotly
- Streamlit
- Scikit-Learn
- Power BI
- OpenAI
"""
)