from reddit_client import get_reddit_instance
from utils import extract_username
from fetcher import fetch_user_data
from analyzer import analyze_persona
from bul1 import build_output
from pdf_generator import PersonaPDF  # ✅ Corrected import


def generate_user_persona(profile_url):
    reddit = get_reddit_instance()
    username = extract_username(profile_url)

    if not username:
        print("❌ Invalid Reddit profile URL.")
        return

    print(f"🔍 Fetching data for u/{username}...")
    posts, comments = fetch_user_data(reddit, username)

    print("📊 Analyzing user activity...")
    persona = analyze_persona(posts, comments)

    print("📝 Creating user persona (text)...")
    build_output(username, persona, posts, comments)

    print("📄 Generating PDF persona...")
    pdf = PersonaPDF()
    pdf.create_persona_pdf(username, persona)  # ✅ Call method of the class

    print("✅ All files created!")


if __name__ == "__main__":
    profile = input("Enter Reddit profile URL: ")
    generate_user_persona(profile)
