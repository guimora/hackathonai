# Importar la librería de ChatGPT (gpt-3.5-turbo)
import openai

# Configurar la API key de OpenAI
openai.api_key = ''


# Llamar a la API de ChatGPT para obtener sugerencias
def get_response_chatgpt(req: str) -> str:
    prompt = f"Generate 10 or less behaviours using gherkin language for the following requirement: {req}"
    response = openai.Completion.create(
        engine="text-davinci-003",  # Motor de ChatGPT
        prompt=prompt,
        # Texto ingresado por el usuario
        max_tokens=500  # Máximo número de tokens en la respuesta
    )
    return response.choices[0].text.strip()
