# Reddit User Persona Generator

This project scrapes a Reddit user's posts and comments, then uses Google Gemini (LLM) to generate a detailed user persona. Each persona characteristic is supported by citations from the user's Reddit activity.

---

## Features

- **Scrapes all available posts and comments** from any public Reddit profile using the Reddit API (PRAW).
- **Uses Google Gemini** (via `google-generativeai`) to analyze the user's Reddit activity and generate a structured persona.
- **Citations:** Each persona trait, motivation, or preference is supported by a citation from the user's posts or comments.
- **Output:** Saves the generated persona to a text file named after the Reddit username (e.g., `kojied.txt`).

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <your-repo-link>
cd RedditAI-Persona
```

### 2. Install Dependencies
Make sure you have Python 3.8+ installed. Then run:
```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables
Create a `.env` file in the project root with the following content:
```ini
REDDIT_CLIENT_ID=your_reddit_client_id
REDDIT_CLIENT_SECRET=your_reddit_client_secret
REDDIT_USER_AGENT=your_user_agent
GOOGLE_API_KEY=your_gemini_api_key
```
- Get Reddit API credentials from: https://www.reddit.com/prefs/apps
- Get a Google Gemini API key from: https://aistudio.google.com/app/apikey

---

## How to Run

Run the script and enter a Reddit profile URL when prompted:
```bash
python main.py
```
Example input:
```
Please enter the Reddit username or profile URL: https://www.reddit.com/user/kojied/
```

This will create a file named `kojied.txt` in the project directory containing the user persona in a structured, readable format.

---

## Notes

- The script fetches as many posts and comments as Reddit's API allows (up to 1000 each).
- The persona output includes citations for each characteristic, referencing the relevant post or comment.
- Make sure your API keys are valid and have sufficient quota.
- The code follows PEP-8 guidelines.

---

## Sample Output

See the `.txt` files in the repository for sample personas generated for the users provided in the assignment.
