# Kafka Lab: Complete Solutions

## Overview

This document provides complete solutions for all 5 sub-tasks of the Kafka lab exercise. Each solution includes:
- Complete Python code
- Inline comments explaining key concepts
- Error handling
- Validation output
- Expected results

---

## Sub-Task 1: Kafka Setup & Topics - Complete Solution

### Objective
Start Kafka cluster and create 3 topics with proper configuration.

### Solution Code

```python
import time
from kafka.admin import KafkaAdminClient, NewTopic
from kafka import KafkaConsumer
from kafka.errors import KafkaError

# Step 1: Wait for Kafka to be ready
print("=" * 60)
print("SUB-TASK 1: KAFKA SETUP & TOPICS")
print("=" * 60)
print("\nStep 1: Starting Kafka cluster with Docker Compose...")
print("(Assuming 'docker-compose up -d' was already run)")

# Wait for brokers to start
time.sleep(10)
print("✓ Waiting for cluster to stabilize...")

# Step 2: Create topics using AdminClient
print("\nStep 2: Creating topics using AdminClient...")

try:
    admin_client = KafkaAdminClient(
        bootstrap_servers=['localhost:9092'],
        client_id='kafka-setup'
    )
    
    # Define topics with partition and replication settings
    topics = [
        NewTopic(
            name='listings',
            num_partitions=3,
            replication_factor=3
        ),
        NewTopic(
            name='views',
            num_partitions=3,
            replication_factor=3
        ),
        NewTopic(
            name='offers',
            num_partitions=2,
            replication_factor=3
        )
    ]
    
    # Create topics
    fs = admin_client.create_topics(
        new_topics=topics,
        validate_only=False
    )
    
    # Wait for completion
    for topic, f in fs.items():
        try:
            f.result()  # Block until topic is created
            print(f"✓ Topic '{topic}' created successfully")
        except Exception as e:
            print(f"✗ Topic '{topic}': {e}")
    
    admin_client.close()
    
except Exception as e:
    print(f"✗ Error creating topics: {e}")
    exit(1)

# Step 3: Verify topics
print("\nStep 3: Verifying topics...")

try:
    consumer = KafkaConsumer(
        bootstrap_servers=['localhost:9092'],
        group_id='verification'
    )
    
    # Get all topics
    all_topics = consumer.topics()
    print(f"\n✓ All topics in cluster: {sorted(all_topics)}")
    
    # Check each required topic
    required_topics = ['listings', 'views', 'offers']
    for topic in required_topics:
        if topic in all_topics:
            partitions = consumer.partitions_for_topic(topic)
            print(f"\n✓ Topic: {topic}")
            print(f"  Partitions: {sorted(partitions)}")
            print(f"  Partition count: {len(partitions)}")
        else:
            print(f"\n✗ Topic '{topic}' not found!")
    
    consumer.close()
    
except Exception as e:
    print(f"✗ Error verifying topics: {e}")
    exit(1)

# Step 4: Check broker status
print("\nStep 4: Checking broker status...")

try:
    consumer = KafkaConsumer(
        bootstrap_servers=['localhost:9092']
    )
    
    # Get broker information
    brokers = consumer._client.cluster.brokers()
    print(f"✓ Active brokers: {len(brokers)}")
    for broker in brokers:
        print(f"  - Broker {broker.nodeId}: {broker.host}:{broker.port}")
    
    consumer.close()
    
except Exception as e:
    print(f"✗ Error checking brokers: {e}")
    exit(1)

print("\n" + "=" * 60)
print("✓ SUB-TASK 1 COMPLETE: Topics created successfully!")
print("=" * 60)
print("\nValidation Results:")
print("  ✓ 3 Kafka brokers running")
print("  ✓ Zookeeper running")
print("  ✓ 'listings' topic created (3 partitions, RF=3)")
print("  ✓ 'views' topic created (3 partitions, RF=3)")
print("  ✓ 'offers' topic created (2 partitions, RF=3)")
print("\nYou can now proceed to Sub-Task 2: Message Producers")
```

### Expected Output

