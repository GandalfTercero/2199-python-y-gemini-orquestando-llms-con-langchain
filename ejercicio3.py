from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from langchain_cohere import ChatCohere
from my_models import GEMINI_FLASH
from my_keys import GEMINI_API_KEY, COHERE_API_KEY
from my_helper import encode_image
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = ChatGoogleGenerativeAI(
    api_key=GEMINI_API_KEY,
    model=GEMINI_FLASH
)

imagen = encode_image('datos/ejemplo_grafico.jpg')

template_analisis = ChatPromptTemplate.from_messages(
    [
    ("system",
     """
     Asume que eres analista de imágenes. Tu principal tarea consiste en: 
     analizar una imagen para extraer las informaciones más relevantes de manera objetiva."

     # FORMATO DE SALIDA
     Descripción de la imagen: Tu descripción de la imagen aqui.
     Etiquetas: Una lista con 3 palabras-clave separadas con comas.
     """
    ),
    (
        "user",
          [
            {
                "type": "texto",
                "text": "Describe la imagen:"
            },
            {
                "type": "image_url",
                "image_url": "data:image/jpeg;base64,{imagen_informada}"
            }
          ]
     )
    ]
)
    

cadena_analisis = template_analisis | llm | StrOutputParser()
respuesta_analisis = cadena_analisis.invoke({"imagen_informada": imagen})

print(respuesta_analisis)
