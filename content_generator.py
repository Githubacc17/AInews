import openai
import pyjokes
import random
import os
from dotenv import load_dotenv

load_dotenv()

class ContentGenerator:
    def __init__(self):
        self.openai_client = openai.OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        
    def generate_tech_image(self):
        """Generate an AI image related to technology"""
        try:
            prompts = [
                "futuristic technology concept art, bright colors, digital art style",
                "artificial intelligence visualization, modern, minimalist",
                "innovative tech gadgets of the future, creative digital art",
                "cybersecurity concept art, digital landscape",
                "robotics and automation, futuristic scene"
            ]
            
            response = self.openai_client.images.generate(
                model="dall-e-3",
                prompt=random.choice(prompts),
                size="1024x1024",
                quality="standard",
                n=1,
            )
            
            return response.data[0].url
        except Exception as e:
            print(f"Error generating image: {str(e)}")
            return None

    def generate_tech_quiz(self, count=3):
        """Generate technology-related quiz questions"""
        quiz_questions = [
            {
                "question": "What does AI stand for?",
                "options": ["Artificial Intelligence", "Automated Integration", "Advanced Interface", "Algorithmic Implementation"],
                "correct": "Artificial Intelligence"
            },
            {
                "question": "Which company created ChatGPT?",
                "options": ["Google", "OpenAI", "Microsoft", "Meta"],
                "correct": "OpenAI"
            },
            {
                "question": "What is the term for a malicious software that demands payment?",
                "options": ["Spyware", "Ransomware", "Adware", "Malware"],
                "correct": "Ransomware"
            },
            {
                "question": "What does CPU stand for?",
                "options": ["Central Processing Unit", "Computer Personal Unit", "Central Program Utility", "Computer Processing Unit"],
                "correct": "Central Processing Unit"
            },
            {
                "question": "Which programming language is known as the 'language of the web'?",
                "options": ["Python", "Java", "JavaScript", "C++"],
                "correct": "JavaScript"
            }
        ]
        return random.sample(quiz_questions, min(count, len(quiz_questions)))

    def get_tech_joke(self):
        """Get a technology-related joke"""
        tech_jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs!",
            "Why did the programmer quit his job? Because he didn't get arrays!",
            "What's a programmer's favorite place? The Cloud!",
            "Why do programmers always mix up Halloween and Christmas? Because Oct 31 equals Dec 25!",
            "What did the computer do at lunchtime? Had a byte!",
            "Why don't programmers like nature? It has too many bugs!",
            "What's a programmer's favorite hangout spot? Foo Bar!"
        ]
        return random.choice(tech_jokes) 