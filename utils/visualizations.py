"""
Container Lifecycle Visualizations for Harbor Docker Learning

Educational Purpose: Visual representations help learners understand the
container lifecycle through the harbor metaphor.

Metaphor Mapping:
- Created = Ship blueprint ready, vessel under construction
- Running = Ship sailing in the harbor
- Stopped = Ship anchored/docked
- Removing = Ship leaving the harbor
"""

import streamlit as st
from typing import List, Dict


def render_container_lifecycle_diagram():
    """
    Render an interactive container lifecycle diagram

    Educational Value: Shows all possible states and transitions
    Metaphor: The journey of a ship through the harbor
    """
    st.markdown("""
    ### 🚢 Container Lifecycle (Harbor Metaphor)

    The lifecycle of a Docker container mirrors the journey of ships in a harbor:
    """)

    # Create columns for the lifecycle stages
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
        <div style='text-align: center; padding: 20px; background-color: #E8F4F8; border-radius: 10px; border: 2px solid #20B2AA;'>
            <div style='font-size: 48px;'>🏗️</div>
            <div style='font-weight: bold; color: #1E3A5F; margin-top: 10px;'>CREATED</div>
            <div style='color: #2C3E50; font-size: 14px; margin-top: 5px;'>Blueprint Ready</div>
            <div style='font-size: 12px; color: #666; margin-top: 5px;'>Ship under construction</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style='text-align: center; padding: 20px; background-color: #E1F5E1; border-radius: 10px; border: 2px solid #2E8B57;'>
            <div style='font-size: 48px;'>⛵</div>
            <div style='font-weight: bold; color: #1E3A5F; margin-top: 10px;'>RUNNING</div>
            <div style='color: #2C3E50; font-size: 14px; margin-top: 5px;'>Actively Sailing</div>
            <div style='font-size: 12px; color: #666; margin-top: 5px;'>Ship is in motion</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div style='text-align: center; padding: 20px; background-color: #FFF8E1; border-radius: 10px; border: 2px solid #FFB347;'>
            <div style='font-size: 48px;'>⚓</div>
            <div style='font-weight: bold; color: #1E3A5F; margin-top: 10px;'>STOPPED</div>
            <div style='color: #2C3E50; font-size: 14px; margin-top: 5px;'>Anchored</div>
            <div style='font-size: 12px; color: #666; margin-top: 5px;'>Ship is docked</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div style='text-align: center; padding: 20px; background-color: #FFE5E5; border-radius: 10px; border: 2px solid #DC143C;'>
            <div style='font-size: 48px;'>🗑️</div>
            <div style='font-weight: bold; color: #1E3A5F; margin-top: 10px;'>REMOVED</div>
            <div style='color: #2C3E50; font-size: 14px; margin-top: 5px;'>Decommissioned</div>
            <div style='font-size: 12px; color: #666; margin-top: 5px;'>Ship left harbor</div>
        </div>
        """, unsafe_allow_html=True)

    # Transition arrows
    st.markdown("""
    <div style='text-align: center; margin: 20px 0; color: #20B2AA; font-size: 24px;'>
        ➡️ docker run ➡️ docker stop ➡️ docker rm ➡️
    </div>
    """, unsafe_allow_html=True)

    # Command mapping
    st.markdown("### 🎯 Docker Commands & State Transitions")

    transitions = {
        "docker run": ("Created → Running", "Launch a ship from blueprint", "🏗️ ➡️ ⛵"),
        "docker stop": ("Running → Stopped", "Anchor a sailing ship", "⛵ ➡️ ⚓"),
        "docker start": ("Stopped → Running", "Set a docked ship back in motion", "⚓ ➡️ ⛵"),
        "docker restart": ("Running → Running", "Bring ship to dock and send out again", "⛵ 🔄 ⛵"),
        "docker rm": ("Stopped → Removed", "Decommission and remove ship", "⚓ ➡️ 🗑️"),
        "docker rm -f": ("Running → Removed", "Force remove sailing ship", "⛵ ➡️ 🗑️")
    }

    for cmd, (transition, description, emoji) in transitions.items():
        col1, col2, col3 = st.columns([2, 3, 1])
        with col1:
            st.code(cmd, language="bash")
        with col2:
            st.markdown(f"**{transition}**  \n{description}")
        with col3:
            st.markdown(f"<div style='font-size: 24px; text-align: center;'>{emoji}</div>", unsafe_allow_html=True)


def render_harbor_view(containers: List[Dict] = None):
    """
    Render a visual representation of the current harbor state

    Educational Value: Shows containers as ships in various states
    Metaphor: A bird's eye view of the harbor

    Args:
        containers: List of container dictionaries with 'name', 'state', 'image'
    """
    if containers is None:
        containers = []

    st.markdown("### 🌊 Current Harbor View")

    if not containers:
        st.info("""
        ```
        ╔══════════════════════════════════════════╗
        ║          HARBOR - EMPTY                  ║
        ║                                          ║
        ║              🌊 ~ ~ ~ ~ ~                ║
        ║         No ships in harbor               ║
        ║                                          ║
        ║       Use 'docker run' to launch         ║
        ║            your first ship!              ║
        ║                                          ║
        ╚══════════════════════════════════════════╝
        ```
        """)
        return

    # Render each container as a ship
    st.markdown("```")
    st.markdown("╔══════════════════════════════════════════╗")
    st.markdown("║           HARBOR - ACTIVE                ║")
    st.markdown("╠══════════════════════════════════════════╣")

    for container in containers:
        name = container.get('name', 'unknown')
        state = container.get('state', 'unknown')
        image = container.get('image', 'unknown')

        # Choose ship icon based on state
        if state == 'running':
            icon = '⛵'
            state_display = 'SAILING'
        elif state == 'stopped':
            icon = '⚓'
            state_display = 'ANCHORED'
        elif state == 'created':
            icon = '🏗️'
            state_display = 'DOCKED'
        else:
            icon = '🚢'
            state_display = state.upper()

        st.markdown(f"║ {icon} {name:<20} [{state_display:<8}] ║")
        st.markdown(f"║    └─ Image: {image:<25} ║")

    st.markdown("╚══════════════════════════════════════════╝")
    st.markdown("```")


def render_command_visual_feedback(command_action: str, target: str = ""):
    """
    Render animated visual feedback for a command execution

    Educational Value: Immediate visual reinforcement of actions
    Metaphor: What happens in the harbor when you issue commands

    Args:
        command_action: The Docker action (run, stop, rm, etc.)
        target: Target container or image name
    """
    feedback_visuals = {
        'run': {
            'emoji': '🚢⛵',
            'animation': """
            ```
            🏗️  →  🚢  →  ⛵
            Blueprint  Ship Built  Ship Sailing

            A new ship is launched into the harbor!
            ```
            """,
            'color': 'success'
        },
        'stop': {
            'emoji': '⚓',
            'animation': """
            ```
            ⛵  →  🚢  →  ⚓
            Sailing  Slowing  Anchored

            The ship drops anchor and stops.
            ```
            """,
            'color': 'warning'
        },
        'start': {
            'emoji': '⛵',
            'animation': """
            ```
            ⚓  →  🚢  →  ⛵
            Anchored  Raising  Sailing

            The ship weighs anchor and sets sail!
            ```
            """,
            'color': 'success'
        },
        'rm': {
            'emoji': '👋',
            'animation': """
            ```
            ⚓  →  🚢  →  〰️
            Docked  Leaving  Gone

            The ship leaves the harbor.
            ```
            """,
            'color': 'error'
        },
        'ps': {
            'emoji': '📋',
            'animation': """
            ```
            🔍  Harbor Status Check

            Reviewing all ships in the harbor...
            ```
            """,
            'color': 'info'
        },
        'images': {
            'emoji': '📦',
            'animation': """
            ```
            📚  Blueprint Library

            Showing all available ship designs...
            ```
            """,
            'color': 'info'
        },
        'pull': {
            'emoji': '📥',
            'animation': """
            ```
            ☁️  →  📦  →  🏗️
            Registry  Download  Blueprint Ready

            New ship blueprint added to your collection!
            ```
            """,
            'color': 'success'
        }
    }

    if command_action in feedback_visuals:
        visual = feedback_visuals[command_action]

        # Display the visual feedback
        st.markdown(f"### {visual['emoji']} {command_action.upper()} Action")

        if visual['color'] == 'success':
            st.success(visual['animation'])
        elif visual['color'] == 'info':
            st.info(visual['animation'])
        elif visual['color'] == 'warning':
            st.warning(visual['animation'])
        elif visual['color'] == 'error':
            st.error(visual['animation'])


def render_state_badge(state: str) -> str:
    """
    Generate an HTML badge for a container state

    Args:
        state: Container state (created, running, stopped, removing)

    Returns:
        str: HTML string for the badge
    """
    badge_styles = {
        'running': ('⛵ Running', '#2E8B57', '#E1F5E1'),
        'stopped': ('⚓ Stopped', '#FFB347', '#FFF8E1'),
        'created': ('🏗️ Created', '#20B2AA', '#E8F4F8'),
        'removing': ('🗑️ Removing', '#DC143C', '#FFE5E5'),
    }

    label, border_color, bg_color = badge_styles.get(state, ('Unknown', '#666', '#EEE'))

    return f"""
    <span style='
        display: inline-block;
        padding: 5px 15px;
        background-color: {bg_color};
        border: 2px solid {border_color};
        border-radius: 15px;
        font-weight: bold;
        font-size: 14px;
        color: #1E3A5F;
    '>{label}</span>
    """


def render_progress_visual(completed: int, total: int):
    """
    Render a visual progress indicator with harbor theme

    Args:
        completed: Number of completed tutorials
        total: Total number of tutorials
    """
    percentage = (completed / total * 100) if total > 0 else 0

    # Create a visual ship progress bar
    ships_total = 10
    ships_completed = int(ships_total * percentage / 100)
    ships_remaining = ships_total - ships_completed

    progress_bar = "⛵" * ships_completed + "⚓" * ships_remaining

    st.markdown(f"""
    <div style='text-align: center; padding: 20px; background-color: #E8F4F8; border-radius: 10px;'>
        <div style='font-size: 32px; letter-spacing: 5px;'>{progress_bar}</div>
        <div style='margin-top: 10px; color: #1E3A5F; font-weight: bold;'>
            {completed} / {total} Tutorials Completed
        </div>
        <div style='color: #666; font-size: 14px; margin-top: 5px;'>
            {percentage:.0f}% of your voyage complete!
        </div>
    </div>
    """, unsafe_allow_html=True)


# Example usage
if __name__ == "__main__":
    print("Harbor Docker Learning - Visualizations")
    print("=" * 60)
    print("Visual components for teaching container lifecycle")
    print("=" * 60)
