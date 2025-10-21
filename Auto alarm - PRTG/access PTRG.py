import requests
import smtplib
from email.mime.text import MIMEText

# Configuration
PRTG_SERVER = 'https://hcm.hanelcom.vn'
USERNAME = 'vdc_hanelcom'
PASSWORD = 'Hanelcom@123'
SENSOR_ID = '12385'
THRESHOLD = 90

EMAIL_ADDRESS = 'danh.phan@nab.com.au'
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SMTP_USER = 'danhpc1992@gmail.com'
SMTP_PASSWORD = 'Danh@1592'

# Send Email
def send_email(sensor_value):
    subject = 'Sensor Alert: High Value Detected'
    body = f'The sensor value has exceeded the threshold. Current value: {sensor_value}'
    
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = SMTP_USER
    msg['To'] = EMAIL_ADDRESS

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_PASSWORD)
            server.sendmail(SMTP_USER, EMAIL_ADDRESS, msg.as_string())
        print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Check Sensor
def check_sensor():
    url = f'{PRTG_SERVER}/api/getjson.htm?content=sensors&id={SENSOR_ID}&username={USERNAME}&password={PASSWORD}'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        try:
            sensor_value = float(data['sensors'][0]['lastvalue'].replace('%', '').strip())
            print(f'Sensor value: {sensor_value}%')
            if sensor_value > THRESHOLD:
                send_email(sensor_value)
            else:
                print("Sensor value is within the safe range.")
        except Exception as e:
            print(f"Failed to parse sensor value: {e}")
    else:
        print(f'Error fetching sensor data: {response.status_code}')

# Run
check_sensor()
