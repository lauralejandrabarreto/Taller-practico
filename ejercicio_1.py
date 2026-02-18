import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Cargar variables de entorno
load_dotenv()

API_KEY = os.getenv("GENAI_API_KEY")

# Inicializar cliente de Gemini
client = genai.Client(api_key=API_KEY)
config_ej1 = types.GenerateContentConfig(
    max_output_tokens=2048
)

prompt = (
    "Explica qué es la inferencia en Inteligencia Artificial "
    "en menos de 50 palabras."
)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    config=config_ej1,
    contents=prompt
)

print("Ejercicio 1 - Respuesta:")
print(response.text)