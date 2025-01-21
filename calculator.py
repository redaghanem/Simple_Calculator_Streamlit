import streamlit as st

# Title for the app
st.title("Simple Calculator")

# User inputs
st.subheader("Enter two numbers:")
num1 = st.number_input("First number", value=0.0, step=0.1)
num2 = st.number_input("Second number", value=0.0, step=0.1)

# Select operation
operation = st.selectbox(
    "Choose an operation",
    ["Addition", "Subtraction", "Multiplication", "Division"]
)

# Perform the calculation
result = None
if st.button("Calculate"):
    if operation == "Addition":
        result = num1 + num2
    elif operation == "Subtraction":
        result = num1 - num2
    elif operation == "Multiplication":
        result = num1 * num2
    elif operation == "Division":
        if num2 != 0:
            result = num1 / num2
        else:
            st.error("Division by zero is not allowed!")

# Display the result
if result is not None:
    st.success(f"The result is: {result}")