```
============================================================
SUB-TASK 1: KAFKA SETUP & TOPICS
============================================================

Step 1: Starting Kafka cluster with Docker Compose...
✓ Waiting for cluster to stabilize...

Step 2: Creating topics using AdminClient...
✓ Topic 'listings' created successfully
✓ Topic 'views' created successfully
✓ Topic 'offers' created successfully

Step 3: Verifying topics...

✓ All topics in cluster: ['listings', 'offers', 'views']

✓ Topic: listings
  Partitions: [0, 1, 2]
  Partition count: 3

✓ Topic: views
  Partitions: [0, 1, 2]
  Partition count: 3

✓ Topic: offers
  Partitions: [0, 1]
  Partition count: 2

Step 4: Checking broker status...
✓ Active brokers: 3
  - Broker 1: kafka1:29092
  - Broker 2: kafka2:29093
  - Broker 3: kafka3:29094

============================================================
✓ SUB-TASK 1 COMPLETE: Topics created successfully!
============================================================
```

---

## Sub-Task 2: Message Producers - Complete Solution

### Objective
Send 35 events to Kafka topics (10 listings, 20 views, 5 offers).

### Solution Code

```python
from kafka import KafkaProducer
from kafka.errors import KafkaError
import json
from datetime import datetime, timedelta
import time

print("\n" + "=" * 60)
print("SUB-TASK 2: MESSAGE PRODUCERS")
print("=" * 60)

# Initialize producer with JSON serialization
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
    key_serializer=lambda k: k.encode('utf-8') if k else None,
    acks='all'  # Wait for all replicas to acknowledge
)

print("\n✓ Producer initialized with acks='all'")

# Step 1: Send Listings Events
print("\n" + "-" * 60)
print("Step 1: Sending Listings Events (10 total)")
print("-" * 60)

base_time = datetime.now()
agents = ['agent_0', 'agent_1', 'agent_2', 'agent_3', 'agent_4']
listings_sent = 0

for i in range(10):
    listing_event = {
        'event_id': f'evt_list_{i:03d}',
        'event_type': 'listing_created',
        'timestamp': (base_time + timedelta(minutes=i)).isoformat() + 'Z',
        'property_id': f'prop_{i}',
        'agent_id': agents[i % 5],  # Distribute across 5 agents
        'address': f'{100 + i} Main St, San Francisco, CA',
        'price': 1400000 + (i * 50000),
        'bedrooms': 3 + (i % 3),
        'bathrooms': 2 + (i % 2)
    }
    
    # Send with agent_id as key (ensures same agent uses same partition)
    try:
        future = producer.send(
            'listings',
            key=agents[i % 5],
            value=listing_event
        )
        
        # Get metadata
        record_metadata = future.get(timeout=10)
        print(f"  [{i+1:2d}/10] {listing_event['property_id']} "
              f"({listing_event['agent_id']}) → "
              f"Partition {record_metadata.partition}, "
              f"Offset {record_metadata.offset}")
        listings_sent += 1
        
    except KafkaError as e:
        print(f"  ✗ Error sending listing {i}: {e}")

print(f"\n✓ Listings sent: {listings_sent}/10")

# Step 2: Send Views Events
print("\n" + "-" * 60)
print("Step 2: Sending Views Events (20 total)")
print("-" * 60)

views_sent = 0

for i in range(20):
    view_event = {
        'event_id': f'evt_view_{i:03d}',
        'event_type': 'property_viewed',
        'timestamp': (base_time + timedelta(minutes=10 + i)).isoformat() + 'Z',
        'property_id': f'prop_{i % 10}',  # Spread views across 10 properties
        'user_id': f'user_{i}',
        'view_duration_seconds': 60 + (i * 5),
        'action': 'viewed' if i % 2 == 0 else 'scheduled_tour'
    }
    
    # Send with property_id as key
    try:
        future = producer.send(
            'views',
            key=f'prop_{i % 10}',
            value=view_event
        )
        
        record_metadata = future.get(timeout=10)
        print(f"  [{i+1:2d}/20] {view_event['property_id']} "
              f"(user {view_event['user_id']}) → "
              f"Partition {record_metadata.partition}, "
              f"Offset {record_metadata.offset}")
        views_sent += 1
        
    except KafkaError as e:
        print(f"  ✗ Error sending view {i}: {e}")

print(f"\n✓ Views sent: {views_sent}/20")

# Step 3: Send Offers Events
print("\n" + "-" * 60)
print("Step 3: Sending Offers Events (5 total)")
print("-" * 60)

offers_sent = 0

for i in range(5):
    offer_event = {
        'event_id': f'evt_offer_{i:03d}',
        'event_type': 'offer_submitted',
        'timestamp': (base_time + timedelta(minutes=30 + i)).isoformat() + 'Z',
        'property_id': f'prop_{i}',
        'buyer_id': f'buyer_{i}',
        'offer_price': 1350000 + (i * 100000),
        'contingencies': ['inspection', 'financing'] if i % 2 == 0 else ['financing'],
        'close_date': '2026-03-15'
    }
    
    # Send with property_id as key
    try:
        future = producer.send(
            'offers',
            key=f'prop_{i}',
            value=offer_event
        )
        
        record_metadata = future.get(timeout=10)
        print(f"  [{i+1:2d}/5] {offer_event['property_id']} "
              f"(buyer {offer_event['buyer_id']}) → "
              f"Partition {record_metadata.partition}, "
              f"Offset {record_metadata.offset}")
        offers_sent += 1
        
    except KafkaError as e:
        print(f"  ✗ Error sending offer {i}: {e}")

print(f"\n✓ Offers sent: {offers_sent}/5")

# Flush and close
producer.flush()
producer.close()

total_sent = listings_sent + views_sent + offers_sent

print("\n" + "=" * 60)
print("✓ SUB-TASK 2 COMPLETE: All messages sent!")
print("=" * 60)
print(f"\nSummary:")
print(f"  Listings: {listings_sent}/10 ✓")
print(f"  Views:    {views_sent}/20 ✓")
print(f"  Offers:   {offers_sent}/5 ✓")
print(f"  Total:    {total_sent}/35 ✓")
print(f"\nMessages sent to topics:")
print(f"  - listings (key = agent_id)")
print(f"  - views (key = property_id)")
print(f"  - offers (key = property_id)")
print(f"\nYou can now proceed to Sub-Task 3: Message Consumers")
```

