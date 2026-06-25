import time
from langchain.agents.agent import AgentExecutor
from orquestador import AgenteOrquestador

def main():
    agente = AgenteOrquestador()
    ejecutor = AgentExecutor(
        agent=agente.agente,
        tools=agente.tools,
        verbose=True
    )

    pregunta = "Realiza el análisis de la imagen ejemplo_grafico.jpg"
    
    print("Esperando 60 segundos para respetar el límite de cuota...")
    time.sleep(60)  # ← aquí
    
    respuesta = ejecutor.invoke({"input": pregunta})
    
    print(respuesta)

if __name__ == "__main__":
    main()