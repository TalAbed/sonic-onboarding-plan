# Redis Lab: Complete Solutions

This file contains complete Python implementations for all 5 sub-tasks.

---

## Sub-Task 1: Product Cache Solution

```python
import redis
import json

# Connect to Redis
r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

# Sub-Task 1: Product Cache
print("=" * 50)
print("Sub-Task 1: Product Cache")
print("=" * 50)

# Store 5 products
products = {
    1: {"name": "iPhone 15", "price": 999, "category": "Electronics", "stock": 50},
    2: {"name": "MacBook Pro", "price": 2499, "category": "Electronics", "stock": 25},
    3: {"name": "iPad Air", "price": 599, "category": "Electronics", "stock": 40},
    4: {"name": "AirPods Pro", "price": 249, "category": "Electronics", "stock": 100},
    5: {"name": "Samsung TV", "price": 799, "category": "Electronics", "stock": 15},
}

# Store each product as a hash with 1-hour expiration
for product_id, product_data in products.items():
    key = f"product:{product_id}"
    r.hset(key, mapping=product_data)
    r.expire(key, 3600)  # 1 hour
    print(f"✓ Stored {product_data['name']} (expires in 1 hour)")

# Retrieve and display
print("\nRetrieving product:1:")
product_1 = r.hgetall("product:1")
print(f"  {product_1}")

# Update price
r.hset("product:1", "price", 899)
print(f"\nUpdated iPhone 15 price to $899")
print(f"  New price: {r.hget('product:1', 'price')}")

# Check TTL
ttl = r.ttl("product:1")
print(f"\nTime to live for product:1: {ttl} seconds")
```

---

## Sub-Task 2: Shopping Cart Solution

```python
# Sub-Task 2: Shopping Cart
print("\n" + "=" * 50)
print("Sub-Task 2: Shopping Cart")
print("=" * 50)

# Create cart for John (user:1)
print("\nCreating cart for John (user:1):")
r.hset("user:1:cart", mapping={
    "product:1": 1,  # 1 iPhone
    "product:3": 2,  # 2 iPads
})
print("  ✓ Added 1x iPhone 15")
print("  ✓ Added 2x iPad Air")

# Create cart for Jane (user:2)
print("\nCreating cart for Jane (user:2):")
r.hset("user:2:cart", mapping={
    "product:2": 1,  # 1 MacBook
    "product:4": 2,  # 2 AirPods
})
print("  ✓ Added 1x MacBook Pro")
print("  ✓ Added 2x AirPods Pro")

# Add Samsung TV to John's cart
r.hset("user:1:cart", "product:5", 1)
print("\n✓ Added Samsung TV to John's cart")

# Increment iPhone quantity (1 → 2)
r.hincrby("user:1:cart", "product:1", 1)
print("✓ Incremented iPhone quantity: 1 → 2")

# Display John's cart
print("\nJohn's cart:")
cart = r.hgetall("user:1:cart")
for product_id, qty in cart.items():
    product = r.hgetall(product_id)
    print(f"  {qty}x {product['name']} @ ${product['price']}")

# Remove iPad from cart
r.hdel("user:1:cart", "product:3")
print("\n✓ Removed iPad Air from John's cart")

# Set carts to expire in 30 days
r.expire("user:1:cart", 2592000)  # 30 days
r.expire("user:2:cart", 2592000)
print("✓ Set both carts to expire in 30 days")

# Display final cart
print("\nJohn's cart (after removal):")
cart = r.hgetall("user:1:cart")
print(f"  Items in cart: {r.hlen('user:1:cart')}")
for product_id, qty in cart.items():
    product = r.hgetall(product_id)
    print(f"  {qty}x {product['name']}")
```

---

## Sub-Task 3: Recently Viewed Solution

