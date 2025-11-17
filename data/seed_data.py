"""
Database Seeding Script for Harbor Docker Learning

Educational Purpose: Populates the database with initial tutorial content
teaching Docker concepts through the harbor and ship metaphor.

Tutorial Design: Progressive learning from basic concepts to hands-on practice
"""

import sqlite3
from data.database import get_db_connection, DB_PATH


def seed_tutorials():
    """
    Seed the database with initial tutorial content

    Educational Design: Tutorials progress from understanding concepts to
    practicing commands, always connecting the harbor metaphor to Docker reality.
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    # Sample tutorial data following the educational progression
    tutorials = [
        # Section 1: Introduction to Containers
        {
            'section': 'Introduction',
            'step_number': 1,
            'title': 'Welcome to Docker Containers! 🚢',
            'description': '''Welcome aboard! In this tutorial, you'll learn Docker container fundamentals using a familiar metaphor: ships in a harbor.

**Think of it this way:**
- 🏗️ **Docker Images** are like ship blueprints - they define what the ship looks like
- 🚢 **Docker Containers** are like actual ships - running instances created from blueprints
- ⚓ **Your Computer** is like a harbor - where containers/ships operate
- 🎯 **Docker Commands** are like harbor master instructions - controlling ship operations

This approach makes abstract concepts concrete and memorable!''',
            'expected_command': None,
            'visual_state': 'neutral',
            'help_text': 'Take your time to understand the metaphor. Everything we learn will connect back to these simple ideas!',
            'docker_concept': 'Docker containers are lightweight, isolated environments that package applications and their dependencies.',
            'metaphor_explanation': 'Just as ships carry cargo independently while sharing harbor infrastructure, containers run applications independently while sharing the host system.'
        },
        {
            'section': 'Introduction',
            'step_number': 2,
            'title': 'Understanding Images vs Containers 📦',
            'description': '''Let's clarify two key concepts that often confuse beginners:

**Docker Images (Blueprints)** 🏗️
- Read-only templates for creating containers
- Contain application code, runtime, libraries, and dependencies
- Can create many containers from one image
- Like: A ship blueprint can build many ships

**Docker Containers (Ships)** 🚢
- Running instances created from images
- Have their own isolated environment
- Can be started, stopped, and removed
- Like: Each ship built from the blueprint is independent

**The Relationship:**
Blueprint → Ship = Image → Container

You can't sail a blueprint, and you can't build without one!''',
            'expected_command': None,
            'visual_state': 'neutral',
            'help_text': 'Remember: Images are templates (static), Containers are running instances (dynamic)',
            'docker_concept': 'Images are immutable templates; containers are mutable runtime instances.',
            'metaphor_explanation': 'A blueprint stays the same, but each ship built from it has its own journey and can be modified independently.'
        },
        {
            'section': 'Introduction',
            'step_number': 3,
            'title': 'The Container Lifecycle 🔄',
            'description': '''Containers go through different states in their lifecycle, just like ships in a harbor:

**1. Created** 🏗️
- Container is built from an image but not running yet
- Like: Ship is built but still in dry dock

**2. Running** 🚢
- Container is actively executing
- Application inside is working
- Like: Ship is sailing in the harbor

**3. Stopped** ⚓
- Container is paused but still exists
- Can be restarted without rebuilding
- Like: Ship is anchored, can sail again

**4. Removed** 🗑️
- Container is deleted from the system
- Like: Ship is decommissioned and scrapped

Understanding this lifecycle helps you manage containers effectively!''',
            'expected_command': None,
            'visual_state': 'neutral',
            'help_text': 'You can move containers between these states using Docker commands. We\'ll practice this soon!',
            'docker_concept': 'Containers have a lifecycle: created, running, stopped, and removed.',
            'metaphor_explanation': 'Ships don\'t disappear when they stop - they anchor. Same with containers: stopping doesn\'t delete them.'
        },

        # Section 2: Basic Commands
        {
            'section': 'Basic Commands',
            'step_number': 1,
            'title': 'Your First Command: docker run 🚀',
            'description': '''Ready for hands-on practice? Let's start your first container (launch your first ship)!

**The `docker run` Command**

This is the most important Docker command. It:
1. Downloads the image if you don't have it (gets the blueprint)
2. Creates a new container (builds the ship)
3. Starts the container (launches the ship)

**Syntax:**
```
docker run <image-name>
```

**Example:**
```
docker run nginx
```

This command says: "Build and launch a ship from the nginx blueprint!"

**Try it yourself in the CLI box below!**

Type: `docker run nginx`''',
            'expected_command': 'docker run nginx',
            'visual_state': 'creating',
            'help_text': 'Type exactly: docker run nginx',
            'docker_concept': 'docker run creates and starts a container from an image in one command.',
            'metaphor_explanation': 'Like giving an order: "Build me an Nginx ship and send it sailing!"'
        },
        {
            'section': 'Basic Commands',
            'step_number': 2,
            'title': 'Listing Containers: docker ps 📋',
            'description': '''Now that you've launched a container, how do you see what's running in your harbor?

**The `docker ps` Command**

This command lists all **currently running** containers.

**Syntax:**
```
docker ps
```

Think of it as:
- 📋 Harbor master's logbook
- 🔍 Shows all ships currently sailing
- 📊 Displays container details (ID, image, status, etc.)

**Try it:**
```
docker ps
```

**Pro Tip:**
- `docker ps` shows only running containers
- `docker ps -a` shows ALL containers (running and stopped)

Like checking both ships at sea AND ships anchored in port!''',
            'expected_command': 'docker ps',
            'visual_state': 'running',
            'help_text': 'This shows you what containers are currently running. Try it!',
            'docker_concept': 'docker ps lists running containers with their status and details.',
            'metaphor_explanation': 'Like scanning the harbor to see which ships are actively sailing.'
        },
        {
            'section': 'Basic Commands',
            'step_number': 3,
            'title': 'Stopping Containers: docker stop ⛔',
            'description': '''Sometimes you need to stop a container gracefully (anchor a ship).

**The `docker stop` Command**

This command stops a running container safely.

**Syntax:**
```
docker stop <container-id>
```

**Example:**
```
docker stop happy-whale
```

**What happens:**
1. Docker sends a polite "please stop" signal (SIGTERM)
2. Container gets time to finish current work (save data, close connections)
3. If it doesn't stop in time, Docker forces it to stop (SIGKILL)

**Harbor Metaphor:**
It's like signaling a ship to anchor - giving it time to secure cargo and drop anchor properly, not just cutting the engine!

**Try it:**
```
docker stop nginx
```''',
            'expected_command': 'docker stop nginx',
            'visual_state': 'stopped',
            'help_text': 'Stopping is different from removing. The container still exists, just not running.',
            'docker_concept': 'docker stop gracefully stops a running container.',
            'metaphor_explanation': 'Like asking a ship to drop anchor - it stops moving but stays in the harbor.'
        },
        {
            'section': 'Basic Commands',
            'step_number': 4,
            'title': 'Removing Containers: docker rm 🗑️',
            'description': '''When you're done with a container, you can remove it completely (decommission a ship).

**The `docker rm` Command**

This command deletes a stopped container from your system.

**Syntax:**
```
docker rm <container-id>
```

**Example:**
```
docker rm happy-whale
```

**Important Notes:**
- ⚠️ You must **stop** a container before removing it
- 🗑️ Removal is permanent (container data is lost)
- 💾 The image (blueprint) remains - you can create new containers

**Harbor Metaphor:**
Like scrapping a ship - it's gone from the harbor, but you still have the blueprint to build another if needed!

**Try it:**
```
docker rm nginx
```

*(Make sure you stopped it first with docker stop nginx)*''',
            'expected_command': 'docker rm nginx',
            'visual_state': 'neutral',
            'help_text': 'Remember: Stop first, then remove. The image stays, only the container is deleted.',
            'docker_concept': 'docker rm permanently deletes a stopped container.',
            'metaphor_explanation': 'Like decommissioning a ship - it leaves the harbor, but the blueprint remains for building new ships.'
        },

        # Section 3: Practice
        {
            'section': 'Practice',
            'step_number': 1,
            'title': 'Practice: Complete Lifecycle 🔄',
            'description': '''Let's practice the complete container lifecycle!

**Your Mission:**
Manage a container through all its lifecycle states.

**Steps:**
1. 🚀 Create and start: `docker run hello-world`
2. 📋 List containers: `docker ps -a`
3. ⛔ Stop it: `docker stop hello-world`
4. 🗑️ Remove it: `docker rm hello-world`

This sequence demonstrates:
- Creating (launching a new ship)
- Viewing (checking harbor status)
- Stopping (anchoring)
- Removing (decommissioning)

**Start with:**
```
docker run hello-world
```

**Why hello-world?**
It's a special image that runs, prints a welcome message, and exits automatically - perfect for practice!''',
            'expected_command': 'docker run hello-world',
            'visual_state': 'creating',
            'help_text': 'Follow the steps in order. Each command teaches an important container operation.',
            'docker_concept': 'Complete container lifecycle management from creation to removal.',
            'metaphor_explanation': 'Like managing a ship\'s complete journey from launch to decommission.'
        }
    ]

    # Insert tutorials into database
    print("🌱 Seeding tutorial data...")

    for tutorial in tutorials:
        try:
            cursor.execute("""
                INSERT INTO tutorials (
                    section, step_number, title, description, expected_command,
                    visual_state, help_text, docker_concept, metaphor_explanation
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                tutorial['section'],
                tutorial['step_number'],
                tutorial['title'],
                tutorial['description'],
                tutorial['expected_command'],
                tutorial['visual_state'],
                tutorial['help_text'],
                tutorial['docker_concept'],
                tutorial['metaphor_explanation']
            ))
            print(f"   ✅ Added: {tutorial['section']} - Step {tutorial['step_number']}")
        except sqlite3.IntegrityError as e:
            print(f"   ⚠️  Skipped (already exists): {tutorial['section']} - Step {tutorial['step_number']}")

    conn.commit()
    conn.close()
    print("✅ Tutorial data seeded successfully!")


