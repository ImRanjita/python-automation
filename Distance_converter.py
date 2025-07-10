import streamlit as st

st.title("Distance Converter")

conversion_type = st.radio("Select conversion direction:", ["Miles to Kilometers", "Kilometers to Miles"])


if conversion_type == "Miles to Kilometers":
    distance = st.number_input("Enter distance in miles:")
else:
    distance = st.number_input("Enter distance in kilometers:")
if st.button("Convert"):
    if conversion_type == "Miles to Kilometers":
        result = distance * 1.60934
        st.write(f"{distance} miles is equal to {result:.2f} kilometers.")
    else:
        result = distance / 1.60934
        st.write(f"{distance} kilometers is equal to {result:.2f} miles.")
