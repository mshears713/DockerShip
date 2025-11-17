"""
Database Access Layer for Harbor Docker Learning

Educational Purpose: This module provides a clean API for database operations,
abstracting away SQL complexity and making the code more maintainable.

Design Pattern: Repository pattern - separates data access logic from business logic
"""

import sqlite3
from typing import List, Optional, Dict, Tuple
from datetime import datetime
from data.database import get_db_connection
from data.models import TutorialStep, UserProgress, ContainerState


# ============================================================================
# TUTORIAL OPERATIONS
# ============================================================================

def get_all_tutorials() -> List[TutorialStep]:
    """
    Retrieve all tutorial steps from the database

    Educational Note: Returns tutorials ordered by section and step number
    for a logical learning progression.

    Returns:
        List[TutorialStep]: All tutorials in learning order
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, section, step_number, title, description,
               expected_command, visual_state, help_text,
               docker_concept, metaphor_explanation
        FROM tutorials
        ORDER BY section, step_number;
    """)

    tutorials = []
    for row in cursor.fetchall():
        tutorial = TutorialStep(
            id=row['id'],
            section=row['section'],
            step_number=row['step_number'],
            title=row['title'],
            description=row['description'],
            expected_command=row['expected_command'],
            visual_state=row['visual_state'],
            help_text=row['help_text'],
            docker_concept=row['docker_concept'],
            metaphor_explanation=row['metaphor_explanation']
        )
        tutorials.append(tutorial)

    conn.close()
    return tutorials


def get_tutorial_by_id(tutorial_id: int) -> Optional[TutorialStep]:
    """
    Retrieve a specific tutorial by its ID

    Args:
        tutorial_id: The tutorial ID to fetch

    Returns:
        TutorialStep if found, None otherwise
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, section, step_number, title, description,
               expected_command, visual_state, help_text,
               docker_concept, metaphor_explanation
        FROM tutorials
        WHERE id = ?;
    """, (tutorial_id,))

    row = cursor.fetchone()
    conn.close()

    if row:
        return TutorialStep(
            id=row['id'],
            section=row['section'],
            step_number=row['step_number'],
            title=row['title'],
            description=row['description'],
            expected_command=row['expected_command'],
            visual_state=row['visual_state'],
            help_text=row['help_text'],
            docker_concept=row['docker_concept'],
            metaphor_explanation=row['metaphor_explanation']
        )
    return None


def get_tutorials_by_section(section: str) -> List[TutorialStep]:
    """
    Retrieve all tutorials in a specific section

    Educational Note: Allows organizing tutorials into logical learning units

    Args:
        section: Section name (e.g., "Introduction", "Basic Commands")

    Returns:
        List[TutorialStep]: Tutorials in the specified section
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, section, step_number, title, description,
               expected_command, visual_state, help_text,
               docker_concept, metaphor_explanation
        FROM tutorials
        WHERE section = ?
        ORDER BY step_number;
    """, (section,))

    tutorials = []
    for row in cursor.fetchall():
        tutorial = TutorialStep(
            id=row['id'],
            section=row['section'],
            step_number=row['step_number'],
            title=row['title'],
            description=row['description'],
            expected_command=row['expected_command'],
            visual_state=row['visual_state'],
            help_text=row['help_text'],
            docker_concept=row['docker_concept'],
            metaphor_explanation=row['metaphor_explanation']
        )
        tutorials.append(tutorial)

    conn.close()
    return tutorials


def get_all_sections() -> List[str]:
    """
    Get list of all unique tutorial sections

    Returns:
        List[str]: Section names in order of appearance
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT section
        FROM tutorials
        GROUP BY section
        ORDER BY MIN(id);
    """)

    sections = [row['section'] for row in cursor.fetchall()]
    conn.close()
    return sections


def get_section_stats() -> Dict[str, int]:
    """
    Get count of tutorials per section

    Returns:
        Dict[str, int]: Mapping of section name to tutorial count
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT section, COUNT(*) as count
        FROM tutorials
        GROUP BY section
        ORDER BY MIN(id);
    """)

    stats = {row['section']: row['count'] for row in cursor.fetchall()}
    conn.close()
    return stats


# ============================================================================
# USER PROGRESS OPERATIONS
# ============================================================================

