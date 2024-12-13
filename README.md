# Protfolio 2024

A portfolio website built with **Flask**, designed to showcase your personal projects, resume, and contact information.

## Features

- **Homepage**: A welcoming interface that introduces visitors to your portfolio.
- **Projects Page**: Displays your projects with brief descriptions and links.
- **Resume Page**: Highlights your professional experience and skills.
- **Contact Page**: Allows users to reach out through a simple form.

## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS
- **Deployment**: Flask development server (configurable to production servers)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/ubaidalishah/Protfolio_2024.git
   cd Protfolio_2024
   ```

2. Set up a virtual environment (optional but recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:

   ```bash
   python app.py
   ```

5. Open your browser and visit `http://127.0.0.1:5000`.

## Folder Structure

```
Protfolio_2024/
│
├── templates/       # HTML templates for the site
│   ├── index.html
│   ├── contact.html
│   ├── projects.html
│   ├── resume.html
│
├── static/          # Static files (CSS, images, etc.)
├── app.py           # Main Flask application
├── requirements.txt # Dependencies for the project
```

## Future Improvements

- Add a dynamic admin dashboard to manage portfolio content.
- Integrate a database to store project details and contact form submissions.
- Optimize for deployment on platforms like Heroku or Vercel.

## License

This project is open-source and available under the MIT License. Feel free to use and modify it as needed.

## Author

Ubaid Ali Shah

