import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import settings

class Mailer:
    def __init__(self):
        self.server = None

    def connect(self):
        """SMTP sunucusuna bağlanır ve güvenli bağlantı kurar."""
        try:
            # 1. Sunucuya bağlan
            self.server = smtplib.SMTP(settings.SMTP_SERVER, settings.SMTP_PORT)
            # 2. EHLO (Selamlaşma) ve TLS (Şifreleme) başlat
            self.server.starttls() 
            # 3. Giriş yap
            self.server.login(settings.SENDER_EMAIL, settings.SENDER_PASSWORD)
            print("✅ Sunucuya başarıyla bağlanıldı!")
        except Exception as e:
            print(f"❌ Bağlantı hatası: {e}")

    def send_mail(self, recipient, subject, html_content):
        """E-posta oluşturur ve gönderir."""
        try:
            # Email mesajını oluşturma (Zarf hazırlama)
            message = MIMEMultipart()
            message["From"] = settings.SENDER_EMAIL
            message["To"] = recipient
            message["Subject"] = subject

            # İçeriği ekleme
            message.attach(MIMEText(html_content, "html"))

            # Gönderim
            self.server.sendmail(settings.SENDER_EMAIL, recipient, message.as_string())
            print(f"🚀 Mail başarıyla gönderildi: {recipient}")
        except Exception as e:
            print(f"❌ Gönderim hatası: {e}")

    def disconnect(self):
        """Bağlantıyı güvenli bir şekilde kapatır."""
        if self.server:
            self.server.quit()