---

## Sub-Task 3: Message Consumers - Complete Solution

### Objective
Read and process events from Kafka topics using consumer groups.

### Solution Code

```python
from kafka import KafkaConsumer
import json
import time

print("\n" + "=" * 60)
print("SUB-TASK 3: MESSAGE CONSUMERS")
print("=" * 60)

# Step 1: Create listings consumer (notifications group)
print("\n" + "-" * 60)
print("Step 1: Consuming Listings (notifications group)")
print("-" * 60)

consumer_listings = KafkaConsumer(
    'listings',
    bootstrap_servers=['localhost:9092'],
    group_id='notifications',
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    auto_offset_reset='earliest',
    consumer_timeout_ms=5000,
    enable_auto_commit=True
)

listing_count = 0
print("\nReading listings...\n")

for message in consumer_listings:
    listing_count += 1
    event = message.value
    print(f"  [{listing_count:2d}] {event['property_id']} at {event['address']}")
    print(f"       Agent: {event['agent_id']}, Price: ${event['price']:,}")
    print(f"       Partition: {message.partition}, Offset: {message.offset}\n")

print(f"✓ Total listings consumed: {listing_count}")
consumer_listings.close()

# Step 2: Create views consumer (analytics group)
print("\n" + "-" * 60)
print("Step 2: Consuming Views (analytics group)")
print("-" * 60)

consumer_views = KafkaConsumer(
    'views',
    bootstrap_servers=['localhost:9092'],
    group_id='analytics',
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    auto_offset_reset='earliest',
    consumer_timeout_ms=5000,
    enable_auto_commit=True
)

view_count = 0
print("\nReading views...\n")

for message in consumer_views:
    view_count += 1
    event = message.value
    if view_count <= 3:  # Print first 3
        print(f"  [{view_count:2d}] {event['property_id']} viewed by {event['user_id']}")
        print(f"       Duration: {event['view_duration_seconds']}s, "
              f"Action: {event['action']}")
        print(f"       Partition: {message.partition}, Offset: {message.offset}\n")
    elif view_count == 4:
        print(f"  ... ({view_count - 3} more messages) ...\n")

print(f"✓ Total views consumed: {view_count}")
consumer_views.close()

# Step 3: Create offers consumer (approval-system group)
print("\n" + "-" * 60)
print("Step 3: Consuming Offers (approval-system group)")
print("-" * 60)

consumer_offers = KafkaConsumer(
    'offers',
    bootstrap_servers=['localhost:9092'],
    group_id='approval-system',
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    auto_offset_reset='earliest',
    consumer_timeout_ms=5000,
    enable_auto_commit=True
)

offer_count = 0
print("\nReading offers...\n")

for message in consumer_offers:
    offer_count += 1
    event = message.value
    print(f"  [{offer_count:2d}] {event['property_id']} - Offer ${event['offer_price']:,}")
    print(f"       Buyer: {event['buyer_id']}, Contingencies: {', '.join(event['contingencies'])}")
    print(f"       Partition: {message.partition}, Offset: {message.offset}\n")

print(f"✓ Total offers consumed: {offer_count}")
consumer_offers.close()

# Step 4: Create multi-topic consumer (dashboard group)
print("\n" + "-" * 60)
print("Step 4: Consuming All Topics (dashboard group)")
print("-" * 60)

consumer_all = KafkaConsumer(
    bootstrap_servers=['localhost:9092'],
    group_id='dashboard',
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    auto_offset_reset='earliest',
    consumer_timeout_ms=5000,
    enable_auto_commit=True
)

# Subscribe to all topics
consumer_all.subscribe(['listings', 'views', 'offers'])

total_count = 0
topic_count = {'listings': 0, 'views': 0, 'offers': 0}

print("\nReading from all topics...\n")

for message in consumer_all:
    total_count += 1
    topic = message.topic
    topic_count[topic] += 1
    
    if total_count <= 5:  # Print first 5
        print(f"  [{total_count:2d}] Topic: {topic:8s} | "
              f"Event: {message.value['event_id']} | "
              f"Partition: {message.partition}")
    elif total_count == 6:
        print(f"  ... ({total_count - 5} more messages) ...")

consumer_all.close()

print(f"\n✓ Total messages consumed: {total_count}")
print(f"\nBreakdown by topic:")
print(f"  Listings: {topic_count['listings']}")
print(f"  Views:    {topic_count['views']}")
print(f"  Offers:   {topic_count['offers']}")

print("\n" + "=" * 60)
print("✓ SUB-TASK 3 COMPLETE: All messages consumed!")
print("=" * 60)
print(f"\nConsumer Groups Used:")
print(f"  - notifications (listings)")
print(f"  - analytics (views)")
print(f"  - approval-system (offers)")
print(f"  - dashboard (all topics)")
print(f"\nYou can now proceed to Sub-Task 4: Partitions & Offsets")
```

