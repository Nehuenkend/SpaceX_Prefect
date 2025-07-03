import httpx
import pandas as pd
from prefect import task, flow
from prefect.tasks import task_input_hash
from datetime import timedelta
import sqlite3


@task(
    retries=3,
    retry_delay_seconds=5,
    cache_key_fn=task_input_hash,
    cache_expiration=timedelta(days=1),
)
def fetch_spacex_launches(limit: int = 10):
    """Ingiere los últimos lanzamientos de la API de SpaceX."""
    url = f"https://api.spacexdata.com/v5/launches?limit={limit}"
    with httpx.Client() as client:
        response = client.get(url)
        response.raise_for_status()
        return response.json()


@task
def process_launch_data(launches: list) -> pd.DataFrame:
    """Procesa los datos brutos de los lanzamientos a un DataFrame de pandas."""
    processed_data = []
    for launch in launches:
        processed_data.append(
            {
                "flight_number": launch.get("flight_number"),
                "name": launch.get("name"),
                "date_utc": launch.get("date_utc"),
                "success": launch.get("success"),
                "details": launch.get("details", "No details available."),
            }
        )
    return pd.DataFrame(processed_data)


@task
def store_as_csv(data: pd.DataFrame) -> str:
    """Almacena los datos procesados en un archivo CSV."""
    filepath = "db/spacex_launches.csv"
    data.to_csv(filepath, index=False)
    return filepath


@task
def store_in_sqlite(data: pd.DataFrame, db_name: str = "db/spacex.db"):
    """Almacena los datos en una base de datos SQLite."""
    conn = sqlite3.connect(db_name)
    data.to_sql("launches", conn, if_exists="replace", index=False)
    conn.close()
    return f"Stored in {db_name}"


from prefect.task_runners import ConcurrentTaskRunner


@flow(
    name="SpaceX Data Pipeline",
    task_runner=ConcurrentTaskRunner(),
    description="Un pipeline completo que ingiere, procesa y almacena datos de lanzamientos de SpaceX.",
)
def spacex_data_pipeline(limit: int = 10):
    """
    Flujo principal que orquesta el pipeline de datos de SpaceX.
    """
    # Ingesta
    raw_launches = fetch_spacex_launches(limit=limit)

    # Procesamiento
    processed_launches = process_launch_data(raw_launches)

    # Almacenamiento (se ejecutan en paralelo)
    csv_path_future = store_as_csv.submit(processed_launches)
    db_status_future = store_in_sqlite.submit(processed_launches)

    # Espera a que las tareas de almacenamiento finalicen
    csv_path = csv_path_future.result()
    db_status = db_status_future.result()

    print(f"CSV guardado en: {csv_path}")
    print(f"Estado de la base de datos: {db_status}")


if __name__ == "__main__":
    spacex_data_pipeline(limit=5)
