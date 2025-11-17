"""
Thematic Animations and Transitions for Harbor Docker Learning

Educational Purpose: Animations enhance engagement and reinforce learning
through visual feedback and memorable interactions.

Metaphor Connection: Animations bring the harbor to life with ship movements,
waves, and dynamic visual feedback.
"""

import streamlit as st
import time


def animate_ship_launch():
    """
    Display an animated ship launch sequence

    Educational Value: Celebrates container creation with visual feedback
    Metaphor: A ship being launched from the harbor
    """
    st.markdown("""
    <style>
    @keyframes ship-launch {
        0% { transform: translateX(-100px) scale(0.5); opacity: 0; }
        50% { transform: translateX(0px) scale(1); opacity: 1; }
        100% { transform: translateX(100px) scale(1); opacity: 1; }
    }

    .ship-launch {
        animation: ship-launch 2s ease-in-out;
        font-size: 48px;
        text-align: center;
        margin: 20px 0;
    }
    </style>

    <div class="ship-launch">🚢 ⛵</div>
    """, unsafe_allow_html=True)


def animate_wave_separator():
    """
    Display animated wave separator

    Educational Value: Provides visual rhythm and thematic consistency
    Metaphor: Ocean waves in the harbor
    """
    st.markdown("""
    <style>
    @keyframes wave {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-5px); }
    }

    .wave-separator {
        text-align: center;
        color: #20B2AA;
        font-size: 32px;
        margin: 20px 0;
    }

    .wave-separator span {
        display: inline-block;
        animation: wave 2s ease-in-out infinite;
    }

    .wave-separator span:nth-child(2) { animation-delay: 0.2s; }
    .wave-separator span:nth-child(3) { animation-delay: 0.4s; }
    .wave-separator span:nth-child(4) { animation-delay: 0.6s; }
    .wave-separator span:nth-child(5) { animation-delay: 0.8s; }
    </style>

    <div class="wave-separator">
        <span>〰️</span>
        <span>〰️</span>
        <span>〰️</span>
        <span>〰️</span>
        <span>〰️</span>
    </div>
    """, unsafe_allow_html=True)


def animate_anchor_drop():
    """
    Display animated anchor dropping (container stopping)

    Educational Value: Visual feedback for stop command
    Metaphor: Ship dropping anchor
    """
    st.markdown("""
    <style>
    @keyframes anchor-drop {
        0% { transform: translateY(-50px); opacity: 0; }
        50% { transform: translateY(0px); opacity: 1; }
        100% { transform: translateY(10px); opacity: 1; }
    }

    .anchor-drop {
        animation: anchor-drop 1.5s ease-out;
        font-size: 48px;
        text-align: center;
        margin: 20px 0;
    }
    </style>

    <div class="anchor-drop">⚓</div>
    """, unsafe_allow_html=True)


def animate_ship_sailing():
    """
    Display sailing ship animation (container running)

    Educational Value: Shows active container state
    Metaphor: Ship actively sailing
    """
    st.markdown("""
    <style>
    @keyframes sailing {
        0%, 100% { transform: translateX(0px) rotate(-2deg); }
        50% { transform: translateX(10px) rotate(2deg); }
    }

    .ship-sailing {
        animation: sailing 3s ease-in-out infinite;
        font-size: 48px;
        text-align: center;
        margin: 20px 0;
    }
    </style>

    <div class="ship-sailing">⛵</div>
    """, unsafe_allow_html=True)


def animate_success_badge():
    """
    Display animated success badge when tutorial is completed

    Educational Value: Positive reinforcement for learning achievement
    Metaphor: Harbor signal flag indicating success
    """
    st.markdown("""
    <style>
    @keyframes pulse-success {
        0% { transform: scale(1); box-shadow: 0 0 0 0 rgba(46, 139, 87, 0.7); }
        50% { transform: scale(1.05); box-shadow: 0 0 20px 10px rgba(46, 139, 87, 0); }
        100% { transform: scale(1); box-shadow: 0 0 0 0 rgba(46, 139, 87, 0); }
    }

    .success-badge {
        animation: pulse-success 2s ease-in-out 3;
        background: linear-gradient(135deg, #2E8B57 0%, #20B2AA 100%);
        color: white;
        padding: 30px;
        border-radius: 20px;
        text-align: center;
        font-size: 24px;
        font-weight: bold;
        margin: 20px 0;
    }
    </style>

    <div class="success-badge">
        🎉 Tutorial Completed! 🎉
    </div>
    """, unsafe_allow_html=True)


