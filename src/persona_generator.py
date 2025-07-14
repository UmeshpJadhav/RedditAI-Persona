from src.llm_handler import LLMHandler

class PersonaGenerator:
    def __init__(self):
        """Initialize the persona generator with LLM handler."""
        self.llm = LLMHandler()

    def format_reddit_data(self, posts, comments) -> str:
        """
        Format Reddit posts and comments into a structured string.
        
        Args:
            posts: List of Reddit posts
            comments: List of Reddit comments
            
        Returns:
            str: Formatted string containing all posts and comments
        """
        formatted_data = """
        User Reddit Data:
        
        Posts:
        """
        
        for post in posts:
            formatted_data += f"- {post.title}\n  {post.selftext}\n  Score: {post.score}\n  Created: {post.created_utc}\n"
        
        formatted_data += "\nComments:\n"
        for comment in comments:
            formatted_data += f"- {comment.body}\n  Score: {comment.score}\n  Created: {comment.created_utc}\n"
        
        return formatted_data

    def generate_persona(self, posts, comments) -> str:
        """
        Generate a user persona from Reddit data.
        
        Args:
            posts: List of Reddit posts
            comments: List of Reddit comments
            
        Returns:
            str: JSON-formatted persona with citations
        """
        formatted_data = self.format_reddit_data(posts, comments)
        
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
        {formatted_data}
        """
        
        return self.llm.generate_text(prompt)