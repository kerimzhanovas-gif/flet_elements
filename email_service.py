import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailService:
    def __init__(self, smtp_server="smtp.gmail.com", port=587):
        self.smtp_server = smtp_server
        self.port = port
        self.sender_email = "your_email@gmail.com"
        self.sender_password = "your_app_password"
        self.receiver_email = "your_email@gmail.com"
    
    def send_notification(self, profile_data):
        try:
            message = MIMEMultipart()
            message["Subject"] = "Новая анкета создана!"
            message["From"] = self.sender_email
            message["To"] = self.receiver_email

            text = f"""
            Создана новая анкета!
            
            Имя: {profile_data.get('name', 'Не указано')}
            Город: {profile_data.get('city', 'Не указано')}
            Возраст: {profile_data.get('age', 'Не указано')}
            Навыки: {profile_data.get('skills', 'Не указано')}
            Уровень: {profile_data.get('level', 'Не указано')}
            Готов к работе: {profile_data.get('ready', 'Не указано')}
            """

            message.attach(MIMEText(text, "plain"))

            with smtplib.SMTP(self.smtp_server, self.port) as server:
                server.starttls()
                server.login(self.sender_email, self.sender_password)
                server.sendmail(self.sender_email, self.receiver_email, message.as_string())
            
            return True, "Уведомление отправлено на почту"
        except Exception as e:
            return False, f"Ошибка отправки: {str(e)}"