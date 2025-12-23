import streamlit as st
# title()--> it will display a big title on web page
st.title("My First Streamlit App")
# write()--> it will normal text on web page
st.write("Hello World")
st.write("Learning streamlit is fun")

st.title("😹Exploring Streamlit Widgets")
st.header("Bold and Italic Text")
st.write("This is **Bold Text** and this is an *Italic Text*")

st.header("Number Slider")
age = st.slider("Select Your Age",1,100,30)   # min max defaultValue
st.write("Your Age Is 🧓",age)

st.header("Taking an user input")
name = st.text_input("What's Your Name?")
if name:
    st.success(f"Nice To Meet You {name} 😇")


st.header("Streamlit Button")
if st.button("Click Me!"):
    st.balloons()  # pops ballon animation

st.header("Markdown")
st.markdown("Hi I am **Markdown** method of *Streamlit*")
# markdown can be used for HTML content
st.markdown("""
<h3>HTML Tag</h3>
<p>This is a paragraph</p>
""",unsafe_allow_html=True)
st.write("Learn More About Streamlit Using : https://streamlit.io/ Link")
st.markdown("""
<p>Learn More About Streamlit Using :  
            <a href="https://streamlit.io/" title="Streamlit Official Docs">Streamlit</a> Link</p>
""",unsafe_allow_html=True)
 
st.header("Streamlit Code")
code1 = '''
def hello():
     print('I am the function')
'''


st.code(code1,language="python")

# latex() --> used to show ML Formula's
st.latex("(a+b)^2 = a^2 + b^2 + 2a*b")
st.latex(r"\frac {1}{1+e^-score}")

st.write("Finding slope(*m*) and intercept(*c*) formula")
st.latex(r"m = \frac {n(\sum_XY)-(\sum_X)(\sum_Y)}{n(\sum_X^2)-(\sum_X)^2}")
st.latex(r"c = \frac {\sum_Y - m(\sum_X)}{n}")