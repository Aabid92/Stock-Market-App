import streamlit as st


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

def news():
  st.header("Coming Soon Feature")
  st.write("### Please Go to App, Stock Analysis or Mutual Fund")
          
news()
