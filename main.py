import os
import random
from anki.collection import Collection
from dotenv import load_dotenv
from google import genai

load_dotenv()

COLLECTION_PATH = os.getenv("COLLECTION_PATH")
DECK_NAME = os.getenv("DECK_NAME")
FIELD_WORD = os.getenv("FIELD_WORD")
FIELD_MEANING = os.getenv("FIELD_MEANING")

client = genai.Client()


def evaluate_sentence(word: str, meaning: str, user_sentence: str) -> str:
    prompt = f"""
    You are a Japanese language tutor reviewing a student's sentence practice.

    - Target Word: {word}
    - Meaning: {meaning}
    - Student's Sentence: {user_sentence}

    Task:
    1. Check if the sentence is grammatically correct.
    2. Check if '{word}' is used naturally in context.
    3. If there are errors or awkward phrasing, provide corrected/more natural options with brief explanations.
    Keep the feedback concise.
    """

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt,
    )
    return response.text


def practice_seen_word(col_path: str, deck: str):
    col = Collection(col_path)

    try:
        query = f'deck:"{deck}" prop:reps>0'
        card_ids = col.find_cards(query)

        if not card_ids:
            print(f"No seen cards found in deck '{deck}'.")
            return

        card = col.get_card(random.choice(card_ids))
        note = card.note()

        if FIELD_WORD not in note or FIELD_MEANING not in note:
            print(f"Missing expected fields. Available fields: {list(note.keys())}")
            return

        word = note[FIELD_WORD]
        meaning = note[FIELD_MEANING]

        print(f"\nTarget Word: {word}")
        user_sentence = input("Write a sentence: ")

        if not user_sentence.strip():
            print("Empty input. Exiting.")
            return

        print(f"Word Meaning: {meaning}")
        print(f"\n-- Fetching Gemini Feedback ---")

        feedback = evaluate_sentence(word, meaning, user_sentence)
        print(feedback)

    finally:
        col.close()


practice_seen_word(COLLECTION_PATH, DECK_NAME)
