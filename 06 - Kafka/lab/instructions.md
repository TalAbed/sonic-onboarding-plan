# Kafka Lab: Exercise Instructions

**Time:** 1.5-2 hours  
**Format:** 5 integrated sub-tasks (all in one exercise)  
**Objective:** Build a real-time event streaming system

---

## Overview: Build an Event Streaming Pipeline

You're building a real-time event streaming system for a real estate platform. Your goal is to implement 5 key components that work together:

1. Set up Kafka cluster and create topics
2. Create message producers (3 event sources)
3. Create message consumers (3 subscriber groups)
4. Understand partition assignment and offsets
5. Implement consumer groups for parallel processing

**Sample Data:**
- 3 event types: listings, views, offers
- 3 Kafka topics with 2-3 partitions each
- 35+ events total
- JSON message format

---

## Sub-Task 1: Kafka Setup & Topics

**Objective:** Start Kafka cluster and create topics

### The Challenge

You need to start a Kafka cluster and create 3 topics with appropriate partition and replication settings.

### Your Tasks

1. **Start Kafka cluster:**
   - Use Docker Compose to start 3 brokers + 1 Zookeeper instance
   - Wait for cluster to be fully ready
   - Verify all brokers are healthy and communicating

2. **Create 3 topics:**
   - Create `listings` with 3 partitions and replication factor 3
   - Create `views` with 3 partitions and replication factor 3
   - Create `offers` with 2 partitions and replication factor 3

3. **Verify topics:**
   - Print list of all topics
   - Display partition count for each topic
   - Show partition leader and replica assignment

4. **Check broker status:**
   - Confirm 3 brokers are running
   - Show broker IDs
   - Verify topic distribution across brokers

### Questions to Consider

- Why do we create 3 partitions for some topics but only 2 for others?
- What is the purpose of replication factor and why did we choose 3?
- What happens if one broker fails? How does Kafka handle this?
- How does Kafka elect a leader for each partition?
- What's the relationship between brokers and topic partitions?

---

## Sub-Task 2: Message Producers

**Objective:** Send events to Kafka topics

### The Challenge

Create 3 producers that generate realistic real estate events and send them to their respective topics. Use appropriate keys to ensure messages are ordered correctly.

### Data Structure

**Listings Event (10 events total):**
```
Fields: event_id, event_type, timestamp, property_id, agent_id, address, price, bedrooms, bathrooms
Key: agent_id (to keep listings from same agent together)
Topic: listings
```

**Views Event (20 events total):**
```
Fields: event_id, event_type, timestamp, property_id, user_id, view_duration_seconds, action
Key: property_id (to keep views of same property together)
Topic: views
```

**Offers Event (5 events total):**
```
Fields: event_id, event_type, timestamp, property_id, buyer_id, offer_price, contingencies, close_date
Key: property_id (to keep offers for same property together)
Topic: offers
```

### Your Tasks

**Step 1: Create listings producer**
- Initialize a KafkaProducer that connects to the Kafka cluster
- Generate 10 realistic listing events with varied prices and agent assignments
- For each listing, use the agent_id as the message key
- Send each event to the `listings` topic
- Track and confirm delivery of each message

**Step 2: Create views producer**
- Initialize a KafkaProducer for the views topic
- Generate 20 view events spread across different properties
- Use property_id as the message key
- Include realistic view duration and action data
- Send all events to the `views` topic

**Step 3: Create offers producer**
- Initialize a KafkaProducer for the offers topic
- Generate 5 purchase offer events
- Use property_id as the message key
- Include offer price and contingency information
- Send all events to the `offers` topic

**Step 4: Add error handling**
- Implement error handling for message sending
- Catch and log any failures
- Verify all messages are eventually delivered
- Print summary of total messages sent per topic

### Questions to Consider

