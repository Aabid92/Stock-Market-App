from ast import Pass
from email.mime import image
from urllib.parse import scheme_chars
import streamlit as st
from optparse import Option
# from tracemalloc import start
import yfinance as yf 
# import pandas as pd
from tickers import stock_tickers
import datetime
from streamlit_option_menu import option_menu 
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import cufflinks as cf



image1 = Image.open('icon.png')
st.set_page_config(page_title="Stock Market Analysis", page_icon= image1)
image = Image.open('main.png')
st.image(image)

hide_menu_style = """
                <style>
                #MainMenu {visibility: hidden; footer {visibility: hidden;}}
                </style>

                """
st.markdown(hide_menu_style, unsafe_allow_html=True)




# with st.sidebar:
#     choose = option_menu("Main Menu", ["Home", "Technical View", "Mutual Fund", "Market News"],
#                         # orientation= 'horizontal',
#                         default_index=0,
#                         styles={
#         "container": {"padding": "5!important", "background-color": "F2F2F2"},
#         "nav-link": {"font-size": "12px", "text-align": "left", "margin":"0px", "--hover-color": "#03045E"},
#         "nav-link-selected": {"background-color": "#2e54ff"}, ##2e54ff
#     }
#     )

# ........................For On Header Menu Style...............................

# choose = option_menu("Main Menu", ["Home", "Technical View", "Mutual Fund", "Market News"],
#                     orientation= 'horizontal',
#                     menu_icon="app-indicator", default_index=0,
#                     styles={
#         "container": {"padding": "5!important", "background-color": "#474747"},
#         "nav-link": {"font-size": "12px", "text-align": "left", "margin":"0px", "--hover-color": "#000000"},
#         "nav-link-selected": {"background-color": "#F2F2F2"},
#     }
# )


# if choose == "Home":
    

def stock_data():
    Option = st.sidebar.selectbox('Select Stock', (stock_tickers))
    
    # ......................Dating Code Here.................
    
    today = datetime.date.today()
    before = today - datetime.timedelta(days=700)
    start_date = st.sidebar.date_input('Start date', before)
    end_date = st.sidebar.date_input('End date', today)
    if start_date < end_date:
        st.sidebar.success('Start date: `%s`\n\nEnd date:`%s`' % (start_date, end_date))
    else:
        st.sidebar.error('Error: End date must fall after start date.')
                
    #...................Getting Companies Names By Its Ticker.......................
    def companies_name():
        co_name = yf.Ticker(Option)
        name = co_name.info['longName']
        st.header(name)    

    # tickerDf = tickerData.history(start=start_date, end=end_date')
    tickerDf = yf.download(Option, start = start_date, end= end_date)


    companies_name()
    st.write("### Opening Price of Stock")
    st.line_chart(tickerDf.Open)

    st.write("### Closing Price of Stock")
    st.line_chart(tickerDf.Close)

        
    st.write("### High Price of Stock")
    st.line_chart(tickerDf.High)

    st.write("### Low Price of Stock")
    st.line_chart(tickerDf.Low)

    st.write("### Volume of Stock")
    st.bar_chart(tickerDf.Volume)
         
stock_data()

# ..........................Showing Dividend of Companies Here.....................................
 

col1, col2 = st.columns(2)
with col1:
    d_button = st.button('Show Dividend')
with col2:    
    h_button  = st.button('Hide Dividend')
if d_button == True:
    tickerData = yf.Ticker(Option)
    tickerDf = tickerData.history(start='2005-01-01', end='2022-04-01')
    st.write("### Dividend Given By Company to its Shareholders")
    st.line_chart(tickerDf.Dividends)   
else:
    st.write("Click Button to See Dividend") 

    
st.write("Develope with❤️ By Aabid Shaikh")
