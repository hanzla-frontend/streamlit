# chapter 1
import streamlit as st 
st.title("Chai Streamlit App")
st.header("Brewed with streamlit")
st.text("Welcome to your first interactive app")
st.write("Choose of different verity of chia ")
chai=st.selectbox("Select your favorite chia",["Black chia","White chia","Green chai"])
st.write(f"You choose {chai} . Excellent choice!") 
st.success("you chia has been brouded successfully")

