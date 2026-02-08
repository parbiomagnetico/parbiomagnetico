import os
import time
import frontmatter
import google.generativeai as genai
from dotenv import load_dotenv
from tqdm import tqdm
import json
import re

# --- CONFIGURACIÓN ---
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")
DIRECTORIO_BLOG = "./src/content/blog" # ⚠️ REVISA TU RUTA

# --- CONFIGURACIÓN DE FILTRO ---
SOLO_BORRADORES = False 

if not API_KEY:
    raise ValueError("❌ ERROR: No se encontró GOOGLE_API_KEY en el archivo .env")

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-2.5-flash', generation_config={"response_mime_type": "application/json"})

# --- EL CEREBRO ---
SYSTEM_INSTRUCTION = """
ACTÚA COMO: Director de Arte experto en la web 'ParBiomagnetico.es'.

OBJETIVO: Leer el contenido del artículo proporcionado y generar ÚNICAMENTE el prompt de imagen más adecuado.

ESTÉTICA VISUAL (Inamovible):
"Dark mode, bio-energy aesthetic. Deep green background, glowing golden-green energy lines/particles, therapeutic vinyl magnets (one red, one black). Subtle, warm light. Professional, clinical yet mystical."

OPCIONES DE ESTILO (Elige UNA):
1. STYLE_A (General): Persona vestida en camilla con imanes.
2. STYLE_B (Bodegón): Primer plano artístico SOLO de los imanes.
3. STYLE_C (Específico): Primer plano de manos/zona del cuerpo (rodilla, cabeza, etc).

SALIDA JSON:
{
  "chosen_image_style": "STYLE_A" o "STYLE_B" o "STYLE_C",
  "final_image_prompt": "Prompt COMPLETO en inglés..."
}
"""

def limpiar_json(texto_sucio):
    texto_limpio = re.sub(r'```json\s*|\s*```', '', texto_sucio)
    return texto_limpio.strip()

def procesar_imagenes():
    if not os.path.exists(DIRECTORIO_BLOG):
         print(f"❌ Error: No existe el directorio: {DIRECTORIO_BLOG}")
         return

    archivos = [f for f in os.listdir(DIRECTORIO_BLOG) if f.endswith(".md")]
    print(f"🎨 Escaneando {len(archivos)} artículos (Modo Robusto)...")
    
    procesados = 0
    omitidos = 0

    for nombre_archivo in tqdm(archivos, desc="Analizando"):
        ruta_completa = os.path.join(DIRECTORIO_BLOG, nombre_archivo)
        
        try:
            post = frontmatter.load(ruta_completa)
            
            # --- FILTROS ---
            if SOLO_BORRADORES and post.get('active', False) is True:
                omitidos += 1
                continue

            if post.get('midjourney_prompt'):
                omitidos += 1
                continue

            # --- GENERAR ---
            prompt_usuario = f"TÍTULO: {post.get('title', '')}\nCONTENIDO (Extracto):\n{post.content[:800]}..."

            response = model.generate_content(f"{SYSTEM_INSTRUCTION}\n\n{prompt_usuario}")
            datos_ia = json.loads(limpiar_json(response.text))
            
            post['ai_image_style'] = datos_ia['chosen_image_style']
            post['midjourney_prompt'] = datos_ia['final_image_prompt']
            
            with open(ruta_completa, "w", encoding="utf-8") as f:
                f.write(frontmatter.dumps(post))
                
            procesados += 1
            
            # PAUSA DE ÉXITO (15s)
            time.sleep(15) 

        except Exception as e:
            print(f"⚠️ Error en {nombre_archivo}. Pausando 30s para enfriar API...")
            # 🔥 AQUÍ ESTÁ EL ARREGLO: Si falla, esperamos EL DOBLE (30s) antes de seguir
            time.sleep(30)

    print(f"\n✅ RESUMEN: {procesados} nuevos prompts generados. {omitidos} omitidos.")

if __name__ == "__main__":
    procesar_imagenes()