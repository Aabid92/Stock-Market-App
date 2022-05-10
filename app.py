from email.mime import image
import streamlit as st
from optparse import Option
from tracemalloc import start
import yfinance as yf 
import pandas as pd
from tickers import stock_tickers
import datetime
from streamlit_option_menu import option_menu 
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import cufflinks as cf



image = Image.open('main.png')
st.image(image)

with st.sidebar:
    choose = option_menu("Main Menu", ["Home", "Technical View", "Mutual Fund", "Market News"],
                        # orientation= 'horizontal',
                        menu_icon="app-indicator", default_index=0,
                        styles={
        "container": {"padding": "5!important", "background-color": "#474747"},
        "nav-link": {"font-size": "12px", "text-align": "left", "margin":"0px", "--hover-color": "#000000"},
        "nav-link-selected": {"background-color": "#2e54ff"},
    }
    )

# ........................For On Header Menu Style...............................

# choose = option_menu("Main Menu", ["Home", "Technical View", "Mutual Fund", "Market News"],
#                     orientation= 'horizontal',
#                     menu_icon="app-indicator", default_index=0,
#                     styles={
#         "container": {"padding": "5!important", "background-color": "#474747"},
#         "nav-link": {"font-size": "12px", "text-align": "left", "margin":"0px", "--hover-color": "#000000"},
#         "nav-link-selected": {"background-color": "#2e54ff"},
#     }
# )

if choose == "Home":
    
    Option = st.sidebar.selectbox('Select Stock', (stock_tickers))
    def stock_data():
    
        # ......................Dating Code Here.................

        today = datetime.date.today()
        before = today - datetime.timedelta(days=700)
        start_date = st.sidebar.date_input('Start date', before)
        end_date = st.sidebar.date_input('End date', today)
        if start_date < end_date:
            st.sidebar.success('Start date: `%s`\n\nEnd date:`%s`' % (start_date, end_date))
        else:
            st.sidebar.error('Error: End date must fall after start date.')

        # tickerDf = tickerData.history(start=start_date, end=end_date')
        tickerDf = yf.download(Option, start = start_date, end= end_date)



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

# ..........................Showing Devidents of Companies Here.....................................

    col1, col2 = st.columns(2)
    with col1:
        d_button = st.button('Show Devidents')
    with col2:    
        h_button  = st.button('Hide Devidents')
    if d_button == True:
        tickerData = yf.Ticker(Option)
        tickerDf = tickerData.history(start='2005-01-01', end='2022-04-01')
        st.write("### Devidends Given By Company to its Shareholders")
        st.line_chart(tickerDf.Dividends)   
    else:
        st.write("Click Button to See Devidents") 
    
    
    #........................Technical Data Analysis Here.............................   
