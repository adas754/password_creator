import streamlit as st

def create_password():
    password = st.text_input('Enter your password')
    sequential = 'abcdefghijklmnopqrstuvwxyz0123456789'
    if any(password[i:i+2] in sequential or password[i:i+2] in sequential[::-1] for i in range(len(password)-1)):
        st.error('Password is too weak!')
    else:
        st.success('Password accepted!')
if __name__ == "__main__":
    create_password()
