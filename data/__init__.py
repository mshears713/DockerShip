"""
Data package for Harbor Docker Learning

This package contains:
- Data models (models.py)
- Database initialization and management (database.py)
- Database seeding scripts (seed_data.py)
"""

from data.models import (
    TutorialStep,
    UserProgress,
    ContainerState,
    TutorialSection,
    DATABASE_SCHEMAS
)

from data.database import (
    get_db_connection,
    init_database,
    verify_database,
    get_database_info,
    reset_database,
    DB_PATH
)

__all__ = [
    'TutorialStep',
    'UserProgress',
    'ContainerState',
    'TutorialSection',
    'DATABASE_SCHEMAS',
    'get_db_connection',
    'init_database',
    'verify_database',
    'get_database_info',
    'reset_database',
    'DB_PATH'
]
