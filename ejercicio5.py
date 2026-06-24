import langchain
langchain.debug = True

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from langchain_cohere import ChatCohere
from my_models import GEMINI_FLASH
from my_keys import GEMINI_API_KEY
from my_helper import encode_image
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from detalles_imagen import DetallesImagen

# Inicializamos el modelo
llm = ChatGoogleGenerativeAI(
    api_key=GEMINI_API_KEY, 
    model=GEMINI_FLASH
)

imagen = encode_image('datos/ejemplo_grafico.jpg')

# Creamos el parser estructurado
parser_json = JsonOutputParser(pydantic_object=DetallesImagen)

# Unificamos las instrucciones en un solo prompt
template_analisis = ChatPromptTemplate.from_messages(
    [
        ("system",
         """
         Asume que eres analista de imágenes. Tu principal tarea consiste en analizar una imagen 
         para extraer las informaciones más relevantes de manera objetiva.
         
         Genera un resumen utilizando un lenguaje claro y objetivo, enfocado en el público Colombiano.
         La idea es que la comunicación del resultado sea lo más sencillo posible, priorizando los registros 
         para consultas posteriores.

         {formato_salida}
         """
        ),
        (
            "user",
             [
                {
                    "type": "text", 
                    "text": "Describe la imagen basándote en las instrucciones del sistema."
                },
                {
                    "type": "image_url",
                    "image_url": "data:image/jpeg;base64,{imagen_informada}"
                }
             ]
         )
    ]
).partial(formato_salida=parser_json.get_format_instructions()) # Inyectamos el formato JSON aquí
    
# Ahora la cadena solo requiere una llamada al LLM y parsea directamente a JSON
cadena_optimizada = template_analisis | llm | parser_json

# Ejecución final (Solo consume 1 llamada de tu cuota)
respuesta = cadena_optimizada.invoke({"imagen_informada": imagen})
print(respuesta)