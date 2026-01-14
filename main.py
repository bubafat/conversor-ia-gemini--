from google import genai
import os
CHAVE = os.getenv("GOOGLE_API_KEY") 

client = genai.Client(
    api_key=CHAVE,
    http_options={'api_version': 'v1'}
)

print("--- CONVERSOR IA 2026 (Digite 'sair' para encerrar) ---")
while True:
    pergunta = input("\nO que deseja converter? ")
    if pergunta.lower() == 'sair':
        break
    
    # ... (seu código de response aqui)
pergunta = input("O que deseja converter? ")

try:
    # Usando o modelo mais novo da sua lista!
    response = client.models.generate_content(
        model="gemini-2.5-flash", 
        contents=f"Converta e responda apenas o valor: {pergunta}"
    )
    
    print("\n--- RESULTADO ---")
    print(response.text)

except Exception as e:
    if "429" in str(e):
        print("\nErro: Cota esgotada. Aguarde 60 segundos e tente novamente.")
    else:
        print(f"\nErro: {e}")