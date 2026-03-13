import streamlit as st
from PIL import Image

# Import functions from your modules
from text_summarizer import summarize_text
from pdf_summarizer import summarize_pdf
from image_captioning import generate_caption


# Streamlit Page Config
st.set_page_config(
    page_title="AI Summarizer & Caption Generator",
    page_icon="🤖",
    layout="wide"
)

st.title("📄 AI Text / PDF Summarizer + 🖼 Image Caption Generator")
st.write("Upload text, PDF, or images to generate summaries and captions using AI.")

# Sidebar selection
option = st.sidebar.selectbox(
    "Choose Function",
    [
        "Text Summarization",
        "PDF Summarization",
        "Image Captioning"
    ]
)


# ===============================
# TEXT SUMMARIZATION
# ===============================
if option == "Text Summarization":

    st.header("📝 Text Summarization")

    text_input = st.text_area(
        "Enter your text here",
        height=300
    )

    if st.button("Generate Summary"):

        if text_input.strip() == "":
            st.warning("Please enter some text.")
        else:
            with st.spinner("Generating summary..."):
                summary = summarize_text(text_input)

            st.subheader("Summary")
            st.success(summary)


# ===============================
# PDF SUMMARIZATION
# ===============================
elif option == "PDF Summarization":

    st.header("📄 PDF Summarization")

    pdf_file = st.file_uploader(
        "Upload PDF file",
        type=["pdf"]
    )

    if pdf_file is not None:

        if st.button("Summarize PDF"):

            with st.spinner("Extracting and summarizing..."):
                summary = summarize_pdf(pdf_file)

            st.subheader("Summary")
            st.success(summary)


# ===============================
# IMAGE CAPTIONING
# ===============================
elif option == "Image Captioning":

    st.header("🖼 Image Caption Generator")

    image_file = st.file_uploader(
        "Upload Image",
        type=["jpg", "jpeg", "png"]
    )

    if image_file is not None:

        image = Image.open(image_file)

        st.image(image, caption="Uploaded Image", use_column_width=True)

        if st.button("Generate Caption"):

            with st.spinner("Generating caption..."):
                caption = generate_caption(image)

            st.subheader("Caption")
            st.success(caption)


# Footer
st.markdown("---")
st.markdown("Built with 🤖 Transformers + Streamlit")
