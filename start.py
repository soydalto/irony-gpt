#Importa la librería OpenAI, necesaria para este codigo
import openai as o

#Configura la API de OpenAI
o.api_key = "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"

# Mensaje inicial para que openAI entienda cómo debe actuar. Básicamente si el mensaje
# es negativo retorna -1, neutral 0 y positivo 1. Pudiendo también ser un valor flotante.
initialPrompt = """hace de cuenta que sos un analizador de sentimientos. yo te paso sentimientos y vos analizas
                   el sentimiento de los mensaje y me das una respuesta con al menos 1 caracter y un máximo de 4 caracteres
                   SOLO RESPUESTAS NUMÉRICAS, -1 es negatividad máxima, 0 es neutral y 1 es positivo. (podes usar valores flotantes)."""

#Lista de mensajes del chat
messages = [
    {"role": "system", "content": initialPrompt}
]

#creamos la clase "AnalizadorDeSentimientos", en la que crearemos un método que...
# determina si el mensaje es más o menos negativo dependiendo del valor númerico dado por openIA
class AnalizadorDeSentimientos:
        def analizar_sentimiento(self, polaridad):
            if polaridad > -0.6 and polaridad <= -0.3:
                return "\x1b[1;31m"+'negativo'+"\x1b[0;37m"
            elif polaridad > -0.3 and polaridad < 0:
                return "\x1b[1;31m"+'algo negativo'+"\x1b[0;37m"
            elif polaridad == 0:
                return "\x1b[1;33m"+'neutral'+"\x1b[0;37m"
            elif polaridad > 0 and polaridad <= 0.3:
                return "\x1b[1;33m"+'algo positivo'
            elif polaridad > 0.3 and polaridad <= 0.6:
                return "\x1b[1;32m"+'positivo'
            elif polaridad > 0.6 and polaridad <= 0.9:
                return "\x1b[1;32m"+'muy positivo'
            elif polaridad > 0.9 and polaridad <= 1:
                return "\x1b[1;32m"+'muy muy positivo'
            else :
                return "\x1b[1;31m"+'muy negativo'+"\x1b[0;37m"


#Crea una instancia del AnalizadorDeSentimientos
analizador = AnalizadorDeSentimientos()

# Bucle que mantiene la conversación hasta que se termine
while True:
    # Solicita al usuario que ingrese un mensaje
    userPrompt = input("\x1b[1;33m"+"\nDecime algo: "+"\x1b[0;37m")
    messages.append({"role": "user", "content": userPrompt})
    
    # Completar el mensaje del usuario utilizando OpenAI ChatCompletion
    completion = o.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=1200
    )

    # Agregar la respuesta de openIA a la lista de mensajes
    messages.append({
        "role": "assistant",
        "content": completion.choices[0].message['content']
    })
    
    #Analiza el sentimiento del mensaje
    sentimiento = analizador.analizar_sentimiento(float(completion.choices[0].message['content']))

    # Muestra el sentimiento analizado
    print(sentimiento)