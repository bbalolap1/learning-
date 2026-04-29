import streamlit as st
from PIL import Image
import pytesseract
import re

st.set_page_config(page_title="Math Review App", page_icon="📘")

st.title("Math Review Packet Analyzer")

st.subheader("Step 1: Picture Upload")

uploaded_file = st.file_uploader(
    "Upload a picture of your math review packet",
    type=["png", "jpg", "jpeg"]
)

def clean_extracted_text(text):
    text = text.replace("\n\n", "\n")
    text = re.sub(r"[ \t]+", " ", text)
    text = text.strip()
    return text

def split_into_questions(text):
    pattern = r"(?=\n?\d+[\.\)]\s)"
    parts = re.split(pattern, text)

    questions = []

    for part in parts:
        cleaned = part.strip()
        if cleaned:
            questions.append(cleaned)

    return questions

if uploaded_file is not None:
    image = Image.open(uploaded_file)

    st.success("Image uploaded successfully.")
    st.image(image, caption="Uploaded Math Review Image", use_container_width=True)

    st.subheader("Step 2: Image/Text Extraction")

    extracted_text = pytesseract.image_to_string(image)

    st.text_area(
        "Raw Extracted Text",
        extracted_text,
        height=250
    )

    st.subheader("Step 3: Question Cleanup")

    cleaned_text = clean_extracted_text(extracted_text)
    questions = split_into_questions(cleaned_text)

    st.write(f"Found {len(questions)} possible questions.")

    for index, question in enumerate(questions, start=1):
        st.text_area(
            f"Question {index}",
            question,
            height=120
        )

else:
    st.info("Upload a PNG, JPG, or JPEG image to begin.")
