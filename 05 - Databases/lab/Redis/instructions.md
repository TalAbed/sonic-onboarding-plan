# Redis Lab: Exercise Instructions

**Time:** 1.5-2 hours  
**Format:** 5 interconnected sub-tasks  
**Objective:** Build a complete e-commerce caching system

---

## Overview: Build a Caching System

You're building a Redis-based cache for an e-commerce platform. Your goal is to implement 5 key components that work together:

1. Product cache (fast lookups)
2. Shopping carts (persistent storage)
3. View history (personalization)
4. Trending products (real-time analytics)
5. Session management (authentication)

**Sample Data:**
- 5 products: iPhone 15, MacBook Pro, iPad Air, AirPods Pro, Samsung TV
- 2 users: John (user:1), Jane (user:2)

---

## Sub-Task 1: Product Cache

**Objective:** Store product information with expiration

### The Challenge

You need to cache product data so it's instantly accessible without hitting the database. Each product should have:
- Name
- Price
- Category
- Stock quantity

Products should expire from cache after 1 hour (to refresh prices).

### Steps:

**Step 1: Store product information using HASHES**

Redis Hashes are perfect for storing objects. Each product is a hash with fields.

```redis
HSET product:1 name "iPhone 15" price 999 category "Electronics" stock 50
```

This creates a hash called `product:1` with 4 fields.

**Step 2: Retrieve product data**

```redis
HGETALL product:1        # Get all fields
HGET product:1 price     # Get specific field
```

**Step 3: Set expiration (TTL)**

```redis
EXPIRE product:1 3600    # Expire after 1 hour (3600 seconds)
TTL product:1            # Check remaining time
```

**Step 4: Update product**

```redis
HSET product:1 price 899  # Update price (can use same HSET command)
```

### Your Tasks

1. Store 5 sample products in Redis using HASHES:
   - product:1 → iPhone 15, $999, Electronics, 50 stock
   - product:2 → MacBook Pro, $2499, Electronics, 25 stock
   - product:3 → iPad Air, $599, Electronics, 40 stock
   - product:4 → AirPods Pro, $249, Electronics, 100 stock
   - product:5 → Samsung TV, $799, Electronics, 15 stock

2. Set each product to expire after 1 hour

3. Retrieve all fields for product:1

4. Update iPhone 15 price to $899

5. Check the TTL for product:1

### Validation

```redis
HGETALL product:1        # Should show all fields
TTL product:1            # Should show ~3600 seconds
HGET product:1 price     # Should show 899
```

### Questions

- Why use HASH instead of storing entire product as a JSON string?
- What happens when TTL expires? Can you still access the data?
- How would you handle cache invalidation if price changes in database?

---

## Sub-Task 2: Shopping Cart

**Objective:** Build persistent user shopping carts

### The Challenge

Implement shopping carts that:
- Store user cart items and quantities
- Allow adding/removing items
- Persist across sessions (30-day expiration)
- Calculate cart contents on demand

### Hints

**Step 1: Structure**

Use HASHES to store carts. Key format: `user:X:cart`
- Hash field = product ID
- Hash value = quantity

```redis
HSET user:1:cart product:1 1      # John has 1 iPhone 15
HSET user:1:cart product:3 2      # John has 2 iPad Airs
```

**Step 2: View cart**

```redis
HGETALL user:1:cart     # Get entire cart
HGET user:1:cart product:1   # Get qty of specific product
```

**Step 3: Update quantity**

```redis
HSET user:1:cart product:1 2      # Change iPhone qty to 2
HINCRBY user:1:cart product:1 1   # Increment by 1
```

**Step 4: Remove item**

```redis
HDEL user:1:cart product:1        # Remove iPhone from cart
```

**Step 5: Cart expiration**

```redis
EXPIRE user:1:cart 2592000        # 30 days (30 * 24 * 60 * 60)
```

### Your Tasks

1. Create cart for user:1 (John):
   - 1x iPhone 15
   - 2x iPad Airs

2. Create cart for user:2 (Jane):
   - 1x MacBook Pro
   - 2x AirPods Pro

3. Add 1 Samsung TV to John's cart (HSET)

4. Increment iPhone qty by 1 in John's cart (HINCRBY)

5. View John's complete cart

6. Remove iPad from John's cart

7. Set both carts to expire in 30 days

### Validation

```redis
HGETALL user:1:cart              # Should show products with updated quantities
HLEN user:1:cart                 # Should show number of items
HGET user:1:cart product:1       # Should show updated iPhone qty
```

### Questions

- Why use HASH for cart instead of a LIST?
- What if we need to remove all carts for all users? (KEYS pattern matching)
- How to calculate total cart value? (Need to look up prices from product hashes)

---

## Sub-Task 3: Recently Viewed

**Objective:** Track recently viewed products per user

### The Challenge

Implement view history that:
- Tracks products user viewed (in order)
- Shows most recent first
- Keeps only last 10 items
- Expires after 7 days

### Hints

**Step 1: Add to view history**

Use LISTS for ordered data. Key format: `user:X:viewed`

```redis
LPUSH user:1:viewed product:1     # John viewed iPhone (prepend)
LPUSH user:1:viewed product:3     # John viewed iPad (now first)
```

LPUSH adds to the front, so newer items are first.

**Step 2: View recent history**

```redis
LRANGE user:1:viewed 0 4         # Get first 5 (most recent)
LRANGE user:1:viewed 0 -1        # Get all
```

**Step 3: Limit list to 10 items**

```redis
LTRIM user:1:viewed 0 9          # Keep only first 10 items
```

