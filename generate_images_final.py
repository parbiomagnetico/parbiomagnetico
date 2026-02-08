import os
import time
import frontmatter
import logging
from dotenv import load_dotenv
from tqdm import tqdm
from PIL import Image
import io

# --- IMPORTAMOS LA LIBRERÍA NUEVA ---
from google import genai
from google.genai import types

# --- CONFIGURACIÓN ---
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

# ⚠️ RUTAS
DIRECTORIO_BLOG = "./src/content/blog"
DIRECTORIO_IMAGENES = "./public/images/blog"
LOG_FILE = "generation_log.txt"

# --- LOGS ---
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE, encoding='utf-8'),
        logging.StreamHandler()
    ]
)

if not API_KEY:
    raise ValueError("❌ Falta GOOGLE_API_KEY en .env")

# --- CONEXIÓN CLIENTE V2 ---
client = genai.Client(api_key=API_KEY)

# ✅ ESTE ES EL MODELO BUENO (Funcionará al activar el pago)
MODEL_ID = 'imagen-3.0-generate-001' 

os.makedirs(DIRECTORIO_IMAGENES, exist_ok=True)

def generar_imagen_gemini(prompt_texto, nombre_archivo):
    try:
        logging.info(f"🎨 Pintando con Imagen 3: {nombre_archivo}...")
        
        response = client.models.generate_images(
            model=MODEL_ID,
            prompt=prompt_texto,
            config=types.GenerateImagesConfig(
                number_of_images=1,
                aspect_ratio="16:9",
            )
        )
        
        if response.generated_images:
            image_bytes = response.generated_images[0].image.image_bytes
            return Image.open(io.BytesIO(image_bytes))
        
        return None

    except Exception as e:
        # Si falla, captura el error específico de facturación si lo hay
        logging.error(f"❌ Error API: {e}")
        return None

def procesar_blog_reemplazo():
    archivos = [f for f in os.listdir(DIRECTORIO_BLOG) if f.endswith(".md")]
    logging.info(f"🔥 INICIANDO REEMPLAZO MASIVO (IMAGEN 3) EN {len(archivos)} ARTÍCULOS")

    pbar = tqdm(archivos, desc="Sustituyendo Imágenes")

    for nombre_archivo in pbar:
        ruta_completa = os.path.join(DIRECTORIO_BLOG, nombre_archivo)
        
        try:
            post = frontmatter.load(ruta_completa)
            
            # FILTRO: ¿Ya está hecha?
            if post.get('image_generated') is True:
                continue

            prompt_ia = post.get('midjourney_prompt')
            if not prompt_ia:
                continue

            # GENERAR
            imagen_pil = generar_imagen_gemini(prompt_ia, nombre_archivo)
            
            if imagen_pil:
                nombre_jpg = nombre_archivo.replace(".md", ".jpg")
                nombre_final = f"ai_{nombre_jpg}"
                ruta_guardado = os.path.join(DIRECTORIO_IMAGENES, nombre_final)
                
                # 1. GUARDAR
                imagen_pil.save(ruta_guardado, format="JPEG", quality=85)
                
                # 2. ACTUALIZAR
                post['image'] = f"/images/blog/{nombre_final}"
                post['image_generated'] = True
                
                with open(ruta_completa, "w", encoding="utf-8") as f:
                    f.write(frontmatter.dumps(post))
                
                logging.info(f"✅ CAMBIO: {nombre_final}")
                time.sleep(2) 
            else:
                logging.error(f"❌ Fallo al generar imagen para {nombre_archivo}")

        except Exception as e:
            logging.error(f"💥 Error crítico en {nombre_archivo}: {e}")

if __name__ == "__main__":
    procesar_blog_reemplazo()