import time
import ast
from langchain.tools import BaseTool
from langchain_google_genai import ChatGoogleGenerativeAI
from my_models import GEMINI_FLASH
from my_keys import GEMINI_API_KEY
from my_helper import encode_image
from langchain.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from detalles_imagen import DetallesImagen

class HerramientaAnalisisImagen(BaseTool):
    name: str = "HerramientaAnalisisImagen"
    description: str = """
                       Utiliza esta herramienta siempre que te sea solicitado realizar un análisis de imagen.
                       # ENTRADAS REQUERIDAS
        
                       - 'nombre_imagen' (str) : Nombre de la imagen a ser analizada con extensión JPG.
                       Ejemplo: test.jpg o test.jpeg
                     """

    return_direct: bool = False

    def _run(self, accion):
        accion = ast.literal_eval(accion)
        camino_imagen = accion.get("nombre_imagen", "")
        
        llm = ChatGoogleGenerativeAI(
            api_key=GEMINI_API_KEY,
            model=GEMINI_FLASH
        )

        imagen = encode_image(f'datos/{camino_imagen}')

        template_analisis = ChatPromptTemplate.from_messages(
            [
                (
                   "system",
                   """
                   Asume que eres analista de imagenes. Tu principal tarea consiste en: analizar una imagen
                   para extraer las informaciones más relevantes de manera objetiva.
     
                   # FORMATO DE SALIDA
                   Descripción de la imagen: Tu descripción de la imagen aquí.
                   Etiquetas: Una lista con 3 palabras-clave separadas con comas.
                """
               ),
               (
                   "user",
                    [
                        {
                            "type": "text",
                            "text": "Describe la imagen: "
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

        parser_json = JsonOutputParser(pydantic_object=DetallesImagen)

        template_respuesta = PromptTemplate(
            template="""
            Genera un resumen, utilizando un lenguaje claro y objetivo, enfocado en el publico colombiano.
            La idea es que la comunicación del resultado sea lo más sencilla posible, priorizando los registros
            para consultas posteriores.

            #RESULTADO DE LA IMAGEN
            {respuesta_analisis_imagen}

            #FORMATO DE SALIDA
            {formato_salida}
            """,
            input_variables=["respuesta_analisis_imagen"],
            partial_variables={
                "formato_salida": parser_json.get_format_instructions()
            }
        )

        cadena_resumen = template_respuesta | llm | parser_json

        # Llamada 2: análisis de la imagen
        print("Analizando imagen...")
        resultado_analisis = cadena_analisis.invoke({"imagen_informada": imagen})

        # Pausa para respetar el límite de cuota (5 req/min en tier gratuito)
        print("Esperando 20 segundos antes de generar el resumen...")
        time.sleep(20)

        # Llamada 3: generación del resumen JSON
        print("Generando resumen...")
        respuesta = cadena_resumen.invoke({"respuesta_analisis_imagen": resultado_analisis})

        return respuesta