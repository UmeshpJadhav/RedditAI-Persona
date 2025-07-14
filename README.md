# Reddit User Persona Generator

This script scrapes a Reddit user's profile for their posts and comments, then uses a Large Language Model (LLM) via LangChain to generate a user persona based on their activity. For each characteristic in the persona, the script provides citations from the user's content.

## Features

- Scrapes recent posts and comments from any public Reddit profile.
- Uses LangChain to interact with a Hugging Face LLM for persona analysis.
- Generates a detailed persona with citations for each point.
- Saves the output to a clean, readable text file.

## Setup Instructions

1.  **Clone the Repository**
    ```bash
    git clone <your-repo-link>
    cd RedditAI-Persona
    ```

2.  **Create a Virtual Environment**
    ```bash
    python -m venv venv
    ```
    - On Windows:
      ```bash
      .\venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Environment Variables**
    - Copy the `.env.example` file to a new file named `.env`.
    - Open the `.env` file and add your API credentials for Reddit and Hugging Face.

## How to Run

To generate a persona, run the `main.py` script from your terminal, providing the Reddit username as a command-line argument:

```bash
python main.py <reddit_username>
```

### Example

```bash
python main.py kojied
```

This will create a file named `kojied.txt` in the project directory containing the user persona.