def get_user_progress() -> Dict[int, UserProgress]:
    """
    Retrieve all user progress records

    Educational Note: Tracks which tutorials the user has completed

    Returns:
        Dict[int, UserProgress]: Mapping of tutorial_id to progress record
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, tutorial_id, completed, timestamp, attempts
        FROM user_progress;
    """)

    progress = {}
    for row in cursor.fetchall():
        up = UserProgress(
            id=row['id'],
            tutorial_id=row['tutorial_id'],
            completed=bool(row['completed']),
            timestamp=datetime.fromisoformat(row['timestamp']) if row['timestamp'] else None,
            attempts=row['attempts']
        )
        progress[up.tutorial_id] = up

    conn.close()
    return progress


def mark_tutorial_complete(tutorial_id: int) -> bool:
    """
    Mark a tutorial as completed by the user

    Educational Note: Records learning progress for motivation and tracking

    Args:
        tutorial_id: The tutorial ID to mark as complete

    Returns:
        bool: True if successful, False otherwise
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        # Check if progress record exists
        cursor.execute("""
            SELECT id, attempts FROM user_progress
            WHERE tutorial_id = ?;
        """, (tutorial_id,))

        row = cursor.fetchone()

        if row:
            # Update existing record
            cursor.execute("""
                UPDATE user_progress
                SET completed = 1,
                    timestamp = ?,
                    attempts = attempts + 1
                WHERE tutorial_id = ?;
            """, (datetime.now().isoformat(), tutorial_id))
        else:
            # Insert new record
            cursor.execute("""
                INSERT INTO user_progress (tutorial_id, completed, timestamp, attempts)
                VALUES (?, 1, ?, 1);
            """, (tutorial_id, datetime.now().isoformat()))

        conn.commit()
        conn.close()
        return True

    except sqlite3.Error as e:
        print(f"Error marking tutorial complete: {e}")
        conn.close()
        return False


def increment_tutorial_attempts(tutorial_id: int) -> bool:
    """
    Increment the attempt counter for a tutorial

    Educational Note: Tracks engagement even if not completed yet

    Args:
        tutorial_id: The tutorial ID to increment attempts for

    Returns:
        bool: True if successful
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        # Check if progress record exists
        cursor.execute("""
            SELECT id FROM user_progress
            WHERE tutorial_id = ?;
        """, (tutorial_id,))

        if cursor.fetchone():
            # Update existing
            cursor.execute("""
                UPDATE user_progress
                SET attempts = attempts + 1
                WHERE tutorial_id = ?;
            """, (tutorial_id,))
        else:
            # Create new
            cursor.execute("""
                INSERT INTO user_progress (tutorial_id, completed, attempts)
                VALUES (?, 0, 1);
            """, (tutorial_id,))

        conn.commit()
        conn.close()
        return True

    except sqlite3.Error as e:
        print(f"Error incrementing attempts: {e}")
        conn.close()
        return False


