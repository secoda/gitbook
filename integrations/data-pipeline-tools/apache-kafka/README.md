---
description: An overview of Apache Kafka integration with Secoda
---

# Apache Kafka

{% content-ref url="apache-kafka-metadata-extracted.md" %}
[apache-kafka-metadata-extracted.md](apache-kafka-metadata-extracted.md)
{% endcontent-ref %}

### Getting started with Apache Kafka

To integrate Apache Kafka with Secoda, we need the following

1. Create a new user in Kafka
2. Setup authentication for the newly created user to the Kafka brokers. Refer to Kafka [docs](https://kafka.apache.org/documentation/#security\_sasl\_plain\_brokerconfig) for more information

Connect Apache Kafka to Secoda

1. In Secoda, head to the **Integrations** page and click **New Integration**
2. Find **Apache Kafka** under **Data Pipeline**
3. Fill in the connection form with all the necessary details
4. Click **Test Connection** to make sure everything is correct
5. Head to the **Sync History** tab on the side bar and click **Run sync**