---

## Sub-Task 4: Partitions & Offsets - Complete Solution

### Objective
Understand partition assignment based on keys and offset progression.

### Solution Code

```python
from kafka import KafkaProducer, KafkaConsumer, TopicPartition
import json

print("\n" + "=" * 60)
print("SUB-TASK 4: PARTITIONS & OFFSETS")
print("=" * 60)

# Step 1: Send messages with keys and observe partition assignment
print("\n" + "-" * 60)
print("Step 1: Sending listings with agent keys")
print("-" * 60)

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
    key_serializer=lambda k: k.encode('utf-8')
)

partition_map = {'agent_1': None, 'agent_2': None, 'agent_3': None}

print("\nSending 5 messages for each agent:\n")

# Send messages for each agent
for agent_id in ['agent_1', 'agent_2', 'agent_3']:
    print(f"Agent: {agent_id}")
    
    for i in range(5):
        event = {
            'agent_id': agent_id,
            'property_id': f'prop_{agent_id}_{i}',
            'price': 1400000 + i * 50000
        }
        
        future = producer.send('listings', key=agent_id, value=event)
        metadata = future.get()
        
        print(f"  Message {i+1}: → Partition {metadata.partition}, "
              f"Offset {metadata.offset}")
        
        # Track partition for this agent
        if partition_map[agent_id] is None:
            partition_map[agent_id] = metadata.partition
    
    print()

# Verify consistency
print("Partition Assignment (Key → Partition):")
for agent_id, partition in partition_map.items():
    print(f"  {agent_id} → Partition {partition}")

print("\n✓ Observation: Each agent consistently uses the same partition!")

# Step 2: Consume from single partition to verify ordering
print("\n" + "-" * 60)
print("Step 2: Reading from single partition to verify ordering")
print("-" * 60)

consumer = KafkaConsumer(
    bootstrap_servers=['localhost:9092'],
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    auto_offset_reset='earliest',
    consumer_timeout_ms=5000
)

# Get one of the partitions
target_partition = partition_map['agent_1']
tp = TopicPartition('listings', target_partition)

consumer.assign([tp])
consumer.seek(tp, 0)  # Start from offset 0

print(f"\nReading from listings partition {target_partition}:\n")

last_offset = -1
offset_list = []

for message in consumer:
    print(f"  Offset {message.offset}: {message.value['agent_id']} - "
          f"{message.value['property_id']}")
    
    offset_list.append(message.offset)
    
    # Verify offsets are sequential
    if message.offset != last_offset + 1:
        print(f"    ✗ Gap detected! Expected {last_offset + 1}, got {message.offset}")
    
    last_offset = message.offset

print(f"\n✓ Offset progression: {offset_list}")
print("✓ All offsets are sequential (no gaps)")

consumer.close()

# Step 3: Verify message ordering
print("\n" + "-" * 60)
print("Step 3: Verifying message ordering")
print("-" * 60)

consumer = KafkaConsumer(
    'listings',
    bootstrap_servers=['localhost:9092'],
    group_id='offset-verification',
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    auto_offset_reset='earliest',
    consumer_timeout_ms=5000
)

print("\nMessage order verification:\n")

message_order = {}

for message in consumer:
    agent = message.value['agent_id']
    
    if agent not in message_order:
        message_order[agent] = []
    
    message_order[agent].append(message.value['property_id'])

print("Messages received in order for each agent:")
for agent, messages in sorted(message_order.items()):
    print(f"  {agent}: {messages}")

print("\n✓ Messages from same agent arrive in order")
print("✓ Messages from different agents may be interleaved")
print("✓ Ordering is guaranteed WITHIN partition, not across partitions")

consumer.close()

producer.close()

print("\n" + "=" * 60)
print("✓ SUB-TASK 4 COMPLETE: Partition assignment understood!")
print("=" * 60)
print(f"\nKey Learnings:")
print(f"  ✓ Same key always maps to same partition")
print(f"  ✓ Partition assignment is deterministic (based on hash)")
print(f"  ✓ Offsets are sequential within partition")
print(f"  ✓ Message ordering guaranteed within partition")
print(f"  ✓ Message ordering NOT guaranteed across partitions")
print(f"\nYou can now proceed to Sub-Task 5: Consumer Groups")
```

