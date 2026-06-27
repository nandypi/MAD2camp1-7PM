from celery import Celery
from celery.schedules import crontab

app = Celery('tasks', broker='redis://localhost:6379/0')

app.conf.update(
    timezone='Asia/Kolkata',
    enable_utc=False,
)

from app import app as flask_app
from models import Item, User
from mail import send_email
import time, os

@app.task()
def csv_export():
    with flask_app.app_context():
        time.sleep(5)  # Simulating a time-consuming task
        items = Item.query.all()
    csv_data = "id,name,description,image_url\n"
    for item in items:
        csv_data += f"{item.id},{item.name},{item.description},{item.image_url}\n"
    os.makedirs('static', exist_ok=True)
    with open('static/exported_items.csv', 'w') as f:
        time.sleep(5)  # Simulating a time-consuming task
        f.write(csv_data)
    html = """
    <html>
        <body>
            <h1>CSV Export Completed!</h1>
            <p>The CSV export has been completed successfully. <a href="http://127.0.0.1:5000/static/exported_items.csv">Download the CSV file</a>.</p>
        </body>
    </html>
    """
    send_email("admin@gmail.com", "CSV Export Completed", html)
    return "Background task executed successfully!"

@app.task()
def send_daily_reminders():
    with flask_app.app_context():
        users = User.query.all()
    html = """
    <html>
        <body>
            <h1>Daily Reminder</h1>
            <p>This is your daily reminder to check the application.</p>
        </body>
    </html>
    """
    for user in users:
        send_email(user.email, "Daily Reminder", html)
    return "Emails sent successfully!"

@app.task()
def send_monthly_reports():
    with flask_app.app_context():
        users = User.query.all()
    html = f"""
    <html>
        <body>
            <h1>Hey {{ user.name }}! Monthly Report</h1>
            <p>This is your monthly report for the application.</p>
            <h3>This is what you have achieved this month:</h3>
            <table>
            </table>
        </body>
    </html>
    """
    for user in users:
        send_email(user.email, "Monthly Report", html)
    return "Emails sent successfully!"

from gchat_webhook import main as send_message

@app.task()
def send_webhook_message():
    send_message()
    return "Webhook message sent successfully!"

app.conf.beat_schedule = {
    'send-daily-reminders': {
        'task': 'celery_app.send_daily_reminders',
        'schedule': crontab(hour=20, minute=10),  # Every day at 9 AM
    },
    'send-monthly-reports': {
        'task': 'celery_app.send_monthly_reports',
        'schedule': crontab(day_of_month=27, hour=20, minute=10),  # On the first day of every month at 10 AM
    },
    'send-webhook-message': {
        'task': 'celery_app.send_webhook_message',
        'schedule': crontab(hour=20, minute=14),  # Every day at 9 AM
    },
}