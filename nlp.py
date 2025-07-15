from langdetect import detect
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM
from deep_translator import GoogleTranslator

# Detect language
def detect_language(text):
    return detect(text)

# Translate to English if needed
def translate_to_english(text, src_lang):
    if src_lang == "en":
        return text
    return GoogleTranslator(source=src_lang, target="en").translate(text)

# Translate back to original language
def translate_to_original(text, target_lang):
    if target_lang == "en":
        return text
    return GoogleTranslator(source="en", target=target_lang).translate(text)

# Load a general Q&A pipeline
qa_pipeline = pipeline("text2text-generation", model="google/flan-t5-base")

def answer_question(question):
    # Ask the question in English for the model
    return qa_pipeline(question, max_new_tokens=50)[0]['generated_text']

# Generate suggestions based on the question
def generate_suggestions(question):
    # Simple heuristics -- can be expanded
    suggestions_en = [
        "You could try searching for more details.",
        "Consider consulting an official resource.",
        "Break down your question into simpler parts.",
        "Ask an expert for additional help.",
    ]
    # Return suggestions, all translated to the user language
    return suggestions_en

if __name__ == "__main__":
    user_input = input("Enter your question in any language: ")
    user_lang = detect_language(user_input)

    # Translate input to English for the model
    question_en = translate_to_english(user_input, user_lang)

    # Generate the answer
    answer_en = answer_question(question_en)

    # Translate answer back to user language
    answer_local = translate_to_original(answer_en, user_lang)

    # Generate suggestions; then translate each one
    suggestions_en = generate_suggestions(question_en)
    suggestions_local = [translate_to_original(s, user_lang) for s in suggestions_en]

    print(f"\nQuestion: {user_input}")
    print(f"Answer: {answer_local}")
    print("\nSuggestions:")
    for idx, suggestion in enumerate(suggestions_local, 1):
        print(f"{idx}. {suggestion}")

