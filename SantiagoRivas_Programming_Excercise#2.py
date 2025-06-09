# Create the list of words that might be spam.
SPAM_KEYWORDS = [
    "free", "buy now", "limited time", "act now", "winner", "click here", "urgent",
    "cash bonus", "risk-free", "guaranteed", "congratulations", "exclusive deal", 
    "no cost", "cheap", "win", "100% free", "credit card", "instant access",
    "double your income", "work from home", "unsubscribe", "lowest price", "miracle",
    "luxury", "get paid", "lose weight", "offer expires", "save big", "order now", 
    "investment opportunity"
]

# Make sure to track and find all the words that might be spam.
def calculate_spam_score(message):
    """Calculate spam score and track matched keywords."""
    score = 0
    matched_keywords = []

    message_lower = message.lower()  # Make comparison case-insensitive

    for keyword in SPAM_KEYWORDS:
        if keyword in message_lower:
            score += 1
            matched_keywords.append(keyword)
    
    return score, matched_keywords

def classify_spam(score):
    """Classify spam likelihood based on score."""
    if score >= 10:
        return "High likelihood of spam"
    elif score >= 5:
        return "Moderate likelihood of spam"
    else:
        return "Low likelihood of spam"

# Define the main program.
def main():
    print("=== SPAM DETECTION PROGRAM ===")
    email_message = input("Enter your email message:\n")

    score, matched = calculate_spam_score(email_message)
    likelihood = classify_spam(score)

    print("\n=== ANALYSIS RESULTS ===")
    print(f"Spam Score: {score}")
    print(f"Likelihood: {likelihood}")
    print(f"Matched Spam Words/Phrases: {', '.join(matched) if matched else 'None'}")

# Run the main function
main()
