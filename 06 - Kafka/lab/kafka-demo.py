#!/usr/bin/env python3
"""
Kafka Lab - Complete End-to-End Demo
=====================================

This demo showcases a complete real estate event streaming system using Kafka.
It demonstrates all key concepts from the lab in a single runnable example.

Features:
- Creates topics with proper configuration
- Produces events with key-based partitioning
- Consumes events using consumer groups
- Demonstrates partition ordering guarantees
- Shows parallel processing with multiple consumers

Usage:
    python demo.py

Requirements:
    pip install kafka-python

Prerequisites:
    - Docker and Docker Compose installed
    - Kafka cluster running (docker-compose up -d)
"""

import json
import time
import threading
from datetime import datetime, timedelta
from kafka import KafkaProducer, KafkaConsumer, TopicPartition
from kafka.admin import KafkaAdminClient, NewTopic
from kafka.errors import KafkaError, TopicAlreadyExistsError


# =============================================================================
# Configuration
# =============================================================================

BOOTSTRAP_SERVERS = ['localhost:9092']
TOPICS_CONFIG = {
    'listings': {'partitions': 3, 'replication': 3},
    'views': {'partitions': 3, 'replication': 3},
    'offers': {'partitions': 2, 'replication': 3}
}


# =============================================================================
# Helper Functions
# =============================================================================

def print_section(title):
    """Print a formatted section header"""
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70 + "\n")


def print_step(step_num, description):
    """Print a formatted step header"""
    print(f"\n{'─' * 70}")
    print(f"Step {step_num}: {description}")
    print('─' * 70 + "\n")


# =============================================================================
# Phase 1: Cluster Setup and Topic Creation
# =============================================================================

def setup_cluster():
    """Create Kafka topics with proper configuration"""
    print_section("PHASE 1: CLUSTER SETUP")
    
    print("Connecting to Kafka cluster...")
    try:
        admin_client = KafkaAdminClient(
            bootstrap_servers=BOOTSTRAP_SERVERS,
            client_id='demo-admin'
        )
        print("✓ Connected to Kafka cluster\n")
    except Exception as e:
        print(f"✗ Failed to connect: {e}")
        print("\nMake sure Kafka is running:")
        print("  docker-compose up -d")
        exit(1)
    
    # Create topics
    print("Creating topics...")
    topics = []
    for topic_name, config in TOPICS_CONFIG.items():
        topics.append(NewTopic(
            name=topic_name,
            num_partitions=config['partitions'],
            replication_factor=config['replication']
        ))
    
    try:
        admin_client.create_topics(new_topics=topics, validate_only=False)
        print("✓ Topics created successfully")
    except TopicAlreadyExistsError:
        print("✓ Topics already exist (skipping creation)")
    except Exception as e:
        print(f"✗ Error creating topics: {e}")
        admin_client.close()
        exit(1)
    
    # Verify topics
    print("\nVerifying topics...")
    consumer = KafkaConsumer(bootstrap_servers=BOOTSTRAP_SERVERS)
    all_topics = consumer.topics()
    
    for topic_name in TOPICS_CONFIG.keys():
        if topic_name in all_topics:
            partitions = consumer.partitions_for_topic(topic_name)
            print(f"  ✓ {topic_name:12s} - {len(partitions)} partitions")
        else:
            print(f"  ✗ {topic_name} not found!")
    
    consumer.close()
    admin_client.close()
    
    # Wait for topics to be ready
    print("\nWaiting for topics to be ready...")
    time.sleep(2)
    print("✓ Cluster setup complete!\n")


# =============================================================================
# Phase 2: Event Production
# =============================================================================

