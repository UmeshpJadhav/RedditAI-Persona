import os
import sys
import praw
from dotenv import load_dotenv

load_dotenv()

REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
REDDIT_USER_AGENT = os.getenv("REDDIT_USER_AGENT")

def get_reddit_instance():
    """Initializes and returns a PRAW Reddit instance."""
    if not all([REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT]):
        print("Error: Reddit API credentials not found in .env file.")
        print("Please create a .env file with your credentials.")
        sys.exit(1)

    try:
        reddit = praw.Reddit(
            client_id=REDDIT_CLIENT_ID,
            client_secret=REDDIT_CLIENT_SECRET,
            user_agent=REDDIT_USER_AGENT,
        )
        # Set to read-only mode, as we are only scraping data
        reddit.read_only = True
        return reddit
    except Exception as e:
        print(f"Error connecting to Reddit: {e}")
        sys.exit(1)

def get_user_posts(reddit, username, limit=None):
    """Fetches a user's posts. Set limit=None to get all available."""
    try:
        user = reddit.redditor(username)
        # Fetch the submissions (posts)
        return list(user.submissions.new(limit=limit))
    except Exception as e:
        print(f"Error scraping posts for u/{username}: {e}")
        print("Please ensure the username is correct and the user exists.")
        return []

def get_user_comments(reddit, username, limit=None):
    """Fetches a user's comments. Set limit=None to get all available."""
    try:
        user = reddit.redditor(username)
        # Fetch the comments
        return list(user.comments.new(limit=limit))
    except Exception as e:
        print(f"Error scraping comments for u/{username}: {e}")
        print("Please ensure the username is correct and the user exists.")
        return []

def get_user_name(reddit, username):
    """Fetches the Reddit user's display name (username)."""
    try:
        user = reddit.redditor(username)
        return user.name
    except Exception as e:
        print(f"Error fetching name for u/{username}: {e}")
        return username