def seed_sample_container_states():
    """
    Seed some sample container states for demonstration

    Educational Purpose: Provides initial examples of containers in different states
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    print("\n🚢 Seeding sample container states...")

    sample_containers = [
        {
            'container_name': 'demo-nginx',
            'state': 'stopped',
            'image': 'nginx:latest',
            'port_mapping': '8080:80'
        },
        {
            'container_name': 'demo-hello',
            'state': 'created',
            'image': 'hello-world:latest',
            'port_mapping': None
        }
    ]

    for container in sample_containers:
        try:
            cursor.execute("""
                INSERT INTO container_states (
                    container_name, state, image, port_mapping
                ) VALUES (?, ?, ?, ?)
            """, (
                container['container_name'],
                container['state'],
                container['image'],
                container['port_mapping']
            ))
            print(f"   ✅ Added container: {container['container_name']} ({container['state']})")
        except sqlite3.IntegrityError:
            print(f"   ⚠️  Skipped (already exists): {container['container_name']}")

    conn.commit()
    conn.close()
    print("✅ Sample container states seeded!")


def clear_data():
    """
    Clear all data from the database (keep tables)

    ⚠️ WARNING: This deletes all tutorial progress and container states!
    """
    print("🗑️  Clearing all data from database...")

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM user_progress;")
    cursor.execute("DELETE FROM container_states;")
    cursor.execute("DELETE FROM tutorials;")

    conn.commit()
    conn.close()

    print("✅ All data cleared!")


def get_seeding_stats():
    """
    Get statistics about seeded data

    Returns:
        dict: Counts of seeded data
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    stats = {}

    cursor.execute("SELECT COUNT(*) FROM tutorials;")
    stats['tutorials'] = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM container_states;")
    stats['containers'] = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(DISTINCT section) FROM tutorials;")
    stats['sections'] = cursor.fetchone()[0]

    conn.close()

    return stats


if __name__ == "__main__":
    """
    Run this script to seed the database with sample tutorial data

    Usage:
        python data/seed_data.py           # Seed data
        python data/seed_data.py clear     # Clear all data
    """
    import sys

    print("=" * 60)
    print("🚢 Harbor Docker Learning - Database Seeding")
    print("=" * 60)

    if len(sys.argv) > 1 and sys.argv[1] == "clear":
        clear_data()
    else:
        # Check if database exists
        if not DB_PATH.exists():
            print("❌ Database not found! Please run 'python data/database.py' first.")
            sys.exit(1)

        # Seed the data
        seed_tutorials()
        seed_sample_container_states()

    # Show statistics
    print("\n📊 Database Statistics:")
    print("-" * 60)
    stats = get_seeding_stats()
    print(f"   📚 Tutorial steps: {stats['tutorials']}")
    print(f"   📖 Tutorial sections: {stats['sections']}")
    print(f"   🚢 Sample containers: {stats['containers']}")

    print("=" * 60)
    print("✅ Seeding complete!")
    print("=" * 60)
