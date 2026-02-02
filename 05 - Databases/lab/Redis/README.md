# Redis Lab: Essentials

## 🎯 Lab Overview

**Name:** Redis Essentials: Real-Time Caching for E-Commerce

**Time:** 1.5-2 hours  
**Difficulty:** Beginner-Intermediate  
**Prerequisites:** Basic understanding of databases (from PostgreSQL lab optional but helpful)

---

## 📚 What You'll Learn

✅ Redis key-value data model  
✅ All 5 major data structures (strings, hashes, lists, sets, sorted sets)  
✅ TTL (Time-To-Live) and expiration patterns  
✅ Real-time caching strategies  
✅ Python redis-py library integration  

---

## 🏗️ Lab Structure

**Single comprehensive exercise** with 5 interconnected sub-tasks:

1. **Product Cache** (20 min) - Store product info with Hashes + TTL
2. **Shopping Cart** (20 min) - Build persistent user carts
3. **Recently Viewed** (15 min) - Track view history with Lists
4. **Trending Products** (20 min) - Rank popularity with Sorted Sets
5. **Session Management** (20 min) - Handle user sessions with auto-expiry

**Total time: 1.5-2 hours**

---

## 🚀 Quick Start

### 1. Install Redis (Using Docker)

```bash
docker run -d -p 6379:6379 redis:latest
```

### 2. Install Redis CLI (redis-py)

```bash
pip install redis
```

### 3. Start Lab

```bash
redis-cli ping
# Should return: PONG
```

---

## 📋 Exercise Overview

You'll build a **complete caching layer** for an e-commerce platform:

- **Users:** 2 sample users (John, Jane)
- **Products:** 5 sample products (iPhone, MacBook, iPad, AirPods, Samsung TV)
- **Build:** Caching system with products, carts, history, trending, sessions

---

## 🎯 Learning Path

```
Start → Sub-Task 1 → Sub-Task 2 → Sub-Task 3 → Sub-Task 4 → Sub-Task 5 → Complete!
```

---

## 📂 Lab Files

- `instructions/` - Exercise hints (start here!)
- `solutions/` - Complete Python solutions
- `starter-code/` - Helper functions and setup

---

## ✅ How to Use This Lab

1. **Follow exercise instructions** and implement in Python
2. **Check solutions** if you get stuck
3. **Run complete demo** from `starter-code/demo.py`

---

## 🎓 What You'll Build

By the end, you'll have:

✅ Cached product database (fast lookups)  
✅ Persistent shopping carts (auto-cleanup)  
✅ View history tracking (personalization)  
✅ Real-time trending products (analytics)  
✅ User session management (authentication)  

---

## 💡 Tips

- Use `redis-cli` to visualize what's happening
- Type `MONITOR` in redis-cli to see all commands
- Type `KEYS *` to see all keys
- Type `TTL key_name` to check expiration

---

## 📞 Quick Reference

**Common Commands:**
- `SET key value` - Store string
- `HSET hash field value` - Store hash field
- `LPUSH list value` - Add to list front
- `ZADD zset score member` - Add to sorted set
- `EXPIRE key seconds` - Set TTL
- `KEYS pattern` - Find keys

---

## Good luck! 🚀

