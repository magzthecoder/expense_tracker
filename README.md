
# Expense Tracker

A Django-based expense tracking application with JavaScript-powered browser storage features. The application combines server-side expense management with client-side functionality for managing locally stored expenses.

## Features

- **Add Expenses:** Create expenses with a name, category, price and date.
- **View Expenses:** Display and manage recorded expenses.
- **Expense Details:** View individual expense information.
- **Edit Expenses:** Update existing expense records.
- **Delete Expenses:** Remove unwanted expenses.
- **Browser localStorage:** Store and manage expenses directly in the browser.
- **Local Expense Search:** Search locally stored expenses using JavaScript.
- **Environment Configuration:** Securely manage sensitive settings using environment variables.

> Note: Database-backed expenses and browser-local expenses are stored separately. Browser-local expenses are not automatically synchronised with the Django database.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Django | Web framework |
| JavaScript | Client-side functionality |
| HTML | Page structure |
| CSS | Styling |
| SQLite | Database |

## Project Structure

```text
expense_tracker/
│
├── expense_tracker/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── expenses/
│   ├── static/
│   │   └── js/
│   │       ├── add_expense.js
│   │       └── expense_list.js
│   ├── templates/
│   └── ...
│
├── .env.example
├── .gitignore
├── manage.py
└── requirements.txt
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/magzthecoder/expense_tracker.git
```

Navigate into the project directory:

```bash
cd expense_tracker
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it.

**Windows:**

```powershell
.\venv\Scripts\Activate.ps1
```

**macOS/Linux:**

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the same directory as `manage.py`.

Use `.env.example` as a template:

```env
SECRET_KEY=your-new-django-secret-key
DEBUG=True
```

Generate a new Django secret key:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Replace the placeholder with your generated key.

**Important:** Never commit your `.env` file or expose your Django secret key publicly.

### 5. Apply database migrations

```bash
python manage.py migrate
```

### 6. Start the development server

```bash
python manage.py runserver
```

Open your browser and navigate to:

http://127.0.0.1:8000/

## Environment Variables

| Variable | Description |
|---|---|
| SECRET_KEY | Django application's secret key |
| DEBUG | Enables or disables Django debug mode |

For production, set `DEBUG=False` and configure the appropriate allowed hosts and deployment security settings.

## Data Storage

The application uses two separate storage approaches:

**1. Django Database**
- Stores expenses managed through the Django backend.
- Uses the configured Django database.

**2. Browser localStorage**
- Stores locally created expenses in the user's browser.
- Supports client-side expense management and search.
- Data is browser-specific and is not automatically synchronised with the Django database.

Clearing browser site data can remove locally stored expenses.

## Future Improvements

Potential improvements include:

- Expense analytics and visual dashboards.
- Monthly and yearly expense summaries.
- Advanced filtering by category and date.
- Expense export functionality.
- Database synchronisation for locally stored expenses.
- Automated testing.

## Author

**Carlton Magura**

GitHub: https://github.com/magzthecoder

## License

No open-source license has currently been specified.