def animate_progress_bar(percentage: float):
    """
    Display animated progress bar with harbor theme

    Args:
        percentage: Progress percentage (0-100)

    Educational Value: Visual progress tracking with thematic styling
    """
    st.markdown(f"""
    <style>
    @keyframes fill-progress {{
        from {{ width: 0%; }}
        to {{ width: {percentage}%; }}
    }}

    .harbor-progress-container {{
        width: 100%;
        height: 40px;
        background: linear-gradient(to right, #E8F4F8 0%, #D0E8F0 100%);
        border-radius: 20px;
        border: 3px solid #20B2AA;
        position: relative;
        overflow: hidden;
        margin: 20px 0;
    }}

    .harbor-progress-fill {{
        height: 100%;
        background: linear-gradient(to right, #20B2AA 0%, #2E8B57 100%);
        border-radius: 17px;
        animation: fill-progress 2s ease-out;
        width: {percentage}%;
        position: relative;
        display: flex;
        align-items: center;
        justify-content: flex-end;
        padding-right: 15px;
        color: white;
        font-weight: bold;
        font-size: 18px;
    }}

    @keyframes wave-pattern {{
        0% {{ background-position: 0% 50%; }}
        100% {{ background-position: 100% 50%; }}
    }}

    .harbor-progress-fill::before {{
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: linear-gradient(90deg,
            transparent 0%,
            rgba(255,255,255,0.2) 50%,
            transparent 100%);
        background-size: 200% 100%;
        animation: wave-pattern 2s linear infinite;
    }}
    </style>

    <div class="harbor-progress-container">
        <div class="harbor-progress-fill">
            {percentage:.0f}%
        </div>
    </div>
    """, unsafe_allow_html=True)


def animate_container_transition(from_state: str, to_state: str):
    """
    Animate a container state transition

    Args:
        from_state: Starting state (running, stopped, created, removing)
        to_state: Ending state

    Educational Value: Shows state transitions visually
    Metaphor: Ship changing its harbor status
    """
    state_icons = {
        'created': '🏗️',
        'running': '⛵',
        'stopped': '⚓',
        'removing': '👋'
    }

    from_icon = state_icons.get(from_state, '🚢')
    to_icon = state_icons.get(to_state, '🚢')

    st.markdown(f"""
    <style>
    @keyframes transition-fade {{
        0% {{ opacity: 1; transform: scale(1); }}
        45% {{ opacity: 0.3; transform: scale(0.8); }}
        55% {{ opacity: 0.3; transform: scale(0.8); }}
        100% {{ opacity: 1; transform: scale(1); }}
    }}

    .state-transition {{
        text-align: center;
        font-size: 48px;
        margin: 20px 0;
        animation: transition-fade 2s ease-in-out;
    }}

    .transition-arrow {{
        color: #20B2AA;
        font-size: 32px;
        margin: 0 20px;
    }}
    </style>

    <div class="state-transition">
        <span>{from_icon}</span>
        <span class="transition-arrow">→</span>
        <span>{to_icon}</span>
    </div>
    """, unsafe_allow_html=True)


def show_typing_effect(text: str, speed: float = 0.05):
    """
    Display text with typing effect

    Args:
        text: Text to display
        speed: Typing speed in seconds per character

    Educational Value: Creates engagement through animated text
    """
    placeholder = st.empty()
    displayed_text = ""

    for char in text:
        displayed_text += char
        placeholder.markdown(displayed_text)
        time.sleep(speed)


def animate_floating_ships(count: int = 5):
    """
    Display floating ships animation for background ambiance

    Args:
        count: Number of ships to animate

    Educational Value: Creates immersive harbor atmosphere
    Metaphor: Ships moving through the harbor
    """
    ships = ['⛵', '🚢', '⚓']

    animations = []
    for i in range(count):
        delay = i * 0.3
        ship = ships[i % len(ships)]
        duration = 8 + (i * 0.5)

        animations.append(f"""
        .floating-ship-{i} {{
            position: fixed;
            font-size: 32px;
            animation: float-{i} {duration}s ease-in-out infinite;
            animation-delay: {delay}s;
            z-index: -1;
            opacity: 0.3;
        }}

        @keyframes float-{i} {{
            0% {{ left: -50px; top: {20 + i * 15}%; transform: rotate(0deg); }}
            50% {{ left: 50%; top: {25 + i * 15}%; transform: rotate(5deg); }}
            100% {{ left: 110%; top: {20 + i * 15}%; transform: rotate(0deg); }}
        }}
        """)

    st.markdown(f"""
    <style>
    {''.join(animations)}
    </style>

    {''.join([f'<div class="floating-ship-{i}">{ships[i % len(ships)]}</div>' for i in range(count)])}
    """, unsafe_allow_html=True)


def add_harbor_theme_animations():
    """
    Add global harbor-themed CSS animations to the app

    Educational Value: Creates cohesive visual experience
    Metaphor: Brings the harbor environment to life
    """
    st.markdown("""
    <style>
    /* Fade in animation for content */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    .main .block-container {
        animation: fadeIn 0.5s ease-out;
    }

    /* Hover effects for interactive elements */
    button:hover {
        transform: scale(1.05);
        transition: transform 0.2s ease-in-out;
    }

    /* Pulse animation for important callouts */
    @keyframes pulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.02); }
    }

    .stAlert {
        animation: pulse 2s ease-in-out 3;
    }

    /* Smooth transitions for all elements */
    * {
        transition: all 0.3s ease-in-out;
    }
    </style>
    """, unsafe_allow_html=True)


# Example usage
if __name__ == "__main__":
    print("Harbor Docker Learning - Animations")
    print("=" * 60)
    print("Thematic animations for enhanced learning experience")
    print("=" * 60)