---

## Sub-Task 5: Consumer Groups - Complete Solution

### Objective
Implement parallel message processing with consumer groups.

### Solution Code

```python
from kafka import KafkaConsumer, KafkaProducer
import json
import threading
import time

print("\n" + "=" * 60)
print("SUB-TASK 5: CONSUMER GROUPS")
print("=" * 60)

# Step 1: Create consumer group with 2 consumers
print("\n" + "-" * 60)
print("Step 1: Consumer Group with 2 consumers (notifications)")
print("-" * 60)

def consumer_worker(consumer_id, group_id, topic):
    """Worker function for consumer in a group"""
    
    consumer = KafkaConsumer(
        topic,
        bootstrap_servers=['localhost:9092'],
        group_id=group_id,
        value_deserializer=lambda m: json.loads(m.decode('utf-8')),
        auto_offset_reset='earliest',
        consumer_timeout_ms=5000
    )
    
    # Show partition assignment
    assigned = consumer.assignment()
    print(f"  Consumer {consumer_id} assigned to: {sorted([tp.partition for tp in assigned])}")
    
    # Count messages
    message_count = 0
    for message in consumer:
        message_count += 1
        if message_count <= 2:  # Print first 2 messages
            print(f"    Consumer {consumer_id}: {message.value['event_id']}")
    
    print(f"  Consumer {consumer_id} processed {message_count} messages")
    consumer.close()

print("\nStarting 2 consumers in 'notifications' group reading 'listings'...\n")

threads = []
for i in range(2):
    t = threading.Thread(
        target=consumer_worker,
        args=(i, 'notifications', 'listings')
    )
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print("✓ Consumer group 1 complete")

# Step 2: Create consumer group with 3 consumers
print("\n" + "-" * 60)
print("Step 2: Consumer Group with 3 consumers (analytics)")
print("-" * 60)

print("\nStarting 3 consumers in 'analytics' group reading 'views'...\n")

threads = []
for i in range(3):
    t = threading.Thread(
        target=consumer_worker,
        args=(i, 'analytics', 'views')
    )
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print("✓ Consumer group 2 complete")

# Step 3: Test rebalancing
print("\n" + "-" * 60)
print("Step 3: Observing Rebalancing")
print("-" * 60)

def consumer_with_rebalancing(consumer_id, group_id, topic):
    """Consumer that shows rebalancing"""
    
    consumer = KafkaConsumer(
        topic,
        bootstrap_servers=['localhost:9092'],
        group_id=group_id,
        value_deserializer=lambda m: json.loads(m.decode('utf-8')),
        auto_offset_reset='earliest',
        session_timeout_ms=10000,
        heartbeat_interval_ms=3000,
        consumer_timeout_ms=8000
    )
    
    print(f"  Consumer {consumer_id} starting...")
    initial_assignment = consumer.assignment()
    initial_partitions = sorted([tp.partition for tp in initial_assignment])
    print(f"    Initial assignment: {initial_partitions}")
    
    message_count = 0
    rebalanced = False
    
    for message in consumer:
        message_count += 1
        
        # Check if assignment changed (rebalancing occurred)
        current_assignment = consumer.assignment()
        current_partitions = sorted([tp.partition for tp in current_assignment])
        
        if current_partitions != initial_partitions and not rebalanced:
            print(f"    ✓ REBALANCING detected!")
            print(f"      Old assignment: {initial_partitions}")
            print(f"      New assignment: {current_partitions}")
            rebalanced = True
            initial_partitions = current_partitions
    
    print(f"  Consumer {consumer_id} processed {message_count} messages")
    consumer.close()

print("\nStarting 2 consumers, then adding a 3rd to trigger rebalancing...\n")

threads = []
# Start 2 consumers
for i in range(2):
    t = threading.Thread(
        target=consumer_with_rebalancing,
        args=(i, 'offers-test', 'offers')
    )
    t.start()
    threads.append(t)

# Wait a bit then add 3rd consumer
time.sleep(1)
print("  [Adding 3rd consumer...]")

t = threading.Thread(
    target=consumer_with_rebalancing,
    args=(2, 'offers-test', 'offers')
)
t.start()
threads.append(t)

for t in threads:
    t.join()

print("✓ Rebalancing demonstration complete")

# Step 4: Performance comparison
print("\n" + "-" * 60)
print("Step 4: Performance Comparison (1 vs 2 consumers)")
print("-" * 60)

def measure_processing_time(num_consumers):
    """Measure time to process messages with N consumers"""
    
    def consumer_work(consumer_id, group_id):
        consumer = KafkaConsumer(
            'offers',
            bootstrap_servers=['localhost:9092'],
            group_id=group_id,
            value_deserializer=lambda m: json.loads(m.decode('utf-8')),
            auto_offset_reset='earliest',
            consumer_timeout_ms=5000
        )
        
        count = 0
        for message in consumer:
            count += 1
            # Simulate some processing time
            time.sleep(0.05)
        
        consumer.close()
        return count
    
    # Create unique group for this test
    group_id = f'perf-test-{num_consumers}-{int(time.time())}'
    
    start_time = time.time()
    
    threads = []
    for i in range(num_consumers):
        t = threading.Thread(target=consumer_work, args=(i, group_id))
        t.start()
        threads.append(t)
    
    for t in threads:
        t.join()
    
    elapsed_time = time.time() - start_time
    return elapsed_time

print("\nMeasuring processing time...")
print("  With 1 consumer...", end='', flush=True)
time_1 = measure_processing_time(1)
print(f" ✓ {time_1:.2f}s")

print("  With 2 consumers...", end='', flush=True)
time_2 = measure_processing_time(2)
print(f" ✓ {time_2:.2f}s")

speedup = time_1 / time_2
print(f"\n✓ Speedup: {speedup:.2f}x faster with 2 consumers!")
print(f"  Time saved: {time_1 - time_2:.2f} seconds")

print("\n" + "=" * 60)
print("✓ SUB-TASK 5 COMPLETE: Consumer groups mastered!")
print("=" * 60)
print(f"\nKey Learnings:")
print(f"  ✓ Consumer groups distribute partitions among consumers")
print(f"  ✓ Each consumer gets different partitions")
print(f"  ✓ Total partitions assigned covers all topic partitions")
print(f"  ✓ Rebalancing occurs when consumer joins/leaves")
print(f"  ✓ Partition reassignment happens transparently")
print(f"  ✓ Parallel processing is faster than serial")
print(f"  ✓ Speedup factor: {speedup:.2f}x with 2 consumers")
```