```python
# Sub-Task 3: Recently Viewed Products
print("\n" + "=" * 50)
print("Sub-Task 3: Recently Viewed Products")
print("=" * 50)

# Create view history for John
print("\nJohn's view history:")
r.lpush("user:1:viewed", "product:1")  # View iPhone
print("  ✓ Viewed product:1 (iPhone 15)")
r.lpush("user:1:viewed", "product:3")  # View iPad
print("  ✓ Viewed product:3 (iPad Air)")
r.lpush("user:1:viewed", "product:5")  # View Samsung TV
print("  ✓ Viewed product:5 (Samsung TV)")
r.lpush("user:1:viewed", "product:1")  # View iPhone again (now at front)
print("  ✓ Viewed product:1 again (moved to front)")

# Create view history for Jane
print("\nJane's view history:")
r.lpush("user:2:viewed", "product:2")  # View MacBook
print("  ✓ Viewed product:2 (MacBook Pro)")
r.lpush("user:2:viewed", "product:4")  # View AirPods
print("  ✓ Viewed product:4 (AirPods Pro)")

# Get John's 3 most recent views
print("\nJohn's 3 most recent views:")
recent = r.lrange("user:1:viewed", 0, 2)
for product_id in recent:
    product = r.hgetall(product_id)
    print(f"  → {product['name']}")

# Get Jane's entire view history
print("\nJane's view history (all):")
all_views = r.lrange("user:2:viewed", 0, -1)
for product_id in all_views:
    product = r.hgetall(product_id)
    print(f"  → {product['name']}")

# Trim John's list to 10 items
r.ltrim("user:1:viewed", 0, 9)
print("\n✓ Trimmed John's view list to 10 items max")

# Set both to expire in 7 days
r.expire("user:1:viewed", 604800)  # 7 days
r.expire("user:2:viewed", 604800)
print("✓ Set both view lists to expire in 7 days")

# Display list length
print(f"\nJohn's view list length: {r.llen('user:1:viewed')}")
print(f"Jane's view list length: {r.llen('user:2:viewed')}")
```

---

## Sub-Task 4: Trending Products Solution

```python
# Sub-Task 4: Trending Products
print("\n" + "=" * 50)
print("Sub-Task 4: Trending Products")
print("=" * 50)

# Simulate views
print("\nSimulating product views:")
for i in range(50):
    r.incr("product:1:views")
print(f"  ✓ Product 1: {r.get('product:1:views')} views")

for i in range(30):
    r.incr("product:3:views")
print(f"  ✓ Product 3: {r.get('product:3:views')} views")

for i in range(20):
    r.incr("product:5:views")
print(f"  ✓ Product 5: {r.get('product:5:views')} views")

# Add to trending sorted set
print("\nAdding to trending products (sorted set):")
view_counts = {
    1: int(r.get("product:1:views") or 0),
    3: int(r.get("product:3:views") or 0),
    5: int(r.get("product:5:views") or 0),
}

for product_id, views in view_counts.items():
    r.zadd("trending:today", {f"product:{product_id}": views})
    print(f"  ✓ {r.hget(f'product:{product_id}', 'name')}: {views} views")

# Get top 3 trending products
print("\nTop 3 trending products:")
top_products = r.zrevrange("trending:today", 0, 2, withscores=True)
for i, (product_id, score) in enumerate(top_products, 1):
    product = r.hgetall(product_id)
    print(f"  {i}. {product['name']}: {int(score)} views")

# Set to expire in 24 hours
r.expire("trending:today", 86400)
print("\n✓ Trending list set to expire in 24 hours")

# Show rankings
print("\nProduct rankings:")
for product_id in ["product:1", "product:3", "product:5"]:
    rank = r.zrevrank("trending:today", product_id)
    score = r.zscore("trending:today", product_id)
    product = r.hgetall(product_id)
    print(f"  {product['name']}: Rank #{rank + 1} with {int(score)} views")
```

---

## Sub-Task 5: Session Management Solution

