#Alunos: Luiz Filipe Neuwirth - 2111287 
# Carlos Eduardo Cunha Ribeiro - 2110758 
# Douglas Leonel de Almeida -2110213 
# Sebastião Oliveira Neto - 2011478 
# Thiago Silva Soares – 2011250

import google.generativeai as genai
import tweepy
import schedule
import time

#Autenticação da API do chat bot da Google
genai.configure(api_key="AIzaSyBNajXzabICV0Xz9Ixn85yFxlGjBlNeZWI")

# Modelo de conversa
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

# Configurações de segurança
safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

# Inicialização do modelo
model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

convo = model.start_chat(history=[
])

# Autenticação da API do Twitter
api= tweepy.Client(
    consumer_key="y7oCEyLDHx408881tDoxZkH6S",
    consumer_secret="da14f4Ttq4hn7LIRKz3EJuLBpq8IGjYcVNVW2N3Z4kE08Ch2VC",
    access_token="1768400887985111040-By9KHfJdCUg0NhPOzue0WWH2Cee5Hc",
    access_token_secret="DF9CZOVFKhy36A7N6L39R8nuD0nA8nofAn8XNpG4Ljw1k"

)

# Função para enviar o tweet
def send_tweet():
    convo = model.start_chat(history=[])
    # Enviar a mensagem para o chat bot
    convo.send_message("Escreva 3 dicas para melhorar a qualidade do sono, e escreva as dicas de forma curta, objetiva e diretas podendo ser dicas de alimentos, dicas do que não comer antes de dormir, o que fazer antes de dormir para ter um sono melhor, ou outro assunto relacionado ao bem estar no sono. Escreva UM tópico que você vai abordar o assunto e fale sobre. obs: no maximo 120 caracteres total(contando com espaços e simbolos), não repita com algo que você já tenha escrito antes, e não escreva asterisco(*), NAO ESQUEÇA NO MÁXIMO 120 CARACTERES, NÃO PASSE DISSO, NÃO FALE SOBRE CAFEINA E ALCOOL, ABORDE OUTROS ASSUNTOS.")
    tweet = convo.last.text
    try:
        print(tweet) # Mostrar o tweet no console
        # Enviar o tweet
        api.create_tweet(text= tweet)
        print("Tweet enviado com sucesso.") # Mostrar mensagem de sucesso no console
    except:
        print("Erro ao enviar tweet:")

#Enviar o tweet pela primeira vez
send_tweet()

# Agendar o envio do tweet a cada 8 horas
schedule.every(8).hours.do(send_tweet)

while True:
    schedule.run_pending()
    time.sleep(1)