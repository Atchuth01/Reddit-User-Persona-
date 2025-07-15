def cite_examples(trait_words, posts, comments):
    citations = []
    all_items = posts + comments
    for item in all_items:
        text = item.get('title', '') + " " + item.get('text', '') + item.get('body', '')
        if any(word.lower() in text.lower() for word in trait_words):
            citations.append(item['permalink'])
            if len(citations) >= 2:
                break
    return citations


def build_output(username, persona, posts, comments):
    filename = f"{username}_persona.txt"
    with open(filename, "w", encoding='utf-8') as f:
        f.write(f"👤 Reddit Persona: u/{username}\n")
        f.write(f"🖼️ Avatar: https://www.reddit.com/user/{username}/about/avatar/\n\n")

        f.write(f"📌 Name: u/{username}\n")
        f.write(f"🎂 Age: {persona['Age']}\n")
        f.write(f"💼 Occupation: {persona['Occupation']}\n")
        f.write(f"❤️ Status: {persona['Status']}\n")
        f.write(f"📍 Location: {persona['Location']}\n")
        f.write(f"🎯 Tier: {persona['Tier']}\n")
        f.write(f"🧠 Archetype: {persona['Archetype']}\n\n")
        f.write("------------------------------------------------------------\n\n")

        f.write("🚀 Motivations:\n")
        for key, score in persona['Motivations'].items():
            bar = '█' * int(score * 10)
            f.write(f" - {key:<18}: {bar} ({score:.2f})\n")
        f.write("\n")

        f.write("🍴 Preferences:\n")
        for pref in persona['Preferences']:
            f.write(f" - {pref}\n")
        f.write("\n")

        f.write("🧠 Personality Traits:\n")
        for trait, score in persona['Personality'].items():
            bar = '█' * int(score * 10)
            f.write(f" - {trait:<20}: {bar} ({score:.2f})\n")
        f.write("\n")

        f.write("🌀 Behavior & Habits:\n")
        for b in persona['Behavior']:
            f.write(f" - {b}\n")
        f.write("\n")

        f.write("😤 Frustrations:\n")
        for fr in persona['Frustrations']:
            f.write(f" - {fr}\n")
        f.write("\n")

        f.write("🎯 Goals & Needs:\n")
        for g in persona['Goals']:
            f.write(f" - {g}\n")
        f.write("\n")

    print(f"✅ Persona saved to {filename}")
