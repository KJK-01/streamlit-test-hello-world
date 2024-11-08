import streamlit as st
import streamlit.components.v1 as components

# embed streamlit docs in a streamlit app
components.iframe("https://hello-world-23537.web.app/index/", height=500)

#import streamlit as st
#from streamlit.components.v1 import html

# Define your javascript
#my_js = """
#alert("Hola mundo");
#"""

# Wrapt the javascript as html code
#my_html = f"<script>{my_js}</script>"

# Execute your app
#st.title("Javascript example")
#html(my_html)