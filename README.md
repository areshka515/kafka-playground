This project is sepered to 3 namespaces.
1. cpu-reader:
   A namespace for the python application that gets the CPU usage for the host.
   Produces the data as json based to Kafka cluster that is hosted on K8(namespace: kafka).
   the python application is running on CronJob that is triggered every 1 minute.
2. kafka:
   This namespace is used for hosting the Kafka cluster using Bitnami kafka helm chart,
   as a Consumer i chose to use Kafka-connect and its deployed within the helm chart using extraDeploy.
   I deployed an deployment that has init container to retrieve the S3 Sink connector metadata from S3 bucket, volumed it to the main container which is running the kafka image,
   Also created a ConfigMap for the connector settings and mounted it to the main container.
   the Topic is called cpu_reader
4. monitoring:
   Cotaines the helm charts for monitoring applications(metric server and promethues)
   in promethues's helm chart i defined a Lisener that gets the metrics from both kafka cluster and metric server on /metrics.
   
