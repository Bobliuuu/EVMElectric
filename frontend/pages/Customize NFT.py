import streamlit as st

# Function to update the "nft.txt" file with the provided information
def update_nft_info(name, file):
    with open("nft.txt", "w") as nft_file:
        nft_file.write(f"Name: {name}\n")
        nft_file.write(f"File: {file}\n")

# Streamlit app
def main():
    st.title("Customize Flow - NFT Customization")

    # Input fields for name and file
    name = st.text_input("Enter NFT Name:")
    file = st.file_uploader("Upload NFT File (Image, Video, etc.):", type=["txt", "jpg", "jpeg", "png", "gif", "mp4"])

    if st.button("Update NFT Info"):
        if name and file:
            update_nft_info(name, file.name)
            st.success("NFT information updated successfully!")

    # Display the current NFT information from the "nft.txt" file
    st.subheader("Current NFT Information:")
    try:
        with open("nft.txt", "r") as nft_file:
            current_info = nft_file.read()
        st.text(current_info)
    except FileNotFoundError:
        st.warning("NFT information not found. Please update it.")

if __name__ == "__main__":
    main()