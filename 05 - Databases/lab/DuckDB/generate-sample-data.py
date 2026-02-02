#!/usr/bin/env python3
"""
DuckDB Lab: Sample Data Generator

This script generates sample CSV files for the DuckDB lab exercises.
Run this ONCE before starting the lab to create all required data files.

Usage:
    python generate_sample_data.py

Output:
    Creates sample-data/ directory with:
    - users.csv (1000 rows)
    - products.csv (500 rows)
    - orders.csv (5000 rows)
"""

import csv
import os
from datetime import datetime, timedelta
import random

# ============================================================================
# CONFIGURATION
# ============================================================================

NUM_USERS = 1000
NUM_PRODUCTS = 500
NUM_ORDERS = 5000

SAMPLE_DATA_DIR = 'sample-data'

# ============================================================================
# SAMPLE DATA DEFINITIONS
# ============================================================================

COUNTRIES = ['USA', 'UK', 'Canada', 'Australia', 'Germany', 'France', 'India', 'Japan', 'Brazil', 'Mexico']

CATEGORIES = ['Electronics', 'Clothing', 'Home', 'Sports', 'Books', 'Food', 'Beauty']

PRODUCT_TEMPLATES = [
    'iPhone 15', 'MacBook Pro', 'iPad Air', 'AirPods Pro', 'Samsung TV',
    'Laptop Stand', 'USB-C Cable', 'Monitor', 'Keyboard', 'Mouse',
    'T-Shirt', 'Jeans', 'Hoodie', 'Shoes', 'Hat',
    'Coffee Maker', 'Blender', 'Toaster', 'Microwave', 'Desk Lamp',
    'Running Shoes', 'Yoga Mat', 'Dumbbell Set', 'Bicycle', 'Tent',
    'Python Book', 'SQL Guide', 'Data Science', 'Machine Learning', 'Web Dev',
    'Desk Chair', 'Filing Cabinet', 'Bookshelf', 'Desk Organizer', 'Whiteboard',
    'Coffee Mug', 'Water Bottle', 'Lunch Box', 'Plate Set', 'Utensil Set',
    'Jacket', 'Pants', 'Sweater', 'Socks', 'Gloves',
    'Headphones', 'Speaker', 'Microphone', 'USB Hub', 'External Drive'
]

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def create_sample_data_dir():
    """Create sample-data directory if it doesn't exist"""
    os.makedirs(SAMPLE_DATA_DIR, exist_ok=True)
    print(f"✓ Directory '{SAMPLE_DATA_DIR}' created/verified")

def generate_users_csv():
    """Generate users.csv with 1000 sample users"""
    filepath = os.path.join(SAMPLE_DATA_DIR, 'users.csv')
    
    print(f"\n📝 Generating {NUM_USERS} users...")
    
    start_date = datetime(2022, 1, 1)
    
    with open(filepath, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['user_id', 'username', 'country', 'signup_date'])
        
        for i in range(1, NUM_USERS + 1):
            user_id = i
            username = f'user_{i:04d}'
            country = random.choice(COUNTRIES)
            signup_date = start_date + timedelta(days=random.randint(0, 730))
            
            writer.writerow([user_id, username, country, signup_date.date()])
            
            if i % 200 == 0:
                print(f"   Generated {i}/{NUM_USERS} users...")
    
    print(f"✓ Created {filepath} ({NUM_USERS} rows)")
    return filepath

def generate_products_csv():
    """Generate products.csv with 500 sample products"""
    filepath = os.path.join(SAMPLE_DATA_DIR, 'products.csv')
    
    print(f"\n📝 Generating {NUM_PRODUCTS} products...")
    
    with open(filepath, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['product_id', 'name', 'price', 'category'])
        
        for i in range(1, NUM_PRODUCTS + 1):
            product_id = i
            
            # Create product name by cycling through templates
            template = PRODUCT_TEMPLATES[(i - 1) % len(PRODUCT_TEMPLATES)]
            variant = (i - 1) // len(PRODUCT_TEMPLATES) + 1
            name = f'{template} v{variant}' if variant > 1 else template
            
            # Generate price: varies by category
            base_price = random.uniform(10, 3000)
            price = round(base_price, 2)
            
            category = random.choice(CATEGORIES)
            
            writer.writerow([product_id, name, price, category])
            
            if i % 100 == 0:
                print(f"   Generated {i}/{NUM_PRODUCTS} products...")
    
    print(f"✓ Created {filepath} ({NUM_PRODUCTS} rows)")
    return filepath

def generate_orders_csv():
    """Generate orders.csv with 5000 sample orders"""
    filepath = os.path.join(SAMPLE_DATA_DIR, 'orders.csv')
    
    print(f"\n📝 Generating {NUM_ORDERS} orders...")
    
    start_date = datetime(2023, 1, 1)
    
    with open(filepath, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['order_id', 'user_id', 'product_id', 'order_date', 'amount'])
        
        for order_id in range(1, NUM_ORDERS + 1):
            user_id = random.randint(1, NUM_USERS)
            product_id = random.randint(1, NUM_PRODUCTS)
            order_date = start_date + timedelta(days=random.randint(0, 365))
            amount = round(random.uniform(10, 2500), 2)
            
            writer.writerow([order_id, user_id, product_id, order_date.date(), amount])
            
            if order_id % 1000 == 0:
                print(f"   Generated {order_id}/{NUM_ORDERS} orders...")
    
    print(f"✓ Created {filepath} ({NUM_ORDERS} rows)")
    return filepath

def verify_data():
    """Verify generated data by reading CSV headers and row counts"""
    print("\n✅ VERIFICATION:")
    
    for filename in ['users.csv', 'products.csv', 'orders.csv']:
        filepath = os.path.join(SAMPLE_DATA_DIR, filename)
        
        if not os.path.exists(filepath):
            print(f"   ✗ {filename} not found!")
            continue
        
        # Count rows
        with open(filepath, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            headers = next(reader)
            row_count = sum(1 for _ in reader)
        
        # Get file size
        file_size = os.path.getsize(filepath) / 1024  # KB
        
        print(f"   ✓ {filename}")
        print(f"      Columns: {', '.join(headers)}")
        print(f"      Rows: {row_count}")
        print(f"      Size: {file_size:.1f} KB")

def main():
    """Main function to generate all sample data"""
    print("\n" + "=" * 70)
    print("DUCKDB LAB: SAMPLE DATA GENERATOR")
    print("=" * 70)
    
    print("\nThis will create sample CSV files for the DuckDB lab.")
    print(f"  • Users: {NUM_USERS} rows")
    print(f"  • Products: {NUM_PRODUCTS} rows")
    print(f"  • Orders: {NUM_ORDERS} rows")
    print(f"  • Output directory: {SAMPLE_DATA_DIR}/")
    
    # Create directory
    create_sample_data_dir()
    
    # Generate CSVs
    users_file = generate_users_csv()
    products_file = generate_products_csv()
    orders_file = generate_orders_csv()
    
    # Verify
    verify_data()
    
    # Summary
    print("\n" + "=" * 70)
    print("✅ SAMPLE DATA GENERATION COMPLETE!")
    print("=" * 70)
    print("\nNext steps:")
    print("  1. Run the demo: python demo.py")
    print("  2. Or start the exercises: see instructions/exercise-analytics-pipeline.md")
    print("\nYour data is ready! 🚀\n")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n✗ ERROR: {e}")
        import traceback
        traceback.print_exc()
