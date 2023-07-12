# Importar la librería de ChatGPT (gpt-3.5-turbo)
import openai

# Configurar la API key de OpenAI
openai.api_key = 'OPENAI_TOKEN'

# Pedir al usuario que ingrese un texto
texto_usuario = input("Requirement: ")

# Llamar a la API de ChatGPT para obtener sugerencias
response = openai.Completion.create(
  engine="text-davinci-003",  # Motor de ChatGPT
  prompt="Generate 10 or less behaviours using gherkin language for the following requirement: " + texto_usuario,       # Texto ingresado por el usuario
  max_tokens=500               # Máximo número de tokens en la respuesta
)

# Obtener la respuesta de ChatGPT
respuesta_chatgpt = response.choices[0].text.strip()

# Mostrar la respuesta
print("These are your behaviours:")
print(respuesta_chatgpt)