elif choose == "Technical View":
    def technical():
        
        Option2 = st.sidebar.multiselect("Select Multiple Stocks",stock_tickers, 'WIPRO.BO')

        today = datetime.date.today()
        before = today - datetime.timedelta(days=700)
        start_date = st.sidebar.date_input('Start date', before)
        end_date = st.sidebar.date_input('End date', today)
        if start_date < end_date:
            st.sidebar.success('Start date: `%s`\n\nEnd date:`%s`' % (start_date, end_date))
        else:
            st.sidebar.error('Error: End date must fall after start date.')

        st.header("Technical Analysis")

        st.write("### Select Multiple Tickers from dropdown to Start")
    

        tickerDf = yf.download(Option2, start = start_date, end= end_date)

        
        st.write("### Closing and Opening Price Comparison")

       # .....................Open Close Comparision........................
        st.line_chart(tickerDf.Open)
        st.line_chart(tickerDf.Close)

       # ....................Volume of the Stock............................ 
        st.write("### Volume History of Stocks")
        st.line_chart(tickerDf.Volume)

        st.header("Select Ticker for Technical Analysis")
        option3 = st.selectbox('', stock_tickers)
        tickerDf = yf.download(option3, start = start_date, end= end_date)
        
         # .................Bollinger bands....................
        st.header('**Bollinger Bands**')
        qf=cf.QuantFig(tickerDf, title='First Quant Figure', legend='top', name='CS')
        qf.add_bollinger_bands()
        fig = qf.iplot(asFigure=True)
        st.plotly_chart(fig)
        st.write("##### The Bollinger Bands are a type of price envelope developed by John Bollinger. They are envelopes plotted at a standard deviation level above and below a simple moving average of the price. Because the distance of the bands is based on standard deviation, they adjust to volatility swings in the underlying price. Bollinger bands help determine whether prices are high or low on a relative basis. They are used in pairs, both upper and lower bands and in conjunction with a moving average")

        # ................Relative Strength Index RSI................
        st.write("------")
        st.header("Relative Strength Index(RSI)")
        df=cf.QuantFig(tickerDf, title='RSI', legend='top', name='CS')
        df.add_rsi()
        fig = df.iplot(asFigure=True)
        st.plotly_chart(fig)
        st.write("##### Introduced by Welles Wilder Jr. in his seminal 1978 book “New Concepts in Technical Trading Systems”, the relative strength index (RSI) becomes a popular momentum indicator. It measures the magnitude of recent price changes to evaluate overbought or oversold conditions. It is displayed as an oscillator and can have a reading from 0 to 100.  ▶️ RSI >= 70: a security is overbought or overvalued and may be primed for a trend reversal or corrective pullback in price. ▶️ RSI <= 30: an oversold or undervalued condition.")


        #  ...................Moving Average Convergence Divergence......................
        st.write("------")
        st.header("Moving Average Convergence Divergence(MACD)")
        df=cf.QuantFig(tickerDf, title='MACD', legend='top', name='CS')
        df.add_macd()
        fig = df.iplot(asFigure=True)
        st.plotly_chart(fig)
        st.write("##### The MACD was developed by Gerald Appel and is probably the most popular price oscillator. It can be used as a generic oscillator for any univariate series, not only price. Typically MACD is set as the difference between the 12-period simple moving average (SMA) and 26-period simple moving average (MACD = 12-period SMA − 26-period SMA), or “fast SMA — slow SMA”, The MACD has a positive value whenever the 12-period SMA is above the 26-period SMA and a negative value when the 12-period SMA is below the 26-period SMA. The more distant the MACD is above or below its baseline indicates that the distance between the two SMAs is growing.")
        st.write("-----")

        
        # .........................Showing Company Fundamental Data Here.................
        st.write("### Fundamentals Data of Company(Like, Balance Sheet, Income Statement, Cashflow,Holdings etc...)")
        
        
        df = yf.Ticker(option3)

        st.write("----")
        st.write("### Income Statement of Company")
        df.financials
        st.write("----")

        st.write("### Balance Sheet Of Company")
        df.balance_sheet
        st.write("----")
        

        st.write("### Cashflow Of Company")
        df.cashflow
        st.write("----")

        st.write("### Major Holders")
        df.major_holders
        st.write("----")
        st.write("### Institutional Holders of Company")
        df.institutional_holders
        st.write("----")

        st.write("### Mutual Fund Holding of Company")
        df._mutualfund_holders
        st.write("----")

        st.write("### Analysis Of Company")
        df.analysis
        st.write("----")

        st.write("### Action Of Company")
        df.actions
        st.write("----")

        st.write("### Earning Of Company")
        df.earnings
        st.write("----")

        st.write("### Calender of Company")
        df.calendar
        st.write("----")

        st.write("### Dividents Yied History of Company")
        df.dividends
        st.write("----")
        

          
    technical()
    
    
elif choose == "Mutual Fund":
    def news():
        
        st.header("Coming Soon Feature")
        st.write("### Please Go to Home or Technical View")

        
        
    news()
    
   
    
elif choose == "Market News":
    def news():
        st.header("Coming Soon Feature")
        st.write("### Please Go to Home or Technical View")

        
        
    news()

    
st.write("Developed with❤️ By Aabid Shaikh")
