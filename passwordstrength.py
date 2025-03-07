import streamlit as st
import random
import string
import re

def check_password_strength(password):
    score = 0
    feedback = []
    
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")
    
    if any(char.islower() for char in password) and any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("⚠️ Include both uppercase and lowercase letters.")
    
    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("⚠️ Include at least one number.")
    
    if any(char in '!@#$%^&*' for char in password):
        score += 1
    else:
        feedback.append("⚠️ Include at least one special character (!@#$%^&*).")
    
    common_passwords = ['password', '123456', 'qwerty', 'abc123', 'password123']
    if password.lower() in common_passwords:
        score = 1
        feedback = ["❌ Avoid using common passwords."]
    
    if score == 5:
        strength = "🟢 Strong"
        feedback = ["🎉 Great! Your password is strong."]
    elif score >= 3:
        strength = "🟡 Moderate"
    else:
        strength = "🔴 Weak"
    
    return strength, feedback

def generate_strong_password():
    chars = string.ascii_letters + string.digits + '!@#$%^&*'
    return ''.join(random.choice(chars) for _ in range(12))

st.set_page_config(page_title="🔐 Password Strength Meter", layout="centered")

st.markdown("""
    <style>
        .stApp {
            background-color: #white;
            text-align: center;
        }
        .password-box {
            border: 3px solid #4CAF50;
            padding: 15px;
            border-radius: 12px;
            background-color: white;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
            text-align: center;
        }
        .title-text {
            color: #2c3e50;
            font-size: 24px;
            font-weight: bold;
        }
        .feedback {
            color: #d63031;
            font-weight: bold;
        }
        .strong-password {
            color: #27ae60;
            font-size: 18px;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h2 class='title-text'>🔐 Password Strength Meter</h2>", unsafe_allow_html=True)

password = st.text_input("Enter your password:", type="password", placeholder="Type your password here...")
if password:
    strength, feedback = check_password_strength(password)
    
    st.markdown(f"<div class='password-box'><h4>Password Strength: {strength}</h4></div>", unsafe_allow_html=True)
    
    if feedback:
        for msg in feedback:
            st.markdown(f"<p class='feedback'>{msg}</p>", unsafe_allow_html=True)

if st.button("🔑 Generate Strong Password"):
    strong_password = generate_strong_password()
    st.markdown(f"<p class='strong-password'>Suggested Password: {strong_password}</p>", unsafe_allow_html=True)
