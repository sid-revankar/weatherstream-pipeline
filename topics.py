from kafka.admin import KafkaAdminClient, NewTopic
from config import KAFKA_BROKER, TOPIC_NAME

admin_client = KafkaAdminClient(bootstrap_servers=KAFKA_BROKER)

# Create topics if they don’t already exist
existing_topics = admin_client.list_topics()
topic_list = []

for topic, config in TOPIC_NAME.items():
    if topic not in existing_topics:
        topic_list.append(NewTopic(name=topic, num_partitions=config['num_partitions'], replication_factor=config['replication_factor']))

if topic_list:
    admin_client.create_topics(new_topics=topic_list)
    print("✅ Topics created successfully.")
else:
    print("⚠️ Topics already exist, skipping creation.")
