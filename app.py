#import base64
#import streamlit as st

import streamlit.components.v1 as components

# embed streamlit docs in a streamlit app
components.iframe("https://hello-world-23537.web.app/index/", height=500)

# Define your javascript
#my_js = """
#tableau.extensions.initializeAsync().then(function () {

#    console.log("Initialized")

#    //let worksheets = tableau.extensions.dashboardContent.dashboard.worksheets;

#    //let worksheet = worksheets.find(ws => ws.name === "Structure");

#    //worksheet.addEventListener(tableau.TableauEventType.MarkSelectionChanged, edit);

#});

#const edit = async event => {

#    console.log("Hello World");
#}

#"""

#js = """

#    console.log(window.location);

#"""

# Wrapt the javascript as html code
#my_html = f"""

#<script type = "text/javascript" src="tableau.extensions.1.latest.min.js"></script>

#<script type = "text/javascript" src="/index.js" defer></script>   

#""" 

# Execute your app
#st.title("Javascript example")
#html(my_html)


import streamlit as st

conn = st.connection("snowflake")

option = st.selectbox(
    "Which region are you editing?",
    ("E1", "E2", "E3", "E4", "E5", "E6", "E7", "E8", "E9", "W1", "W2", "W3", "W4", "W5", "W6", "W7", "W8"),
)

managerInput = st.text_input("Manager", "")

shopInput = st.text_input("Shop Size", "")

if st.button("Submit"):
    conn.cursor().execute(
        "UPDATE mytable SET MANAGER = '" + managerInput + "' , SHOP_SIZE = " + shopInput + " WHERE REGION = '" + option + "'"
    )
    st.cache_data.clear()
    st.rerun()

