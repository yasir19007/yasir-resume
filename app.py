from pathlib import Path
import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
# css_file = current_dir / "styles" / "main.css"
css_file = current_dir/"main.css"
# resume_file = current_dir / "assets" / "CV.pdf"
resume_file = current_dir / "CV.pdf"
# profile_pic = current_dir / "assets" / "pf1.png"
profile_pic = current_dir / "pf1.png"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Yasir Qayyum"
PAGE_ICON = ":wave:"
NAME = "Yasir Qayyum"
DESCRIPTION = """
Data Science Maverick | Excited to Apply Data Science to Solve Real-World Problems
"""
EMAIL = "yasirabcde1@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/yasir-qayyum-bscs1907/",
    "GitHub": "https://github.com/yasir19007",
    "": "https://twitter.com",
}
PROJECTS = {
    "🏆 Conducted exploratory data analysis on a 911 calls dataset, uncovering key insights and trends that informed decision-making. ": "https://github.com/yasir19007/911_call_data",
    "🏆 Performed in-depth analysis of bank stock data using advanced visualization techniques, providing valuable insights into market trends and performance.": "https://github.com/yasir19007/Bank_Stocks",
    "🏆 Solved binary classification using logistic regression, applying advanced ML techniques effectively.": "https://github.com/yasir19007/LR_2",
    "🏆 Built a predictive model using logistic regression to determine life insurance purchases based on age, demonstrating proficiency in insightful decision-making.": "https://github.com/yasir19007/binary_LR",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFILE PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)

# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
# st.subheader("Experience & Qualifications")
# st.write(
#     """
# - ✔️ 8 months of experience in Hyper Mall as an IT assistant.
# - ✔️ Strong hands-on experience and knowledge in Python and Excel.
# - ✔️ Good understanding of statistical principles and their respective applications.
# - ✔️ Excellent team-player and displaying a strong sense of initiative on tasks.
# """
# )

# st.subheader("Qualifications")
# st.write(
#     """
# - ✔️ Bachelor (4-years) : In Computer Science From University Of Peshawar (2023).
# - ✔️ Intermediate : From Govt Hayatabad College Peshawar.
# - ✔️ Matriculation : From Sir Syed Public School Gulbahar, Peshawar.
# """
# )

st.subheader("Qualifications")
st.write(
    """
- ✔️ Bachelor (4-years) : In Computer Science From University Of Peshawar (2023).
- ✔️ Intermediate : From Govt Hayatabad College Peshawar.
- ✔️ Matriculation : From Sir Syed Public School Gulbahar, Peshawar.
    """
)


# --- SKILLS ---
st.write('\n')
st.subheader("Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas, Numpy, Pandas, Seaborn etc).
- 📊 Data Visualization: Matplotlib, PowerBi, MS Excel, Plotly, Seaborn.
- 🦿 Machine Learning:  Supervised Learning + unsupervised Learning
- 🗄️ Databases:  MySQL
"""
)

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**IT Assistant | Hyper Mall**")
st.write("2017 (8 Months)")
st.write(
    """
- ► Provide technical support to store employees.
- ► Maintain the store's computer network.
- ► Install and configure new hardware and software.
- ► Respond to customer inquiries about IT matters.
"""
)

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")

# --- FINAL YEAR PROJECT ---
st.write('\n')
st.subheader("Final Year Project")
st.write("---")
st.write("""

    Developed a web application using Python to predict whether a person is diabetic or not based on symptoms not on medical reports.\n
    The unique feature of this project is that diabetes still be checked even without a medical record.\n
    The application uses a machine learning model that was trained on a dataset of patient records.\n
    The application is easy to use and can be accessed by anyone with a web browser.\n
    The application has the potential to help people identify diabetes early, which can lead to earlier treatment and better outcomes.
    
""")
st.write("---")
