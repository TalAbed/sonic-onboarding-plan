# Redis Reference Guide

## 📖 Complete Redis Quick Reference

A comprehensive guide for Redis commands, data structures, and Python integration.

---

## 🗄️ Table of Contents
1. [Getting Started](#getting-started)
2. [Data Structures](#data-structures)
3. [Key Commands](#key-commands)
4. [String Commands](#string-commands)
5. [List Commands](#list-commands)
6. [Set Commands](#set-commands)
7. [Hash Commands](#hash-commands)
8. [Sorted Set Commands](#sorted-set-commands)
9. [Pub/Sub](#pubsub)
10. [Transactions](#transactions)
11. [Python Integration](#python-integration)
12. [Caching Patterns](#caching-patterns)
13. [Performance Tips](#performance-tips)

---

## Getting Started

### Installation

```bash
# macOS
brew install redis

# Ubuntu/Debian
sudo apt-get install redis-server

# Windows
# Download from: https://github.com/microsoftarchive/redis/releases

# Docker
docker run -d -p 6379:6379 redis:latest
```

### Starting Redis

```bash
# Start Redis server
redis-server

# Start Redis server on specific port
redis-server --port 6380

# Connect to Redis
redis-cli

# Connect to remote Redis
redis-cli -h hostname -p port
```

### Basic Commands in redis-cli

```bash
# Ping server
PING

# Check server info
INFO

# Monitor commands
MONITOR

# Check memory usage
MEMORY USAGE key

# Get database size
DBSIZE

# Clear database
FLUSHDB

# Select database (0-15)
SELECT 0

# Exit
EXIT or quit
```

---

## Data Structures

Redis supports 5 main data structures:

| Structure | Use Case | Operations |
|-----------|----------|-----------|
| **String** | Simple values | GET, SET, APPEND |
| **List** | Ordered collections | LPUSH, RPUSH, LPOP, RPOP |
| **Set** | Unique collections | SADD, SREM, SMEMBERS |
| **Hash** | Key-value pairs | HSET, HGET, HDEL |
| **Sorted Set** | Ordered with scores | ZADD, ZREM, ZRANGE |

---

## Key Commands

### General Key Operations

```redis
-- Check if key exists
EXISTS key1 key2 key3  # Returns number of existing keys

-- Get type of value
TYPE key

-- Delete key(s)
DEL key1 key2 key3

-- Rename key
RENAME old_key new_key

-- Check if key exists before renaming
RENAMENX old_key new_key  # Returns 1 if successful, 0 if new_key exists

-- List all keys (AVOID in production!)
KEYS pattern

-- More efficient pattern matching
SCAN cursor [MATCH pattern] [COUNT count]

-- Set expiration (seconds)
EXPIRE key 3600  # 1 hour

-- Set expiration (milliseconds)
PEXPIRE key 3600000

-- Set expiration with timestamp
EXPIREAT key 1609459200

-- Get time to live
TTL key  # Returns seconds remaining, -1 if no expiration, -2 if key doesn't exist

-- Get time to live (milliseconds)
PTTL key

-- Remove expiration
PERSIST key

-- Get all keys matching pattern
KEYS user:*  # Get all keys starting with "user:"

-- Random key
RANDOMKEY
```

---

## String Commands

### Basic String Operations

```redis
-- Set value
SET key value

-- Set with expiration
SET key value EX 3600  # Expire in 3600 seconds
SET key value PX 3600000  # Expire in 3600000 milliseconds
SET key value EXAT 1609459200  # Expire at Unix timestamp

-- Set only if not exists
SET key value NX  # Returns OK if set, nil if key exists

-- Set only if exists
SET key value XX  # Returns OK if key exists, nil if not

-- Get value
GET key

-- Get multiple values
MGET key1 key2 key3

-- Set multiple values
MSET key1 value1 key2 value2 key3 value3

-- Set multiple only if none exist
MSETNX key1 value1 key2 value2  # Returns 1 if all set, 0 if any exist

-- Append to string
APPEND key value  # Returns new length

-- Get string length
STRLEN key

-- Get substring
GETRANGE key 0 4  # Get first 5 characters

-- Set substring
SETRANGE key 0 "hello"  # Replace characters starting at offset 0

-- Increment value
INCR key  # Increment by 1
INCRBY key 5  # Increment by 5
INCRBYFLOAT key 0.1  # Increment by float

-- Decrement value
DECR key  # Decrement by 1
DECRBY key 5  # Decrement by 5

-- Get value and set new one
GETSET key new_value  # Returns old value

-- Set and get (atomic)
GETEX key EX 3600  # Get value and set expiration

-- Set and delete (get and remove)
GETDEL key  # Returns value and deletes key
```

### Example: Counter

```redis
-- Initialize counter
SET page_views:home:today 0

-- Increment on each page view
INCR page_views:home:today

-- Get current count
GET page_views:home:today

-- Increment by specific amount
INCRBY page_views:home:today 10
```

---

## List Commands

### Basic List Operations

```redis
-- Push to left (head)
LPUSH mylist value1 value2 value3  # Returns length

-- Push to right (tail)
RPUSH mylist value1 value2 value3

-- Push only if list exists
LPUSHX mylist value
RPUSHX mylist value

-- Pop from left (remove and return)
LPOP mylist [count]

-- Pop from right
RPOP mylist [count]

-- Get length
LLEN mylist

-- Get elements by index range
LRANGE mylist 0 -1  # All elements (0 to end)
LRANGE mylist 0 4   # First 5 elements
LRANGE mylist -5 -1 # Last 5 elements

-- Get element at index
LINDEX mylist 0  # First element
LINDEX mylist -1 # Last element

-- Set element at index
LSET mylist 0 new_value

-- Trim list (keep only range, delete rest)
LTRIM mylist 0 99  # Keep first 100, delete the rest

-- Insert before/after element
LINSERT mylist BEFORE pivot_value new_value
LINSERT mylist AFTER pivot_value new_value

-- Remove elements
LREM mylist count value  # Remove 'count' occurrences of 'value'
                         # count > 0: remove from head
                         # count < 0: remove from tail
                         # count = 0: remove all

-- Blocking pop (wait for element)
BLPOP mylist 0  # Wait indefinitely
BLPOP mylist 5  # Wait 5 seconds

-- Move element between lists
LMOVE source destination LEFT RIGHT  # Pop from source left, push to destination right
```

### Example: Job Queue

```redis
-- Add job to queue
RPUSH job_queue '{"id": 1, "action": "send_email"}'

-- Process job
LPOP job_queue

-- Backup job while processing
RPOPLPUSH job_queue processing_queue

-- Remove from processing if failed
LREM processing_queue 0 job_data

-- Add back to queue if failed
RPUSH job_queue job_data
```

---

## Set Commands

### Basic Set Operations

```redis
-- Add member(s)
SADD myset member1 member2 member3  # Returns number added

-- Remove member(s)
SREM myset member1 member2

-- Check if member exists
SISMEMBER myset member

-- Get all members
SMEMBERS myset

-- Get set size
SCARD myset

-- Get random member(s)
SRANDMEMBER myset     # One random
SRANDMEMBER myset 3   # Three random members
SRANDMEMBER myset -3  # Three random (with duplicates possible)

-- Pop random member
SPOP myset     # One random
SPOP myset 3   # Three random

-- Set operations
SINTER set1 set2 set3      # Intersection (common to all)
SINTERSTORE dest set1 set2 # Store intersection
SUNION set1 set2 set3      # Union (all members from all sets)
SUNIONSTORE dest set1 set2 # Store union
SDIFF set1 set2            # Difference (in set1 but not set2)
SDIFFSTORE dest set1 set2  # Store difference

-- Move member between sets
SMOVE source dest member
```

### Example: Unique Visitors Tracking

```redis
-- Add visitor to today's visitors
SADD visitors:2024-01-22 user_id_123

-- Check if user already visited
SISMEMBER visitors:2024-01-22 user_id_123

-- Get total unique visitors
SCARD visitors:2024-01-22

-- Get common visitors between two days
SINTER visitors:2024-01-22 visitors:2024-01-23
```

---

## Hash Commands

### Basic Hash Operations

```redis
-- Set field(s)
HSET myhash field1 value1             # Returns 1 if new field, 0 if updated
HSET myhash field1 value1 field2 value2  # Multiple fields

-- Set only if not exists
HSETNX myhash field value  # Returns 1 if set, 0 if field exists

-- Get field value
HGET myhash field

-- Get multiple field values
HMGET myhash field1 field2 field3

-- Get all fields and values
HGETALL myhash  # Returns [field1, value1, field2, value2, ...]

-- Get all field names
HKEYS myhash

-- Get all values
HVALS myhash

-- Get number of fields
HLEN myhash

-- Check if field exists
HEXISTS myhash field  # Returns 1 if exists, 0 if not

-- Delete field(s)
HDEL myhash field1 field2 field3

-- Get string length of field value
HSTRLEN myhash field

-- Increment field value
HINCRBY myhash field 5        # Increment by 5
HINCRBYFLOAT myhash field 0.1 # Increment by float

-- Scan hash (for large hashes)
HSCAN myhash cursor [MATCH pattern] [COUNT count]
```

### Example: User Profile

```redis
-- Store user profile
HSET user:1000 name "John Doe" email "john@example.com" age 30 city "New York"

-- Get user's name
HGET user:1000 name

-- Get entire profile
HGETALL user:1000

-- Update email
HSET user:1000 email "newemail@example.com"

-- Increment age
HINCRBY user:1000 age 1

-- Check if user has email set
HEXISTS user:1000 email
```

---

## Sorted Set Commands

### Basic Sorted Set Operations

```redis
-- Add member(s) with score
ZADD myzset 1 "one" 2 "two" 3 "three"  # Returns number added

-- Remove member(s)
ZREM myzset member1 member2

-- Check if member exists
ZSCORE myzset member  # Returns score or nil

-- Get rank (position, 0-indexed)
ZRANK myzset member   # Ascending order
ZREVRANK myzset member # Descending order

-- Get range by index
ZRANGE myzset 0 -1         # All members (ascending by score)
ZRANGE myzset 0 -1 WITHSCORES  # Include scores
ZREVRANGE myzset 0 -1      # All members (descending by score)

-- Get range by score
ZRANGEBYSCORE myzset 1 2         # Members with score between 1 and 2
ZRANGEBYSCORE myzset -inf +inf   # All members
ZRANGEBYSCORE myzset (1 2        # Exclusive range (1 < score <= 2)
ZRANGEBYSCORE myzset 1 2 LIMIT 0 10  # With pagination

-- Reverse range by score
ZREVRANGEBYSCORE myzset 2 1

-- Count members in score range
ZCOUNT myzset 1 2

-- Get sorted set size
ZCARD myzset

-- Increment score
ZINCRBY myzset 10 member  # Add 10 to member's score

-- Get range with scores
ZRANGE myzset 0 -1 WITHSCORES

-- Get members between two members
ZRANGEBYLEX myzset - +

-- Remove by rank range
ZREMRANGEBYRANK myzset 0 10   # Remove first 11 members

-- Remove by score range
ZREMRANGEBYSCORE myzset 1 2

-- Remove by lex range
ZREMRANGEBYLEX myzset [a [z

-- Scan sorted set
ZSCAN myzset cursor [MATCH pattern] [COUNT count]
```

### Example: Leaderboard

```redis
-- Add player scores
ZADD leaderboard 1000 player1 2000 player2 1500 player3

-- Update player score
ZADD leaderboard 2500 player1

-- Get top 10 players
ZREVRANGE leaderboard 0 9 WITHSCORES

-- Get player rank
ZREVRANK leaderboard player1

-- Get players in score range
ZREVRANGEBYSCORE leaderboard 2000 1000

-- Get player's score
ZSCORE leaderboard player1

-- Count players with score > 1500
ZCOUNT leaderboard 1500 +inf
```

---

## Pub/Sub

### Publishing and Subscribing

```redis
-- Subscribe to channel(s)
SUBSCRIBE channel1 channel2 channel3

-- Subscribe to pattern (regex)
PSUBSCRIBE channel:*

-- Publish message
PUBLISH channel1 "Hello World"  # Returns number of subscribers

-- Unsubscribe
UNSUBSCRIBE channel1

-- Unsubscribe from pattern
PUNSUBSCRIBE channel:*

-- Get number of subscribers
PUBSUB CHANNELS

-- Get subscribers to specific channel
PUBSUB NUMSUB channel1

-- Get pattern subscribers
PUBSUB NUMPAT
```

### Example: Real-time Notifications

```redis
-- Subscriber (listens for notifications)
SUBSCRIBE notifications

-- Publisher (sends notification)
PUBLISH notifications "New order received!"

-- Pattern subscriber (listens for all events)
PSUBSCRIBE events:*

-- Publish to specific event
PUBLISH events:user:login "User 123 logged in"
PUBLISH events:user:logout "User 123 logged out"
```

---

## Transactions

### ACID Properties

```redis
-- Start transaction
MULTI

-- Queue commands
SET key1 value1
SET key2 value2
INCR counter

-- Execute transaction
EXEC  # Executes all commands atomically

-- Cancel transaction
DISCARD

-- Watch key (optimistic locking)
WATCH key1 key2
MULTI
SET key1 new_value
EXEC  # Fails if key1 was modified by another client

-- Unwatch
UNWATCH
```

### Example: Bank Transfer

```redis
-- Atomically transfer money
WATCH account1 account2
MULTI
DECRBY account1 100
INCRBY account2 100
EXEC
```

---

## Python Integration

### redis-py Library

```python
import redis

# Connect to Redis
r = redis.Redis(host='localhost', port=6379, db=0)

# or using connection string
r = redis.from_url('redis://localhost:6379/0')

# Ping server
r.ping()  # Returns True if connected
```

### String Operations

```python
# Set value
r.set('key', 'value')
r.set('key', 'value', ex=3600)  # With expiration

# Get value
value = r.get('key')  # Returns bytes, use decode()
value = r.get('key').decode('utf-8')

# Get multiple
values = r.mget(['key1', 'key2', 'key3'])

# Set multiple
r.mset({'key1': 'value1', 'key2': 'value2'})

# Increment
r.incr('counter')
r.incrby('counter', 5)
r.incrbyfloat('counter', 0.1)

# Append
r.append('key', ' additional')

# Get length
r.strlen('key')

# Get substring
r.getrange('key', 0, 4)

# Set and delete
value = r.getdel('key')  # Returns value and deletes
```

### List Operations

```python
# Push values
r.lpush('mylist', 'value1', 'value2', 'value3')
r.rpush('mylist', 'value4')

# Pop values
value = r.lpop('mylist')
values = r.lpop('mylist', count=3)

# Get range
values = r.lrange('mylist', 0, -1)  # All values
values = r.lrange('mylist', 0, 4)   # First 5 values

# Get length
length = r.llen('mylist')

# Get specific index
value = r.lindex('mylist', 0)

# Set specific index
r.lset('mylist', 0, 'new_value')

# Trim list
r.ltrim('mylist', 0, 99)
```

### Set Operations

```python
# Add members
r.sadd('myset', 'member1', 'member2', 'member3')

# Remove members
r.srem('myset', 'member1')

# Get all members
members = r.smembers('myset')  # Returns set of bytes

# Check if member exists
exists = r.sismember('myset', 'member1')

# Get set size
size = r.scard('myset')

# Get random members
random_members = r.srandmember('myset', 3)

# Set operations
intersection = r.sinter('set1', 'set2')
union = r.sunion('set1', 'set2')
difference = r.sdiff('set1', 'set2')
```

### Hash Operations

```python
# Set fields
r.hset('myhash', 'field1', 'value1')
r.hset('myhash', mapping={'field2': 'value2', 'field3': 'value3'})

# Get field
value = r.hget('myhash', 'field1')

# Get all fields
all_data = r.hgetall('myhash')  # Returns dict

# Get multiple fields
values = r.hmget('myhash', ['field1', 'field2'])

# Check if field exists
exists = r.hexists('myhash', 'field1')

# Delete field
r.hdel('myhash', 'field1')

# Increment field
r.hincrby('myhash', 'counter', 5)

# Get all field names
fields = r.hkeys('myhash')

# Get all values
values = r.hvals('myhash')

# Get hash size
size = r.hlen('myhash')
```

### Sorted Set Operations

```python
# Add members with scores
r.zadd('myzset', {'member1': 1, 'member2': 2, 'member3': 3})

# Remove members
r.zrem('myzset', 'member1')

# Get score
score = r.zscore('myzset', 'member1')

# Get rank
rank = r.zrank('myzset', 'member1')  # Ascending
rank = r.zrevrank('myzset', 'member1')  # Descending

# Get range
members = r.zrange('myzset', 0, -1)  # All members
members = r.zrange('myzset', 0, -1, withscores=True)

# Get by score range
members = r.zrangebyscore('myzset', 1, 2)

# Increment score
r.zincrby('myzset', 10, 'member1')

# Get size
size = r.zcard('myzset')

# Count in score range
count = r.zcount('myzset', 1, 2)
```

### Key Operations

```python
# Check if key exists
exists = r.exists('key1', 'key2')

# Get key type
key_type = r.type('key')

# Delete key(s)
r.delete('key1', 'key2', 'key3')

# Set expiration
r.expire('key', 3600)  # Seconds
r.pexpire('key', 3600000)  # Milliseconds

# Get TTL
ttl = r.ttl('key')  # -1 if no expiration, -2 if key doesn't exist

# Get all keys (avoid in production!)
keys = r.keys('pattern')

# Rename key
r.rename('old_key', 'new_key')

# Persist key (remove expiration)
r.persist('key')
```

### Pipeline (Multiple Commands)

```python
# Pipeline reduces network round-trips
pipe = r.pipeline()
pipe.set('key1', 'value1')
pipe.set('key2', 'value2')
pipe.get('key1')
results = pipe.execute()

# Or using context manager
with r.pipeline() as pipe:
    pipe.set('key1', 'value1')
    pipe.set('key2', 'value2')
    pipe.incr('counter')
    results = pipe.execute()
```

### Pub/Sub

```python
# Create pub/sub object
pubsub = r.pubsub()

# Subscribe to channel
pubsub.subscribe('mychannel')

# Listen for messages
for message in pubsub.listen():
    if message['type'] == 'message':
        print(message['data'])

# Publish message (from another connection)
r.publish('mychannel', 'Hello World')

# Unsubscribe
pubsub.unsubscribe('mychannel')
```

### Connection Pooling

```python
from redis import ConnectionPool

# Create connection pool
pool = ConnectionPool(host='localhost', port=6379, db=0)
r = redis.Redis(connection_pool=pool)

# Or with parameters
r = redis.Redis(
    host='localhost',
    port=6379,
    db=0,
    max_connections=50,
    socket_connect_timeout=5,
    socket_keepalive=True
)
```

---

## Caching Patterns

### Cache-Aside (Lazy Loading)

```python
def get_user(user_id):
    # Try cache first
    cache_key = f'user:{user_id}'
    user = redis_client.get(cache_key)
    
    if user:
        return json.loads(user)
    
    # Cache miss: fetch from database
    user = db.get_user(user_id)
    
    # Store in cache
    redis_client.setex(
        cache_key,
        3600,  # Expire in 1 hour
        json.dumps(user)
    )
    
    return user
```

### Write-Through

```python
def update_user(user_id, data):
    # Update database
    user = db.update_user(user_id, data)
    
    # Update cache
    cache_key = f'user:{user_id}'
    redis_client.setex(
        cache_key,
        3600,
        json.dumps(user)
    )
    
    return user
```

### Cache Invalidation

```python
def delete_user(user_id):
    # Delete from database
    db.delete_user(user_id)
    
    # Invalidate cache
    cache_key = f'user:{user_id}'
    redis_client.delete(cache_key)
```

### Session Storage

```python
def create_session(user_id):
    session_id = str(uuid.uuid4())
    session_data = {
        'user_id': user_id,
        'created_at': time.time(),
        'last_activity': time.time()
    }
    
    redis_client.setex(
        f'session:{session_id}',
        86400,  # 24 hours
        json.dumps(session_data)
    )
    
    return session_id

def get_session(session_id):
    data = redis_client.get(f'session:{session_id}')
    return json.loads(data) if data else None

def update_session_activity(session_id):
    redis_client.expire(f'session:{session_id}', 86400)
```

### Rate Limiting

```python
def check_rate_limit(client_id, limit=10, window=60):
    key = f'rate_limit:{client_id}'
    current = redis_client.incr(key)
    
    if current == 1:
        redis_client.expire(key, window)
    
    return current <= limit
```

---

## Performance Tips

### Best Practices

```
1. Use pipelines for multiple commands
2. Use connection pooling
3. Choose right data structures
4. Set appropriate TTLs
5. Monitor memory usage
6. Use SCAN instead of KEYS
7. Batch operations
8. Use Lua scripts for complex operations
```

### Common Mistakes

```
❌ Using KEYS * in production (blocks server)
❌ Storing large objects without compression
❌ Not setting TTL (memory leaks)
❌ Using FLUSHDB carelessly
❌ Not using pipelining for bulk operations
❌ Storing sensitive data unencrypted
```

---

## Summary

This reference guide covers:
- ✅ All Redis data structures (strings, lists, sets, hashes, sorted sets)
- ✅ Pub/Sub messaging
- ✅ Transactions and atomicity
- ✅ Python redis-py integration
- ✅ Common caching patterns
- ✅ Performance optimization

For more: https://redis.io/docs/

