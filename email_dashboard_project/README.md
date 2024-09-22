# Email Dashboard Project

<img src='https://cdn.intheloop.io/blog/wp-content/uploads/2019/03/loop-email-shared-inbox-feature.jpg'>

This project is designed to send scheduled emails using a PostgreSQL database, Docker, and Python's `smtplib`. The user interface (UI) for managing email schedules is built with Streamlit. The main module responsible for sending emails is `run.py`.

## Features
- **Streamlit Dashboard**: A web-based UI for scheduling and managing emails.
- **PostgreSQL Database**: Stores email schedules and recipient information.
- **Dockerized Environment**: PostgreSQL is set up and managed using Docker.
- **Python Automation**: Python `smtplib` is used to handle email sending.
- **Scheduling**: Emails are sent based on the scheduled time stored in the database.
  
## Prerequisites

Make sure you have the following installed:

- [Docker](https://www.docker.com/get-started)
- [Python 3.x](https://www.python.org/downloads/)
- [Streamlit](https://streamlit.io/)
- PostgreSQL (via Docker)
- Required Python packages (listed in `requirements.txt`)

## Project Structure

```
EMAIL_DASHBOARD_PROJECT/
├── notebook/                  # Jupyter notebooks for testing and prototyping
│   ├── email-dashboard.ipynb   # Prototype of the dashboard in a notebook
│   └── test.ipynb              # Test notebook for email functionality
├── src/                        # Source files
│   ├── __pycache__/            # Python cache files
│   ├── db.py                   # Database handling logic
│   ├── email_dashboard.py      # Streamlit dashboard logic
│   ├── email_smtplib.py        # Logic for sending emails
│   └── run.py                  # Main script to schedule and send emails
├── .env                        # Environment variables for credentials
├── README.md                   # Project documentation (this file)
├── requirements.txt            # Python dependencies
└── docker-compose.yml          # Docker configuration for PostgreSQL
```

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/andishehtavakoli/email-dashboard-project.git
cd email-dashboard-project
```

### 2. Set Up the PostgreSQL Database Using Docker

```bash
docker-compose up -d
```

### 3. Initialize the Database

Run the SQL script inside the `db/` folder to create necessary tables. You can access the PostgreSQL container and run the script:

```bash
docker exec -it <container_name> psql -U <username> -d <database>
\i /db/init.sql
```

### 4. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Your Email Settings

Update the `.env` file with your email service credentials (e.g., Gmail, Outlook). It should contain:

```
sender_email =your-email@gmail.com
sender_password=your-email-password
```

### 6. Run the Streamlit Dashboard

To launch the Streamlit dashboard for managing email schedules:

```bash
streamlit run src/email_dashboard.py
```

### 7. Run the Main Email Sending Module

To start checking the schedules and sending emails:

```bash
python src/run.py
```

## Usage

- **Schedule Emails**: Use the Streamlit dashboard to schedule emails by specifying recipient, subject, message body, and scheduled time.
- **Send Emails**: The `run.py` script checks for scheduled emails and sends them using `smtplib`.

## Docker Commands

- **Start PostgreSQL container**:
    ```bash
    docker-compose up -d
    ```

- **Stop PostgreSQL container**:
    ```bash
    docker-compose down
    ```


