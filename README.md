# Anki Gemini Sentence Tutor

A Python CLI tool that pulls a random word you've previously reviewed from your local Anki collection and uses Google's Gemini API to evaluate a custom Japanese sentence you write for grammar, natural phrasing, and context.

## Example Output
```
Target Word: 話[はなし]
Write a sentence: 彼の話は面白いね。
Word Meaning: talk, story (This appears after sending sentence)

-- Fetching Gemini Feedback ---
Here is the feedback on your sentence practice:

1. **Grammar Check:** **100% Correct!** 
2. **Naturalness:** **Very Natural!** The word 話[はなし] is used perfectly here.

### **Translation & Meaning:**
* "His stories are interesting, aren't they?" / "What he says is funny, isn't it?"

---

### **Notes & Variations:**
* **Casual Tone:** Your sentence is in casual/informal Japanese, which is great for talking with friends.
* **Polite Version:** If you want to say this to a teacher or acquaintance, add **です**:
  > 彼の話は面白**いですね**。  
  > *(Kare no hanashi wa omoshiroi desu ne.)*

* **Nuance Tip:** Keep in mind that 面白い (*omoshiroi*) can mean both "interesting" (fascinating) and "funny" (humorous) depending on the context.

Great job! Keep up the good work.
```

## Prerequisites

- Python 3
- Anki Desktop
- A free Gemini API key from [Google AI Studio](https://aistudio.google.com/)

## Installation
1.  Clone the repository:
    ```
    git clone https://github.com/clearcasting/anki-sentence.git
    cd anki-sentence
    ```

2.  Create and activate a virtual environment:
    ```
    python -m venv venv
    source venv/bin/activate
    # On Windows: venv\Scripts\activate
    ```

3. Install dependencies:
    ```
    pip install -r requirements.txt
    ```
## Configuration
1. Set up Environment Variables:
    ```
    cp .env.example .env
    ```

2. Add your Gemini API Key:
    ```
    # Open .env and paste your actual API key
    GEMINI_API_KEY=your_actual_api_key_here
    ```

3. Verify Anki Path and Deck Settings:
    ```
    # Replace the collection path in .env to match your collection path
    # This changes depending on your OS
    COLLECTION_PATH="/home/user/.local/share/Anki2/User 1/collection.anki2"
    ```

## Usage
1. Run the script:
    ```
    python main.py
    ```