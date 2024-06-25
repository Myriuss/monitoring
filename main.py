import os
from loguru import logger
from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
import pika

app = FastAPI()

# Configure Prometheus
Instrumentator().instrument(app).expose(app)

# RabbitMQ connection setup
rabbitmq_host = os.getenv('RABBITMQ_HOST', 'localhost')
connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host))
channel = connection.channel()

# Assurez-vous que le répertoire existe
log_directory = "./logs"
os.makedirs(log_directory, exist_ok=True)

# Ajouter le fichier de log dans le répertoire 'logs'
logger.add(f"{log_directory}/clients-api.log", rotation="500 MB")
# Pour produits-api
logger.add(f"{log_directory}/produits-api.log", rotation="500 MB")
# Pour commandes-api
logger.add(f"{log_directory}/commandes-api.log", rotation="500 MB")

@app.get("/")
async def read_root():
    logger.info("Root endpoint accessed")
    return {"Hello": "World"}

@app.get("/metrics")
async def metrics():
    return {"message": "Metrics endpoint"}

@app.post("/message")
async def send_message(message: str):
    channel.basic_publish(exchange='', routing_key='task_queue', body=message)
    logger.info(f"Sent message to RabbitMQ: {message}")
    return {"message": "Message sent"}
