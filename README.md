# GitHub Repository Scraper

A Django-based web application that allows users to scrape and analyze GitHub repositories and user profiles. This tool provides insights into repository and user data through a user-friendly web interface.

## Features

- GitHub Data Scraping
	- Extract repository information and user profiles
	- Analyze user data including followers, following, and public repos
	- Display results in a structured format

- Web Interface
	- Clean and responsive design using Tailwind CSS
	- User-friendly forms
	- Detailed result visualization
	- Custom theme integration

## Project Structure

```
github-scraper-django/
├── core/                   # Project configuration
│   ├── settings.py        # Django settings
│   ├── urls.py            # Main URL configuration
│   └── wsgi.py            # WSGI configuration
│
├── scraper/               # Main application
│   ├── admin.py          # Admin interface configuration
│   ├── forms.py          # Form definitions
│   ├── models.py         # Database models
│   ├── scrape.py         # Scraping functionality
│   ├── urls.py           # App URL configuration
│   ├── views.py          # View controllers
│   └── templates/        # HTML templates
│       └── scraper/
│           ├── index.html
│           └── result.html
│
├── theme/                 # Custom theme
│   └── templates/
│       └── base.html
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/github-scraper-django.git
cd github-scraper-django
```

2. Create a virtual environment:
```bash
python -m venv venv
```

3. Activate the virtual environment:
	 - Windows:
	 ```bash
	 venv\Scripts\activate
	 ```
	 - Unix or MacOS:
	 ```bash
	 source venv/bin/activate
	 ```

4. Install required packages:
```bash
pip install -r requirements.txt
```

5. Apply database migrations:
```bash
python manage.py migrate
```

## Usage

1. Start the development server:
```bash
python manage.py runserver
```

2. Open your web browser and navigate to `http://localhost:8000`

3. Enter a GitHub username in the main form

4. View the scraped data and analysis in the results page

## Development

- Built with Django web framework
- Uses Python's requests library for data scraping
- Tailwind CSS for responsive design
- SQLite database for data storage

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License.
