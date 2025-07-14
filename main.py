import sys
from src.reddit_scraper import get_reddit_instance, get_user_posts, get_user_comments
from src.persona_generator import PersonaGenerator

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

    print(f"\nStarting data scraping for user: u/{username}")

    reddit = get_reddit_instance()
    
    # Scrape posts and comments
    posts = get_user_posts(reddit, username)
    comments = get_user_comments(reddit, username)

    # Use the Reddit username for persona name
    persona_name = username

    if not posts and not comments:
        print(f"\nNo data found for user u/{username}. Exiting.")
        return

    print(f"\nScraping complete!")
    print(f"- Found {len(posts)} posts.")
    print(f"- Found {len(comments)} comments.")

    # Generate persona
    print("\nGenerating persona...")
    generator = PersonaGenerator()
    persona = generator.generate_persona(posts, comments, persona_name)
    
    print("\nGenerated Persona:")
    print(persona)

    # Save persona to a text file
    output_filename = f"{username}.txt"
    with open(output_filename, "w", encoding="utf-8") as f:
        f.write(persona)
    print(f"\nPersona saved to {output_filename}")

if __name__ == "__main__":
    main()