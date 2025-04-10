import streamlit as st

st.title("User Profile Form")

# Collect user input
with st.form("user_info_form"):
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0, step=1)
    favorite_color = st.color_picker("Favorite Color")
    submitted = st.form_submit_button("Submit")

# Display user profile
if submitted:
    st.subheader("🎉 User Profile")
    st.markdown(f"**Name:** {name}")
    st.markdown(f"**Age:** {age}")
    st.markdown(f"**Favorite Color:** {favorite_color}")
    st.markdown(f"<div style='width:100px;height:30px;background-color:{favorite_color};border-radius:5px;'></div>", unsafe_allow_html=True)

