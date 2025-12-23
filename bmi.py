import streamlit as st
import pandas as pd
import altair as alt
 
st.set_page_config(page_title="BMI Calculator",layout="centered")
 
st.title("💪 BMI Calculator")
st.write("Let's Calculate Your **Body Mass Index** And Understand What It Means")
 
st.header(" 🖋 Enter Your Details")
height = st.number_input("Enter Your Height (in cm)",min_value=50,max_value=250,value=170)
weight = st.number_input("Enter Your Weight (in kg)",min_value=10,max_value=200,value=65)
 
st.write("📏 Your Height : ",height,"cm")
st.write("🧸 Your Weight : ",weight,"kg")
 
if st.button("Calculate BMI"):
    h_m = height / 100                   # convert cm to meter
    bmi = weight / (h_m ** 2)
    st.success(f"📍 Your BMI Is : **{bmi:.2f}**")
 
    # BMI Category
    if bmi < 18.5:
        category = "Underweight 🫣"
        color = "#0EE3D5"
 
    elif 18.5 <= bmi < 25:
        category = "Normal 😄"
        color = "#F0F0A5"
 
    elif 25 <= bmi < 30:
        category = "Overweight 🧐"
        color = "#968CE7"
 
    else:
        category = "Obese 😬"
        color = "#E70E65"
   
    st.markdown(
        f"""
        <div style='background-color:{color};text-align:center'>
        <h3>Your BMI Category {category}</h3>
        </div>""",unsafe_allow_html=True
    )
 
st.header("📊 BMI Range Chart")
bmi_data = pd.DataFrame({"Category":["Underweight","Normal","Overweight","Obese"] ,
                         "Range":[18.5,24.9,29.9,40]})
 
# Define custom colors for each category
color_scale = alt.Scale(
    domain=["Underweight", "Normal", "Overweight", "Obese"],
    range=["#0EE3D5", "#F0F0A5", "#968CE7", "#E70E65"]
)
 
# Create chart
chart = (
    alt.Chart(bmi_data)
    .mark_bar()
    .encode(
        x=alt.X("Category:N", title="BMI Category"),
        y=alt.Y("Range:Q", title="BMI Range"),
        color=alt.Color("Category:N", scale=color_scale, legend=None)
    )
    .properties(width=600, height=400)
)
 
st.altair_chart(chart, width='stretch')
 