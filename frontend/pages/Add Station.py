import streamlit as st
from datetime import time
import os

def show_add_station_page():
    st.title("Add Station")

    st.info('In order to be validated as the owner, we must mint an NFT and transfer it to you.')

    # Input fields
    vehicle_type = st.text_input("Vehicle Type")
    
    st.write("Select Opening Time:")
    opening_time = st.time_input("Opening Time", time(0, 0))
    
    st.write("Select Closing Time:")
    closing_time = st.time_input("Closing Time", time(23, 0))

    wallet_address = st.text_input("Wallet Address")

    st.write("Upload Station Image:")
    station_image = st.file_uploader("Choose a file...", type=["jpg", "png", "jpeg"])

    if st.button("Submit"):
        if vehicle_type and opening_time and closing_time and wallet_address:
            st.success("Station Added Successfully!")
            st.write(f"Vehicle Type: {vehicle_type}")
            st.write(f"Opening Time: {opening_time.strftime('%H:%M')}")
            st.write(f"Closing Time: {closing_time.strftime('%H:%M')}")
            st.write(f"Wallet Address: {wallet_address}")
            if station_image:
                st.image(station_image, caption="Station Image", use_column_width=True)
            st.info('NFT minted!')
            st.info('View transaction here: https://mumbai.polygonscan.com/tx/0xa0abba499c7a5fd769d7a6693e281fa6ddbfae0d498c37bfe969710801a48aed')
        else:
            st.error("Please fill in all required fields.")

if __name__ == "__main__":
    show_add_station_page()
