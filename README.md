# Taller Práctico – Google Gemini API con Python

## 📌 Descripción general

Este repositorio contiene el desarrollo de un taller práctico cuyo objetivo es
implementar un script en Python que utilice la librería **google-genai** para
realizar peticiones a modelos de lenguaje, procesar textos y gestionar
conversaciones interactivas con roles definidos.

El proyecto está dividido en tres ejercicios progresivos que abarcan desde una
consulta básica hasta un sistema de chat con historial (few-shot learning).

---

## 🛠️ Tecnologías utilizadas

- Python 3.11
- Google Gemini API
- Librería `google-genai`
- Librería `python-dotenv`
- Visual Studio Code

---

## 📂 Estructura del proyecto

```text
taller-practico-gemini/
├── ejercicio_1.py
├── ejercicio_2.py
├── ejercicio_3.py
├── requirements.txt
├── README.md
└── images/
```

---

# 🚀 Ejercicio 1: Conexión y Petición Básica

## Objetivo

Inicializar el cliente de Gemini y realizar una consulta simple.  
El modelo explica qué es la **inferencia en Inteligencia Artificial**  
en menos de 50 palabras.

## Funcionamiento

- Se inicializa el cliente con una API Key.  
- Se envía un prompt directo al modelo.  
- Se imprime la respuesta generada.

📷 *Ejemplo de ejecución:*

![Ejecución Ejercicio 1](imagenes/ejercicio_1.png)

---
# 🧠 Ejercicio 2: Procesador de Textos Inteligente

## Objetivo

Desarrollar una función `procesar_articulo(texto, tarea)` que permita:

- **Resumir** un texto largo en un resumen ejecutivo.  
- **Profesionalizar** un texto con un tono formal y técnico.

## Restricción cumplida

Se utiliza una `system_instruction` que define a la IA como un  
**Editor Editorial de prestigio**.

## Funcionamiento

- La función recibe un texto y una tarea.  
- Dependiendo de la tarea, se genera el prompt correspondiente.  
- Se retorna el texto procesado por el modelo.

📷 *Ejemplo de ejecución:*

![Ejecución Ejercicio 1](imagenes/ejercicio_2.png)

---
# 💬 Ejercicio 3: Chat de Soporte con Historial (Few-Shot)

## Objetivo

Construir un sistema de chat interactivo para una tienda de tecnología.

## Características

- Rol definido mediante `system_instruction` (vendedor amable).  
- Historial precargado con ejemplos (few-shot learning).  
- Bucle de conversación hasta que el usuario escribe **"finalizar"**.

## Funcionamiento

- Se inicializa un chat con contexto previo.  
- El usuario puede realizar múltiples preguntas.  
- El sistema responde con información técnica y cordial.

📷 *Ejemplo de ejecución:*

![Ejecución Ejercicio 1](imagenes/ejercicio_3.png)
