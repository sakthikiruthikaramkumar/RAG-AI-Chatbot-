import streamlit as st
from PyPDF2 import PdfReader
from main import analyze


st.set_page_config(
    page_title="Medical Symptom Wellness Assistant",
    layout="centered"
)



st.markdown("""
<style>
.main-title{
    text-align:center;
    color:#7ED957;
    font-size:40px;
    font-weight:900;
}
.sub-text{
    text-align:center;
    color:#C9D1D9;
    font-size:18px;
}
.section-box{
    padding:20px;
    background:#161B22;
    border-radius:12px;
    margin-top:10px;
}
</style>
""", unsafe_allow_html=True)



st.markdown('<p class="main-title">Medical Symptom Wellness Assistant</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-text">Upload a symptom PDF or type your symptoms. This tool provides NON-DIAGNOSTIC wellness guidance only.</p>', unsafe_allow_html=True)




uploaded_pdf = st.file_uploader("Upload Symptom / Medical Note PDF", type=["pdf"])


def extract_pdf_text(pdf_file):
    reader = PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text


pdf_text = ""

if uploaded_pdf:
    pdf_text = extract_pdf_text(uploaded_pdf)
    st.success("PDF uploaded and processed successfully.")




symptoms = st.text_area("Describe your symptoms", value=pdf_text, height=180)

lifestyle = st.text_area("Provide lifestyle details (diet, sleep, stress, exercise, habits)", height=160)

history = st.text_area("Any past conditions, allergies, or medications? (optional)", height=140)

age = st.number_input("Age", min_value=1, max_value=120)
gender = st.selectbox("Gender", ["Prefer not to say","Female","Male","Other"])




if st.button("Get Wellness Guidance"):
    if not symptoms.strip():
        st.warning("Please describe your symptoms or upload a PDF first.")
    else:
        with st.spinner("Analyzing your inputs..."):
            try:
                response = analyze(symptoms, lifestyle, history, age, gender)

                st.markdown('<div class="section-box">', unsafe_allow_html=True)
            
                st.json(response)
                st.markdown('</div>', unsafe_allow_html=True)

            except Exception as e:
                st.error(e)
