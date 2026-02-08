import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    print("❌ Falta la API Key en .env")
else:
    client = genai.Client(api_key=API_KEY)
    print("🔍 Buscando modelos disponibles en tu cuenta...\n")
    
    try:
        # Listamos todos los modelos
        for model in client.models.list():
            # Filtramos para ver si hay alguno de imagen
            if "image" in model.name or "imagen" in model.name:
                print(f"🎨 MODELO DE IMAGEN ENCONTRADO: {model.name}")
                print(f"   - Display Name: {model.display_name}")
                print(f"   - Métodos: {model.supported_generation_methods}")
                print("-" * 30)
            
            # Solo por curiosidad, listamos también los Gemini nuevos
            elif "gemini-2" in model.name or "gemini-1.5" in model.name:
                print(f"🧠 {model.name}")

    except Exception as e:
        print(f"❌ Error al listar modelos: {e}")