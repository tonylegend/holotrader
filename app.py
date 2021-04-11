import streamlit as st
# import asyncio
# import nest_asyncio
# from datetime import date, datetime, timedelta
# import pytz
# import numpy as np
# import pandas as pd
# import backend
# from utils.config import config

# Add title on the page
st.title("Holo Trader")
st.markdown(
    "## **Back-testing & Analysis tools**"
)

st.sidebar.header('User Input Parameters')

# def user_input_features():
#     ticker = st.sidebar.text_input("Ticker", 'TSLA')
#     cash = st.sidebar.number_input("Cash", min_value=0, value=int(config.backtest.cash), format='%i')
#     start_date = st.sidebar.date_input("Start Date", value=date.today())
#     end_date = st.sidebar.date_input("End Date", value=date.today())
#     return ticker, cash, start_date, end_date
#
# symbol, cash, start, end = user_input_features()
# start = pd.to_datetime(start)
# end = pd.to_datetime(end)
#
# module = st.sidebar.selectbox("Select Strategy Module", options=[name for name in config.backtest.modules.split(',')])
#
# new_bid = ""
# est = pytz.timezone("America/New_York")
#
# strategy = st.sidebar.selectbox("Select a Strategy to Run", options=backend.test_list(module))
env = st.sidebar.selectbox("Select environment", ("PAPER", "BACKTEST", "PROD"))

# @st.cache
# def run_strategy():
#     with st.spinner('Running Strategy...'):
#         return st.success('Done!')


# loop = asyncio.new_event_loop()
# asyncio.set_event_loop(loop)
# nest_asyncio.apply()
# loop.run_until_complete(database.create_db_connection())

# st.write("Strategy Parameters:")
# if module and strategy and symbol:
#     st.table(pd.DataFrame(backend.params_list(module, strategy, symbol)))
