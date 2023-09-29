import streamlit as st

st.title("BMI Calculator")

# Input Fields
weight = st.number_input("Enter your weight (in kilograms)")
height = st.number_input("Enter your height (in centimeters)")

# Calculate BMI
if st.button("Calculate BMI"):
    height_meters = height / 100
    bmi = weight / (height_meters ** 2)
    st.write(f"Your BMI is {bmi:.2f}")

    # Interpret BMI
    if bmi < 18.5:
        st.write("You are underweight.")
    elif 18.5 <= bmi < 24.9:
        st.write("You have a normal weight.")
    elif 25 <= bmi < 29.9:
        st.write("You are overweight.")
    else:
        st.write("You are obese.")
