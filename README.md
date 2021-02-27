# MLFlow Docker Deployment with Databricks Integration

Containerized Deployment of MLFlow Models with Databricks Integration

- [MLFlow Docker Deployment with Databricks Integration](#mlflow-docker-deployment-with-databricks-integration)
- [Architecture](#architecture)
- [Methods](#methods)
  - [Used Python Libraries](#used-python-libraries)
  - [Open Ports](#open-ports)
- [Requirements](#requirements)
- [Instructions](#instructions)
  - [Setting up a Databricks Service Account](#setting-up-a-databricks-service-account)
  - [Retrieving Databricks credentials](#retrieving-databricks-credentials)
  - [Configuration](#configuration)
  - [Run the Code](#run-the-code)
    - [Prepare the Data](#prepare-the-data)
    - [Prediction Endpoint](#prediction-endpoint)
  - [Test if gunicorn is working](#test-if-gunicorn-is-working)

# Architecture

![mlflow_architecture](https://raw.githubusercontent.com/brickmeister/mlflow_docker/main/images/MLFlow%20Docker%20Deployment.png)

# Methods

The following code utilizes gunicorn, docker, docker-compose, and mlflow to deploy models. Models are retrieved from Databricks' MLFlow registry and loaded in a dockerized gunicorn wsgi app. See [Accessing MLFlow Outside of Databricks](https://docs.databricks.com/applications/mlflow/access-hosted-tracking-server.html) for more details.

## Used Python Libraries

* MLFlow
* gunicorn
* flask

## Open Ports

* 5000

# Requirements

* Docker Deployment Support
* Databricks Account
* Connection to Databricks MLFlow Registry

# Instructions

## Setting up a Databricks Service Account

To retrieve models from Databricks, it is highly suggested to use a service account in Databricks. See [Databricks User Admin Guide](https://docs.databricks.com/administration-guide/users-groups/users.html) for details on how to manager users.

## Retrieving Databricks credentials

To retrieve Databricks tokens and credentials. See [Databricks-CLI Guide](https://docs.databricks.com/dev-tools/cli/index.html) for more details on how to setup the databricks cli.

## Configuration

Please modify the values in `config/web_srv.env` to provide the needed credentials
|Variable|Description| Extra Details|
|--------|-----------|--------------|
|FLASK_APP| Location of flask app code, do not modify!||
|MLFLOW_TRACKING_URI| MLFlow Tracking server URI, keep as databricks||
|DATABRICKS_HOST|URL for Databricks deployment, obtained from `databricks configure`| listed as `host` in `~/.databrickscfg`|
|DATABRICKS_TOKEN|Token used for authorization/authentication against Databricks, obtained from `databricks configure`| listed as `password` in `~/.databrickscfg`|
|LOGGED_MODEL| MLFlow model URI to retrieve||

## Run the Code

Clone this repo and run the following `docker-compose` command to bring up the `gunicorn` server.

```
docker-compose up
```

### Prepare the Data
Convert a `pandas` dataframe to `json` with the `records` format

### Prediction Endpoint
Post a `POST` request to `localhost:5000/predict` with a `json payload` to predict.

## Test if gunicorn is working

In a separate terminal, run the following command to test if the gunicorn server is up. ** Note there is some startup time to connect to the MLFlow registry, so it is suggested to wait a few minutes before attempting curl the rest endpoint.

```
curl localhost:5000
```

Expected result is.
```
{"hello":"world"}
```