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

## Sub-Task 1: Kafka Setup & Topics (15 minutes)

**Objective:** Start Kafka cluster and create topics

### The Challenge

You need to start a Kafka cluster and create 3 topics with appropriate partition and replication settings.

### Hints

**Step 1: Start Kafka with Docker Compose**
- Create a docker-compose.yml file that starts a 3-broker Kafka cluster with Zookeeper
- Start the cluster using docker-compose
- Verify all containers are running and healthy
- Wait for the cluster to be fully ready (check broker logs)

**Step 2: Create topics using AdminClient**
- Connect to the Kafka cluster using KafkaAdminClient
- Create 3 topics with the following configuration:
  - Topic: `listings` → 3 partitions, replication factor 3
  - Topic: `views` → 3 partitions, replication factor 3
  - Topic: `offers` → 2 partitions, replication factor 3
- Handle creation completion and any errors

**Step 3: Verify topics created**
- List all topics in the cluster
- For each topic (listings, views, offers):
  - Show the number of partitions
  - Display partition details
  - Verify replication factor

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

### Validation Checklist

- [ ] 3 Kafka brokers are running and healthy
- [ ] Zookeeper is running
- [ ] Topic `listings` exists with 3 partitions
- [ ] Topic `views` exists with 3 partitions
- [ ] Topic `offers` exists with 2 partitions
- [ ] All topics have replication factor of 3
- [ ] All partitions have a leader elected

### Questions to Consider

- Why do we create 3 partitions for some topics but only 2 for others?
- What is the purpose of replication factor and why did we choose 3?
- What happens if one broker fails? How does Kafka handle this?
- How does Kafka elect a leader for each partition?
- What's the relationship between brokers and topic partitions?

---

## Sub-Task 2: Message Producers (20 minutes)

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

### Hints

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

### Your Tasks

1. **Create listings producer:**
   - Generate 10 listing events with unique property IDs
   - Assign each listing to one of 5 different agents
   - Include realistic pricing (starting from $1.4M+)
   - Use agent_id as the key
   - Send to `listings` topic

2. **Create views producer:**
   - Generate 20 property view events
   - Distribute views across 10 different properties
   - Include realistic view durations (60+ seconds)
   - Vary the action (viewed vs scheduled_tour)
   - Use property_id as the key
   - Send to `views` topic

3. **Create offers producer:**
   - Generate 5 purchase offer events
   - Assign to 5 different properties
   - Include offer prices, contingencies, and close dates
   - Use property_id as the key
   - Send to `offers` topic

4. **Verify delivery:**
   - Confirm all messages sent successfully
   - Print message count for each topic (10, 20, 5)
   - Show which partition each message was assigned to
   - Display offset assigned to each message

5. **Add error handling:**
   - Catch send failures
   - Print error messages for any failures
   - Ensure all events eventually send
   - Report total successful deliveries

### Validation Checklist

- [ ] 10 listing events sent to `listings` topic
- [ ] 20 view events sent to `views` topic
- [ ] 5 offer events sent to `offers` topic
- [ ] Each message has an event_id
- [ ] Each message has the correct key assigned
- [ ] Each message is assigned to a partition
- [ ] Each message receives an offset
- [ ] Total message count is 35

### Questions to Consider

- Why did we use different keys for different event types?
- What does the key do in Kafka? How does it affect partitioning?
- Why use `acks='all'` vs other ack settings?
- What happens if a broker is down during sending?
- How does Kafka ensure message ordering with keys?

---

## Sub-Task 3: Message Consumers (20 minutes)

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

### Hints

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

### Your Tasks

1. **Create listings consumer:**
   - Subscribe to `listings` topic
   - Use consumer group `notifications`
   - Read and print each listing event
   - Display property address and price
   - Count total messages received

2. **Create views consumer:**
   - Subscribe to `views` topic
   - Use consumer group `analytics`
   - Print view details (property, user, duration)
   - Count total view events

3. **Create offers consumer:**
   - Subscribe to `offers` topic
   - Use consumer group `approval-system`
   - Display offer information (property, buyer, price)
   - Count total offers received

4. **Create multi-topic consumer:**
   - Subscribe to all 3 topics at once
   - Use consumer group `dashboard`
   - Show which topic each message came from
   - Print the event details
   - Display total count of all messages (should be 35)

5. **Track offset progression:**
   - Print partition number for each message
   - Print offset number for each message
   - Notice offsets increase sequentially
   - Understand consumer position tracking

### Validation Checklist

- [ ] Listings consumer receives 10 messages
- [ ] Views consumer receives 20 messages
- [ ] Offers consumer receives 5 messages
- [ ] Multi-topic consumer receives 35 messages total
- [ ] Each message has partition and offset information
- [ ] Each message is successfully deserialized
- [ ] Consumer groups are correctly identified
- [ ] All messages are from the expected time period

### Questions to Consider

- What does `auto_offset_reset='earliest'` do?
- What would happen if you used `auto_offset_reset='latest'`?
- Why do we use different consumer groups for different purposes?
- What is a consumer group and why are they useful?
- How does Kafka track where each consumer group is reading?