- Why did we use different keys for different event types?
- What does the key do in Kafka? How does it affect partitioning?
- Why use `acks='all'` vs other ack settings?
- What happens if a broker is down during sending?
- How does Kafka ensure message ordering with keys?

---

## Sub-Task 3: Message Consumers

**Objective:** Read and process events from Kafka topics

### The Challenge

Create 3 consumers that read from the topics you populated in Sub-Task 2. Use consumer groups to organize them.

### Consumer Groups

**Group 1: notifications**
- Subscribes to: `listings` topic
- Purpose: Send email alerts about new listings

**Group 2: analytics**
- Subscribes to: `views` topic
- Purpose: Collect metrics and statistics

**Group 3: approval-system**
- Subscribes to: `offers` topic
- Purpose: Process and approve purchase offers

### Your Tasks

**Step 1: Create listings consumer**
- Create a KafkaConsumer that connects to the Kafka cluster
- Subscribe to the `listings` topic
- Assign it to consumer group `notifications`
- Read messages from the beginning
- For each message, extract and display the event details
- Print partition and offset information
- Count total messages received

**Step 2: Create views consumer**
- Create a KafkaConsumer for the views topic
- Use consumer group `analytics`
- Read all messages from the beginning
- Extract property_id, user_id, and view duration
- Display the event information
- Count total messages

**Step 3: Create offers consumer**
- Create a KafkaConsumer for the offers topic
- Use consumer group `approval-system`
- Read all messages from the beginning
- Extract offer details (property_id, buyer_id, offer_price)
- Display offer information
- Count total messages

**Step 4: Create multi-topic consumer**
- Create a KafkaConsumer that subscribes to all 3 topics simultaneously
- Use consumer group `dashboard`
- Read all messages from the beginning
- For each message, display which topic it came from
- Show the event details
- Count total messages from all topics

**Step 5: Understand offset behavior**
- Print partition and offset for each message as you consume it
- Notice how offsets progress sequentially
- Track which consumer group is reading the messages
- Understand how Kafka tracks consumer position

### Questions to Consider

- What does `auto_offset_reset='earliest'` do?
- What would happen if you used `auto_offset_reset='latest'`?
- Why do we use different consumer groups for different purposes?
- What is a consumer group and why are they useful?
- How does Kafka track where each consumer group is reading?

---

## Sub-Task 4: Partitions & Offsets

**Objective:** Understand partition assignment and message ordering

### The Challenge

Learn how Kafka assigns messages to partitions based on keys and how to track message positions within partitions.

### Your Tasks

**Step 1: Send messages with keys and observe partition assignment**
- Create a producer that sends listing events with specific agent keys
- Send 5 listing events with key='agent_1'
- Send 5 listing events with key='agent_2'
- Send 5 listing events with key='agent_3'
- For each message, record which partition it was assigned to
- Observe the pattern of partition assignments
- Notice that the same key always maps to the same partition

**Step 2: Verify consistent partition assignment**
- Repeat sending messages with the same keys
- Confirm that agent_1 always goes to the same partition
- Confirm that agent_2 always goes to the same partition
- Confirm that agent_3 always goes to the same partition
- Document the mapping (agent → partition)

**Step 3: Consume from a single partition**
- Create a consumer that reads from only one partition of the listings topic
- Specify the exact partition number (e.g., partition 0)
- Start reading from offset 0
- For each message, display its offset
- Notice that offsets are sequential (0, 1, 2, 3, etc.)
- Verify there are no gaps in the offset sequence

**Step 4: Track offset progression**
- Create a consumer reading from the listings topic
- As you read each message, display:
  - The partition number
  - The offset of the current message
  - The consumer's current position
  - The next offset to be read
- Follow the progression through multiple messages
- Understand how offsets track position within a partition

**Step 5: Compare ordering across vs within partitions**
- Send multiple messages with different keys
- Observe messages from the same key stay ordered
- Observe messages from different keys can be out of order
- Verify ordering is guaranteed within a partition
- Confirm ordering is NOT guaranteed across partitions

