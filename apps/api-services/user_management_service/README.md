
```shell


Django==4.2
djangorestframework==3.14.0
azure-eventhub==5.9.0
kafka-python==2.0.2
azure-storage-blob==12.10.0
azure-mgmt-datalake-store==0.1.2
pyspark==3.3.2
requests==2.28.2
python-dotenv==0.21.0
psycopg2==2.9.3  # For PostgreSQL (if you're using it in production)

```

python manage.py startapp core_users
python manage.py startapp api_users

```shell

# PostgreSQL Database Adapter
psycopg2

# Python-dotenv for managing environment variables
python-dotenv

# Requests library for HTTP requests
requests


# Azure Event Hubs - For event publishing
azure-eventhub

# Azure Storage Blob - If you're working with Azure Blob Storage or Data Lake
azure-storage-blob

# Azure SDK for Data Lake management
azure-mgmt-datalake-store==0.1.2

# Azure SDK for general cloud integrations (e.g., authentication, resource management)
azure-identity

# Azure SDK for managing Databricks resources
azure-mgmt-databricks

# Kafka for local development (Only used when configured to use Kafka)
kafka-python

# PySpark - Required for Databricks integration
pyspark

# For asynchronous task management (e.g., Celery)
celery

# Optional: Fast JSON handling
orjson
```

```shell

python manage.py crontab add
# List the registered cron jobs
python manage.py crontab show

# To remove jobs later
python manage.py crontab remove
```

Handling Zero or Large Batches Automatically

- Your consume_and_write_to_adls() implementation already:
- Skips writes when no messages arrive. 
- Writes in batches when messages are large. 
- Flushes remaining messages before exit. 
- So the cron will safely handle:
  - 0 messages → no upload 
  - Few messages → one small file 
  - Millions of messages → multiple uploads in chunks

## Connecting to Postgres Database through pgAdmin

Use host.docker.internal as the hostname instead of localhost or 127.0.0.1 to connect to the Postgres database running in Docker from pgAdmin on your host machine.