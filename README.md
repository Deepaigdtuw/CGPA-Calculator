# CGPA Calculator

A simple Flask-based web application for calculating cumulative GPA from semester SGPA values.

## Features

- Accepts SGPA values for up to eight semesters.
- Calculates the average CGPA.
- Displays the result on the same page.
- Uses a separate CSS file for styling.

## Project Files

- `CGPA.PY` — Flask application and CGPA calculation logic.
- `app.py` — Deployment-ready Flask application module.
- `body.html` — Web page layout and input form.
- `body.css` — Page styling.
- `requirements.txt` — Python dependencies.
- `render.yaml` — Render deployment configuration.

## Requirements

- Python 3.12 or later
- Flask

Install Flask if it is not already installed:

```text
pip install flask
```

## Running the Application

1. Open a terminal in the project folder.
2. Install the dependencies:

```text
pip install -r requirements.txt
```

3. Start the Flask application:

```text
python CGPA.PY
```

4. Open the application in a browser at:

**http://127.0.0.1:5000/**

The stylesheet is served by the application at:

**http://127.0.0.1:5000/body.css**

## Deploy Globally with Render

1. Push this project to a GitHub repository.
2. Sign in to [Render](https://render.com/).
3. Choose **New > Web Service** and connect the GitHub repository.
4. Use these settings:
	- **Runtime:** Python 3
	- **Build Command:** `pip install -r requirements.txt`
	- **Start Command:** `gunicorn app:app`
5. Click **Deploy Web Service**.

Render will provide a public HTTPS URL, for example:

**https://cgpa-calculator.onrender.com/**

Use that Render URL when sharing the application. Do not share `127.0.0.1`, because it only works on the computer running Flask.

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
