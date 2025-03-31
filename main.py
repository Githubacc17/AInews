from multi_source_fetcher import MultiSourceFetcher
from ppt_generator import PPTGenerator
from email_sender import EmailSender
from content_generator import ContentGenerator
import os
from dotenv import load_dotenv

def generate_and_send_newsletter():
    """Generate and send the tech newsletter to all configured recipients"""
    try:
        print("Starting newsletter generation...")
        
        # Initialize components
        fetcher = MultiSourceFetcher()
        ppt_gen = PPTGenerator()
        email_sender = EmailSender()
        
        # Fetch news articles
        print("Fetching news articles...")
        articles = fetcher.fetch_all_news()
        
        if not articles:
            print("No articles found. Skipping newsletter generation.")
            return
        
        # Generate PowerPoint presentation
        pptx_file = ppt_gen.generate_presentation(articles)
        print(f"PowerPoint presentation generated: {pptx_file}")
        
        # Send newsletter to all configured recipients
        email_sender.send_newsletter(pptx_file)
        print("Newsletter sent successfully!")
        
        # Clean up the generated file
        try:
            os.remove(pptx_file)
            print(f"Cleaned up temporary file: {pptx_file}")
        except Exception as e:
            print(f"Error cleaning up file {pptx_file}: {str(e)}")
            
    except Exception as e:
        print(f"Error generating/sending newsletter: {str(e)}")

if __name__ == "__main__":
    print("Generating and sending tech newsletter...")
    generate_and_send_newsletter() 