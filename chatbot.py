# chatbot_simple.py
from sentence_transformers import SentenceTransformer, util

# Load a small embedding model (works offline after download)
model = SentenceTransformer('all-MiniLM-L6-v2')

# Simple knowledge base
knowledge_base = {
    "leave policy": "Employees can take 12 casual leaves and 10 earned leaves per year.",
    "salary slip": "You can download your salary slip from the HR portal.",
    "work from home": "Work from home is allowed two days a week with manager approval.",
    "internet issue": "Please contact the IT helpdesk at it_support@example.com.",
    "password reset": "Use the company portal and click 'Forgot Password' to reset it.",
    "company event": "The next company event is the Annual Day in December.",
    "holiday list": "You can view the official holiday list on the HR website.",
    "attendance": "Attendance must be marked daily before 10 AM."
}

# Profanity filter
bad_words = ["stupid", "damn", "bloody"]

def clean_message(msg):
    words = msg.split()
    for i, w in enumerate(words):
        if w.lower() in bad_words:
            words[i] = "*" * len(w)
    return " ".join(words)

# Precompute embeddings for the knowledge base
kb_questions = list(knowledge_base.keys())
kb_embeddings = model.encode(kb_questions, convert_to_tensor=True)

print("🤖 Simple Employee Chatbot")
print("Type 'exit' to stop.\n")

while True:
    user_input = input("You: ").strip()
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break

    # Clean profanity
    user_input = clean_message(user_input)

    # Compute similarity to each known question
    query_embedding = model.encode(user_input, convert_to_tensor=True)
    scores = util.cos_sim(query_embedding, kb_embeddings)[0]
    best_match = scores.argmax().item()
    best_score = scores[best_match].item()

    # Confidence threshold
    if best_score > 0.55:
        response = knowledge_base[kb_questions[best_match]]
    else:
        response = "I'm not sure about that. Please contact HR or IT support."

    print(f"Chatbot: {response}\n")
