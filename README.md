# Ons Platform - Student Mental Health Support

A prototype web application built with Flask, HTML (Jinja templates), and Tailwind CSS for student mental health support.

## Features

- **Home Page**: Hero section with feature cards and call-to-action
- **Articles**: Demo articles on stress management, time management, and anxiety
- **Stress Assessment**: Interactive form with 3 questions and result calculation
- **AI Chatbot**: Chat interface with hardcoded responses for emotional support
- **Login**: Placeholder authentication form (no backend logic)

## Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML with Jinja2 templates
- **Styling**: Tailwind CSS (via CDN)
- **Icons**: Font Awesome (via CDN)

## Installation & Setup

1. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application:**
   ```bash
   python app.py
   ```

3. **Access the application:**
   Open your browser and go to `http://localhost:5000`

## Project Structure

```
ons-platform/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── templates/            # Jinja2 HTML templates
│   ├── base.html         # Base template with navbar/footer
│   ├── home.html         # Home page
│   ├── articles.html     # Articles page
│   ├── tests.html        # Stress assessment page
│   ├── chatbot.html      # AI chatbot page
│   └── login.html        # Login page
└── static/               # Static files (CSS, images, etc.)
```

## Pages Overview

### Home Page (`/`)
- Hero section with welcome message
- Three feature cards (Articles, Tests, Chatbot)
- Statistics section
- Responsive design

### Articles Page (`/articles`)
- Grid of 3 demo article cards
- Topics: Stress Management, Time Management, Anxiety
- Placeholder for additional resources

### Tests Page (`/tests`)
- Interactive stress assessment form
- 3 multiple-choice questions
- Result calculation (Low/Medium/High stress levels)
- Form submission with flash messages

### Chatbot Page (`/chatbot`)
- Chat interface similar to messaging apps
- Hardcoded bot responses for common inputs
- Quick response buttons
- Support resources section

### Login Page (`/login`)
- Placeholder authentication form
- Email and password fields
- Social login buttons (non-functional)
- Demo account information

## Design Features

- **Color Scheme**: Calm blues and greens for mental health theme
- **Responsive**: Mobile-first design with Tailwind CSS
- **Modern UI**: Rounded corners, soft shadows, smooth transitions
- **Accessibility**: Proper form labels and semantic HTML
- **Icons**: Font Awesome icons throughout the interface

## Notes

- This is a prototype with no authentication or database functionality
- The chatbot uses simple if/else logic for responses
- The stress test provides basic scoring and feedback
- All styling is done via Tailwind CSS CDN
- No backend data persistence (all data is session-based)

## Future Enhancements

- User authentication and sessions
- Database integration
- Real AI chatbot implementation
- More comprehensive mental health assessments
- User progress tracking
- Professional counselor matching
- Mobile app development