def produce_events():
    """Produce real estate events to Kafka topics"""
    print_section("PHASE 2: EVENT PRODUCTION")
    
    # Initialize producer
    producer = KafkaProducer(
        bootstrap_servers=BOOTSTRAP_SERVERS,
        value_serializer=lambda v: json.dumps(v).encode('utf-8'),
        key_serializer=lambda k: k.encode('utf-8') if k else None,
        acks='all'
    )
    
    print("✓ Producer initialized (acks='all')\n")
    
    base_time = datetime.now()
    stats = {'listings': 0, 'views': 0, 'offers': 0}
    
    # Step 1: Produce Listing Events
    print_step(1, "Producing Listing Events")
    
    agents = ['agent_0', 'agent_1', 'agent_2', 'agent_3', 'agent_4']
    
    for i in range(10):
        event = {
            'event_id': f'evt_list_{i:03d}',
            'event_type': 'listing_created',
            'timestamp': (base_time + timedelta(minutes=i)).isoformat() + 'Z',
            'property_id': f'prop_{i}',
            'agent_id': agents[i % 5],
            'address': f'{100 + i} Main St, San Francisco, CA',
            'price': 1400000 + (i * 50000),
            'bedrooms': 3 + (i % 3),
            'bathrooms': 2 + (i % 2)
        }
        
        try:
            future = producer.send('listings', key=agents[i % 5], value=event)
            metadata = future.get(timeout=10)
            stats['listings'] += 1
            
            if i < 3:  # Print first 3
                print(f"  [{i+1:2d}/10] {event['property_id']} "
                      f"({event['agent_id']}) → "
                      f"Partition {metadata.partition}")
        except KafkaError as e:
            print(f"  ✗ Error: {e}")
    
    if stats['listings'] > 3:
        print(f"  ... and {stats['listings'] - 3} more listings")
    print(f"\n✓ Sent {stats['listings']}/10 listings")
    
    # Step 2: Produce View Events
    print_step(2, "Producing View Events")
    
    for i in range(20):
        event = {
            'event_id': f'evt_view_{i:03d}',
            'event_type': 'property_viewed',
            'timestamp': (base_time + timedelta(minutes=10 + i)).isoformat() + 'Z',
            'property_id': f'prop_{i % 10}',
            'user_id': f'user_{i}',
            'view_duration_seconds': 60 + (i * 5),
            'action': 'viewed' if i % 2 == 0 else 'scheduled_tour'
        }
        
        try:
            future = producer.send('views', key=f'prop_{i % 10}', value=event)
            metadata = future.get(timeout=10)
            stats['views'] += 1
            
            if i < 3:
                print(f"  [{i+1:2d}/20] {event['property_id']} "
                      f"(user {event['user_id']}) → "
                      f"Partition {metadata.partition}")
        except KafkaError as e:
            print(f"  ✗ Error: {e}")
    
    if stats['views'] > 3:
        print(f"  ... and {stats['views'] - 3} more views")
    print(f"\n✓ Sent {stats['views']}/20 views")
    
    # Step 3: Produce Offer Events
    print_step(3, "Producing Offer Events")
    
    for i in range(5):
        event = {
            'event_id': f'evt_offer_{i:03d}',
            'event_type': 'offer_submitted',
            'timestamp': (base_time + timedelta(minutes=30 + i)).isoformat() + 'Z',
            'property_id': f'prop_{i}',
            'buyer_id': f'buyer_{i}',
            'offer_price': 1350000 + (i * 100000),
            'contingencies': ['inspection', 'financing'] if i % 2 == 0 else ['financing'],
            'close_date': '2026-03-15'
        }
        
        try:
            future = producer.send('offers', key=f'prop_{i}', value=event)
            metadata = future.get(timeout=10)
            stats['offers'] += 1
            print(f"  [{i+1:2d}/5] {event['property_id']} "
                  f"(buyer {event['buyer_id']}) → "
                  f"Partition {metadata.partition}")
        except KafkaError as e:
            print(f"  ✗ Error: {e}")
    
    print(f"\n✓ Sent {stats['offers']}/5 offers")
    
    # Flush and close
    producer.flush()
    producer.close()
    
    total = sum(stats.values())
    print(f"\n{'─' * 70}")
    print(f"✓ Production complete: {total}/35 events sent")
    print(f"  Listings: {stats['listings']}, Views: {stats['views']}, Offers: {stats['offers']}")
    print('─' * 70)


