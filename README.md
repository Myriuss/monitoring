# Monitoring Setup

This directory contains the configuration files for setting up monitoring using Prometheus, Grafana, Loki, and Promtail.

## Services

- **Prometheus**: Time series database for monitoring and alerting.
- **Grafana**: Analytics and interactive visualization web application.
- **Loki**: Log aggregation system.
- **Promtail**: Agent for collecting logs and sending them to Loki.
- **RabbitMQ**: Message broker for handling communication between services.

## Setup

1. Ensure Docker and Docker Compose are installed on your system.
2. Navigate to the `monitoring` directory.
3. Run `docker-compose up -d` to start all services.

## Configuration

- **Prometheus**: Configured to scrape metrics from various endpoints.
- **Loki**: Configured to store and index logs.
- **Promtail**: Configured to read logs from the `/var/log` directory and push them to Loki.
