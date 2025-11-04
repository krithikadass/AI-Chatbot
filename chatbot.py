

print("Company Chatbot")
print("Type 'exit' to quit.\n")
responses = {
    "leave": "Employees can take 12 casual and 10 earned leaves per year.",
    "salary": "Salary slips can be downloaded from the HR portal.",
    "work from home": "Work from home is allowed two days a week with manager approval.",
    "internet": "Please contact the IT helpdesk at it_support@example.com.",
    "password": "Go to the company portal and click 'Forgot Password' to reset it.",
    "event": "The next company event is the Annual Day in December.",
    "holiday": "You can view the official holiday list on the HR website.",
    "attendance": "Attendance must be marked before 10 AM daily."
}

bad_words = ["stupid", "damn", "bloody"]

def clean_message(message):
    """Replace bad words with stars"""
    words = message.split()
    for i, w in enumerate(words):
        if w.lower() in bad_words:
            words[i] = "*" * len(w)
    return " ".join(words)

while True:
    user = input("You: ").strip().lower()
    if user == "exit":
        print("Chatbot: Goodbye! Have a nice day 👋")
        break
    user = clean_message(user)
    found = False
    for key in responses:
        if key in user:
            print("Chatbot:", responses[key])
            found = True
            break

    if not found:
        print("Chatbot: Sorry, I don’t have an answer for that. Please contact HR or IT support.")
