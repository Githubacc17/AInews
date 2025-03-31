# AI Tech Newsletter Automation

This project automatically generates and sends daily tech news updates in PowerPoint format via email.

## Features
- Fetches latest tech news using NewsAPI
- Generates beautiful PowerPoint presentations
- Automated email delivery
- Daily scheduling

## Setup
1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate virtual environment:
- Windows: `.\venv\Scripts\activate`
- Linux/Mac: `source venv/bin/activate`

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment variables:
- Copy `.env.example` to `.env`
- Add your NewsAPI key (get from https://newsapi.org)
- Add your Gmail credentials
  - Use App-Specific Password for security
  - Enable 2FA and generate App Password from Google Account settings

5. Run the script:
```bash
python main.py
```

## Configuration
- Edit `.env` file to customize:
  - Email settings
  - API keys
  - Recipient email

## Note
Make sure to:
1. Get NewsAPI key from https://newsapi.org
2. Enable 2FA on your Gmail account
3. Generate App-Specific Password for email sending 