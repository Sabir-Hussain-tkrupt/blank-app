import streamlit as st
from datetime import datetime
import os

# Page Configuration
st.set_page_config(page_title="📘 Assignment Submission", layout="centered")

# Title and Subtitle
st.title("📘 Student Assignment Submission Portal")
st.caption("Submit your assignment securely. Only PDF or DOC/DOCX files are accepted.")

# Form Container
with st.form("assignment_form", clear_on_submit=True):
    st.subheader("📝 Enter Your Details")
    student_name = st.text_input("Full Name", placeholder="e.g., John Doe")
    uploaded_file = st.file_uploader(
        "Upload Assignment File (PDF or DOC/DOCX)", 
        type=["pdf", "doc", "docx"]
    )
    submitted = st.form_submit_button("Submit Assignment")

# Handle Form Submission
if submitted:
    if not student_name:
        st.error("Please enter your name.")
    elif not uploaded_file:
        st.error("Please upload a file.")
    else:
        # Create a directory to save submissions
        save_dir = "submissions"
        os.makedirs(save_dir, exist_ok=True)

        # Create a unique file name
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_ext = os.path.splitext(uploaded_file.name)[1]
        safe_name = student_name.replace(" ", "_")
        save_path = os.path.join(save_dir, f"{safe_name}_{timestamp}{file_ext}")

        # Save file
        with open(save_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.success(f"✅ Thank you, {student_name}! Your assignment has been submitted.")
        st.info(f"📁 Saved as: `{save_path}`")
