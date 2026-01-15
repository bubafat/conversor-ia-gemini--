# Conversor Universal com IA (Gemini 2.5 Flash)

Este projeto é um assistente de conversão inteligente que utiliza a API do Google Gemini para realizar conversões complexas através de linguagem natural.

## Desafios Superados (Aprendizado Técnico)
Durante o desenvolvimento, foram resolvidos os seguintes problemas de engenharia de software:
- **Integração de API:** Configuração e autenticação com o SDK `google-genai`.
- **Tratamento de Erros:** Implementação de blocos `try/except` para lidar com erros de cota (429) e modelos não encontrados (404).
- **Gestão de Versões:** Ajuste manual de `http_options` para forçar a API `v1`, garantindo estabilidade no Python 3.14.
- **Segurança:** Uso de variáveis de ambiente para proteção de chaves sensíveis.

## Tecnologias
- Python 3.14
- Google Gemini API (Modelo 2.5 Flash)
- Biblioteca `google-genai`

## Como usar
1. Clone o repositório.
2. Crie um arquivo `.env` com sua `GOOGLE_API_KEY`.
3. Instale as dependências: `pip install google-genai`.
4. Execute: `python main.py`.
