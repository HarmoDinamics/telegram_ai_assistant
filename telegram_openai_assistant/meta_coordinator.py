class MetaCoordinator:
    def __init__(self):
        self.user_profiles = {}  # Speichert MBTI-Profile der User

    def analyze_message(self, user_id, message):
        """Analysiert die Nachricht und entscheidet, welcher AI-Agent antwortet"""
        mbti_type = self.get_mbti_profile(user_id)
        
        # Beispielhafte Entscheidungslogik: Je nach MBTI-Profil wird ein anderer AI-Agent verwendet
        if mbti_type in ["INTP", "ENTP"]:
            return self.send_to_ai_agent("LogicMaster", message)
        elif mbti_type in ["INFJ", "ENFJ"]:
            return self.send_to_ai_agent("EmpathyBot", message)
        else:
            return self.send_to_ai_agent("DefaultAI", message)

    def get_mbti_profile(self, user_id):
        """Gibt das MBTI-Profil des Nutzers zurück (Default: 'DefaultAI')"""
        return self.user_profiles.get(user_id, "DefaultAI")

    def send_to_ai_agent(self, agent_name, message):
        """Leitet die Nachricht an den passenden AI-Agenten weiter"""
        responses = {
            "LogicMaster": "Hier ist eine logische Antwort mit viel analytischem Denken.",
            "EmpathyBot": "Ich verstehe, wie du dich fühlst. Ich helfe dir gerne weiter.",
            "DefaultAI": "Hier ist eine Standardantwort auf deine Nachricht."
        }
        return responses.get(agent_name, "Keine passende Antwort gefunden.")