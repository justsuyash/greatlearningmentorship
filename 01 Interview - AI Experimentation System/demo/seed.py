import duckdb
import random
import numpy as np

# Fixed seed for deterministic demo replication
random.seed(42)
np.random.seed(42)

def seed_database():
    conn = duckdb.connect("warehouse.duckdb")
    
    # Drop tables if they exist
    conn.execute("DROP TABLE IF EXISTS ab_test_events")
    conn.execute("DROP TABLE IF EXISTS user_stats")
    
    # Create ab_test_events
    conn.execute("""
    CREATE TABLE ab_test_events (
        session_id TEXT,
        experiment_id TEXT,
        variant TEXT,
        converted INTEGER,
        revenue REAL,
        load_time_ms INTEGER,
        error_rate REAL,
        event_date TEXT
    )
    """)
    
    # Generate EXP_CART_REDESIGN control
    print("Seeding EXP_CART_REDESIGN control...")
    n_control = 150000
    conv_control = 3000
    converted_ctrl = [1]*conv_control + [0]*(n_control-conv_control)
    random.shuffle(converted_ctrl)
    
    # Control AOV is exactly 50
    # Revenue is 0 if not converted, 50 if converted
    
    control_data = []
    for i in range(n_control):
        c = converted_ctrl[i]
        r = 50.0 if c == 1 else 0.0
        control_data.append((
            f"ctrl_{i}", "EXP_CART_REDESIGN", "control",
            c, r,
            random.randint(900, 1400),
            round(random.uniform(0.008, 0.016), 4),
            f"2026-05-{random.randint(1,15):02d}"
        ))
        
    import pandas as pd
    df_ctrl = pd.DataFrame(control_data, columns=["session_id", "experiment_id", "variant", "converted", "revenue", "load_time_ms", "error_rate", "event_date"])
    conn.execute("INSERT INTO ab_test_events SELECT * FROM df_ctrl")
    
    # Generate EXP_CART_REDESIGN treatment
    print("Seeding EXP_CART_REDESIGN treatment...")
    n_trt = 151000
    conv_trt = 3450
    converted_trt = [1]*conv_trt + [0]*(n_trt-conv_trt)
    random.shuffle(converted_trt)
    
    # Treatment AOV is ~50.7246 -> total 175000
    # We will just assign exactly 175000/3450 to each converted to be safe
    trt_aov = 175000.0 / 3450.0
    
    trt_data = []
    for i in range(n_trt):
        c = converted_trt[i]
        r = trt_aov if c == 1 else 0.0
        # Treatment has higher error rate (0.015 - 0.025)
        trt_data.append((
            f"trt_{i}", "EXP_CART_REDESIGN", "treatment",
            c, r,
            random.randint(900, 1400),
            round(random.uniform(0.015, 0.025), 4),
            f"2026-05-{random.randint(1,15):02d}"
        ))
        
    df_trt = pd.DataFrame(trt_data, columns=["session_id", "experiment_id", "variant", "converted", "revenue", "load_time_ms", "error_rate", "event_date"])
    conn.execute("INSERT INTO ab_test_events SELECT * FROM df_trt")
    
    # Create user_stats for CUPED
    print("Seeding user_stats for CUPED...")
    conn.execute("""
    CREATE TABLE user_stats (
        user_id TEXT,
        experiment_id TEXT,
        variant TEXT,
        pre_revenue REAL,
        post_revenue REAL,
        pre_converted INTEGER,
        post_converted INTEGER
    )
    """)
    
    # Seed user_stats with positive correlation
    user_stats = []
    for i in range(10000): # Just 10k sample for speed
        pre_rev = random.choice([0.0, 0.0, 50.0, 100.0])
        # correlation mock:
        post_rev = pre_rev if random.random() < 0.7 else random.choice([0.0, 50.0])
        user_stats.append((
            f"usr_{i}", "EXP_CART_REDESIGN", "control" if i%2==0 else "treatment",
            pre_rev, post_rev,
            1 if pre_rev > 0 else 0,
            1 if post_rev > 0 else 0
        ))
    df_user_stats = pd.DataFrame(user_stats, columns=["user_id", "experiment_id", "variant", "pre_revenue", "post_revenue", "pre_converted", "post_converted"])
    conn.execute("INSERT INTO user_stats SELECT * FROM df_user_stats")

    # Ingest Real CSVs for EXP_NEW_PRICING
    print("Seeding EXP_NEW_PRICING from real CSVs...")
    import os
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DATA_DIR = os.path.join(BASE_DIR, "..", "Pricing_Test_Data")
    
    test_csv = os.path.join(DATA_DIR, "test_results.csv")
    user_csv = os.path.join(DATA_DIR, "user_table.csv") # Actually named user_table.csv not user_table-2.csv
    
    conn.execute("DROP TABLE IF EXISTS raw_pricing_events")
    conn.execute(f"""
        CREATE TABLE raw_pricing_events AS 
        SELECT * FROM read_csv_auto('{test_csv}')
    """)
    
    conn.execute("DROP TABLE IF EXISTS user_locations")
    conn.execute(f"""
        CREATE TABLE user_locations AS
        SELECT * FROM read_csv_auto('{user_csv}')
    """)
    
    # Append the clean data to ab_test_events
    conn.execute("""
        INSERT INTO ab_test_events
        SELECT 
            CAST(user_id AS VARCHAR) as session_id,
            'EXP_NEW_PRICING' as experiment_id,
            CASE WHEN test=0 THEN 'control' ELSE 'treatment' END as variant,
            converted,
            converted * price as revenue,
            1200 as load_time_ms, -- Mock guardrail data
            0.01 as error_rate,   -- Mock guardrail data
            CAST(timestamp AS VARCHAR) as event_date
        FROM raw_pricing_events
        -- Remove misassigned price rows (data quality fix)
        WHERE NOT (test=0 AND price=59) 
        AND NOT (test=1 AND price=39)
        AND operative_system != 'linux'  -- remove bug segment
    """)

    print("✅ Database seeded successfully (warehouse.duckdb)")
    conn.close()

if __name__ == "__main__":
    seed_database()
