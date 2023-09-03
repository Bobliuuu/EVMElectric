import streamlit as st

def show_use_station_page():
    st.title("Use Station")

    station_title = st.experimental_get_query_params().get("station_title", ["Station Name"])[0]
    st.subheader(f"Station: {station_title}'s Charging Station")

    payment_method = st.selectbox("Payment Method", ["ETH", "Hedera"])

    if payment_method == "ETH":
        price = st.text_input("Price (ETH)", value="0.03285 ETH", key="price", disabled=True)
    else: 
        price = st.text_input("Price (hbar)", value="34.586 h", key="price", disabled=True)

    wallet_address = st.text_input("Wallet Address")

    if st.button("Pay"):
        if wallet_address:
            if payment_method == "ETH":
                st.success(f"Payment Successful! {price} paid via Metamask.")
            else:
                st.success(f"Payment Successful! {price} paid via Hedera.")
            st.info('''Logged to Hedera Consensus Service. Response: 
                    Your topic ID is: 0.0.1163900
                    The message transaction status: SUCCESS
                    Sun Sep 03 2023 08:49:56 GMT-0400 (Eastern Daylight Time) Received: Payment recieved!''')
        else:
            st.error("Please provide a valid wallet address.")

if __name__ == "__main__":
    show_use_station_page()