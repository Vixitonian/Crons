
import schedule
import time

def my_task():
    print("Cron job is running!")

# Schedule the task to run every day at 3:30 PM
schedule.every().day.at("15:30").do(my_task)

while True:
    schedule.run_pending()
    time.sleep(1)  # Sleep for 1 second to avoid high CPU usage

