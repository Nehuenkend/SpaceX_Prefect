**Proyecto Integral de Orquestación de Datos con Prefect: De la Ingesta a la Visualización**

Este proyecto demuestra un pipeline de datos completo y robusto utilizando todas las funcionalidades clave de Prefect, una moderna plataforma de orquestación de flujos de trabajo. El objetivo es diseñar, desarrollar y mantener un pipeline que ingiere datos de una API pública, los procesa, los enriquece, los almacena y notifica sobre su estado, aprovechando al máximo las capacidades de Prefect para la automatización, la resiliencia y la observabilidad.

Objetivo del Proyecto
Crear un flujo de trabajo de datos que:

Ingiera datos de la API pública de SpaceX para obtener información sobre sus lanzamientos.

Procese y transforme los datos para extraer información relevante.

Enriquezca los datos con información meteorológica del día del lanzamiento utilizando otra API.

Almacene los datos procesados en un archivo CSV y en una base de datos SQLite.

Genere una visualización simple de los datos.

Notifique el éxito o fracaso del pipeline a través de Slack.

Se ejecute de forma programada y también pueda ser desencadenado por eventos.

Gestione fallos con reintentos automáticos.

Optimice la ejecución mediante el almacenamiento en caché de resultados.
