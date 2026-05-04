def detect_priority(text):
    text = text.lower()

    high_keywords = ["urgent", "immediately", "today", "asap", "now"]
    medium_keywords = ["week", "soon", "few days", "3 days"]
    low_keywords = ["month", "no rush", "later", "normal"]

    if any(word in text for word in high_keywords):
        return "High"
    elif any(word in text for word in medium_keywords):
        return "Medium"
    elif any(word in text for word in low_keywords):
        return "Low"
    else:
        return "Medium"