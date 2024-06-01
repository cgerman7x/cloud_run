# cloud_run
Cloud Run example that consumes from Pub/Sub and ingest into Cloud SQL

# Cloud Run
## Container contract
Details can be found here https://cloud.google.com/run/docs/container-contract

# Local Set Up
## Create orders docker image from parent directory
sudo docker build . --tag=orders -f orders/Dockerfile
