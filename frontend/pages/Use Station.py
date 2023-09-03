import streamlit as st

def show_use_station_page():
    st.title("Use Station")

    station_title = st.experimental_get_query_params().get("station_title", ["Station Name"])[0]
    st.subheader(f"Station: {station_title}")

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
        else:
            st.error("Please provide a valid wallet address.")

if __name__ == "__main__":
    show_use_station_page()