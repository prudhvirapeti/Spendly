# Spendly 💸

A personal expense tracking web application built with Flask and Python — developed using Claude Code.

## Features

- User registration and authentication
- Add, edit, and delete expenses
- Expense categorization
- Personal profile management
- Clean, responsive UI

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python · Flask |
| Database | SQLite |
| Frontend | HTML · CSS · JavaScript |
| Testing | pytest · pytest-flask |
| Built with | Claude Code |

## Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/prudhvirapeti/Spendly.git
cd Spendly
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
python app.py
```

Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

## Project Structure

```
Spendly/
├── app.py              # Flask routes and app setup
├── database/
│   ├── db.py           # Database connection and queries
│   └── __init__.py
├── templates/          # HTML templates
│   ├── base.html
│   ├── landing.html
│   ├── login.html
│   ├── register.html
│   └── ...
├── static/             # CSS and JavaScript
│   ├── css/
│   └── js/
├── requirements.txt
└── .gitignore
```

## Roadmap

- [x] Project setup and routing
- [x] User registration and login pages
- [x] Base HTML templates
- [ ] Database integration
- [ ] User authentication (session management)
- [ ] Add / edit / delete expenses
- [ ] Expense dashboard with summary
- [ ] Category filtering
- [ ] Export to CSV
