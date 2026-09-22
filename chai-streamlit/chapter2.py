import streamlit as st 

st.title("Chia Maker App")
 
if st.button("Make Chia"):
    # pass 
    st.success("Your chia is being brewed!") 
    
add_masala=st.checkbox("Add Masala")

if add_masala:
    st.write("Masala added to your chia ")


tea_type= st.radio("Pick your chai base",["Milk","water","Tea"])    

st.write(f"Selected base : {tea_type}")

favour=st.selectbox("Choose flavour :" ,["Adrak","Kesar","Tulsi"])

st.write(f"Selected flavour : {favour}")

sugar=st.slider("Select sugar Level", 0,5,2)
st.write(f"Selected sugar level : {sugar}") 


