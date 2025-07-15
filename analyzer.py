from textblob import TextBlob
from collections import Counter
import re
import nltk
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')


def clean_text(text):
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'[^a-zA-Z ]', '', text)
    return text.lower()


def extract_keywords(posts, comments):
    stop_words = set(stopwords.words('english'))
    combined_text = " ".join([
        (p.get('title', '') + ' ' + p.get('text', '') + ' ' + p.get('body', '')) for p in posts
    ] + [
        c.get('body', '') for c in comments
    ])
    words = [word for word in clean_text(combined_text).split() if word not in stop_words and len(word) > 3]
    return Counter(words).most_common(10)


def get_sentiment_distribution(texts):
    polarities = [TextBlob(text).sentiment.polarity for text in texts if text.strip()]
    subjectivities = [TextBlob(text).sentiment.subjectivity for text in texts if text.strip()]
    polarity_score = sum(polarities) / len(polarities) if polarities else 0
    subjectivity_score = sum(subjectivities) / len(subjectivities) if subjectivities else 0
    return round(polarity_score, 2), round(subjectivity_score, 2)


def get_motivation_scores(posts, comments):
    keywords = {
        "Convenience": ["easy", "fast", "quick", "accessible"],
        "Wellness": ["health", "exercise", "fit", "mental"],
        "Speed": ["fast", "quick", "time-saving"],
        "Preferences": ["like", "prefer", "favourite", "wish"],
        "Comfort": ["comfortable", "cozy", "relax"],
        "Dietary Needs": ["diet", "food", "vegetarian", "vegan", "allergy"]
    }
    text = " ".join([
        (p.get('title', '') + ' ' + p.get('text', '') + ' ' + p.get('body', '')) for p in posts
    ] + [
        c.get('body', '') for c in comments
    ]).lower()
    scores = {}
    for category, words in keywords.items():
        matches = sum(text.count(word) for word in words)
        scores[category] = min(matches / 5, 1.0)
    return scores


def get_personality_scores(posts, comments):
    traits = {
        "Introvert": ["alone", "quiet"],
        "Intuition": ["gut", "feel"],
        "Feeling": ["emotional", "feel"],
        "Perceiving": ["spontaneous"]
    }
    text = " ".join([
        (p.get('title', '') + ' ' + p.get('text', '') + ' ' + p.get('body', '')) for p in posts
    ] + [
        c.get('body', '') for c in comments
    ]).lower()
    scores = {}
    for trait, words in traits.items():
        matches = sum(text.count(word) for word in words)
        scores[trait] = min(matches / 5, 1.0)
    return scores


def extract_goals(posts, comments):
    goals = []
    for item in posts + comments:
        text = item.get('title', '') + ' ' + item.get('text', '') + item.get('body', '')
        if any(kw in text.lower() for kw in ["want to", "goal", "need to"]):
            goals.append(text.strip())
    return goals[:3] if goals else ["Not clear"]


def extract_frustrations(posts, comments):
    frus = []
    for item in posts + comments:
        text = item.get('title', '') + ' ' + item.get('text', '') + item.get('body', '')
        if any(word in text.lower() for word in ["frustrated", "annoyed", "hate", "can't", "won't"]):
            frus.append(text.strip())
    return frus[:3] if frus else ["Not clear"]


def extract_behavior(posts, comments):
    behaviors = []
    keywords = ["routine", "usually", "tend to", "always", "every day"]
    for item in posts + comments:
        text = item.get('title', '') + ' ' + item.get('text', '') + item.get('body', '')
        if any(k in text.lower() for k in keywords):
            behaviors.append(text.strip())
    return behaviors[:3] if behaviors else ["Not mentioned"]


def extract_status_location(posts, comments):
    text = " ".join([
        (p.get('title', '') + ' ' + p.get('text', '') + ' ' + p.get('body', '')) for p in posts
    ] + [
        c.get('body', '') for c in comments
    ]).lower()
    location = "India" if "india" in text else "Not mentioned"
    status = "Single" if "single" in text else "Not mentioned"
    return status, location


def analyze_persona(posts, comments):
    keywords = extract_keywords(posts, comments)
    polarity, subjectivity = get_sentiment_distribution([
        (p.get('title', '') + ' ' + p.get('text', '') + ' ' + p.get('body', '')) for p in posts
    ] + [
        c.get('body', '') for c in comments
    ])
    motivations = get_motivation_scores(posts, comments)
    personality = get_personality_scores(posts, comments)
    frustrations = extract_frustrations(posts, comments)
    goals = extract_goals(posts, comments)
    behavior = extract_behavior(posts, comments)
    status, location = extract_status_location(posts, comments)

    return {
        "Avatar": None,
        "Age": "Not mentioned",
        "Occupation": keywords[0][0] if keywords else "Not mentioned",
        "Status": status,
        "Location": location,
        "Tier": "Early Adopter",
        "Archetype": "The Realist",
        "Motivations": motivations,
        "Preferences": [k[0] for k in keywords],
        "Personality": personality,
        "Frustrations": frustrations,
        "Goals": goals,
        "Behavior": behavior
    }
