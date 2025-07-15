
# 🧠 Reddit User Persona Generator

A smart script-based system that fetches Reddit user data and generates a **visually appealing, one-page persona PDF**, capturing user behavior, preferences, goals, and personality traits — useful for research, marketing, or user modeling.

---

## 🚀 Features

- 🔍 Fetches Reddit user posts & comments using the Reddit API (via `praw`)
- 🧠 Analyzes content to extract:
  - Motivations
  - Preferences
  - Personality traits
  - Goals & Frustrations
- 📄 Generates a clean, modern **landscape PDF** with:
  - Profile information
  - Trait bars
  - Behavioral tags
  - Bullet-point summaries
- ✅ Unicode-clean text, safe formatting, no external font dependencies

---

## 📁 Project Structure

```

reddit-user-persona/
├── analyser.py         # Extracts motivations, preferences, personality, goals, etc.
├── bul1.py           # Cleans and truncates list items for PDF
├── fetcher.py          # Pulls recent posts & comments from a Reddit user
├── main.py             # Main executable: runs the pipeline from input to PDF
├── pdf\_generator.py    # Generates persona PDF using FPDF
├── reddit\_client.py    # Reddit API client setup (PRAW credentials go here)
├── utils.py            # Helper functions (normalization, keyword scoring)
├── requirements.txt    # Required Python packages
├── sample\_outputs/     # Sample `.txt` personas (optional per assignment)
└── README.md           # This file

````

---

## 🛠️ Requirements

Install dependencies:

```bash
pip install -r requirements.txt
````

**Dependencies:**

* `praw` – Reddit API wrapper
* `fpdf` – PDF generation
* `unicodedata`, `re` – Text preprocessing (standard library)

---

## 🔧 Setup Instructions

### 1️⃣ Create a Reddit API Application

Go to 👉 [https://www.reddit.com/prefs/apps](https://www.reddit.com/prefs/apps)
Create a script app and copy your `client_id`, `client_secret`, and `user_agent`.

Update `reddit_client.py`:

```python
# reddit_client.py
import praw

reddit = praw.Reddit(
    client_id='YOUR_CLIENT_ID',
    client_secret='YOUR_CLIENT_SECRET',
    user_agent='persona-generator by u/YOUR_USERNAME'
)
```

---

### 2️⃣ Run the Project

```bash
python main.py
```

When prompted:

```
🔗 Enter Reddit profile URL (e.g., https://www.reddit.com/user/elonmusk):
```

The system will fetch the data, generate insights, and create:

* ✅ `elonmusk_persona.txt`
* ✅ `elonmusk_persona.pdf`

---

## 📄 Sample Output

> Example of the generated PDF (1-page landscape):

![Persona PDF Screenshot](user_persona.png)

---

## 🧩 Use Cases

* 🎯 **Marketing personas**
* 🔬 **UX/user research**
* 📊 **Social media analysis**
* 🧠 **AI behavior modeling**

---

## ⚠️ Ethical Notice

This tool is for **educational and analytical** use only.
Respect Reddit’s [API Terms of Service](https://www.redditinc.com/policies/data-api-terms) and user privacy.
**Do not use this to profile users maliciously or without consent.**

---

## 📌 Roadmap Ideas

* [ ] Support batch mode for multiple users
* [ ] Add profile image download
* [ ] Integrate basic sentiment or topic modeling
* [ ] Build Streamlit web app version

---

## 👤 Author

**Atchuth Pavan Sai Vutukuri**
GitHub: [@Atchuth01](https://github.com/Atchuth01)

---