**Step 4: Set expiration**

```redis
EXPIRE user:1:viewed 604800      # 7 days
```

### Your Tasks

1. Create view history for user:1:
   - View product:1
   - View product:3
   - View product:5
   - View product:1 (again, will go to front)

2. Create view history for user:2:
   - View product:2
   - View product:4

3. Get John's 3 most recent views

4. Get entire view history for Jane

5. Trim John's list to keep only 10 items (use LTRIM)

6. Set both lists to expire in 7 days

### Validation

```redis
LRANGE user:1:viewed 0 -1        # Should show products with most recent first
LLEN user:1:viewed               # Should show list length
LINDEX user:1:viewed 0           # Should show most recent product
```

### Questions

- Why use LIST instead of SET for this?
- What if user views same product twice? (Doesn't prevent duplicates)
- How would you implement "last N items without duplicates"?

---

## Sub-Task 4: Trending Products

**Objective:** Track and rank trending products by views

### The Challenge

Implement real-time trending that:
- Counts views per product
- Ranks products by popularity
- Returns top N products
- Resets daily

### Hints

**Step 1: Count views (Simple counter)**

Use STRINGS for simple counters.

```redis
INCR product:1:views        # Increment view count
GET product:1:views         # Check current count
```

**Step 2: Add to trending (Sorted Set)**

Use SORTED SETS for rankings. Key: `trending:today`
- Member = product ID
- Score = view count

```redis
ZADD trending:today 1 product:1      # Add product:1 with score 1
ZINCRBY trending:today 1 product:1   # Increment score by 1
```

**Step 3: Get top N products**

```redis
ZREVRANGE trending:today 0 4 WITHSCORES   # Top 5 (highest scores first)
ZREVRANGE trending:today 0 -1             # All (ranked)
```

**Step 4: Reset daily (expire entire key)**

```redis
EXPIRE trending:today 86400         # Expire after 24 hours
```

### Your Tasks

1. Simulate 50 views for product:1
   - INCR product:1:views 50 times (or use a loop)

2. Simulate 30 views for product:3

3. Simulate 20 views for product:5

4. Add each to sorted set `trending:today` with view count as score:
   - product:1: 50 views
   - product:3: 30 views
   - product:5: 20 views

5. Get top 3 trending products with their view counts

6. Set trending list to expire in 24 hours

### Validation

```redis
ZREVRANGE trending:today 0 -1 WITHSCORES   # Should show all, ranked by score
ZRANK trending:today product:1             # Should show rank (position)
ZSCORE trending:today product:1            # Should show score (views)
GET product:1:views                        # Should show view count
```

### Questions

- Why use SORTED SET instead of just incrementing counters?
- How would you track trends per hour instead of per day?
- What if you want to weight recent views higher?

---

## Sub-Task 5: Session Management

**Objective:** Manage user sessions with auto-expiry

### The Challenge

Implement session management that:
- Stores user session data (as JSON)
- Sets 30-minute timeout
- Auto-expires on inactivity
- Refreshes on activity

### Hints

**Step 1: Create session (String with TTL)**

Store session as JSON string. Key format: `session:SESSION_ID`

```redis
SET session:abc123 '{"user_id":1,"username":"john","login_at":"2024-01-25T14:30:00Z"}' EX 1800
```

`EX 1800` sets 30-minute expiration in one command.

**Step 2: Check session**

```redis
GET session:abc123              # Retrieve session
EXISTS session:abc123           # Check if valid
```

**Step 3: Check TTL**

```redis
TTL session:abc123              # Seconds remaining
```

**Step 4: Refresh session (extend timeout)**

```redis
EXPIRE session:abc123 1800      # Reset 30-minute timer
```

**Step 5: Manual logout**

```redis
DEL session:abc123              # Delete session
```

### Your Tasks

1. Create session for John (user_id=1):
   - Session ID: `john_session_12345`
   - Username: john
   - Login timestamp: current time
   - 30-minute expiration

2. Create session for Jane (user_id=2):
   - Session ID: `jane_session_67890`
   - Username: jane
   - Login timestamp: current time
   - 30-minute expiration

3. Retrieve John's session

4. Check TTL for both sessions

5. Simulate activity: refresh John's session (extend timer)

6. Check updated TTL for John's session

7. Simulate logout: delete Jane's session

### Validation

```redis
GET session:john_session_12345       # Should show JSON session data
TTL session:john_session_12345       # Should show ~1800 seconds
EXISTS session:jane_session_67890    # Should show 0 (deleted)
```

### Questions

- Why use SET with EX instead of separate EXPIRE command?
- What happens after 30 minutes of inactivity? (Session auto-deletes)
- How would you handle session refresh automatically?

---

## 📋 Completion Checklist

After completing all 5 sub-tasks, verify:

- [ ] Sub-Task 1: 5 products stored with HASHES + TTL
- [ ] Sub-Task 2: 2 user carts with multiple items
- [ ] Sub-Task 3: View history for 2 users (ordered)
- [ ] Sub-Task 4: Trending products ranked by views
- [ ] Sub-Task 5: Sessions with auto-expiry

---

## 🎯 Next Steps

1. Try implementations in **redis-cli** OR **Python**
2. Check **solutions/** folder if stuck
3. Run **starter-code/demo.py** to see complete system

---

## Tips

- Use `redis-cli` and type `MONITOR` to see all commands execute in real-time
- Type `KEYS *` to see all keys in Redis
- Type `FLUSHDB` to clear entire database (useful for restart)
- Commands are case-insensitive but capitalized by convention

---

Good luck! 🚀

