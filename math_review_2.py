import streamlit as st
import easyocr
from PIL import Image
import numpy as np

st.title("Math Review - OCR Step")

uploaded_file = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image)

    reader = easyocr.Reader(['en'])
    result = reader.readtext(np.array(image))

    st.subheader("Extracted Text")

    for (bbox, text, prob) in result:
        st.write(text)
