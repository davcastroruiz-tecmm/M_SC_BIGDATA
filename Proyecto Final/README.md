# Proyecto de Big Data

## Descripción del Proyecto

Este proyecto tiene como objetivo diseñar, implementar y documentar un sistema completo de procesamiento de Big Data que abarca desde la adquisición y almacenamiento de datos hasta su transformación y análisis. El enfoque principal es aplicar los conocimientos adquiridos en el curso, implementando una arquitectura eficiente utilizando herramientas y servicios de Big Data, con un pipeline ETL (Extracción, Transformación y Carga) robusto.

### Objetivos:
- Diseñar e implementar un pipeline ETL que cubra las etapas de adquisición, transformación y carga de datos.
- Modelar los datos utilizando técnicas de normalización para optimizar su análisis.
- Desplegar la solución tanto en ambiente local como en la nube (AWS u otros servicios).
- Generar evidencias funcionales que incluyan scripts, logs, pantallazos y resultados de consultas.
- Documentar y analizar los resultados obtenidos, proporcionando un análisis crítico sobre el rendimiento y la efectividad de la solución implementada.

## Estructura del Repositorio

Este repositorio contiene los siguientes directorios y archivos clave:

- **`README.md`**: Documentación principal del proyecto, incluyendo el propósito, objetivos y estructura general.
- **`docs/`**: Contiene diagramas, arquitectura de la solución, rúbrica de evaluación, evidencias y análisis crítico.
- **`data/`**: Scripts para la generación de datasets de ejemplo representativos. (Los datasets completos no están incluidos por razones de tamaño y seguridad).
- **`src/`**: Código fuente modularizado y documentado del proyecto, incluyendo las transformaciones y la lógica del pipeline ETL.
- **`notebooks/`**: Notebooks con resultados, experimentos y ejemplos reproducibles, que sirven como evidencia del análisis realizado.
- **`dags/`**: Archivos de orquestación con Airflow, si se ha utilizado para automatizar el flujo de trabajo.
- **`docker/`**: Archivos Docker necesarios para levantar el sistema en contenedores y facilitar la implementación en diferentes entornos.
- **`tests/`**: Pruebas unitarias y funcionales para evaluar automáticamente la correcta ejecución de las funcionalidades clave.

## Requisitos

Para ejecutar este proyecto, necesitas tener instalados los siguientes programas y dependencias:

- Python 3.x
- Docker (si vas a utilizar la opción de contenedores)
- Apache Airflow (si se incluye la orquestación)
- AWS CLI (si se usa en la nube)
- Librerías necesarias (consultar `requirements.txt`)

## Instrucciones de Instalación

1. Clona el repositorio en tu máquina local:
    ```bash
    git clone https://github.com/usuario/proyecto-big-data.git
    cd proyecto-big-data
    ```

2. Instala las dependencias del proyecto:
    ```bash
    pip install -r requirements.txt
    ```

3. Si vas a usar Docker para desplegar el sistema, construye la imagen:
    ```bash
    docker build -t bigdata-project .
    ```

4. Para ejecutar el pipeline ETL, sigue las instrucciones específicas en el directorio `src/`.

## Instrucciones de Ejecución

1. **Ejecutar el pipeline ETL**: 
    Para ejecutar el pipeline, solo necesitas correr el siguiente script (asegúrate de tener configurados los parámetros correctos para tu entorno):
    ```bash
    python src/etl_pipeline.py
    ```

2. **Cargar datos a la nube** (si es necesario):
    ```bash
    aws s3 cp data/dataset.csv s3://tu-bucket/
    ```

3. **Ejecutar las pruebas**:
    Puedes correr los tests automáticos con:
    ```bash
    pytest tests/
    ```

## Evidencias Funcionales

En el directorio `docs/` se incluyen los siguientes elementos como evidencia de la funcionalidad del proyecto:
- **Logs de ejecución**: Ejemplos de logs generados durante el procesamiento de datos.
- **Pantallazos**: Imágenes que muestran la correcta ejecución del pipeline y los resultados de las consultas.
- **Resultados de consultas**: Resultados extraídos durante el análisis de datos que muestran la efectividad de la solución.

## Análisis Crítico

En el directorio `docs/` también se presenta un análisis crítico de los resultados obtenidos. Este análisis incluye una evaluación del rendimiento del sistema, los desafíos enfrentados durante el desarrollo del pipeline ETL, y las conclusiones finales respecto a la solución implementada.

## Conclusiones

Este proyecto pone en práctica el ciclo completo de procesamiento de Big Data utilizando herramientas modernas y mejores prácticas. A través de la implementación del pipeline ETL, la normalización de datos y el análisis crítico de los resultados, se demuestra la capacidad para abordar problemas complejos en entornos de Big Data.

## Licencia

Este proyecto está bajo la licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.