---

## Sub-Task 4: Partitions & Offsets (20 minutes)

**Objective:** Understand partition assignment and message ordering

### The Challenge

Learn how Kafka assigns messages to partitions based on keys and how to track message positions within partitions.

### Hints

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

### Your Tasks

1. **Send events with keys and observe partition assignment:**
   - Send 5 listing events with key='agent_1'
   - Send 5 listing events with key='agent_2'
   - Send 5 listing events with key='agent_3'
   - Display which partition each message was assigned to
   - Show the partition mapping for each agent

2. **Verify partition assignment consistency:**
   - Send additional messages with the same keys
   - Confirm each agent consistently uses the same partition
   - Display final mapping (agent_1 → partition X, etc.)
   - Verify no agent's messages went to different partitions

3. **Track offsets within a partition:**
   - Read messages from a single partition
   - Print offset for each message in order
   - Verify offsets are sequential (0, 1, 2, ...)
   - Check for any gaps in the offset sequence

4. **Verify message ordering:**
   - Consume messages from partition
   - Confirm they arrive in the order they were sent
   - Show that ordering is guaranteed within the partition
   - Demonstrate that order is NOT guaranteed across partitions

5. **Understand offset tracking:**
   - Display consumer position after reading messages
   - Show the next offset to be read
   - Demonstrate how offsets track progress

### Validation Checklist

- [ ] Same key always maps to same partition
- [ ] agent_1 consistently uses one partition
- [ ] agent_2 consistently uses one partition
- [ ] agent_3 consistently uses one partition
- [ ] Offsets within a partition are sequential
- [ ] No gaps exist in offset numbers
- [ ] Messages from same key arrive in order
- [ ] Consumer position accurately reflects offset progress

### Questions to Consider

- How does Kafka determine which partition a message goes to?
- What's the formula for partition assignment based on keys?
- Why is message ordering guaranteed within a partition but not across?
- What's the relationship between offset and message order?
- Can offsets have gaps? If so, why?
- What happens if two messages have the same key?

---

## Sub-Task 5: Consumer Groups (20 minutes)

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

### Your Tasks

1. **Create consumer group 'notifications' with 2 consumers:**
   - Start 2 consumers in the notifications group
   - Both read from `listings` topic
   - Display partition assignment for each consumer
   - Show how many messages each consumer processes
   - Verify all 10 messages are processed

2. **Create consumer group 'analytics' with 3 consumers:**
   - Start 3 consumers in the analytics group
   - All read from `views` topic
   - Display partition assignment for each
   - Show message count per consumer
   - Verify load is distributed among consumers
   - Check that all 20 messages are received

3. **Test rebalancing behavior:**
   - Start 2 consumers in a test group
   - While consuming, add a 3rd consumer
   - Document partition reassignment
   - Explain what happened during rebalancing
   - Show before/after partition assignments

4. **Measure performance improvement:**
   - Process messages with 1 consumer, measure time
   - Process messages with 2 consumers, measure time
   - Calculate speedup (time_1 / time_2)
   - Show that parallel processing is faster
   - Document the performance gain

5. **Test failure recovery:**
   - Start 2 consumers in a group
   - Begin consuming messages
   - Kill one consumer
   - Observe rebalancing and recovery
   - Confirm remaining consumer processes all messages

### Validation Checklist

- [ ] Consumer group distributes partitions among consumers
- [ ] Each consumer is assigned different partitions
- [ ] Total partitions assigned equals topic partition count
- [ ] Each consumer receives some messages
- [ ] Total messages processed equals messages sent
- [ ] Rebalancing occurs when consumer joins/leaves
- [ ] Partition reassignment happens correctly
- [ ] Parallel processing is faster than single consumer
- [ ] Failed consumer's work is recovered by group

### Questions to Consider

- How does Kafka decide which partitions go to which consumer?
- What happens during the rebalancing process?
- Why do consumers pause when rebalancing occurs?
- What are the benefits of using consumer groups?
- How does parallel processing improve performance?
- What happens if a consumer in a group fails?
- How long does rebalancing take?

---

## 📋 Completion Checklist

After completing all 5 sub-tasks, verify:

- [ ] Sub-Task 1: 3 topics created with correct partition counts (3, 3, 2)
- [ ] Sub-Task 2: 35 events sent total (10 + 20 + 5)
- [ ] Sub-Task 3: All 35 events consumed successfully
- [ ] Sub-Task 4: Partitions assigned correctly based on keys
- [ ] Sub-Task 5: Consumer groups process in parallel

---

## 🎯 Next Steps

1. **Try implementations** - Follow each sub-task in order
2. **Understand concepts** - Connect what you do to why it matters
3. **Verify each step** - Run validation checks before moving forward
4. **Review solutions** - See complete code in solutions/
5. **Run demo** - Execute demo.py to see everything working together

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
7. **Check reference guide** - Look up concepts in [322]
8. **Compare with demo** - See how solution works

---

Good luck! 🚀

