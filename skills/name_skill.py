from core.skill import Skill

class NameSkill(Skill):
    @property
    def name(self):
        return "name_skill"

    def run(self, text):
        if "your name" in text.lower():
            return "My name is Ashu Assistant."
        return None