# =============================================================================
# Phase 3: Event Consumption
# =============================================================================

def consume_events():
    """Consume events from Kafka topics"""
    print_section("PHASE 3: EVENT CONSUMPTION")
    
    # Step 1: Single-topic consumer
    print_step(1, "Consuming Listings (notifications group)")
    
    consumer = KafkaConsumer(
        'listings',
        bootstrap_servers=BOOTSTRAP_SERVERS,
        group_id='notifications',
        value_deserializer=lambda m: json.loads(m.decode('utf-8')),
        auto_offset_reset='earliest',
        consumer_timeout_ms=5000
    )
    
    count = 0
    for message in consumer:
        count += 1
        if count <= 3:
            event = message.value
            print(f"  [{count:2d}] {event['property_id']} - "
                  f"Agent: {event['agent_id']}, "
                  f"Price: ${event['price']:,}")
    
    if count > 3:
        print(f"  ... and {count - 3} more listings")
    print(f"\n✓ Consumed {count} listings")
    consumer.close()
    
    # Step 2: Multi-topic consumer
    print_step(2, "Consuming All Topics (dashboard group)")
    
    consumer = KafkaConsumer(
        bootstrap_servers=BOOTSTRAP_SERVERS,
        group_id='dashboard',
        value_deserializer=lambda m: json.loads(m.decode('utf-8')),
        auto_offset_reset='earliest',
        consumer_timeout_ms=5000
    )
    consumer.subscribe(['listings', 'views', 'offers'])
    
    topic_counts = {'listings': 0, 'views': 0, 'offers': 0}
    total = 0
    
    for message in consumer:
        total += 1
        topic_counts[message.topic] += 1
        
        if total <= 3:
            print(f"  [{total:2d}] Topic: {message.topic:12s} | "
                  f"Event: {message.value['event_id']}")
    
    if total > 3:
        print(f"  ... and {total - 3} more events")
    
    print(f"\n✓ Consumed {total} total events")
    print(f"  Listings: {topic_counts['listings']}, "
          f"Views: {topic_counts['views']}, "
          f"Offers: {topic_counts['offers']}")
    
    consumer.close()


# =============================================================================
# Phase 4: Partition & Ordering Demo
# =============================================================================

def demonstrate_partitioning():
    """Demonstrate partition assignment and ordering"""
    print_section("PHASE 4: PARTITIONING & ORDERING")
    
    # Step 1: Key-based partitioning
    print_step(1, "Key-Based Partition Assignment")
    
    producer = KafkaProducer(
        bootstrap_servers=BOOTSTRAP_SERVERS,
        value_serializer=lambda v: json.dumps(v).encode('utf-8'),
        key_serializer=lambda k: k.encode('utf-8')
    )
    
    partition_map = {}
    
    for agent_id in ['agent_1', 'agent_2', 'agent_3']:
        for i in range(3):
            event = {
                'agent_id': agent_id,
                'property_id': f'prop_{agent_id}_{i}',
                'price': 1400000 + i * 50000
            }
            
            future = producer.send('listings', key=agent_id, value=event)
            metadata = future.get()
            partition_map[agent_id] = metadata.partition
            
            if i == 0:  # Print first message for each agent
                print(f"  {agent_id} → Partition {metadata.partition}")
    
    print("\n✓ Same key always maps to same partition (deterministic)")
    producer.close()
    
    # Step 2: Ordering within partition
    print_step(2, "Message Ordering Within Partition")
    
    consumer = KafkaConsumer(
        bootstrap_servers=BOOTSTRAP_SERVERS,
        value_deserializer=lambda m: json.loads(m.decode('utf-8')),
        auto_offset_reset='earliest',
        consumer_timeout_ms=5000
    )
    
    # Read from one partition
    target_partition = partition_map['agent_1']
    tp = TopicPartition('listings', target_partition)
    consumer.assign([tp])
    consumer.seek(tp, 0)
    
    print(f"Reading from partition {target_partition}:\n")
    
    messages = []
    for message in consumer:
        messages.append(message)
        if len(messages) <= 3:
            print(f"  Offset {message.offset}: {message.value['agent_id']} - "
                  f"{message.value['property_id']}")
    
    if len(messages) > 3:
        print(f"  ... and {len(messages) - 3} more messages")
    
    # Verify ordering
    offsets = [m.offset for m in messages]
    is_sequential = all(offsets[i] + 1 == offsets[i + 1] for i in range(len(offsets) - 1))
    
    print(f"\n✓ Offsets are sequential: {is_sequential}")
    print("✓ Messages from same key arrive in order")
    
    consumer.close()


