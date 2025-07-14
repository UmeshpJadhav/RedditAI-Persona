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

    def generate_persona(self, posts, comments, display_name) -> str:
        """
        Generate a user persona from Reddit data.
        
        Args:
            posts: List of Reddit posts
            comments: List of Reddit comments
            display_name: The Reddit user's display name
            
        Returns:
            str: Persona in a structured, human-readable format with citations
        """
        formatted_data = self.format_reddit_data(posts, comments)
        
        prompt = f"""
Based on the following Reddit user data, generate a detailed user persona in the following format:

Name: {display_name}
Age: [Estimated Age]
Occupation: [If possible]
Status: [Relationship status if possible]
Location: [Likely location]
Tier: [e.g., Early Adopters, if possible]
Archetype: [e.g., The Creator, if possible]

Personality Traits:
- [Trait 1] (cite post/comment)
- [Trait 2] (cite post/comment)

Motivations:
- [Motivation 1] (cite post/comment)
- [Motivation 2] (cite post/comment)

Preferences:
- [Preference 1] (cite post/comment)
- [Preference 2] (cite post/comment)

Behaviour & Habits:
- [Narrative paragraph or bullet points, with citations]

Goals & Needs:
- [Goal 1] (cite post/comment)
- [Goal 2] (cite post/comment)

Intuition:
- [Intuition 1] (cite post/comment)

Frustrations:
- [Frustration 1] (cite post/comment)

For each point, cite the post or comment (by ID or short quote) that supports it.

User Data:
{formatted_data}
"""
        
        return self.llm.generate_text(prompt)