### Questions to Consider

- How does Kafka determine which partition a message goes to?
- What's the formula for partition assignment based on keys?
- Why is message ordering guaranteed within a partition but not across?
- What's the relationship between offset and message order?
- Can offsets have gaps? If so, why?
- What happens if two messages have the same key?

---

## Sub-Task 5: Consumer Groups

**Objective:** Implement parallel message processing with consumer groups

### The Challenge

Create multiple consumers in a group that together process messages faster through parallel processing and load distribution.

### Hints

**Step 1: Create consumer group with 2 consumers**
- Initialize 2 consumers in the same consumer group
- Have them both subscribe to the `listings` topic
- Start both consumers running (use threading or separate processes)
- Display which partitions each consumer is assigned to
- Process messages through both consumers
- Count how many messages each consumer processes
- Calculate how partitions were distributed between them

**Step 2: Create consumer group with 3 consumers**
- Initialize 3 consumers in the same consumer group
- Have them all subscribe to the `views` topic
- Start all 3 consumers running
- Display partition assignment for each consumer
- Process messages
- Count messages per consumer
- Show how load was distributed

**Step 3: Test rebalancing**
- Start 2 consumers in a group reading from a topic
- Let them start consuming messages
- While still consuming, add a 3rd consumer to the same group
- Observe what happens to partition assignments
- Notice when the rebalancing occurs
- Watch which partitions are reassigned to which consumers
- See how consumers pause and resume during rebalancing

**Step 4: Measure performance with parallel processing**
- Produce 30 messages to a test topic (or reuse offers)
- Measure time to process all messages with 1 consumer
- Reset and measure time to process with 2 consumers
- Calculate the speedup factor
- Compare the results
- Understand the benefit of parallel processing

**Step 5: Test failure and recovery**
- Start 2 consumers in a group
- Let them consume messages
- Kill one consumer while the other is running
- Observe what happens (rebalancing occurs)
- Watch remaining consumer take over additional partitions
- See if messages are still processed correctly

### Questions to Consider

- How does Kafka decide which partitions go to which consumer?
- What happens during the rebalancing process?
- Why do consumers pause when rebalancing occurs?
- What are the benefits of using consumer groups?
- How does parallel processing improve performance?
- What happens if a consumer in a group fails?
- How long does rebalancing take?

---

## 💡 Key Concepts Reinforced

**Sub-Task 1:** Brokers → Topics → Partitions → Replication  
**Sub-Task 2:** Producers → Keys → Partitioning → Delivery acknowledgment  
**Sub-Task 3:** Consumers → Groups → Offsets → Message deserialization  
**Sub-Task 4:** Hash-based partitioning → Message ordering → Offset progression  
**Sub-Task 5:** Consumer group coordination → Rebalancing → Parallel processing  

---

## 📚 Tips for Success

1. **Start with Sub-Task 1** - Set up infrastructure first
2. **Send before consuming** - Produce events before reading them
3. **Use keys consistently** - Apply the same key logic throughout
4. **Monitor offsets** - Track message positions as you go
5. **Test with multiple consumers** - See parallelization work in practice
6. **Set appropriate timeouts** - Use timeouts during testing
7. **Handle errors gracefully** - Expect and handle failures
8. **Verify at each step** - Run validation checks before moving on

---

## Stuck? Try These

1. **Check Docker:** Are Kafka containers running? (`docker ps`)
2. **Check Kafka:** Do topics exist? (`kafka-topics.sh --list`)
3. **Check Python:** Is kafka-python installed? (`pip list`)
4. **Check Connection:** Can you connect to Kafka? (`telnet localhost 9092`)
5. **Check Logs:** What do container logs say? (`docker logs <container>`)
6. **Review hints** - Re-read the steps for each task
7. **Check reference guide** - Look up for common concepts
8. **Compare with demo** - See how solution works

---

## Good luck! 🚀

