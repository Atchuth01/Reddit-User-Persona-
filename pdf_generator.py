from fpdf import FPDF
import unicodedata

def clean_text(text):
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    return text.replace("\n", " ").strip()

def truncate_text(text, max_chars=200):
    text = clean_text(text)
    return text if len(text) <= max_chars else text[:max_chars] + "..."

class PersonaPDF(FPDF):
    def __init__(self):
        super().__init__(orientation="L", format="A4")

    def header(self):
        self.set_font("Helvetica", "B", 18)
        self.set_text_color(33, 37, 41)  # dark gray/black
        self.cell(0, 12, f"{self.username} Persona", ln=True)

    def footer(self):
        self.set_y(-10)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(150, 150, 150)
        self.cell(0, 10, "Created by Atchuth V", align='C')

    def add_profile_info(self, persona):
        self.set_font("Helvetica", size=10)
        self.set_text_color(0, 0, 0)
        info = [
            f"Age: {persona['Age']}",
            f"Occupation: {persona['Occupation']}",
            f"Status: {persona['Status']}",
            f"Location: {persona['Location']}",
            f"Tier: {persona['Tier']}",
            f"Archetype: {persona['Archetype']}"
        ]
        self.set_xy(10, 20)
        for line in info:
            self.cell(0, 6, clean_text(line), ln=True)

    def add_avatar(self):
        self.set_xy(240, 20)
        self.set_draw_color(180, 180, 180)
        self.rect(240, 20, 45, 45)
        self.set_xy(240, 42)
        self.set_font("Helvetica", size=8)
        self.set_text_color(100, 100, 100)
        self.cell(45, 6, "Profile Image", ln=True, align='C')
        self.set_font("Helvetica", "I", 7)
        self.set_x(240)
        self.cell(45, 5, "(Image based on Reddit)", ln=True, align='C')

    def add_tags(self):
        tags = ["Practical", "Adaptable", "Spontaneous", "Active"]
        self.set_font("Helvetica", size=9)
        for i, tag in enumerate(tags):
            x = 10 + i * 42
            y = 60
            self.set_fill_color(52, 152, 219)  # soft blue
            self.set_text_color(255, 255, 255)  # white text
            self.rect(x, y, 38, 10, style='F')
            self.set_xy(x, y)
            self.cell(38, 10, tag, align='C')

    def add_trait_bars(self, traits, title, x, y):
        self.set_xy(x, y)
        self.set_font("Helvetica", "B", 11)
        self.set_text_color(33, 37, 41)
        self.cell(0, 6, title, ln=True)
        self.set_font("Helvetica", size=9)

        max_bar_width = 50
        bar_height = 6
        spacing = 2

        for trait, val in traits.items():
            self.set_x(x)
            self.set_text_color(52, 152, 219)  # blue
            self.cell(30, bar_height, clean_text(trait), ln=False)

            # Background
            self.set_fill_color(230, 230, 230)
            self.rect(x + 32, self.get_y(), max_bar_width, bar_height, style='F')

            # Filled portion
            self.set_fill_color(52, 152, 219)
            self.rect(x + 32, self.get_y(), int(max_bar_width * val), bar_height, style='F')

            self.ln(bar_height + spacing)

    def add_bullet_list(self, items, title, x, y, max_items=4, width=125):
        # Light background block
        self.set_fill_color(245, 245, 245)
        total_height = (len(items[:max_items]) * 6) + 12
        self.rect(x, y - 4, width, total_height, style='F')

        self.set_xy(x, y)
        self.set_font("Helvetica", "B", 11)
        self.set_text_color(0, 0, 128)
        self.multi_cell(width, 6, title)
        self.set_font("Helvetica", size=9)
        self.set_text_color(0, 0, 0)

        for item in items[:max_items]:
            self.set_x(x)
            self.multi_cell(width, 5, "- " + truncate_text(item, max_chars=200))

    def create_persona_pdf(self, username, persona):
        self.username = username
        self.add_page()
        self.set_auto_page_break(auto=False)

        self.add_profile_info(persona)
        self.add_avatar()
        self.add_tags()

        self.add_trait_bars(persona['Motivations'], "Motivations", x=10, y=80)
        self.add_trait_bars(persona['Personality'], "Personality", x=150, y=80)

        self.add_bullet_list(persona['Preferences'], "Preferences", x=10, y=140)
        self.add_bullet_list(persona['Behavior'], "Behavior & Habits", x=150, y=140)

        self.add_bullet_list(persona['Goals'], "Goals & Needs", x=10, y=170, max_items=2)
        self.add_bullet_list(persona['Frustrations'], "Frustrations", x=150, y=170, max_items=2)

        self.footer()

        filename = f"{username}_persona.pdf"
        self.output(filename)
        print(f"✅ Themed PDF saved to {filename}")
