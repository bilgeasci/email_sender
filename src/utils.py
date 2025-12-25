import csv
import os

def load_recipients(file_name):
    """data/ klasörü altındaki CSV dosyasını okur."""
    # Dosya yolunu oluştur
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)
    file_path = os.path.join(project_root, "data", file_name)
    
    recipients = []
    try:
        with open(file_path, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f) # Sütun isimlerini (name, email) anahtar olarak kullanır
            for row in reader:
                recipients.append(row)
        return recipients
    except FileNotFoundError:
        print(f"❌ Hata: {file_path} bulunamadı!")
        return []