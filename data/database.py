"""
Database Setup and Initialization for Harbor Docker Learning

Educational Purpose: This module manages the SQLite database that stores
tutorial content and tracks user progress.

Why SQLite? It's lightweight, requires no separate server, and is perfect
for learning applications where simplicity is key.
"""

import sqlite3
import os
from pathlib import Path
from typing import Optional
from data.models import DATABASE_SCHEMAS


# Database file path
DB_DIR = Path(__file__).parent.parent / "db"
DB_PATH = DB_DIR / "tutorials.sqlite"


def get_db_connection() -> sqlite3.Connection:
    """
    Get a connection to the SQLite database

    Educational Note: This function ensures we always use the same database
    file and that connections are configured consistently.

    Returns:
        sqlite3.Connection: Active database connection
    """
    # Ensure the db directory exists
    DB_DIR.mkdir(exist_ok=True)

    # Create connection with row factory for easier data access
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row  # Access columns by name

    # Enable foreign key constraints
    # Educational note: This ensures data integrity between related tables
    conn.execute("PRAGMA foreign_keys = ON;")

    return conn


def init_database(drop_existing: bool = False) -> bool:
    """
    Initialize the database with required tables

    Educational Value: Sets up the foundation for storing and retrieving
    tutorial content and user progress.

    Args:
        drop_existing: If True, drop existing tables first (useful for development)

    Returns:
        bool: True if initialization successful, False otherwise
    """
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # If requested, drop existing tables (CAUTION: Deletes all data)
        if drop_existing:
            print("⚠️  Dropping existing tables...")
            cursor.execute("DROP TABLE IF EXISTS user_progress;")
            cursor.execute("DROP TABLE IF EXISTS container_states;")
            cursor.execute("DROP TABLE IF EXISTS tutorials;")
            print("   Tables dropped.")

        # Create all tables from schemas
        print("📊 Creating database tables...")

        for table_name, schema in DATABASE_SCHEMAS.items():
            print(f"   Creating table: {table_name}")
            cursor.execute(schema)

        # Create indexes for better query performance
        # Educational note: Indexes speed up searches, important for good UX
        print("🔍 Creating indexes for better performance...")

        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_tutorials_section
            ON tutorials(section);
        """)

        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_user_progress_tutorial_id
            ON user_progress(tutorial_id);
        """)

        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_container_states_name
            ON container_states(container_name);
        """)

        # Commit changes
        conn.commit()
        conn.close()

        print(f"✅ Database initialized successfully at: {DB_PATH}")
        return True

    except sqlite3.Error as e:
        print(f"❌ Database initialization error: {e}")
        return False


def verify_database() -> bool:
    """
    Verify that the database exists and has required tables

    Educational Purpose: Health check to ensure the database is properly set up

    Returns:
        bool: True if database is valid, False otherwise
    """
    if not DB_PATH.exists():
        print(f"❌ Database not found at: {DB_PATH}")
        return False

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Check for required tables
        required_tables = ['tutorials', 'user_progress', 'container_states']

        cursor.execute("""
            SELECT name FROM sqlite_master
            WHERE type='table' AND name NOT LIKE 'sqlite_%';
        """)

        existing_tables = [row[0] for row in cursor.fetchall()]

        missing_tables = set(required_tables) - set(existing_tables)

        if missing_tables:
            print(f"❌ Missing tables: {missing_tables}")
            conn.close()
            return False

        # Verify we can query the tables
        for table in required_tables:
            cursor.execute(f"SELECT COUNT(*) FROM {table};")
            count = cursor.fetchone()[0]
            print(f"✅ Table '{table}' exists with {count} rows")

        conn.close()
        return True

    except sqlite3.Error as e:
        print(f"❌ Database verification error: {e}")
        return False


def get_database_info() -> dict:
    """
    Get information about the database

    Returns:
        dict: Database statistics and info
    """
    if not DB_PATH.exists():
        return {"exists": False}

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        info = {
            "exists": True,
            "path": str(DB_PATH),
            "size_bytes": DB_PATH.stat().st_size,
            "tables": {}
        }

        # Get table information
        cursor.execute("""
            SELECT name FROM sqlite_master
            WHERE type='table' AND name NOT LIKE 'sqlite_%';
        """)

        for row in cursor.fetchall():
            table_name = row[0]
            cursor.execute(f"SELECT COUNT(*) FROM {table_name};")
            count = cursor.fetchone()[0]
            info["tables"][table_name] = count

        conn.close()
        return info

    except sqlite3.Error as e:
        return {"exists": True, "error": str(e)}


def reset_database() -> bool:
    """
    Reset the database by dropping and recreating all tables

    ⚠️ WARNING: This will delete all data!

    Educational Note: Use this during development to start fresh

    Returns:
        bool: True if reset successful
    """
    print("🔄 Resetting database...")
    print("⚠️  This will delete ALL data!")

    return init_database(drop_existing=True)


if __name__ == "__main__":
    """
    Script can be run directly to initialize the database

    Usage:
        python data/database.py         # Initialize database
        python data/database.py reset   # Reset database (delete all data)
    """
    import sys

    print("=" * 60)
    print("🚢 Harbor Docker Learning - Database Setup")
    print("=" * 60)

    if len(sys.argv) > 1 and sys.argv[1] == "reset":
        # Reset database
        success = reset_database()
    else:
        # Normal initialization
        success = init_database(drop_existing=False)

    if success:
        print("\n📋 Database Information:")
        print("-" * 60)
        verify_database()

        info = get_database_info()
        if "size_bytes" in info:
            size_kb = info["size_bytes"] / 1024
            print(f"\n💾 Database size: {size_kb:.2f} KB")

    print("=" * 60)
    print("✅ Setup complete!" if success else "❌ Setup failed!")
    print("=" * 60)
