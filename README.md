Python Email Sender
Bu araç, SMTP protokolü üzerinden CSV tabanlı toplu HTML e-posta gönderimi yapar.

🛠️ Teknik Özellikler
SMTP & TLS: Güvenli mail iletimi.

HTML Templating: Dinamik veri destekli şablon motoru.

CSV Handling: Alıcı listesini dosyadan yönetme.

Security: .env ile çevre değişkenleri yönetimi.

📂 Dosya Yapısı
Plaintext

├── src/            # Mailer ve Template Engine
├── templates/      # welcome_email.html, newsletter.html
├── data/           # recipients.csv
├── config/         # settings.py (.env okuyucu)
└── tests/          # Unit testler
🚀 Hızlı Başlangıç
pip install python-dotenv

.env dosyasını oluştur (SENDER_EMAIL, SENDER_PASSWORD).

python3 -m src.main

⚖️ Lisans
MIT License - © 2025 Bilge Aşcı
