# Daily Expense Tracker

## Overview
The **Daily Expense Tracker** is a simple web application built using **Flask (Python)** for the backend and **Tailwind CSS** for a responsive, modern frontend. It allows users to add and view their daily expenses with details like date, amount, and description.

## Technologies Used
- **Flask (Python)**: Backend framework
- **Tailwind CSS**: Frontend styling
- **HTML**: Page structure
- **Jinja2**: Template rendering

## Features
- **Add Expenses**: Users can input the date, amount, and description of an expense.
- **Expense List**: Displays a list of all entered expenses.
- **Responsive UI**: Built with Tailwind CSS, adjusts to different screen sizes.

## How to Run
1. Clone the repo: `git clone <repo-url>`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the app: `python app.py`
4. Access the app at `http://127.0.0.1:5000/`

## app.py Breakdown
- Flask handles routes (`/` for displaying expenses and `/add` for adding expenses).
- Expenses are stored in memory (can be enhanced with a database).
- Uses Jinja2 to render HTML templates dynamically.

## Future Enhancements
- Add database support for persistent storage.
- Implement user authentication.
- Integrate charts and analytics for expense visualization.
