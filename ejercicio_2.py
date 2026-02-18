import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Cargar variables de entorno
load_dotenv()

API_KEY = os.getenv("GENAI_API_KEY")

# Inicializar cliente de Gemini
client = genai.Client(api_key=API_KEY)

def procesar_articulo(texto, tarea):
    """
    Procesa un texto según la tarea indicada:
    - 'resumir': devuelve un resumen ejecutivo
    - 'profesionalizar': devuelve una versión formal y técnica
    """

    if tarea not in ["resumir", "profesionalizar"]:
        return "Tarea no válida. Use 'resumir' o 'profesionalizar'."

    system_instruction = """
Eres un Editor Editorial de prestigio.
Tu trabajo es transformar textos manteniendo claridad,
precisión técnica y estilo profesional.
"""

    if tarea == "resumir":
        prompt = f"Resume el siguiente texto en un resumen ejecutivo:\n\n{texto}"
    else:
        prompt = f"Reescribe el siguiente texto con un tono formal y técnico:\n\n{texto}"

    config = types.GenerateContentConfig(
        max_output_tokens=2048,
        system_instruction=system_instruction
    )

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        config=config,
        contents=prompt
    )

    return response.text
if __name__ == "__main__":
    texto_prueba = """
La inteligencia artificial ha avanzado rápidamente en los últimos años
y se utiliza en múltiples sectores de la industria.
"""

    print("Resumen:\n")
    print(procesar_articulo(texto_prueba, "resumir"))

    print("\nTexto profesionalizado:\n")
    print(procesar_articulo(texto_prueba, "profesionalizar"))

