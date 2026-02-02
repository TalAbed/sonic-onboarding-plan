# Redis Lab: Starter Code & Demo

Complete runnable Python script demonstrating all 5 sub-tasks.

---

## Quick Start

```bash
# Install Redis (if not already done)
pip install redis

# Make sure Redis is running
redis-cli ping
# Should return: PONG

# Run this demo
python demo.py
```

---

## Complete Demo Script

```python
#!/usr/bin/env python3
"""
Redis Lab: Complete E-Commerce Caching System Demo

This script demonstrates all 5 sub-tasks:
1. Product Cache
2. Shopping Cart
3. Recently Viewed
4. Trending Products
5. Session Management

Run: python demo.py
"""

import redis
import json
from datetime import datetime
import time

# ============================================================================
# SETUP
# ============================================================================

def setup():
    """Connect to Redis and clear database"""
    r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
    
    # Verify connection
    try:
        r.ping()
        print("✓ Connected to Redis")
    except Exception as e:
        print(f"✗ Failed to connect to Redis: {e}")
        print("Make sure Redis is running: redis-cli ping")
        exit(1)
    
    # Clear database for fresh start (optional)
    # r.flushdb()
    # print("✓ Database cleared")
    
    return r

# ============================================================================
# SUB-TASK 1: PRODUCT CACHE
# ============================================================================

def task_1_product_cache(r):
    """Sub-Task 1: Store products with Hashes + TTL"""
    print("\n" + "=" * 70)
    print("SUB-TASK 1: Product Cache")
    print("=" * 70)
    
    # Sample products
    products = {
        1: {"name": "iPhone 15", "price": 999, "category": "Electronics", "stock": 50},
        2: {"name": "MacBook Pro", "price": 2499, "category": "Electronics", "stock": 25},
        3: {"name": "iPad Air", "price": 599, "category": "Electronics", "stock": 40},
        4: {"name": "AirPods Pro", "price": 249, "category": "Electronics", "stock": 100},
        5: {"name": "Samsung TV", "price": 799, "category": "Electronics", "stock": 15},
    }
    
    print("\n1. Storing 5 products with HASHES + 1-hour TTL:")
    for product_id, product_data in products.items():
        key = f"product:{product_id}"
        r.hset(key, mapping=product_data)
        r.expire(key, 3600)  # 1 hour
        print(f"   ✓ {product_data['name']} (${product_data['price']})")
    
    print("\n2. Retrieving product:1:")
    product_1 = r.hgetall("product:1")
    print(f"   {product_1}")
    
    print("\n3. Updating iPhone 15 price: $999 → $899")
    r.hset("product:1", "price", 899)
    print(f"   ✓ Updated price: {r.hget('product:1', 'price')}")
    
    print("\n4. Checking TTL:")
    ttl = r.ttl("product:1")
    print(f"   ✓ product:1 expires in {ttl} seconds (~1 hour)")

# ============================================================================
# SUB-TASK 2: SHOPPING CART
# ============================================================================

def task_2_shopping_cart(r):
    """Sub-Task 2: Persistent user shopping carts"""
    print("\n" + "=" * 70)
    print("SUB-TASK 2: Shopping Cart")
    print("=" * 70)
    
    print("\n1. Creating cart for John (user:1):")
    r.hset("user:1:cart", mapping={
        "product:1": 1,  # 1 iPhone
        "product:3": 2,  # 2 iPads
    })
    print("   ✓ Added 1x iPhone 15")
    print("   ✓ Added 2x iPad Air")
    
    print("\n2. Creating cart for Jane (user:2):")
    r.hset("user:2:cart", mapping={
        "product:2": 1,  # 1 MacBook
        "product:4": 2,  # 2 AirPods
    })
    print("   ✓ Added 1x MacBook Pro")
    print("   ✓ Added 2x AirPods Pro")
    
    print("\n3. Adding Samsung TV to John's cart:")
    r.hset("user:1:cart", "product:5", 1)
    print("   ✓ Added 1x Samsung TV")
    
    print("\n4. Incrementing iPhone quantity (1 → 2):")
    r.hincrby("user:1:cart", "product:1", 1)
    print("   ✓ Incremented using HINCRBY")
    
    print("\n5. John's current cart:")
    cart = r.hgetall("user:1:cart")
    for product_id, qty in cart.items():
        product = r.hgetall(product_id)
        price = float(product['price'])
        print(f"   {qty}x {product['name']} @ ${price:.2f} = ${price * int(qty):.2f}")
    
    print("\n6. Removing iPad Air from cart:")
    r.hdel("user:1:cart", "product:3")
    print("   ✓ Removed using HDEL")
    
    print("\n7. Setting carts to expire in 30 days:")
    r.expire("user:1:cart", 2592000)
    r.expire("user:2:cart", 2592000)
    print("   ✓ Both carts will auto-cleanup in 30 days")
    
    print("\n8. Final cart for John:")
    cart = r.hgetall("user:1:cart")
    print(f"   Items in cart: {r.hlen('user:1:cart')}")
    for product_id, qty in cart.items():
        product = r.hgetall(product_id)
        print(f"   → {qty}x {product['name']}")

# ============================================================================
# SUB-TASK 3: RECENTLY VIEWED
# ============================================================================

def task_3_recently_viewed(r):
    """Sub-Task 3: Track view history with Lists"""
    print("\n" + "=" * 70)
    print("SUB-TASK 3: Recently Viewed Products")
    print("=" * 70)
    
    print("\n1. John's view history (in order):")
    r.lpush("user:1:viewed", "product:1")
    print("   ✓ Viewed product:1 (iPhone 15)")
    r.lpush("user:1:viewed", "product:3")
    print("   ✓ Viewed product:3 (iPad Air)")
    r.lpush("user:1:viewed", "product:5")
    print("   ✓ Viewed product:5 (Samsung TV)")
    r.lpush("user:1:viewed", "product:1")
    print("   ✓ Viewed product:1 again (moved to front)")
    
    print("\n2. Jane's view history:")
    r.lpush("user:2:viewed", "product:2")
    print("   ✓ Viewed product:2 (MacBook Pro)")
    r.lpush("user:2:viewed", "product:4")
    print("   ✓ Viewed product:4 (AirPods Pro)")
    
    print("\n3. John's 3 most recent views:")
    recent = r.lrange("user:1:viewed", 0, 2)
    for i, product_id in enumerate(recent, 1):
        product = r.hgetall(product_id)
        print(f"   {i}. {product['name']}")
    
    print("\n4. Jane's entire view history:")
    all_views = r.lrange("user:2:viewed", 0, -1)
    for i, product_id in enumerate(all_views, 1):
        product = r.hgetall(product_id)
        print(f"   {i}. {product['name']}")
    
    print("\n5. Trimming John's list to 10 items max:")
    r.ltrim("user:1:viewed", 0, 9)
    print("   ✓ Trimmed using LTRIM")
    
    print("\n6. Setting both to expire in 7 days:")
    r.expire("user:1:viewed", 604800)
    r.expire("user:2:viewed", 604800)
    print("   ✓ View lists will auto-cleanup in 7 days")
    
    print("\n7. List lengths:")
    print(f"   John's view list: {r.llen('user:1:viewed')} items")
    print(f"   Jane's view list: {r.llen('user:2:viewed')} items")

# ============================================================================
# SUB-TASK 4: TRENDING PRODUCTS
# ============================================================================

def task_4_trending_products(r):
    """Sub-Task 4: Rank products by popularity"""
    print("\n" + "=" * 70)
    print("SUB-TASK 4: Trending Products")
    print("=" * 70)
    
    print("\n1. Simulating product views (INCR counters):")
    for i in range(50):
        r.incr("product:1:views")
    print(f"   ✓ product:1: 50 views")
    
    for i in range(30):
        r.incr("product:3:views")
    print(f"   ✓ product:3: 30 views")
    
    for i in range(20):
        r.incr("product:5:views")
    print(f"   ✓ product:5: 20 views")
    
    print("\n2. Adding to trending (ZADD to sorted set):")
    view_counts = {
        1: int(r.get("product:1:views") or 0),
        3: int(r.get("product:3:views") or 0),
        5: int(r.get("product:5:views") or 0),
    }
    
    for product_id, views in view_counts.items():
        r.zadd("trending:today", {f"product:{product_id}": views})
        product = r.hgetall(f"product:{product_id}")
        print(f"   ✓ {product['name']}: {views} views")
    
    print("\n3. Getting top 3 trending products (ZREVRANGE):")
    top_products = r.zrevrange("trending:today", 0, 2, withscores=True)
    for i, (product_id, score) in enumerate(top_products, 1):
        product = r.hgetall(product_id)
        print(f"   #{i} {product['name']}: {int(score)} views")
    
    print("\n4. Setting to expire in 24 hours:")
    r.expire("trending:today", 86400)
    print("   ✓ Trending list will reset daily")
    
    print("\n5. Product rankings (ZREVRANK):")
    for product_id in [1, 3, 5]:
        rank = r.zrevrank("trending:today", f"product:{product_id}")
        score = r.zscore("trending:today", f"product:{product_id}")
        product = r.hgetall(f"product:{product_id}")
        print(f"   Rank #{rank + 1}: {product['name']} ({int(score)} views)")

# ============================================================================
# SUB-TASK 5: SESSION MANAGEMENT
# ============================================================================

def task_5_session_management(r):
    """Sub-Task 5: Auto-expiring user sessions"""
    print("\n" + "=" * 70)
    print("SUB-TASK 5: Session Management")
    print("=" * 70)
    
    print("\n1. Creating session for John (30-min timeout):")
    john_session = {
        "user_id": 1,
        "username": "john",
        "login_at": datetime.now().isoformat(),
    }
    r.set("session:john_session_12345", 
          json.dumps(john_session), 
          ex=1800)  # 30 minutes
    print(f"   ✓ Session: {john_session['username']}")
    print(f"   ✓ Expires in: 30 minutes (1800 seconds)")
    
    print("\n2. Creating session for Jane (30-min timeout):")
    jane_session = {
        "user_id": 2,
        "username": "jane",
        "login_at": datetime.now().isoformat(),
    }
    r.set("session:jane_session_67890", 
          json.dumps(jane_session), 
          ex=1800)
    print(f"   ✓ Session: {jane_session['username']}")
    print(f"   ✓ Expires in: 30 minutes (1800 seconds)")
    
    print("\n3. Retrieving John's session data:")
    john_data = json.loads(r.get("session:john_session_12345"))
    print(f"   Username: {john_data['username']}")
    print(f"   User ID: {john_data['user_id']}")
    print(f"   Login time: {john_data['login_at']}")
    
    print("\n4. Checking session TTL (time remaining):")
    john_ttl = r.ttl("session:john_session_12345")
    jane_ttl = r.ttl("session:jane_session_67890")
    print(f"   John's session: ~{john_ttl} seconds remaining")
    print(f"   Jane's session: ~{jane_ttl} seconds remaining")
    
    print("\n5. Simulating user activity (refreshing John's session):")
    r.expire("session:john_session_12345", 1800)
    new_ttl = r.ttl("session:john_session_12345")
    print(f"   ✓ Session refreshed")
    print(f"   ✓ New TTL: ~{new_ttl} seconds")
    
    print("\n6. Checking session existence:")
    john_exists = r.exists("session:john_session_12345")
    jane_exists = r.exists("session:jane_session_67890")
    print(f"   John's session exists: {bool(john_exists)}")
    print(f"   Jane's session exists: {bool(jane_exists)}")
    
    print("\n7. Simulating logout (deleting Jane's session):")
    r.delete("session:jane_session_67890")
    jane_exists = r.exists("session:jane_session_67890")
    print(f"   ✓ Session deleted")
    print(f"   ✓ Jane's session now exists: {bool(jane_exists)}")

# ============================================================================
# SUMMARY
# ============================================================================

def summary(r):
    """Show complete system summary"""
    print("\n" + "=" * 70)
    print("COMPLETE SYSTEM SUMMARY")
    print("=" * 70)
    
    print("\n📦 Products Cached:")
    for i in range(1, 6):
        key = f"product:{i}"
        if r.exists(key):
            product = r.hgetall(key)
            ttl = r.ttl(key)
            print(f"   ✓ {product['name']} (expires in {ttl}s)")
    
    print("\n🛒 Shopping Carts:")
    for user in [1, 2]:
        key = f"user:{user}:cart"
        if r.exists(key):
            count = r.hlen(key)
            ttl = r.ttl(key)
            print(f"   ✓ User {user}: {count} items (expires in {ttl}s)")
    
    print("\n👁️ View Histories:")
    for user in [1, 2]:
        key = f"user:{user}:viewed"
        if r.exists(key):
            count = r.llen(key)
            ttl = r.ttl(key)
            print(f"   ✓ User {user}: {count} views (expires in {ttl}s)")
    
    print("\n🔥 Trending Products:")
    trending = r.zrevrange("trending:today", 0, -1, withscores=True)
    if trending:
        for product_id, score in trending:
            product = r.hgetall(product_id)
            print(f"   ✓ {product['name']}: {int(score)} views")
    
    print("\n🔐 Active Sessions:")
    john_exists = r.exists("session:john_session_12345")
    jane_exists = r.exists("session:jane_session_67890")
    print(f"   ✓ John's session: {'Active' if john_exists else 'Expired'}")
    print(f"   ✓ Jane's session: {'Active' if jane_exists else 'Expired'}")
    
    print("\n" + "=" * 70)
    print("✅ ALL SUB-TASKS COMPLETE!")
    print("=" * 70)
    print("\nYou've built a complete e-commerce caching system with:")
    print("  • Product caching with TTL")
    print("  • Persistent shopping carts")
    print("  • View history tracking")
    print("  • Real-time trending")
    print("  • Session management")
    print("\nNow try implementing these yourself! 🚀")

# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    print("\n" + "=" * 70)
    print("REDIS LAB: COMPLETE E-COMMERCE CACHING SYSTEM")
    print("=" * 70)
    
    # Connect to Redis
    r = setup()
    
    # Run all 5 sub-tasks
    task_1_product_cache(r)
    task_2_shopping_cart(r)
    task_3_recently_viewed(r)
    task_4_trending_products(r)
    task_5_session_management(r)
    
    # Show summary
    summary(r)

```

---

## How to Use

1. **Save as `demo.py`:**
   ```bash
   cp demo.py starter-code/demo.py
   ```

2. **Make sure Redis is running:**
   ```bash
   redis-cli ping
   # Should return: PONG
   ```

3. **Run the demo:**
   ```bash
   python demo.py
   ```

4. **Expected output:**
   - All 5 sub-tasks execute with detailed output
   - Shows what commands do
   - Displays final system state
   - ~300 lines of console output

---

## What This Demo Shows

✅ All 5 sub-tasks in action  
✅ How each data structure works  
✅ Real values and output  
✅ TTL and expiration  
✅ Complete system integration  
✅ Ready to run immediately  

---

## Customization

Students can:
- Modify sample data
- Change TTL values
- Add more products/users
- Experiment with commands
- Build their own demo