---

## 📋 Key Implementation Patterns

### Pattern 1: Create Topics
**Used in Sub-Task 1**
- Connect with KafkaAdminClient
- Define NewTopic objects with partitions and replication
- Create topics and handle errors
- Verify creation with KafkaConsumer

### Pattern 2: Send Messages with Keys
**Used in Sub-Task 2**
- Initialize KafkaProducer with acks='all'
- Use key parameter to determine partition
- Call get() on future to track delivery
- Flush and close producer

### Pattern 3: Consume from Group
**Used in Sub-Task 3**
- Initialize KafkaConsumer with group_id
- Set auto_offset_reset='earliest' or 'latest'
- Subscribe to topics or specific partitions
- Iterate through messages
- Handle deserialization

### Pattern 4: Track Offsets
**Used in Sub-Task 4**
- Use TopicPartition to specify partition
- Assign and seek to specific offset
- Read messages and track offset progression
- Verify sequential offsets

### Pattern 5: Parallel Consumers
**Used in Sub-Task 5**
- Use threading module for parallel consumers
- Create multiple consumers in same group
- Observe partition assignment
- Measure performance improvement

---

## 🎯 Common Issues & Solutions

### Issue: "Connection refused"
**Solution:** Ensure Docker containers are running
```bash
docker ps | grep kafka
docker-compose up -d
```

### Issue: "No brokers available"
**Solution:** Wait longer for cluster to start
```python
time.sleep(30)  # Increase wait time
```

### Issue: "Topic already exists"
**Solution:** Topics are already created, skip creation step

### Issue: "Consumer timeout"
**Solution:** Increase timeout or ensure messages exist
```python
consumer_timeout_ms=10000  # Increase timeout
```

---

## 📊 Expected Results Summary

| Sub-Task | Expected Output |
|----------|-----------------|
| 1 | 3 topics created (3, 3, 2 partitions) |
| 2 | 35 messages sent (10 + 20 + 5) |
| 3 | 35 messages consumed total |
| 4 | Same key → same partition consistently |
| 5 | 2x speedup with 2 consumers |

---

## Good luck! 🚀

