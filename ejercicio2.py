from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from langchain_cohere import ChatCohere
from my_models import GEMINI_FLASH
from my_keys import GEMINI_API_KEY, COHERE_API_KEY
from my_helper import encode_image

llm = ChatGoogleGenerativeAI(
    api_key=GEMINI_API_KEY,
    model=GEMINI_FLASH
)

respuesta = llm.invoke("Cuáles canales colombianos de youtube me recomiendas para saber más sobre inversiones?")
print(f"Gemini: ",respuesta.content)

llm = ChatCohere(
    cohere_api_key=COHERE_API_KEY
)

# Antes (lo que te está dando error):
#respuesta = llm.invoke(HumanMessage(content="Cuáles canales colombianos de youtube me recomiendas para saber más sobre inversiones?"))

# Después:
respuesta = llm.invoke("Cuáles canales colombianos de youtube me recomiendas para saber más sobre inversiones?")
print(f"Cohere: ",respuesta.content)