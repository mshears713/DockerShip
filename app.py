"""
Harbor Docker Learning - Interactive Streamlit Application
Teaching Docker container concepts through the harbor and ship metaphor

Educational Purpose: This app simulates Docker CLI operations without requiring
Docker installation, making it perfect for beginners.

Metaphor: Ships in a harbor = Containers in Docker
- Ships docking = Containers starting
- Ships sailing = Containers running
- Ships leaving = Containers stopping/removing
"""

import streamlit as st
import sys
import os
from typing import Optional

# Add project directories to path for imports
sys.path.append(os.path.dirname(__file__))

# Import database access functions
from data.db_access import (
    get_all_tutorials,
    get_all_sections,
    get_section_stats,
    get_tutorials_by_section,
    get_progress_percentage,
    get_user_progress,
    mark_tutorial_complete,
    increment_tutorial_attempts
)

# Import command parser utilities
from utils.command_parser import parse_command, validate_docker_command, get_command_help

# Import visualization utilities
from utils.visualizations import (
    render_container_lifecycle_diagram,
    render_command_visual_feedback,
    render_progress_visual
)

# Import animation utilities
from utils.animations import (
    animate_wave_separator,
    animate_success_badge,
    add_harbor_theme_animations
)

# Page configuration with harbor theme
st.set_page_config(
    page_title="Harbor Docker Learning",
    page_icon="🚢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for harbor theme
# Educational note: We use nautical colors to reinforce the learning metaphor
st.markdown("""
    <style>
    /* Harbor-themed color palette */
    .stApp {
        background-color: #F0F4F8;  /* Sky/harbor background */
    }

    /* Headers styled with nautical theme */
    h1 {
        color: #1E3A5F;  /* Deep water navy */
        font-weight: bold;
    }

    h2, h3 {
        color: #20B2AA;  /* Teal harbor water */
    }

    /* Make the interface welcoming and professional */
    .stMarkdown {
        color: #2C3E50;
    }

    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background-color: #1E3A5F;  /* Navy blue */
    }

    [data-testid="stSidebar"] .stMarkdown {
        color: #F0F4F8;
    }

    /* Success boxes styled as harbor signals */
    .stSuccess {
        background-color: #2E8B57;  /* Sea green */
        border-left: 4px solid #20B2AA;
    }

    /* Info boxes styled as harbor notes */
    .stInfo {
        background-color: #E8F4F8;
        border-left: 4px solid #20B2AA;
    }

    /* Warning boxes styled as caution signals */
    .stWarning {
        background-color: #FFF8E1;
        border-left: 4px solid #FFB347;
    }

    /* Harbor wave separator */
    .harbor-wave {
        text-align: center;
        color: #20B2AA;
        font-size: 24px;
        margin: 20px 0;
    }
    </style>
""", unsafe_allow_html=True)

# Add thematic animations
add_harbor_theme_animations()


def render_sidebar():
    """
    Render the sidebar with navigation and progress tracking

    Educational Purpose: Provides easy navigation between tutorial sections
    and shows overall learning progress.
    """
    with st.sidebar:
        # Harbor logo/header
        st.markdown("# 🚢 Harbor")
        st.markdown("### Docker Learning")
        st.markdown("---")

        # Progress tracking with enhanced statistics
        progress = get_progress_percentage()
        user_progress = get_user_progress()
        all_tutorials = get_all_tutorials()

        # Calculate statistics
        total_tutorials = len(all_tutorials)
        completed_count = sum(1 for p in user_progress.values() if p.completed)
        in_progress_count = sum(1 for p in user_progress.values() if p.attempts > 0 and not p.completed)

        st.markdown("### 📊 Your Progress")
        st.progress(progress / 100)
        st.caption(f"{progress:.0f}% Complete")

        # Detailed statistics
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Completed", f"{completed_count}/{total_tutorials}")
        with col2:
            st.metric("In Progress", in_progress_count)

        # Achievement badges
        if progress >= 100:
            st.success("🏆 Harbor Master!")
        elif progress >= 75:
            st.success("⭐ Senior Captain!")
        elif progress >= 50:
            st.info("🌟 Captain!")
        elif progress >= 25:
            st.info("⚓ First Mate!")
        elif progress > 0:
            st.info("🚢 Sailor!")

        st.markdown("---")

        # Navigation
        st.markdown("### 🧭 Navigation")

        # Get sections and stats
        sections = get_all_sections()
        stats = get_section_stats()

        # Section selection
        section_options = (
            ["🏠 Home", "🚢 Container Lifecycle"] +
            [f"📚 {section}" for section in sections]
        )

        selected = st.radio(
            "Choose a section:",
            section_options,
            key="section_nav"
        )

        # Show section stats
        if selected != "🏠 Home":
            section_name = selected.replace("📚 ", "")
            if section_name in stats:
                st.caption(f"{stats[section_name]} tutorials in this section")

        st.markdown("---")

        # Help and info
        with st.expander("ℹ️ About Harbor"):
            st.markdown("""
            **Harbor Docker Learning** teaches Docker through the metaphor of
            ships in a harbor.

            - 🚢 Containers = Ships
            - 🏗️ Images = Blueprints
            - ⚓ Docker = Harbor

            Navigate using the menu above!
            """)

        # Version info
        st.caption("Version 1.0 - Phase 1")

    return selected


def render_footer():
    """
    Render the footer with project info and navigation hints

    Educational Purpose: Provides context, credits, and helpful navigation tips
    """
    st.markdown("---")
    st.markdown('<div class="harbor-wave">〰️ 〰️ 〰️ 〰️ 〰️</div>', unsafe_allow_html=True)

    # Footer content in columns
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### ⚓ About")
        st.markdown("""
        **Harbor Docker Learning** is an interactive educational platform designed to
        teach Docker container fundamentals through the engaging harbor and ship metaphor.
        """)
        st.caption("Version 1.0 - Phase 1")

    with col2:
        st.markdown("### 🧭 Navigation Tips")
        st.markdown("""
        - Use the **sidebar** to switch sections
        - **Expand tutorials** to read content
        - Track your **progress bar** in sidebar
        - Look for **💡 help hints** in tutorials
        """)

    with col3:
        st.markdown("### 🚢 Metaphor Guide")
        st.markdown("""
        - 🚢 **Ships** = Containers
        - 🏗️ **Blueprints** = Images
        - ⚓ **Harbor** = Docker Engine
        - 🎯 **Dock** = Host System
        """)

    # Copyright and educational note
    st.markdown("---")
    st.caption("""
    🎓 **Educational Project** |
    Built with Streamlit & Python |
    Designed for Docker beginners |
    Learning through metaphor
    """)


def render_cli_input(tutorial):
    """
    Render interactive CLI input area for practicing Docker commands

    Educational Purpose: Allows users to practice commands with instant feedback
    Metaphor Connection: The CLI is like the harbor control center

    Args:
        tutorial: TutorialStep object containing expected command
    """
    # Initialize session state for command history if not exists
    if 'command_history' not in st.session_state:
        st.session_state.command_history = {}

    # Unique key for this tutorial's command input
    tutorial_key = f"cmd_input_{tutorial.id}"
    result_key = f"cmd_result_{tutorial.id}"

    # Command input box
    col1, col2 = st.columns([4, 1])

    with col1:
        user_command = st.text_input(
            "Enter your Docker command:",
            key=tutorial_key,
            placeholder="e.g., docker run nginx",
            help="Type the Docker command you want to practice",
            label_visibility="collapsed"
        )

    with col2:
        execute_button = st.button("Execute 🚀", key=f"btn_{tutorial.id}", use_container_width=True)

    # Process command when button is clicked or Enter is pressed
    if execute_button and user_command:
        # Parse the command
        result = parse_command(user_command)

        # Store result in session state
        st.session_state[result_key] = result

        # Increment attempts counter
        increment_tutorial_attempts(tutorial.id)

        # Check if it matches the expected command
        if tutorial.expected_command and validate_docker_command(user_command, tutorial.expected_command):
            st.session_state[f"correct_{tutorial.id}"] = True
            # Mark tutorial as complete
            mark_tutorial_complete(tutorial.id)

    # Display results if available
    if result_key in st.session_state:
        result = st.session_state[result_key]

        # Display feedback message
        if result.valid and result.success:
            st.success(result.message)

            # Show metaphor explanation
            if result.metaphor_explanation:
                st.info(result.metaphor_explanation)

            # Show simulated output
            if result.output:
                st.markdown("**Command Output:**")
                st.code(result.output, language="bash")

            # Show visual feedback for the command
            if result.action:
                with st.expander("🎨 Visual Harbor Feedback", expanded=False):
                    render_command_visual_feedback(result.action, result.target)

            # Check if matches expected command
            if tutorial.expected_command and f"correct_{tutorial.id}" in st.session_state:
                if st.session_state[f"correct_{tutorial.id}"]:
                    st.balloons()
                    animate_success_badge()
                else:
                    st.warning(f"✨ Command executed successfully, but try to match the expected command: `{tutorial.expected_command}`")
        else:
            # Show error message
            st.error(result.message)

            # Show help hint if available
            if result.help_hint:
                st.warning(f"💡 **Hint:** {result.help_hint}")

    # Show command help button
    with st.expander("📖 Command Reference"):
        if tutorial.expected_command:
            # Extract action from expected command
            parts = tutorial.expected_command.split()
            if len(parts) > 1:
                action = parts[1]
                help_text = get_command_help(action)
                st.code(help_text, language="text")
        else:
            st.markdown("No command reference available for this tutorial.")


def render_tutorial_section(section_name: str):
    """
    Render a specific tutorial section

    Educational Purpose: Displays all tutorials within a section for focused learning

    Args:
        section_name: Name of the section to display
    """
    # Get tutorials for this section
    tutorials = get_tutorials_by_section(section_name)

    if not tutorials:
        st.warning(f"No tutorials found for section: {section_name}")
        return

    # Section header
    st.title(f"📚 {section_name}")
    st.markdown("---")

    # Show overview
    st.markdown(f"**{len(tutorials)} tutorial{'s' if len(tutorials) != 1 else ''} in this section**")
    st.markdown("---")

    # Display each tutorial in the section
    for idx, tutorial in enumerate(tutorials, 1):
        # Create an expander for each tutorial
        with st.expander(f"**{idx}. {tutorial.title}**", expanded=(idx == 1)):
            # Tutorial content
            st.markdown(tutorial.description)

            # Show Docker concept if available
            if tutorial.docker_concept:
                st.info(f"**🎯 Docker Concept:** {tutorial.docker_concept}")

            # Show metaphor explanation if available
            if tutorial.metaphor_explanation:
                st.success(f"**🚢 Harbor Metaphor:** {tutorial.metaphor_explanation}")

            # Show help text if available
            if tutorial.help_text:
                with st.expander("💡 Need Help?"):
                    st.markdown(tutorial.help_text)

            # Show expected command if available
            if tutorial.expected_command:
                st.markdown("**Expected Command:**")
                st.code(tutorial.expected_command, language="bash")

            # Add interactive CLI practice section
            if tutorial.expected_command:
                st.markdown("---")
                st.markdown("### 💻 Practice Command")
                render_cli_input(tutorial)

        # Add separator between tutorials
        if idx < len(tutorials):
            animate_wave_separator()

    # Render footer
    render_footer()


def render_lifecycle_page():
    """
    Render the container lifecycle visualization page

    Educational Purpose: Visual guide to understanding container states
    and transitions using the harbor metaphor
    """
    # Page header
    st.title("🚢 Container Lifecycle Guide")
    st.markdown("### *Understanding Docker Container States Through the Harbor Metaphor*")
    st.markdown("---")

    # Introduction
    st.markdown("""
    Docker containers go through different states during their lifecycle, much like
    ships in a harbor. Understanding these states is crucial for managing your containers
    effectively.
    """)

    st.markdown("---")

    # Render the interactive lifecycle diagram
    render_container_lifecycle_diagram()

    # Additional educational content
    st.markdown("---")
    st.header("📖 Understanding Each State")

    # Detailed state explanations
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        #### 🏗️ Created State
        **Docker:** Container is created but not started yet
        **Harbor:** Ship blueprint is ready, vessel under construction

        A container in the "created" state exists but is not running. It's like having
        a ship ready at the dock but not yet set sail.

        **Common Commands:**
        - `docker create <image>` - Create without starting
        - `docker start <container>` - Start a created container
        """)

        st.markdown("""
        #### ⚓ Stopped State
        **Docker:** Container was running but has been stopped
        **Harbor:** Ship is anchored or docked in the harbor

        A stopped container maintains all its data and configuration but is not actively
        running. It can be restarted quickly without losing its state.

        **Common Commands:**
        - `docker stop <container>` - Stop a running container
        - `docker start <container>` - Restart a stopped container
        """)

    with col2:
        st.markdown("""
        #### ⛵ Running State
        **Docker:** Container is actively executing
        **Harbor:** Ship is sailing and performing its duties

        A running container is actively executing its process. This is the operational
        state where the container does its work.

        **Common Commands:**
        - `docker run <image>` - Create and start container
        - `docker ps` - List running containers
        - `docker logs <container>` - View container output
        """)

        st.markdown("""
        #### 🗑️ Removed State
        **Docker:** Container has been deleted
        **Harbor:** Ship has left the harbor permanently

        Once removed, a container and its data are gone (unless volumes were used).
        The image remains, allowing you to create new containers from it.

        **Common Commands:**
        - `docker rm <container>` - Remove stopped container
        - `docker rm -f <container>` - Force remove running container
        """)

    # Interactive practice section
    st.markdown("---")
    st.header("🎯 Test Your Understanding")

    with st.expander("📝 Quick Quiz", expanded=False):
        st.markdown("""
        **Question 1:** What command changes a container from STOPPED to RUNNING?

        **Answer:** `docker start <container>`

        ---

        **Question 2:** Can you remove a RUNNING container without stopping it first?

        **Answer:** Yes, using `docker rm -f <container>` (force flag)

        ---

        **Question 3:** What's the difference between CREATED and STOPPED states?

        **Answer:** CREATED means the container was never started. STOPPED means it was
        running before and was intentionally stopped.

        ---

        **Question 4:** Which command shows only RUNNING containers?

        **Answer:** `docker ps` (use `docker ps -a` to show all states)
        """)

    # Visual progress reminder
    st.markdown("---")
    st.header("📊 Your Learning Progress")

    all_tutorials = get_all_tutorials()
    user_progress = get_user_progress()
    completed_count = sum(1 for p in user_progress.values() if p.completed)

    render_progress_visual(completed_count, len(all_tutorials))

    # Footer
    render_footer()


def main():
    """
    Main application entry point

    Educational scaffolding: Each section is designed to introduce concepts
    progressively, starting with the metaphor and building to Docker concepts.
    """

    # Render sidebar and get navigation selection
    selected_section = render_sidebar()

    # Route to appropriate view based on selection
    if selected_section == "🏠 Home":
        render_home_page()
    elif selected_section == "🚢 Container Lifecycle":
        render_lifecycle_page()
    else:
        # Extract section name (remove emoji prefix)
        section_name = selected_section.replace("📚 ", "")
        render_tutorial_section(section_name)


def render_home_page():
    """
    Render the home/welcome page

    Educational Purpose: Introduces the metaphor and sets expectations
    """
    # Welcome header with ship icon
    st.title("🚢 Welcome to Harbor Docker Learning")
    st.markdown("### *Master Docker Containers Through an Interactive Harbor Experience*")

    # Add visual separator
    st.markdown("---")

    # Main welcome content area
    col1, col2 = st.columns([2, 1])

    with col1:
        st.header("⚓ Welcome Aboard!")

        st.markdown("""
        Welcome to **Harbor Docker Learning**, where you'll learn Docker container
        concepts through an engaging harbor and ship metaphor!

        **Think of it this way:**
        - 🚢 **Ships** represent **Docker Containers**
        - ⚓ **Harbor** represents your **Docker Environment**
        - 🏗️ **Blueprints** represent **Docker Images**

        Just as harbor workers manage ships docking, sailing, and leaving port,
        you'll learn to manage Docker containers through their entire lifecycle.
        """)

        st.info("""
        💡 **Why this metaphor?**
        Docker concepts can seem abstract at first. By connecting them to familiar
        ideas like ships in a harbor, we make learning intuitive and memorable!
        """)

    with col2:
        # Visual representation using emojis
        st.markdown("### 🌊 Your Harbor")
        st.markdown("""
        ```

              🚢  🚢
            ⚓      ⚓
        ~~~~~~~~~~~~~~~~~~~
          HARBOR  DOCK
        ~~~~~~~~~~~~~~~~~~~

        ```
        """)

        st.success("✅ Environment Ready!")
        st.caption("Your learning harbor is set up and ready to receive ships.")

    # Introduction to the learning journey
    st.markdown("---")
    st.header("🎯 What You'll Learn")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        #### 📦 Container Basics
        - What containers are
        - Container lifecycle
        - Running your first container
        """)

    with col2:
        st.markdown("""
        #### 🔧 Docker Commands
        - docker run
        - docker ps
        - docker stop
        - docker rm
        """)

    with col3:
        st.markdown("""
        #### 🎨 Visual Learning
        - Interactive simulations
        - Real-time feedback
        - Progress tracking
        """)

    # Getting started section
    st.markdown("---")
    st.header("🚀 Getting Started")

    st.markdown("""
    This application is organized into progressive tutorials that will guide you
    step-by-step through Docker fundamentals.

    **Ready to begin your journey?**
    - 👈 Use the **sidebar** to navigate between tutorials
    - 📝 Follow the **step-by-step instructions** in each section
    - 💻 Practice with the **simulated Docker CLI**
    - 📊 Track your **progress** as you master each concept
    """)

    # Quick start section
    st.markdown("---")
    st.markdown("### 🎓 Ready to Start?")
    st.info("""
    👈 **Open the sidebar** and select a tutorial section to begin your learning journey!

    Start with **Introduction** to understand the basics, then move to **Basic Commands**
    for hands-on practice.
    """)

    # Render footer
    render_footer()

if __name__ == "__main__":
    # Educational note: This is the entry point for the Streamlit application
    # When you run 'streamlit run app.py', this is where execution begins
    main()
