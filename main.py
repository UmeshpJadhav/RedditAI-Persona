import sys
from src.reddit_scraper import get_reddit_instance, get_user_posts, get_user_comments

def main():
    """Main function to run the Reddit persona generator."""
    # Prompt the user for a username or URL
    username_input = input("Please enter the Reddit username or profile URL: ")

    # Automatically parse the username from a URL
    if "/user/" in username_input:
        try:
            username = username_input.split('/user/')[1].split('/')[0]
        except IndexError:
            print("Invalid URL format. Could not extract username.")
            sys.exit(1)
    else:
        username = username_input

    if not username:
        print("No username provided. Exiting.")
        sys.exit(1)

    print(f"Starting data scraping for user: u/{username}")

    reddit = get_reddit_instance()
    
    # Scrape posts and comments
    posts = get_user_posts(reddit, username)
    comments = get_user_comments(reddit, username)

    if not posts and not comments:
        print(f"\nNo data found for user u/{username}. Exiting.")
        return

    print(f"\nScraping complete!")
    print(f"- Found {len(posts)} posts.")
    print(f"- Found {len(comments)} comments.")

    print("\n--- Posts ---")
    for post in posts:
        print(f"\n>>> POST TITLE: {post.title}")
        print(f">>> POST BODY: {post.selftext}")

    print("\n--- Comments ---")
    for comment in comments:
        # Replace newlines with spaces for cleaner, single-line output
        comment_body = comment.body.replace('\n', ' ')
        print(f"- {comment_body}")

if __name__ == "__main__":
    main()