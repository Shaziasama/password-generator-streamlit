import string
import random

import streamlit as st
import re

#page styling
st.set_page_config(page_title="Password Strength Checker By Shazia Samma", page_icon="🔐" , layout="centered")
# custom css
st.markdown("""
<style>
     .main {text-align: center;}
     .stTextInput {width: 60% !important; margin: auto;}
     .stButton button {width:50%; background-c0lor #4CAF50 color: white; font-size: 18px;} 
     .stButton button:hover {background-color: #45a049;}  
</style>        
     
""", unsafe_allow_html=True)

st.title("🔐Password Strength Generator")


def generate_password(length):
    characters = string.digits + string.ascii_letters + "!@#$%^&*"
    return "".join(random.choice(characters) for i in range(length))

def check_password_strength(password):
    score = 0
    common_password = [
        "password",
        "abc123",
        "123abc",
        "khan123"
    ]
    # Check if password contains at least one digit
    if password is common_password:
        return "❌ This is too common.choose a different password","Weak password"
    
    feedback = []

    if len(password) >= 8:
            score += 1
    else:
            feedback.append("Password must be at least 8 characters long.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Password must contain both uppercase and lowercase characters.")

    if re.search(r"\d+", password):
         score += 1

    else:
         feedback.append("Add at least one number (0-9).")

    if re.search(r"[!#$%&]",password):
         score += 1
    else:
         feedback.append("Include at least one special character (!#$%&).")
    if score ==4:
         return "Strong Password!", "Strong"
    elif score ==3:
         return "Moderate Password - consider adding more security feactures.","Moderate"
    else:
         return"\n" .join(feedback), "Weak password"
    
check_password = st.text_input("Enter your pasword",type="password")
if st.button("Check Password Strength"):
     if check_password:
          check_password_strength(check_password)
          result, strength = check_password_strength(check_password)
          if strength == "strong":
               st.success(result)
               st.balloons()
          elif strength == "Moderate":
               st.warning(result)
          else:
               st.error("Weak Password  Improve it using therse tips:")
               for tip in result.split("\n"):
                    st.error(tip)
                    

     else:
         st.warning("Please enter a password")




    





password_length = st.number_input("Enter the length of password", min_value=8, max_value=20, value=10 )
if st.button("Generate Password"):
    password = generate_password(password_length)
    st.write("Your generated password is:", password)


