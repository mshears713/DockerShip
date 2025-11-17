"""
Utility modules for Harbor Docker Learning

Educational Purpose: These utilities provide the simulation engine for Docker commands,
allowing users to practice without requiring actual Docker installation.
"""

from .command_parser import (
    parse_command,
    CommandResult,
    validate_docker_command
)

from .visualizations import (
    render_container_lifecycle_diagram,
    render_harbor_view,
    render_command_visual_feedback,
    render_state_badge,
    render_progress_visual
)

from .animations import (
    animate_wave_separator,
    animate_success_badge,
    animate_progress_bar,
    animate_container_transition,
    add_harbor_theme_animations
)

__all__ = [
    'parse_command',
    'CommandResult',
    'validate_docker_command',
    'render_container_lifecycle_diagram',
    'render_harbor_view',
    'render_command_visual_feedback',
    'render_state_badge',
    'render_progress_visual',
    'animate_wave_separator',
    'animate_success_badge',
    'animate_progress_bar',
    'animate_container_transition',
    'add_harbor_theme_animations'
]
