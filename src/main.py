from src.mailer import Mailer
from src.template_engine import render_template
from src.utils import load_recipients

def main():
    mail_client = Mailer()
    mail_client.connect()
    
    # 1. Alıcı listesini CSV'den yükle (data/recipients.csv)
    recipients = load_recipients("recipients.csv")
    
    if not recipients:
        print("⚠️ Gönderilecek kimse bulunamadı.")
        return

    # 2. Her alıcı için işlemleri yap
    for person in recipients:
        print(f"🔄 {person['name']} için mailler hazırlanıyor...")
        
        # --- SENARYO 1: Hoş Geldin Maili ---
        welcome_body = render_template("welcome_email.html", {"name": person['name']})
        mail_client.send_mail(
            recipient=person['email'], 
            subject=f"Hoş geldin {person['name']}!", 
            html_content=welcome_body
        )
        
        # --- SENARYO 2: Bülten (Newsletter) Maili ---
        newsletter_data = {
            "name": person['name'],
            "title": "Aralık Ayı Teknoloji Bülteni",
            "content": "Bu ayki bültenimizde Python ile otomasyon konusunu işledik. Kodlarımız artık çok daha temiz ve modüler!"
        }
        newsletter_body = render_template("newsletter.html", newsletter_data)
        mail_client.send_mail(
            recipient=person['email'], 
            subject="Haftalık Bülteniniz Geldi", 
            html_content=newsletter_body
        )
    
    # 3. Bağlantıyı kapat
    mail_client.disconnect()

if __name__ == "__main__":
    main()