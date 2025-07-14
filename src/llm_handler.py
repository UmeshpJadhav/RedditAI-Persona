import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=GOOGLE_API_KEY)

if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY not found in environment variables")

class LLMHandler:
    def __init__(self):
        """Initialize the LLM handler with the Gemini model."""
        self.model = genai.GenerativeModel('gemini-2.0-flash')

    def generate_text(self, prompt: str) -> str:
        """
        Generate text using the Gemini model.
        
        Args:
            prompt (str): The input prompt for the model.
            
        Returns:
            str: The generated text from the model.
        """
        try:
            response = self.model.generate_content(
                prompt,
                generation_config={
                    "temperature": 0.7,
                    "max_output_tokens": 1024
                }
            )
            # The response structure may vary; try to extract the text
            if hasattr(response, 'text'):
                return response.text
            elif hasattr(response, 'candidates') and response.candidates:
                # Gemini API may return candidates list
                candidate = response.candidates[0]
                if hasattr(candidate, 'content') and hasattr(candidate.content, 'parts'):
                    return candidate.content.parts[0].text
            return str(response)
        except Exception as e:
            print(f"Error generating text: {e}")
            return ""

    def generate_persona(self, user_data: str) -> str:
        """
        Generate a user persona from the provided data.
        
        Args:
            user_data (str): Formatted string containing user's posts and comments.
            
        Returns:
            str: JSON-formatted persona with citations.
        """
        try:
            prompt = f"""Based on the following Reddit user data, generate a detailed user persona.
            For each characteristic, include at least one citation from their posts or comments.
            Format the response as JSON with these fields:
            - name: The user's Reddit username
            - age: Estimated age range
            - location: Likely location based on posts
            - interests: List of interests with citations
            - personality: Personality traits with citations
            - values: Core values with citations
            - citations: List of post/comment IDs used for each characteristic

            User Data:
            {user_data}
            """
            return self.generate_text(prompt)
        except Exception as e:
            print(f"Error generating persona: {e}")
            return ""