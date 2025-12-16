import streamlit as st
import os
from persona_generator import generate_persona_pdf  # adjust import if needed

st.set_page_config(
    page_title="Reddit User Persona Generator",
    layout="centered"
)

st.title("🧠 Reddit User Persona Generator")
st.write(
    "Enter a Reddit username to generate a one-page persona PDF "
    "based on posts, comments, and behavioral analysis."
)

# Input
username = st.text_input("Reddit Username", placeholder="e.g. spez")

# Button
if st.button("Generate Persona"):
    if not username:
        st.warning("Please enter a Reddit username.")
    else:
        with st.spinner("Fetching Reddit data and generating persona..."):
            try:
                pdf_path = generate_persona_pdf(username)
                
                with open(pdf_path, "rb") as f:
                    st.success("Persona generated successfully!")
                    st.download_button(
                        label="📄 Download Persona PDF",
                        data=f,
                        file_name=f"{username}_persona.pdf",
                        mime="application/pdf"
                    )

            except Exception as e:
                st.error(f"Error: {e}")
