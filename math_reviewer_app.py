import streamlit as st
from PIL import Image

st.set_page_config(page_title="Math Review App", page_icon="📘")

st.title("Math Review Packet Analyzer")
st.subheader("Step 1: Picture Upload")

uploaded_file = st.file_uploader(
    "Upload a picture of your math review packet",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file)

    st.success("Image uploaded successfully.")

    st.image(image, caption="Uploaded Math Review Image", use_container_width=True)

    st.write("File name:", uploaded_file.name)
    st.write("File type:", uploaded_file.type)
    st.write("File size:", uploaded_file.size, "bytes")
else:
    st.info("Upload a PNG, JPG, or JPEG image to begin.")
