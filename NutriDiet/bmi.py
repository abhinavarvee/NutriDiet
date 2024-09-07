import streamlit as st
# st.set_page_config(page_title='NutriDiet',page_icon="🍎")
def bmi_calculator():
    st.title("BMI Calculator")


    height = None
    weight = None
    height_unit = "meters"
    weight_unit = "kilograms"

    height_unit = st.selectbox("Select height unit", ["meters", "centimeters"])
    weight_unit = st.selectbox("Select weight unit", ["kilograms", "pounds"])

    if height_unit == "meters":
        height = st.number_input("Enter your height (in meters)", min_value=0.1, max_value=2.5, step=0.01)
    else:  
        height = st.number_input("Enter your height (in centimeters)", min_value=10.0, max_value=250.0, step=1.0)

    if weight_unit == "kilograms":
        weight = st.number_input("Enter your weight (in kilograms)", min_value=10.0, max_value=300.0, step=0.1)
    else:  
        weight = st.number_input("Enter your weight (in pounds)", min_value=22.0, max_value=660.0, step=0.1)


    if height is not None and weight is not None:
     
        if weight_unit == "pounds":
            weight = weight * 0.453592  

        if height_unit == "centimeters":
            height = height / 100.0 

        bmi = weight / (height ** 2)
        bmi_category = get_bmi_category(bmi)
        st.write(f"Your BMI: {bmi:.2f}")
        st.write(f"BMI Category: {bmi_category}")
    else:
        st.warning("Please enter all required information (height and weight).")

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obesity"

if __name__ == "__main__":
    bmi_calculator()