def get_progress_percentage() -> float:
    """
    Calculate overall progress percentage

    Returns:
        float: Percentage of tutorials completed (0-100)
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    # Get total tutorials
    cursor.execute("SELECT COUNT(*) as total FROM tutorials;")
    total = cursor.fetchone()['total']

    if total == 0:
        conn.close()
        return 0.0

    # Get completed count
    cursor.execute("""
        SELECT COUNT(*) as completed
        FROM user_progress
        WHERE completed = 1;
    """)
    completed = cursor.fetchone()['completed']

    conn.close()
    return (completed / total) * 100


# ============================================================================
# CONTAINER STATE OPERATIONS
# ============================================================================

def get_all_containers() -> List[ContainerState]:
    """
    Retrieve all container states

    Educational Note: Shows the current "harbor" state with all ships

    Returns:
        List[ContainerState]: All simulated containers
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, container_name, state, image, created_at, port_mapping
        FROM container_states
        ORDER BY created_at DESC;
    """)

    containers = []
    for row in cursor.fetchall():
        container = ContainerState(
            id=row['id'],
            container_name=row['container_name'],
            state=row['state'],
            image=row['image'],
            created_at=datetime.fromisoformat(row['created_at']) if row['created_at'] else None,
            port_mapping=row['port_mapping']
        )
        containers.append(container)

    conn.close()
    return containers


def get_container_by_name(name: str) -> Optional[ContainerState]:
    """
    Get a specific container by name

    Args:
        name: Container name to find

    Returns:
        ContainerState if found, None otherwise
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, container_name, state, image, created_at, port_mapping
        FROM container_states
        WHERE container_name = ?;
    """, (name,))

    row = cursor.fetchone()
    conn.close()

    if row:
        return ContainerState(
            id=row['id'],
            container_name=row['container_name'],
            state=row['state'],
            image=row['image'],
            created_at=datetime.fromisoformat(row['created_at']) if row['created_at'] else None,
            port_mapping=row['port_mapping']
        )
    return None


def create_container(name: str, image: str, port_mapping: Optional[str] = None) -> bool:
    """
    Create a new simulated container

    Args:
        name: Container name
        image: Docker image name
        port_mapping: Optional port mapping (e.g., "8080:80")

    Returns:
        bool: True if successful
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO container_states (container_name, state, image, port_mapping)
            VALUES (?, 'created', ?, ?);
        """, (name, image, port_mapping))

        conn.commit()
        conn.close()
        return True

    except sqlite3.IntegrityError:
        # Container already exists
        conn.close()
        return False


def update_container_state(name: str, new_state: str) -> bool:
    """
    Update the state of a container

    Educational Note: Simulates container lifecycle state transitions

    Args:
        name: Container name
        new_state: New state (created, running, stopped, removing)

    Returns:
        bool: True if successful
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            UPDATE container_states
            SET state = ?
            WHERE container_name = ?;
        """, (new_state, name))

        conn.commit()
        success = cursor.rowcount > 0
        conn.close()
        return success

    except sqlite3.Error as e:
        print(f"Error updating container state: {e}")
        conn.close()
        return False


def remove_container(name: str) -> bool:
    """
    Remove a container from the database

    Args:
        name: Container name to remove

    Returns:
        bool: True if successful
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            DELETE FROM container_states
            WHERE container_name = ?;
        """, (name,))

        conn.commit()
        success = cursor.rowcount > 0
        conn.close()
        return success

    except sqlite3.Error as e:
        print(f"Error removing container: {e}")
        conn.close()
        return False


# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

def get_next_tutorial(current_id: int) -> Optional[TutorialStep]:
    """
    Get the next tutorial in sequence

    Args:
        current_id: Current tutorial ID

    Returns:
        TutorialStep: Next tutorial, or None if at the end
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id FROM tutorials
        WHERE id > ?
        ORDER BY id
        LIMIT 1;
    """, (current_id,))

    row = cursor.fetchone()
    conn.close()

    if row:
        return get_tutorial_by_id(row['id'])
    return None


def get_previous_tutorial(current_id: int) -> Optional[TutorialStep]:
    """
    Get the previous tutorial in sequence

    Args:
        current_id: Current tutorial ID

    Returns:
        TutorialStep: Previous tutorial, or None if at the beginning
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id FROM tutorials
        WHERE id < ?
        ORDER BY id DESC
        LIMIT 1;
    """, (current_id,))

    row = cursor.fetchone()
    conn.close()

    if row:
        return get_tutorial_by_id(row['id'])
    return None


if __name__ == "__main__":
    """
    Test the database access layer
    """
    print("=" * 60)
    print("🚢 Testing Database Access Layer")
    print("=" * 60)

    # Test tutorial retrieval
    print("\n📚 Testing Tutorial Retrieval:")
    tutorials = get_all_tutorials()
    print(f"   Total tutorials: {len(tutorials)}")

    if tutorials:
        first = tutorials[0]
        print(f"   First tutorial: {first.title}")

    # Test sections
    print("\n📖 Testing Sections:")
    sections = get_all_sections()
    print(f"   Sections: {sections}")

    stats = get_section_stats()
    for section, count in stats.items():
        print(f"   - {section}: {count} tutorials")

    # Test progress
    print("\n📊 Testing Progress:")
    progress = get_user_progress()
    print(f"   Progress records: {len(progress)}")
    print(f"   Completion: {get_progress_percentage():.1f}%")

    # Test containers
    print("\n🚢 Testing Containers:")
    containers = get_all_containers()
    print(f"   Containers: {len(containers)}")
    for container in containers:
        print(f"   - {container.container_name}: {container.state}")

    print("\n" + "=" * 60)
    print("✅ All tests completed!")
    print("=" * 60)
