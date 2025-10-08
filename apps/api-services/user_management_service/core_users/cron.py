import datetime
import json
from kafka import KafkaConsumer
from azure.storage.blob import BlobClient
from django.conf import settings
from dotenv import load_dotenv
import os
import logging

LOGGER = logging.getLogger(__name__)

load_dotenv()


def consume_and_write_to_adls():
    LOGGER.info("Kafka to ADLS batch job started")
    print(f"[{datetime.datetime.now()}] Kafka to ADLS batch job started")

    # Kafka setup
    kafka_server = os.getenv('KAFKA_SERVER', 'localhost:9092')
    kafka_topic = os.getenv('KAFKA_TOPIC', 'user_updates')

    consumer = KafkaConsumer(
        kafka_topic,
        bootstrap_servers=[kafka_server],
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='user-batch-consumer-group'
    )

    # Azure setup
    storage_account_name = os.getenv('STORAGE_ACCOUNT_NAME', 'djangolocalevents01')
    storage_account_key = os.getenv('STORAGE_ACCOUNT_KEY','GET_IT_FROM_AZURE_PORTAL')
    container_name = os.getenv('CONTAINER_NAME', 'django-kafka-users')
    connection_string = os.getenv('CONTAINER_STRING', 'GET_IT_FROM_AZURE_PORTAL')

    # Batch settings
    MAX_BATCH_SIZE = 5000
    BATCH_FILE_PREFIX = "user_batch"
    BATCH_FILE_EXTENSION = ".json"
    batch_data = []

    def get_blob_client(blob_name):
        return BlobClient.from_connection_string(
            connection_string, container_name=container_name, blob_name=blob_name
        )

    def upload_to_adls(blob_name, data):
        blob_client = get_blob_client(blob_name)
        blob_client.upload_blob(data, overwrite=True)
        print(f"Uploaded batch to ADLS: {blob_name}")

    for message in consumer:
        message_value = json.loads(message.value)
        batch_data.append(message_value)

        if len(batch_data) >= MAX_BATCH_SIZE:
            timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
            blob_name = f"users/raw/{timestamp}/{BATCH_FILE_PREFIX}_{timestamp}{BATCH_FILE_EXTENSION}"
            upload_to_adls(blob_name, json.dumps(batch_data))
            batch_data.clear()

    if batch_data:
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        blob_name = f"users/raw/{timestamp}/{BATCH_FILE_PREFIX}_{timestamp}{BATCH_FILE_EXTENSION}"
        upload_to_adls(blob_name, json.dumps(batch_data))

    print(f"[{datetime.datetime.now()}] Kafka to ADLS batch job completed")
    LOGGER.info("Kafka to ADLS batch job completed")
