import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image



st.set_page_config(page_title="My Webpage", page_icon="🇩🇿:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/myStyle.css")

# ---- LOAD ASSETS ----
# https://lottie.host/c2c5d4bc-a5d4-4aa7-b7b1-9fd8ee6569cf/4oDhMWERFu.json
# lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
lottie_coding = load_lottieurl("https://lottie.host/c2c5d4bc-a5d4-4aa7-b7b1-9fd8ee6569cf/4oDhMWERFu.json")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, I am Nabila :wave:")
    st.title("A Data Scientist From Algeria")
    st.write(
        "I am passionate about finding ways to use Artificial intelligence to be more efficient and effective in business settings."
    )
    st.write("[Learn more about me >](https://www.linkedin.com/in/nabila-zergoug/)")


# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            I am a recent graduate with a Bachelor's degree in Information Systems and Software Engineering, where I developed a financial tracking system for construction projects, and a Master's degree in Intelligent Information Systems Engineering, where I created a system for monitoring and predicting blood glucose levels in children.

            Currently, I am enrolled in a Data Scientist Bootcamp to further enhance my skills.

            In April 2024, I started working as a Database Manager, and I learn a lot every day in the professional world.

            On my YouTube channel, I am creating tutorials for people who:
            - are looking for a way to leverage the power of Python in their day-to-day work.
            - are struggling with repetitive tasks in Excel and are looking for a way to use Python and VBA.
            - want to learn Data Analysis & Data Science to perform meaningful and impactful analyses.
            - are working with Excel and found themselves thinking - "there has to be a better way."

            If this sounds interesting to you, consider subscribing and turning on the notifications, so you don’t miss any content.
            """
)



    with right_column:
        # Apply CSS class to center the Lottie animation
        st.markdown("<div class='center-lottie'>", unsafe_allow_html=True)
        st_lottie(lottie_coding, height=400, key="coding")
        st.markdown("</div>", unsafe_allow_html=True)



    # ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/zergougnabila@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()

