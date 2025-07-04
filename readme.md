# **🚀 Proyecto Integral de Orquestación de Datos con Prefect: De la Ingesta a la Visualización**

Este proyecto demuestra un pipeline de datos completo y robusto utilizando todas las funcionalidades clave de **Prefect**, una moderna plataforma de orquestación de flujos de trabajo.  
El objetivo es diseñar, desarrollar y mantener un pipeline que:

- Ingiera datos de una API pública.
- Los procese, enriquezca, almacene y visualice.
- Notifique sobre su estado.
- Aproveche la automatización, resiliencia y observabilidad que ofrece Prefect.

---

## 🎯 Objetivo del Proyecto

Crear un flujo de trabajo de datos que:

- 🔄 **Ingiera** datos de la API pública de SpaceX para obtener información sobre sus lanzamientos.
- 🔍 **Procese y transforme** los datos para extraer información relevante.
- 🌦️ **Enriquezca** los datos con información meteorológica del día del lanzamiento utilizando otra API.
- 💾 **Almacene** los datos procesados en un archivo CSV y en una base de datos SQLite.
- 📊 **Genere visualizaciones** simples de los datos.
- 📣 **Notifique** el éxito o fracaso del pipeline a través de Slack.
- 🕒 **Se ejecute de forma programada** y también pueda ser desencadenado por eventos.
- ♻️ **Gestione fallos** con reintentos automáticos.
- ⚡ **Optimice** la ejecución mediante el almacenamiento en caché de resultados.

---

## 🧪 Cómo Ejecutar el Proyecto

## Instalar Prefect y Autenticarse con Prefect Cloud:

```bash
uvx prefect-cloud login
```

**Desde la carpeta src:**

## Ejecutar el Flujo Localmente:

```bash
uv run spacex_pipeline.py
```

## Aplicar el Deploy de forma remota:

```bash
uvx prefect-cloud deploy spacex_pipeline.py:spacex_data_pipeline \
--name spacex_pipeline_deployment \
--from .
```

## Para correr el WorkFlow de forma remota:

```bash
uvx prefect-cloud run main/spacex_pipeline_deployment
```
