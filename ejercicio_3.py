import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Cargar variables de entorno
load_dotenv()

API_KEY = os.getenv("GENAI_API_KEY")

# Inicializar cliente de Gemini
client = genai.Client(api_key=API_KEY)

config_chat = types.GenerateContentConfig(
    max_output_tokens=2048,
    system_instruction="""
Eres un vendedor amable de una tienda de tecnología.
Respondes de forma clara, cordial y con especificaciones técnicas.
"""
)

# Historial few-shot
history = [
    {
        "role": "user",
        "parts": [{"text": "¿Qué características tiene el iPhone 15?"}]
    },
    {
        "role": "model",
        "parts": [{"text": "El iPhone 15 cuenta con pantalla OLED de 6.1 pulgadas, "
            "chip A16 Bionic, cámara principal de 48 MP y conectividad USB-C."}]
    },
    {
        "role": "user",
        "parts": [{"text": "¿Qué incluye un portátil para gaming?"}]
    },
    {
        "role": "model",
        "parts": [{"text":"Un portátil gaming suele incluir procesador de alto rendimiento, "
            "tarjeta gráfica dedicada, mínimo 16 GB de RAM y sistema de refrigeración avanzado."
            }]
    }
]

chat = client.chats.create(
    model="gemini-2.5-flash",
    config=config_chat,
    history=history
)

print("--- Chat de Soporte Técnico ---")
print("(Escribe 'finalizar' para terminar)\n")

while True:
    user_input = input("Cliente: ")

    if user_input.lower() == "finalizar":
        print("Vendedor: ¡Gracias por visitarnos! Que tengas un excelente día.")
        break

    response = chat.send_message(user_input)
    print(f"\nVendedor: {response.text}\n")
