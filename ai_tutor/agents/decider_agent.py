import re

class DeciderAgent:
    def __init__(self):
        pass

    def decide_subject(self, prompt: str) -> str:
        prompt_lower = prompt.lower()

        # Placeholder for more sophisticated NLP-based subject detection
        # TODO: Implement NLP-based subject detection

        math_keywords = ["math", "algebra", "calculus", "equation", "number"]
        physics_keywords = ["physics", "force", "energy", "motion", "gravity"]
        chemistry_keywords = ["chemistry", "molecule", "element", "reaction", "compound"]
        biology_keywords = ["biology", "cell", "organism", "dna", "evolution", "life"]
        history_keywords = ["history", "past", "events", "war", "ancient"]
        geography_keywords = ["geography", "earth", "map", "country", "region"]
        economics_keywords = ["economics", "money", "market", "trade", "finance"]

        if any(re.search(r"\b" + keyword + r"\b", prompt_lower) for keyword in math_keywords):
            return "maths"
        if any(re.search(r"\b" + keyword + r"\b", prompt_lower) for keyword in physics_keywords):
            return "physics"
        if any(re.search(r"\b" + keyword + r"\b", prompt_lower) for keyword in chemistry_keywords):
            return "chemistry"
        if any(re.search(r"\b" + keyword + r"\b", prompt_lower) for keyword in biology_keywords):
            return "biology"
        if any(re.search(r"\b" + keyword + r"\b", prompt_lower) for keyword in history_keywords):
            return "history"
        if any(re.search(r"\b" + keyword + r"\b", prompt_lower) for keyword in geography_keywords):
            return "geography"
        if any(re.search(r"\b" + keyword + r"\b", prompt_lower) for keyword in economics_keywords):
            return "economics"

        return "unknown"