```python
import json
from datetime import datetime

# Sub-Task 5: Session Management
print("\n" + "=" * 50)
print("Sub-Task 5: Session Management")
print("=" * 50)

# Create session for John
print("\nCreating session for John:")
john_session = {
    "user_id": 1,
    "username": "john",
    "login_at": datetime.now().isoformat(),
}
r.set("session:john_session_12345", 
      json.dumps(john_session), 
      ex=1800)  # 30 minutes
print(f"  ✓ Session created: {john_session['username']}")
print(f"  ✓ Expires in: 30 minutes")

# Create session for Jane
print("\nCreating session for Jane:")
jane_session = {
    "user_id": 2,
    "username": "jane",
    "login_at": datetime.now().isoformat(),
}
r.set("session:jane_session_67890", 
      json.dumps(jane_session), 
      ex=1800)  # 30 minutes
print(f"  ✓ Session created: {jane_session['username']}")
print(f"  ✓ Expires in: 30 minutes")

# Retrieve John's session
print("\nRetrieving John's session:")
john_data = json.loads(r.get("session:john_session_12345"))
print(f"  User: {john_data['username']}")
print(f"  Login time: {john_data['login_at']}")

# Check TTL
print("\nSession TTL:")
john_ttl = r.ttl("session:john_session_12345")
jane_ttl = r.ttl("session:jane_session_67890")
print(f"  John's session: {john_ttl} seconds remaining")
print(f"  Jane's session: {jane_ttl} seconds remaining")

# Refresh John's session (extend timeout)
print("\nRefreshing John's session (extending timeout):")
r.expire("session:john_session_12345", 1800)
new_ttl = r.ttl("session:john_session_12345")
print(f"  ✓ Session refreshed")
print(f"  ✓ New TTL: {new_ttl} seconds")

# Check if sessions exist
print("\nSession existence check:")
john_exists = r.exists("session:john_session_12345")
jane_exists = r.exists("session:jane_session_67890")
print(f"  John's session exists: {bool(john_exists)}")
print(f"  Jane's session exists: {bool(jane_exists)}")

# Simulate logout: delete Jane's session
print("\nSimulating logout for Jane:")
r.delete("session:jane_session_67890")
jane_exists = r.exists("session:jane_session_67890")
print(f"  ✓ Session deleted")
print(f"  ✓ Jane's session now exists: {bool(jane_exists)}")
```

---

## Complete Integration Test

```python
# Complete integration test
print("\n" + "=" * 50)
print("Complete System Summary")
print("=" * 50)

print("\n📦 Products Cached:")
for i in range(1, 6):
    key = f"product:{i}"
    if r.exists(key):
        product = r.hgetall(key)
        ttl = r.ttl(key)
        print(f"  ✓ {product['name']} (expires in {ttl}s)")

print("\n🛒 Shopping Carts:")
for user in [1, 2]:
    key = f"user:{user}:cart"
    if r.exists(key):
        count = r.hlen(key)
        ttl = r.ttl(key)
        print(f"  ✓ User {user}: {count} items (expires in {ttl}s)")

print("\n👁️ View Histories:")
for user in [1, 2]:
    key = f"user:{user}:viewed"
    if r.exists(key):
        count = r.llen(key)
        ttl = r.ttl(key)
        print(f"  ✓ User {user}: {count} views (expires in {ttl}s)")

print("\n🔥 Trending Products:")
trending = r.zrevrange("trending:today", 0, -1, withscores=True)
for product_id, score in trending:
    product = r.hgetall(product_id)
    ttl = r.ttl("trending:today")
    print(f"  ✓ {product['name']}: {int(score)} views")

print("\n🔐 Active Sessions:")
john_exists = r.exists("session:john_session_12345")
jane_exists = r.exists("session:jane_session_67890")
print(f"  ✓ John's session: {'Active' if john_exists else 'Expired'}")
print(f"  ✓ Jane's session: {'Active' if jane_exists else 'Expired'}")

print("\n" + "=" * 50)
print("✅ All sub-tasks complete!")
print("=" * 50)
```

---

## Running This Solution

```bash
# Save as redis_lab_solution.py
python redis_lab_solution.py

# You should see output from all 5 sub-tasks
# showing products, carts, views, trending, and sessions
```

---

## Key Concepts Demonstrated

✅ **Hashes:** Product cache and shopping cart  
✅ **Strings:** Session data and view counters  
✅ **Lists:** View history (ordered)  
✅ **Sorted Sets:** Trending products (ranked)  
✅ **Expiration:** TTL and auto-cleanup  
✅ **JSON Storage:** Complex data in strings  
✅ **Atomic Operations:** HINCRBY, INCR, ZADD  

