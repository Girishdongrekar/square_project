import streamlit as st

def square(n):
    return n * n

if __name__ == "__main__":
    st.title("🔢 Square Calculator")
    num = st.number_input("Enter a number", step=1, format="%d")
    if st.button("Calculate Square"):
        result = square(num)
        st.success(f"✅ The square of {num} is {result}")
