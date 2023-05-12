from google.cloud import bigquery
import pandas as pd


def save_museum(museums):
    """
    Save a list of museum based on the following dictionnary
    {
        "museum": INT,
        "city": INT,
        "visitor": INT,
        "city_population": INT,
        "type": STRING,
        "director": STRING,
        "curator": STRING,
        "website": STRING
    }
    :param museums: list of museum
    :return:
    """
    client = bigquery.Client()
    job_config = bigquery.LoadJobConfig(
        schema=[
            bigquery.SchemaField("museum", bigquery.enums.SqlTypeNames.STRING),
            bigquery.SchemaField("city", bigquery.enums.SqlTypeNames.STRING),
            bigquery.SchemaField("visitors", bigquery.enums.SqlTypeNames.INT64),
            bigquery.SchemaField("city_population", bigquery.enums.SqlTypeNames.INT64),
            bigquery.SchemaField("type", bigquery.enums.SqlTypeNames.STRING),
            bigquery.SchemaField("director", bigquery.enums.SqlTypeNames.STRING),
            bigquery.SchemaField("curator", bigquery.enums.SqlTypeNames.STRING),
            bigquery.SchemaField("website", bigquery.enums.SqlTypeNames.STRING),
        ],
        write_disposition="WRITE_TRUNCATE"
    )

    df = pd.DataFrame.from_dict(museums)
    job = client.load_table_from_dataframe(
        df,
        "GCP_PROJECT_NAME.BQ_DATABASE_NAME.museums",
        job_config=job_config
    )