# =============================================================================
# Phase 5: Parallel Processing Demo
# =============================================================================

def demonstrate_parallel_processing():
    """Demonstrate parallel processing with consumer groups"""
    print_section("PHASE 5: PARALLEL PROCESSING")
    
    print_step(1, "Consumer Group with 2 Consumers")
    
    results = {'consumer_0': 0, 'consumer_1': 0}
    
    def consumer_worker(consumer_id):
        """Worker function for parallel consumer"""
        consumer = KafkaConsumer(
            'views',
            bootstrap_servers=BOOTSTRAP_SERVERS,
            group_id='parallel-demo',
            value_deserializer=lambda m: json.loads(m.decode('utf-8')),
            auto_offset_reset='earliest',
            consumer_timeout_ms=5000
        )
        
        count = 0
        for message in consumer:
            count += 1
        
        results[f'consumer_{consumer_id}'] = count
        consumer.close()
    
    # Start 2 consumers in parallel
    threads = []
    for i in range(2):
        t = threading.Thread(target=consumer_worker, args=(i,))
        t.start()
        threads.append(t)
    
    # Wait for completion
    for t in threads:
        t.join()
    
    # Report results
    total = sum(results.values())
    print(f"  Consumer 0 processed: {results['consumer_0']} messages")
    print(f"  Consumer 1 processed: {results['consumer_1']} messages")
    print(f"  Total processed:      {total} messages")
    
    print("\n✓ Partitions automatically distributed among consumers")
    print("✓ Each partition processed by exactly one consumer")
    print("✓ Parallel processing improves throughput")


# =============================================================================
# Main Demo
# =============================================================================

def main():
    """Run the complete Kafka demo"""
    print("\n" + "=" * 70)
    print("  KAFKA LAB - COMPLETE END-TO-END DEMO")
    print("  Real Estate Event Streaming System")
    print("=" * 70)
    
    try:
        # Phase 1: Setup
        setup_cluster()
        
        # Phase 2: Production
        produce_events()
        
        # Phase 3: Consumption
        consume_events()
        
        # Phase 4: Partitioning
        demonstrate_partitioning()
        
        # Phase 5: Parallel Processing
        demonstrate_parallel_processing()
        
        # Success summary
        print_section("DEMO COMPLETE!")
        print("✓ Cluster setup and topic creation")
        print("✓ Event production with key-based partitioning")
        print("✓ Event consumption using consumer groups")
        print("✓ Partition assignment and ordering guarantees")
        print("✓ Parallel processing with multiple consumers")
        
        print("\n" + "=" * 70)
        print("  All Kafka concepts demonstrated successfully!")
        print("=" * 70 + "\n")
        
    except KeyboardInterrupt:
        print("\n\n✗ Demo interrupted by user")
    except Exception as e:
        print(f"\n\n✗ Demo failed: {e}")
        import traceback
        traceback.print_exc()


if __name__ == '__main__':
    main()
