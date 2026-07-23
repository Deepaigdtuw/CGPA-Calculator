# CGPA Calculator

A simple Flask-based web application for calculating cumulative GPA from semester SGPA values.

## Features

- Accepts SGPA values for up to six semesters.
- Calculates the average CGPA.
- Displays the result on the same page.
- Uses a separate CSS file for styling.

## Project Files

- `CGPA.PY` — Flask application and CGPA calculation logic.
- `body.html` — Web page layout and input form.
- `body.css` — Page styling.

## Requirements

- Python 3.12 or later
- Flask

Install Flask if it is not already installed:

```text
pip install flask
```

## Running the Application

1. Open a terminal in the project folder.
2. Start the Flask application:

```text
python CGPA.PY
```

3. Open the application in a browser at:

**http://127.0.0.1:5000/**

The stylesheet is served by the application at:

**http://127.0.0.1:5000/body.css**

## How It Works

1. Enter one or more semester SGPA values.
2. Click **Calculate**.
3. The application calculates the average of the entered values and displays the CGPA.

For example, if the entered values are 8.0 and 7.5:

```text
CGPA = (8.0 + 7.5) / 2 = 7.75
```

## Flask Routes

| URL | Method | Purpose |
|---|---|---|
| `/` | GET, POST | Displays the calculator and processes SGPA values. |
| `/body.css` | GET | Serves the stylesheet. |
