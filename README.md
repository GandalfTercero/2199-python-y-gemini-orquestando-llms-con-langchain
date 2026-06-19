# Título del proyecto

2199 - Python y Gemini: Orquestando LLMs con LangChain

## 🔨 Funcionalidades del proyecto

En este proyecto, utilizaremos LangChain como framework principal para orquestar una solución integrada de análisis y organización de imágenes enriquecidas con anotaciones inteligentes. LangChain será empleado debido a su capacidad para conectar y gestionar flujos complejos que combinan IA multimodal y modelos de lenguaje, lo que permite un desarrollo más modular y escalable.

![](img/amostra.gif)

## ✔️ Técnicas y tecnologías utilizadas

Las técnicas y tecnologías utilizadas son:

- Programación en Python  
- Uso de la API Gemini  
- Uso del framework LangChain  
- Cadenas simples  
- Agente orquestador  
- Agente como herramientas

## 📋 Prerrequisitos
Antes de empezar, asegúrate de tener instalado:
- [Python 3.10 o superior](https://www.python.org/downloads/)
- [Git](https://git-scm.com/)
- Una API Key de [Cohere](https://dashboard.cohere.com/api-keys)

## 🚀 Paso a paso para ejecutarlo en tu máquina

### 1. Clonar el repositorio
Abre tu terminal y ejecuta:
```bash
git clone https://github.com/TU_USUARIO/nombre-del-repo.git
cd nombre-del-repo
```

### venv en Windows:
Esto aísla las dependencias del proyecto.
```bash
python -m venv .venv-gemini-3
.\.venv-gemini-3\Scripts\activate
```

### venv en Mac/Linux:

```bash
python3 -m venv .venv-gemini-3
source .venv-gemini-3/bin/activate
```

Después, instala los paquetes/dependencias utilizando:

```bash
pip install -r requirements.txt
```

## 🔑 Generar API\_KEYs y asociarlas al archivo .env
Crea un archivo llamado .env en la raíz del proyecto (al mismo nivel que requirements.txt) y añade tu clave:

```python
GEMINI_API_KEY = "TU_API_KEY_AQUÍ"
COHERE_API_KEY = "TU_API_KEY_AQUÍ"
```

