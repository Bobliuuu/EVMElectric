import streamlit as st
import webbrowser

st.title("Stations")

# Add a button to add a new station
if st.button("Add New Station"):
    webbrowser.open("https://google.ca", new = 0, autoraise = True)

# Search bar
search_query = st.text_input("Search Stations", "")

# Dummy list of stations (you can replace this with your data)
stations = [
    {"name": "Bob's Charging Station", "description": "Description of Station 1"},
    {"name": "Tiffany's Charging Station", "description": "Description of Station 2"},
    {"name": "Luke's Charging Station", "description": "Description of Station 3"},
]

# Filter and display stations
for station in stations:
    if search_query.lower() in station["name"].lower():
        st.subheader(station["name"])
        st.write(f"Description: {station['description']}")
        if st.button(f"Use {station['name']}"):
            webbrowser.open("https://google.ca")
