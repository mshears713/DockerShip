"""
Data Models for Harbor Docker Learning

Educational Purpose: These models define the structure of tutorial content,
making it easy to create, store, and retrieve learning materials.

Design Philosophy: Each tutorial step is self-contained with all information
needed to teach a specific Docker concept through the harbor metaphor.
"""

from dataclasses import dataclass, field
from typing import Optional, List
from datetime import datetime


@dataclass
class TutorialStep:
    """
    Represents a single tutorial step in the learning journey

    Educational Value: Each step teaches one focused Docker concept
    Metaphor Connection: Steps guide users through harbor operations

    Attributes:
        id: Unique identifier for the tutorial step
        section: Category/grouping (e.g., "Container Basics", "Images")
        step_number: Order within the section
        title: Clear, descriptive title for the step
        description: Detailed explanation with harbor metaphor
        expected_command: The Docker command users should practice (optional)
        visual_state: State to display in the harbor visualization
        help_text: Additional guidance and tips
        docker_concept: The actual Docker concept being taught
        metaphor_explanation: How the metaphor relates to Docker
    """
    id: int
    section: str
    step_number: int
    title: str
    description: str
    expected_command: Optional[str] = None
    visual_state: str = "neutral"  # States: neutral, running, stopped, creating, removing
    help_text: Optional[str] = None
    docker_concept: Optional[str] = None
    metaphor_explanation: Optional[str] = None

    def __post_init__(self):
        """Validate the tutorial step data"""
        if self.step_number < 1:
            raise ValueError("Step number must be positive")
        if not self.section.strip():
            raise ValueError("Section cannot be empty")
        if not self.title.strip():
            raise ValueError("Title cannot be empty")


@dataclass
class UserProgress:
    """
    Tracks user progress through tutorials

    Educational Value: Helps users see their learning journey and maintain motivation
    Persistence: Stored in SQLite to survive app restarts

    Attributes:
        id: Unique identifier for the progress record
        tutorial_id: Reference to the TutorialStep being tracked
        completed: Whether the user has completed this step
        timestamp: When the step was completed
        attempts: Number of times user tried the step (for learning analytics)
    """
    id: Optional[int] = None
    tutorial_id: int = 0
    completed: bool = False
    timestamp: Optional[datetime] = None
    attempts: int = 0

    def __post_init__(self):
        """Set timestamp if not provided"""
        if self.timestamp is None and self.completed:
            self.timestamp = datetime.now()


@dataclass
class ContainerState:
    """
    Represents the state of a simulated Docker container (ship in harbor)

    Educational Value: Visualizes container lifecycle
    Metaphor Connection: Ships have states (docked, sailing, anchored)

    Attributes:
        id: Unique identifier
        container_name: Name of the container/ship
        state: Current state (running, stopped, created, removing)
        image: The Docker image this container is based on (ship blueprint)
        created_at: When the container was created
        port_mapping: Simulated port mappings (harbor dock numbers)
    """
    id: Optional[int] = None
    container_name: str = ""
    state: str = "created"  # States: created, running, stopped, removing
    image: str = ""
    created_at: Optional[datetime] = None
    port_mapping: Optional[str] = None

    # State constants for validation
    VALID_STATES = {"created", "running", "stopped", "removing"}

    def __post_init__(self):
        """Validate and set defaults"""
        if self.created_at is None:
            self.created_at = datetime.now()
        if self.state not in self.VALID_STATES:
            raise ValueError(f"State must be one of {self.VALID_STATES}")

    def is_running(self) -> bool:
        """Check if container is in running state (ship is sailing)"""
        return self.state == "running"

    def is_stopped(self) -> bool:
        """Check if container is stopped (ship is anchored)"""
        return self.state == "stopped"


@dataclass
class TutorialSection:
    """
    Represents a grouping of related tutorial steps

    Educational Value: Organizes learning into logical units
    Example sections: "Container Basics", "Working with Images", "Container Lifecycle"

    Attributes:
        name: Section name
        description: What this section teaches
        icon: Emoji or icon representing the section
        steps: List of tutorial steps in this section
        order: Display order
    """
    name: str
    description: str
    icon: str = "📚"
    steps: List[TutorialStep] = field(default_factory=list)
    order: int = 0

    def add_step(self, step: TutorialStep):
        """Add a tutorial step to this section"""
        self.steps.append(step)
        # Sort steps by step_number
        self.steps.sort(key=lambda s: s.step_number)

    def get_step_count(self) -> int:
        """Get the number of steps in this section"""
        return len(self.steps)


# Database schema definitions (for reference and documentation)
# These will be used when creating the actual SQLite tables

TUTORIAL_SCHEMA = """
CREATE TABLE IF NOT EXISTS tutorials (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    section TEXT NOT NULL,
    step_number INTEGER NOT NULL,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    expected_command TEXT,
    visual_state TEXT DEFAULT 'neutral',
    help_text TEXT,
    docker_concept TEXT,
    metaphor_explanation TEXT,
    UNIQUE(section, step_number)
);
"""

USER_PROGRESS_SCHEMA = """
CREATE TABLE IF NOT EXISTS user_progress (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tutorial_id INTEGER NOT NULL,
    completed BOOLEAN DEFAULT 0,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    attempts INTEGER DEFAULT 0,
    FOREIGN KEY (tutorial_id) REFERENCES tutorials(id)
);
"""

CONTAINER_STATES_SCHEMA = """
CREATE TABLE IF NOT EXISTS container_states (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    container_name TEXT UNIQUE NOT NULL,
    state TEXT NOT NULL DEFAULT 'created',
    image TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    port_mapping TEXT
);
"""

# Export all schemas for easy database initialization
DATABASE_SCHEMAS = {
    'tutorials': TUTORIAL_SCHEMA,
    'user_progress': USER_PROGRESS_SCHEMA,
    'container_states': CONTAINER_STATES_SCHEMA
}


def validate_tutorial_step(step: TutorialStep) -> List[str]:
    """
    Validate a tutorial step and return list of validation errors

    Educational note: Validation ensures tutorial content quality
    """
    errors = []

    if not step.title or len(step.title) < 3:
        errors.append("Title must be at least 3 characters")

    if not step.description or len(step.description) < 10:
        errors.append("Description must be at least 10 characters")

    if step.expected_command and not step.expected_command.startswith('docker'):
        errors.append("Expected command should start with 'docker'")

    if step.visual_state not in ["neutral", "running", "stopped", "creating", "removing"]:
        errors.append(f"Invalid visual state: {step.visual_state}")

    return errors


if __name__ == "__main__":
    # Example usage and testing
    print("Harbor Docker Learning - Data Models")
    print("=" * 50)

    # Create a sample tutorial step
    sample_step = TutorialStep(
        id=1,
        section="Container Basics",
        step_number=1,
        title="Welcome to Docker Containers",
        description="Learn what Docker containers are using the ship metaphor",
        visual_state="neutral",
        docker_concept="Containers are isolated runtime environments",
        metaphor_explanation="Think of containers as ships - each is independent but uses the same harbor infrastructure"
    )

    print(f"\n✅ Sample Tutorial Step Created:")
    print(f"   Title: {sample_step.title}")
    print(f"   Section: {sample_step.section}")
    print(f"   Docker Concept: {sample_step.docker_concept}")

    # Validate the step
    validation_errors = validate_tutorial_step(sample_step)
    if validation_errors:
        print(f"\n❌ Validation Errors: {validation_errors}")
    else:
        print(f"\n✅ Tutorial step is valid!")

    print("\n" + "=" * 50)
    print("Data models ready for use!")
