import os
import time
import frontmatter
import google.generativeai as genai
from dotenv import load_dotenv
from tqdm import tqdm

# --- CONFIGURACIÓN ---
# 1. Carga la API Key del archivo .env
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

# 2. Ruta donde están tus archivos .md (AJUSTA ESTO SI ES NECESARIO)
# Ejemplo: "./src/pages/blog" o "./src/content/blog" o "./_drafts"
DIRECTORIO_BLOG = "./src/content/blog" 

# 3. Configuración de Gemini
if not API_KEY:
    raise ValueError("❌ ERROR: No se encontró GOOGLE_API_KEY en el archivo .env")

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-2.5-flash') # Usamos el modelo PRO para mejor calidad

# --- EL CEREBRO (PROMPT) ---
SYSTEM_INSTRUCTION = """
ACTÚA COMO: Cristina Murciano, Terapeuta Experta en Par Biomagnético (Método del Dr. Isaac Goiz) y Salud Bioenergética con consulta en Monzón (Huesca).

OBJETIVO: Reescribir el artículo proporcionado para convertirlo en una "Guía Pilar" de SEO local y autoridad técnica.

REGLAS DE CONTENIDO:
1. TONO: Profesional pero cercano. Usa terminología correcta (pH, patógenos, resonancia, equilibrio ácido-básico) pero explicada para pacientes.
2. ENFOQUE: No prometas "curas milagrosas" (Google YMYL), habla de "restablecer el equilibrio", "apoyar al organismo", "eliminar patógenos".
3. ESTRUCTURA:
   - H1: Título con Gancho + Keyword Local (Monzón).
   - Introducción: Empatía con el síntoma.
   - La visión del Biomagnetismo: Explicación técnica del pH y el par específico.
   - Beneficios de la sesión.
   - CTA: Llamada a la acción clara para pedir cita.

REGLAS DE FORMATO (STRICT MARKDOWN):
Devuelve SOLO el contenido del archivo Markdown completo, incluyendo el FRONTMATTER (YAML) al principio.

ESTRUCTURA DEL FRONTMATTER REQUERIDA:
---
title: "Título Optimizado Aquí"
date: "2026-02-02" (Usa fecha actual o mantén la original si es reciente)
active: false (MANTENER SIEMPRE EN FALSE)
excerpt: "Meta descripción persuasiva de 150 caracteres para Google."
image: "/images/blog/nombre-descriptivo-del-tema.jpg" (Sugiere un nombre de archivo lógico)
social_caption: "Escribe aquí un post para Instagram/Facebook/LinkedIn. Máximo 50 palabras. Usa emojis 🧲✨ y hashtags #ParBiomagnetico #SaludMonzon #Bienestar."
---

(A partir de aquí el contenido del artículo con H2, H3, bold, etc.)
"""

def procesar_articulos():
    archivos = [f for f in os.listdir(DIRECTORIO_BLOG) if f.endswith(".md")]
    print(f"📂 Encontrados {len(archivos)} archivos en {DIRECTORIO_BLOG}")
    
    # Barra de progreso
    for nombre_archivo in tqdm(archivos, desc="Refinando Biomagnetismo"):
        ruta_completa = os.path.join(DIRECTORIO_BLOG, nombre_archivo)
        
        try:
            # 1. Leer metadata actual
            post = frontmatter.load(ruta_completa)
            
            # 2. FILTRO: Solo procesamos si active es False (o si no tiene campo active)
            is_active = post.get('active', False)
            
            if is_active is True:
                # Si está activo, lo saltamos para no tocar lo publicado
                continue
            
            # 3. Preparar el Prompt
            contenido_actual = post.content
            titulo_actual = post.get('title', 'Sin título')
            
            prompt_usuario = f"""
            ARTÍCULO ORIGINAL A REESCRIBIR:
            Título: {titulo_actual}
            Contenido:
            {contenido_actual}
            """

            # 4. Llamar a Gemini
            response = model.generate_content(
                f"{SYSTEM_INSTRUCTION}\n\n{prompt_usuario}"
            )
            
            nuevo_texto = response.text
            
            # 5. Limpieza básica (por si Gemini mete ```markdown al principio)
            nuevo_texto = nuevo_texto.replace("```markdown", "").replace("```", "").strip()

            # 6. Sobrescribir archivo
            with open(ruta_completa, "w", encoding="utf-8") as f:
                f.write(nuevo_texto)
                
            # Pequeña pausa para no saturar la API (Rate Limit)
            time.sleep(2)

        except Exception as e:
            print(f"⚠️ Error en {nombre_archivo}: {e}")

if __name__ == "__main__":
    print("🚀 Iniciando Refinería de Contenidos con IA (Biomagnetismo)...")
    if not os.path.exists(DIRECTORIO_BLOG):
        print(f"❌ Error: No existe la carpeta {DIRECTORIO_BLOG}. Edita el script y pon la ruta correcta.")
    else:
        procesar_articulos()
        print("✅ ¡Proceso completado! Revisa tus artículos.")