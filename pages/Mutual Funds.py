from ast import Pass
from email.mime import image
from urllib.parse import scheme_chars
from nbformat import write
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


def mutual_fund():
        st.write("### Popular Mutual Fund List")
        txt = st.text_area('Enter Mutual Fund code in Below input filed ', '''
        Axix Mutual Funds:
            Axis Small Cap Fund Direct Growth -Code: 0P00011MAX.BO
            Axis Growth Opportunities Fund Direct Growth -Code: 0P0001EP9T.BO
            Axis Midcap Fund Direct Growth -Code: 0P0000XVUH.BO
            Axis Gold Fund Direct Growth -Code: 0P0000XVTX.BO
            Axis Bluechip Fund Direct Plan -Code: 0P0000XVTL.BO
            ---------------------------------------------------------------
        Aditya Birla Mutual Funds:
            Aditya Birla Sun Life Savings Fund Daily Dividend Reinvestment Regular Plan -Code: 0P00009N0X.BO)
            Aditya Birla Sun Life Mid Cap Fund Plan A Direct Growth -Code: 0P0000XVXK.BO
            Aditya Birla Sun Life India Gennext Fund Direct Growth -Code: 0P0000XVWN.BO
            Aditya Birla Sun Life Gold Fund Growth Direct Plan -Code: 0P0000XVWW.BO
            Aditya Birla Sun Life NASDAQ 10 -Code: 0P0001NJK1.BO
            ---------------------------------------------------------------
        HDFC Mutual Funds:
            HDFC Retirement Savings Fund Equity Plan Direct Growth -Code: 0P00017K5T.BO
            HDFC Small Cap Fund Direct Growth -Code: 0P0000XVAA.BO
            HDFC Mid Cap Opportunities Fund Direct Growth -Code: 0P0000XVAA.BO
            HDFC Equity Fund Growth -Code: 0P00005WLZ.BO
            HDFC Gold Fund Direct Growth -Code: 0P0000XW7I.BO
            ---------------------------------------------------------------
        ICICI Mutual Funds:
            ICICI Prudential Technology Fund Direct Growth -Code: 0P0000XUZ6.BO
            ICICI Prudential US Bluechip Equity Fund Growth -Code: 0P0000WD5E.BO
            ICICI Prudential Pharma Healthcare And Diagnostics Fund Direct Growth -Code: 0P0001DJWZ.BO
            ICICI Prudential Equity & Debt Fund Direct Plan Growth -Code: 0P0000XWA2.BO
            ICICI Prudential Value Discovery Fund Direct Growth -Code: 0P0000XWAB.BO
            ---------------------------------------------------------------
        SBI Mutual Funds:
            SBI Technology Opportunities Fund Direct Growth -Code: 0P0000XVKP.BO
            SBI Small Cap Fund Direct Plan Growth -Code: 0P0000XW1B.BO
            SBI Magnum Midcap Fund Direct Growth -Code: 0P0000XVKO.BO
            SBI Infrastructure Fund Direct Dividend Payout -Code: 0P0000XVJH.BO
            ---------------------------------------------------------------
        Nippon India Mutual Funds:
            Nippon India Small Cap Fund Direct Growth Plan -Code: 0P0000XVFY.BO
            Nippon India Pharma Fund Direct Growth Plan -Code: 0P0000XVFK.BO
            Nippon India Growth Fund Direct Growth Plan -Code: 0P0000XVDP.BO
            Nippon India Consumption Fund Direct Growth -Code: 0P0000XVF1.BO
            Nippon India Index Fund Sensex Plan Direct Growth -Code: 0P0000XW44.BO
            ---------------------------------------------------------------
        Motilal Oswal Mutual Funds:
            Motilal Oswal Nasdaq 100 fof Direct Growth -Code: 0P0001F0CK.BO
            Motilal Oswal Focused 25 Regular Growth -Code: 0P0000YU92.BO
            Motilal Oswal Equity Hybrid Fund Direct Growth -Code: 0P0001EDSI.BO
            Motilal Oswal Most Focused Midcap 30 Fund Direct Growth -Code: 0P00012ALS.BO
            Motilal Oswal Nifty 200 Momentu -Code: 0P0001OACA.BO
            ---------------------------------------------------------------
        Tata Mutual Funds:
            Tata Digital India Fund Direct Growth -Code: 0P0001784G.BO
            Tata Resources Energy Fund Direct Growth -Code: 0P0001784M.BO
            Tata Small Cap Fund Direct Growth -Code: 0P0001EUZZ.BO
            Tata India Pharma And Healthcare Fund Direct Growth -Code: 0P0001784W.BO
            Tata Multicap Fund Direct Growth -Code: 0P0001ECG8.BO    

        ''',max_chars=3790)

        today = datetime.date.today()
        before = today - datetime.timedelta(days=700)
        start_date = st.sidebar.date_input('Start date', before)
        end_date = st.sidebar.date_input('End date', today)
        if start_date < end_date:
            st.sidebar.success('Start date: `%s`\n\nEnd date:`%s`' % (start_date, end_date))
        else:
            st.sidebar.error('Error: End date must fall after start date.')

        def companies_name():
            co_name = yf.Ticker(mutual_option)
            name = co_name.info['longName']
            st.header(name)

        mutual_option = st.text_input('Enter Mutual Fund Code Here','0P0001784G.BO')
        mf = yf.download(mutual_option,start=start_date, end=end_date)
        companies_name()
        st.bar_chart(mf)

        
mutual_fund()