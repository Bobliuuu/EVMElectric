import streamlit as st
import webbrowser 

st.title("EVMElectric")

st.markdown("""Tired of finding a charging station for your electric vehicles?  
            EVMelectric helps crowdcource electric charging stations using a DAO!""")

st.image('evmelectriclogo.png')

if st.button('Learn More: '):
    webbrowser.open('https://creator.voiceflow.com/prototype/64f470cb730b0eb116bcd26f')