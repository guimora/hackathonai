# Importar la librería de ChatGPT (gpt-3.5-turbo)
import os
import openai
from dotenv import load_dotenv

# Configurar la API key de OpenAI
load_dotenv()

openai.api_key = os.getenv("OPENAI_KEY")


# Llamar a la API de ChatGPT para obtener sugerencias
def get_response_chatgpt(req: str) -> str:
    prompt = f"You are a Quality Assurance Engineer" \
             f"You have been doing this task for 20 years" \
             f"Your task is to generate 5 behaviours using gherkin language for the following requirement: {req} " \
             f"and create unit testing for a Development team and test cases for the QA team"
    response = openai.Completion.create(
        engine="text-davinci-003",  # Motor de ChatGPT
        prompt=prompt,
        # Texto ingresado por el usuario
        max_tokens=1000  # Máximo número de tokens en la respuesta
    )
    return response.choices[0].text.strip()
