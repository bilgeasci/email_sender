import os

def render_template(template_name, context):
    # Projenin ana dizinini (root) bulalım
    # Bu dosyanın bulunduğu yerin (src) bir üst klasörü ana dizindir.
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)
    
    # Şablonun tam yolunu oluştur: /Users/.../email_sender/templates/welcome.html
    template_path = os.path.join(project_root, "templates", template_name)
    
    try:
        with open(template_path, "r", encoding="utf-8") as f:
            html_content = f.read()
        
        # Şablondaki {{ key }} alanlarını değiştir
        for key, value in context.items():
            placeholder = "{{" + f" {key} " + "}}"
            html_content = html_content.replace(placeholder, str(value))
            
        return html_content
    except FileNotFoundError:
        print(f"❌ Hata: {template_path} dosyası bulunamadı!")
        raise