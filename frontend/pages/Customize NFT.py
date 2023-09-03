import streamlit as st

def update_nft_info(name, file):
    #nft_file.write(f"Name: {name}\n")
    #nft_file.write(f"File: {file}\n")
    pass

def main():
    st.title("Customize Flow")

    name = st.text_input("Enter NFT Name:")
    file = st.file_uploader("Upload NFT File (Image, Video, etc.):", type=["txt", "jpg", "jpeg", "png", "gif", "mp4"])

    if st.button("Update NFT Info"):
        if name and file:
            update_nft_info(name, file.name)
            st.success("NFT information updated successfully!")

    st.subheader("Current NFT Information:")
    try:
        with open("nft.txt", "r") as nft_file:
            current_info = nft_file.read()
        st.text(current_info)
    except FileNotFoundError:
        st.warning("NFT information not found. Please update it.")

if __name__ == "__main__":
    main()