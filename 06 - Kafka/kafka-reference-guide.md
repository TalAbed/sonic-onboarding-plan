# Kafka Reference Guide

Complete reference for Kafka concepts, architecture, and operations.

---

## Table of Contents

1. [Kafka Architecture](#kafka-architecture)
2. [Core Concepts](#core-concepts)
3. [Producers](#producers)
4. [Consumers](#consumers)
5. [Topics & Partitions](#topics--partitions)
6. [Consumer Groups](#consumer-groups)
7. [Error Handling](#error-handling)
8. [Python kafka-python Library](#python-kafka-python-library)

---

## Kafka Architecture

### Cluster Components

```
┌─────────────────────────────────────────────────────────┐
│                    Kafka Cluster                        │
├─────────────────┬──────────────┬───────────────────────┤
│   Broker 1      │   Broker 2   │      Broker 3         │
│  (Leader)       │  (Replica)   │     (Replica)         │
├─────────────────┴──────────────┴───────────────────────┤
│  Topic: listings (3 partitions, replication factor 3)  │
├─────────────────────────────────────────────────────────┤
│  Zookeeper: Coordination & Leader Election              │
└─────────────────────────────────────────────────────────┘
```

### Components

**Broker** - Individual Kafka server that stores partitions
- Handles producer requests
- Handles consumer requests
- Manages data replication
- Typical setup: 3+ brokers for HA

**Zookeeper** - Coordinates brokers
- Elects partition leaders
- Manages cluster membership
- Stores cluster metadata

**Producer** - Sends messages
- Can target specific partition
- Receives acknowledgment
- Handles retries

**Consumer** - Reads messages
- Reads from one or more partitions
- Tracks offset (position)
- Part of consumer group

---

## Core Concepts

### Topics

**Definition:** Named feed of messages (like a category or channel)

**Characteristics:**
- Multiple producers can write to same topic
- Multiple consumers can read from same topic
- Immutable: messages cannot be deleted (only by retention)
- Distributed: spans multiple brokers
- Replicated: copies for fault tolerance

**Example:**
```
Topic: listings
├── Partition 0 → [msg1, msg2, msg3, msg4]
├── Partition 1 → [msg5, msg6, msg7]
└── Partition 2 → [msg8, msg9, msg10, msg11]
```

### Partitions

**Definition:** Ordered, immutable sequence of messages within a topic

**Key Features:**
- **Ordered:** Messages in partition have strict order
- **Offset:** Each message has unique position (0, 1, 2, ...)
- **Replication:** Replicated across brokers
- **Leader:** One broker handles reads/writes
- **Replicas:** Other brokers keep copies

**Partition Assignment:**
```python
# Key determines partition
message = {"property_id": "prop_123", ...}
# hash(key) % num_partitions = partition number
```

### Offset

**Definition:** Position or index of a message within a partition

**Uses:**
- Consumer tracks offset to know what's already read
- Allows resuming from where you left off
- Enables replaying messages

**Offset Management:**
```
Partition 0:  [0:msg1] [1:msg2] [2:msg3] [3:msg4]
                                          ↑
                           Consumer offset = 3
```

### Replication

**Definition:** Copies of partition data across multiple brokers

**Replication Factor:** How many copies (typically 3)
```
Topic: listings
  Partition 0:
    - Leader: Broker 1
    - Replicas: Broker 2, Broker 3
  Partition 1:
    - Leader: Broker 2
    - Replicas: Broker 1, Broker 3
```

**Benefits:**
- Fault tolerance: if broker dies, replicas available
- Availability: can read from in-sync replicas
- Durability: data persisted across servers

---

## Producers

### What Producers Do

Send messages to Kafka topics

### Producer Architecture

```
Application
    ↓
KafkaProducer
    ↓
Serializer (JSON → bytes)
    ↓
Partitioner (choose partition)
    ↓
Batch Accumulator (group messages)
    ↓
Network (send to broker)
    ↓
Broker (stores message)
    ↓
Response: offset of stored message
```

### Key Operations

**Send Message (Async):**
```python
from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Fire and forget
producer.send('listings', {'property_id': '123', 'price': 550000})
```

**Send with Callback:**
```python
def on_send_success(record_metadata):
    print(f"Message sent to {record_metadata.topic} partition {record_metadata.partition} at offset {record_metadata.offset}")

def on_send_error(exc):
    print(f"Error sending message: {exc}")

future = producer.send('listings', {'property_id': '123'})
future.add_callback(on_send_success)
future.add_errback(on_send_error)
```

**Send with Key (ensures ordering):**
```python
# All messages with same key go to same partition
producer.send('listings', 
    key=b'agent_567',  # Key must be bytes
    value={'action': 'listing_created'}
)
```

### Producer Configuration

```python
KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    
    # Serialization
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
    key_serializer=lambda k: k.encode('utf-8') if k else None,
    
    # Acknowledgments
    acks='all',  # Wait for all replicas (safe but slower)
    # acks=1    # Wait for leader only (faster, some risk)
    # acks=0    # No wait (fastest, risky)
    
    # Batching
    batch_size=16384,  # Bytes to batch
    linger_ms=10,      # Wait up to 10ms for batching
    
    # Retries
    retries=3,
    retry_backoff_ms=100,
    
    # Compression
    compression_type='snappy'  # or 'gzip', 'lz4'
)
```

---

## Consumers

### What Consumers Do

Read messages from Kafka topics

### Consumer Architecture

```
KafkaConsumer
    ↓
Subscribe to Topic(s)
    ↓
Join Consumer Group
    ↓
Fetch messages from assigned partitions
    ↓
Deserializer (bytes → JSON)
    ↓
Application processes message
    ↓
Commit offset (mark as processed)
```

### Key Operations

**Basic Consumer:**
```python
from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'listings',  # topic
    bootstrap_servers=['localhost:9092'],
    group_id='my-group',
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    auto_offset_reset='earliest'  # Start from beginning
)

for message in consumer:
    print(f"Received: {message.value}")
```

**Manual Offset Management:**
```python
consumer = KafkaConsumer(
    'listings',
    bootstrap_servers=['localhost:9092'],
    group_id='my-group',
    auto_commit_offset=False  # Manual control
)

for message in consumer:
    process(message)
    consumer.commit()  # Commit after processing
```

**Seek to Offset:**
```python
from kafka import TopicPartition

# Seek to specific offset
tp = TopicPartition('listings', partition=0)
consumer.assign([tp])
consumer.seek(tp, 100)  # Start from offset 100
```

### Consumer Configuration

```python
KafkaConsumer(
    'listings',
    bootstrap_servers=['localhost:9092'],
    
    # Consumer group
    group_id='my-group',
    
    # Offset management
    auto_offset_reset='earliest',  # or 'latest', 'none'
    enable_auto_commit=True,
    auto_commit_interval_ms=5000,
    
    # Deserialization
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    key_deserializer=lambda k: k.decode('utf-8') if k else None,
    
    # Fetching
    fetch_min_bytes=1,
    fetch_max_wait_ms=500,
    max_poll_records=500,
    
    # Session management
    session_timeout_ms=10000,
    heartbeat_interval_ms=3000
)
```

---

## Topics & Partitions

### Creating Topics

**Using kafka-python AdminClient:**
```python
from kafka.admin import KafkaAdminClient, NewTopic

admin_client = KafkaAdminClient(bootstrap_servers=['localhost:9092'])

topic_list = [
    NewTopic(
        name='listings',
        num_partitions=3,
        replication_factor=3
    ),
    NewTopic(
        name='views',
        num_partitions=3,
        replication_factor=3
    )
]

fs = admin_client.create_topics(new_topics=topic_list)

for topic, f in fs.items():
    try:
        f.result()  # Block until topic created
        print(f"Topic {topic} created")
    except Exception as e:
        print(f"Error creating {topic}: {e}")
```

### Viewing Topics

```python
from kafka import KafkaConsumer

consumer = KafkaConsumer(bootstrap_servers=['localhost:9092'])
topics = consumer.topics()
print(f"Topics: {topics}")

# Get partition info
partitions = consumer.partitions_for_topic('listings')
print(f"Partitions for listings: {partitions}")
```

### Partition Assignment Strategies

**RoundRobin** - Distribute partitions evenly
```
3 consumers, 3 partitions:
Consumer 0 → Partition 0
Consumer 1 → Partition 1
Consumer 2 → Partition 2
```

**Range** - Assign partitions by range
```
3 consumers, 6 partitions:
Consumer 0 → Partitions 0-1
Consumer 1 → Partitions 2-3
Consumer 2 → Partitions 4-5
```

**Sticky** - Minimize partition movement on rebalancing

---

## Consumer Groups

### What Are Consumer Groups?

Multiple consumers that work together to read from a topic

```
Topic: listings (3 partitions)
│
├─ Consumer Group 1: notifications
│  ├─ Consumer 1a → reads from Partition 0
│  ├─ Consumer 1b → reads from Partition 1
│  └─ Consumer 1c → reads from Partition 2
│
├─ Consumer Group 2: analytics
│  ├─ Consumer 2a → reads from Partition 0, 1
│  └─ Consumer 2b → reads from Partition 2
│
└─ Consumer Group 3: approval-system
   └─ Consumer 3a → reads from all Partitions (0, 1, 2)
```

### Benefits

**Scalability:** Add more consumers to process faster
**Parallel Processing:** Each consumer handles different partitions
**Load Balancing:** Kafka distributes work automatically

### Consumer Group Lifecycle

```
1. Consumer joins group
   ↓
2. Group coordinates (rebalancing)
   ↓
3. Each consumer assigned partitions
   ↓
4. Consumers read from assigned partitions
   ↓
5. Group tracks committed offsets
   ↓
6. Consumer fails → rebalance → new assignment
```

### Rebalancing

Triggered when:
- Consumer joins group
- Consumer leaves group
- Consumer timeout (heartbeat miss)
- Partition added to topic

During rebalancing:
- All consumers pause reading
- Kafka reassigns partitions
- Consumers resume from last committed offset

---

## Error Handling

### Producer Errors

**Retryable Errors** (Kafka automatically retries):
- BROKER_NOT_AVAILABLE
- REQUEST_TIMED_OUT
- NOT_COORDINATOR
- NETWORK_EXCEPTION

**Non-Retryable Errors** (application must handle):
- MESSAGE_TOO_LARGE
- INVALID_TOPIC_EXCEPTION
- AUTHORIZATION_FAILED

```python
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    retries=3,              # Retry up to 3 times
    retry_backoff_ms=100,   # Wait 100ms between retries
    request_timeout_ms=30000  # 30 second timeout
)

future = producer.send('listings', {'data': 'value'})
try:
    record_metadata = future.get(timeout=10)
except Exception as e:
    print(f"Error: {e}")
```

### Consumer Errors

**Session Timeout** - Consumer didn't send heartbeat
```python
# Consumer heartbeat every 3 seconds
# Dies if no heartbeat for 10 seconds
consumer = KafkaConsumer(
    'listings',
    heartbeat_interval_ms=3000,
    session_timeout_ms=10000
)
```

**Deserialization Error** - Cannot parse message
```python
def safe_deserializer(data):
    try:
        return json.loads(data.decode('utf-8'))
    except Exception as e:
        print(f"Deserialization failed: {e}")
        return None

consumer = KafkaConsumer(
    'listings',
    value_deserializer=safe_deserializer
)
```

---

## Python kafka-python Library

### Installation

```bash
pip install kafka-python
```

### Key Classes

**KafkaProducer** - Send messages
```python
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
```

**KafkaConsumer** - Receive messages
```python
from kafka import KafkaConsumer

consumer = KafkaConsumer('topic', bootstrap_servers=['localhost:9092'])
```

**KafkaAdminClient** - Manage topics
```python
from kafka.admin import KafkaAdminClient

admin = KafkaAdminClient(bootstrap_servers=['localhost:9092'])
```

**TopicPartition** - Reference specific partition
```python
from kafka import TopicPartition

tp = TopicPartition('listings', partition=0)
```

### Common Patterns

**Request-Reply Pattern:**
```python
# Producer
producer.send('requests', {'request_id': '123', 'action': 'validate'})

# Consumer processes and publishes to reply topic
for message in consumer:
    result = process(message.value)
    producer.send('replies', {'request_id': message.value['request_id'], 'result': result})
```

**Event Sourcing Pattern:**
```python
# All changes as events
producer.send('events', {'entity': 'property', 'id': '123', 'action': 'created'})
producer.send('events', {'entity': 'property', 'id': '123', 'action': 'price_updated'})
producer.send('events', {'entity': 'property', 'id': '123', 'action': 'sold'})
```

**Fan-Out Pattern:**
```python
# One producer sends to topic
producer.send('notifications', {'message': 'New listing'})

# Multiple consumer groups process independently
# Group 1: Email notifications
# Group 2: SMS notifications
# Group 3: Analytics
```

---

## Performance Tuning

### Producer Throughput

```python
producer = KafkaProducer(
    batch_size=32768,       # Larger batches
    linger_ms=100,          # Wait 100ms for batching
    compression_type='snappy',  # Compress data
    acks=1                  # Only wait for leader
)
```

### Consumer Throughput

```python
consumer = KafkaConsumer(
    fetch_min_bytes=1024*10,  # 10KB minimum
    fetch_max_wait_ms=500,    # Wait 500ms
    max_poll_records=1000     # Pull more records
)
```

### Network Optimization

```python
producer = KafkaProducer(
    connections_max_idle_ms=540000,  # Keep connections open
    socket_keepalive_enabled=True,
    buffer_memory=67108864  # 64MB buffer
)
```

---

## Monitoring & Debugging

### Check Broker Health

```python
from kafka import KafkaConsumer

consumer = KafkaConsumer(bootstrap_servers=['localhost:9092'])
brokers = consumer._client.cluster.brokers()
print(f"Connected brokers: {brokers}")
```

### Monitor Consumer Lag

```python
# Get current offset
consumer.assignment()  # Assigned partitions
consumer.position(tp)  # Current offset

# Get end offset (latest)
consumer.end_offsets([tp])

# Lag = end_offset - current_offset
lag = consumer.end_offsets([tp])[tp] - consumer.position(tp)
print(f"Consumer lag: {lag} messages")
```

### View Topic Metrics

```bash
# Using Kafka CLI
kafka-consumer-groups.sh --describe \
  --group my-group \
  --bootstrap-server localhost:9092
```

---

## Common Use Cases

**Event Streaming:** Real-time events (clicks, purchases, logins)  
**Microservice Communication:** Inter-service messaging  
**Data Pipelines:** ETL and real-time analytics  
**Activity Tracking:** User activity and behavior  
**Metrics & Monitoring:** System metrics and logs  
**Database Replication:** CDC (Change Data Capture)  

---

## Best Practices

✅ **Always use keys** - Ensures message ordering within partition  
✅ **Set replication factor to 3** - For production  
✅ **Monitor consumer lag** - Detect processing issues  
✅ **Handle errors gracefully** - Retry with backoff  
✅ **Use consumer groups** - For parallel processing  
✅ **Compress messages** - Reduce network load  
✅ **Set appropriate timeouts** - Avoid hanging consumers  
✅ **Test partitioning strategy** - Ensure even distribution  

---

## Troubleshooting

**"BrokerNotAvailable"**
- Check if Kafka is running
- Verify bootstrap_servers configuration
- Check firewall/network access

**"Group Coordinator Not Available"**
- Wait for cluster to stabilize
- Check Zookeeper status
- Verify broker configuration

**"Message too large"**
- Increase `max.message.bytes` on broker
- Compress messages
- Split large messages

**Consumer not receiving messages**
- Check auto_offset_reset setting
- Verify topic exists and has data
- Check consumer group ID
- Monitor consumer lag

---

This reference covers all major Kafka concepts needed for the lab!

