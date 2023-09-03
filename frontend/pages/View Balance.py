import streamlit as st

payment_method = st.selectbox("Payment Method", ["ETH", "Hedera"])

if payment_method == "ETH":
    price = st.text_input("Amount", value="0.0344 ETH", key="price", disabled=True)
else: 
    price = st.text_input("Amount", value="10000 h", key="price", disabled=True)