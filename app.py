import streamlit as st
import os

from reddit_client import get_reddit_instance
from utils import extract_username
from fetcher import fetch_user_data
from analyser import analyze_persona
from bul1 import build_output
from pdf_generator import PersonaPDF

# -------------------- Page Config --------------------
st.set_page_config(
    page_title="Reddit User Persona Generator",
    page_icon="🧠",
    layout="centered"
)

# -------------------- UI --------------------
st.title("🧠 Reddit User Persona Generator")
st.markdown(
    "Generate a **one-page professional persona** from a Reddit user's activity."
)

st.divider()

profile_url = st.text_input(
    "🔗 Enter Reddit Profile URL",
    placeholder="https://www.reddit.com/user/username/"
)

generate = st.button("🚀 Generate Persona")

# -------------------- Logic --------------------
if generate:
    if not profile_url.strip():
        st.warning("Please enter a valid Reddit profile URL.")
    else:
        try:
            with st.spinner("🔍 Fetching Reddit data..."):
                reddit = get_reddit_instance()
                username = extract_username(profile_url)

                if not username:
                    st.error("Invalid Reddit profile URL.")
                    st.stop()

                posts, comments = fetch_user_data(reddit, username)

            with st.spinner("📊 Analyzing user activity..."):
                persona = analyze_persona(posts, comments)

            with st.spinner("📝 Generating persona files..."):
                # Generate TXT
                build_output(username, persona, posts, comments)

                # Generate PDF
                pdf = PersonaPDF()
                pdf.create_persona_pdf(username, persona)

            st.success("✅ Persona generated successfully!")

            # -------------------- Downloads --------------------
            txt_file = f"{username}_persona.txt"
            pdf_file = f"{username}_persona.pdf"

            col1, col2 = st.columns(2)

            with col1:
                if os.path.exists(txt_file):
                    with open(txt_file, "r", encoding="utf-8") as f:
                        st.download_button(
                            "📄 Download TXT",
                            f.read(),
                            file_name=txt_file,
                            mime="text/plain"
                        )

            with col2:
                if os.path.exists(pdf_file):
                    with open(pdf_file, "rb") as f:
                        st.download_button(
                            "📕 Download PDF",
                            f,
                            file_name=pdf_file,
                            mime="application/pdf"
                        )

        except Exception as e:
            st.error("Something went wrong while generating the persona.")
            st.exception(e)

# -------------------- Footer --------------------
st.divider()
st.caption(
    "Built by Atchuth Pavan Sai Vutukuri | Internship Selection Task"
)
