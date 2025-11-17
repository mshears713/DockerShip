# 🚢 Harbor Docker Learning

**An Interactive Streamlit App to Master Docker Containers**

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-FF4B4B)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 🌊 What is Harbor Docker Learning?

Harbor Docker Learning transforms the way beginners learn Docker by using an intuitive **harbor and ship metaphor**. Just as harbor workers manage ships docking, sailing, and leaving port, you'll explore Docker containers' lifecycle through relatable, thematic visuals and interactive tutorials.

**No Docker installation required!** Practice Docker CLI commands in a safe, simulated environment that provides immediate feedback and visual representations of what's happening.

### 🎯 Perfect For

- **Beginners** new to Docker and containerization
- **Students** learning about DevOps and cloud technologies
- **Educators** teaching container concepts
- **Developers** wanting to practice Docker commands safely

---

## ✨ Key Features

### 🎓 Interactive Learning Experience
- **Step-by-step tutorials** with progressive difficulty
- **Simulated Docker CLI** - practice without Docker installation
- **Real-time feedback** on your commands
- **Visual metaphors** connecting concepts to familiar harbor operations

### 🏗️ Comprehensive Docker Coverage
- Container lifecycle management (run, stop, start, restart, remove)
- Docker image operations (pull, build, tag)
- Container inspection and logging
- Port mapping and networking basics
- Best practices and common patterns

### 🎨 Engaging User Interface
- **Harbor-themed design** with nautical colors and ship emojis
- **Animated transitions** showing state changes
- **Progress tracking** with achievement badges
- **Responsive layout** works on desktop and mobile
- **Dark/light mode** support with harbor color palette

### 🔒 Safe Learning Environment
- **Command validation** prevents dangerous operations
- **Input sanitization** with security best practices
- **Helpful error messages** guide you to correct solutions
- **Command suggestions** for common typos

---

## 🚀 Quick Start

### Prerequisites

- **Python 3.8 or higher**
- **pip** (Python package manager)
- **Virtual environment** (recommended)

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/harbor-docker-learning.git
cd harbor-docker-learning

# 2. Create a virtual environment
python -m venv env

# 3. Activate the virtual environment
# On Windows:
env\Scripts\activate
# On macOS/Linux:
source env/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Initialize the database
python -c "from data.database import init_database; from data.seed_data import seed_database; init_database(); seed_database()"

# 6. Run the application
streamlit run app.py
```

The app will open automatically in your default web browser at `http://localhost:8501`

---

## 📖 How to Use

### 1. **Start Learning**
   - Launch the app and explore the welcome page
   - Read the introduction to the harbor metaphor
   - Navigate through the sidebar to different tutorial sections

### 2. **Follow Tutorials**
   - Each tutorial teaches a specific Docker concept
   - Read the instructions and key concepts
   - Try the Docker commands in the CLI input box
   - Watch the visual feedback as containers "dock" and "sail"

### 3. **Practice Commands**
   - Type Docker commands just like you would in a real terminal
   - Get instant feedback on command correctness
   - See visual representations of container states
   - Learn from helpful error messages

### 4. **Track Progress**
   - View your progress bar in the sidebar
   - Earn achievement badges as you complete tutorials
   - Resume where you left off (progress is saved automatically)

### Example Commands to Try

```bash
# View running containers (ships in harbor)
docker ps

# Run a new container
docker run nginx

# Run a container in the background with port mapping
docker run -d -p 8080:80 nginx

# Stop a container
docker stop container-name

# View all containers (including stopped)
docker ps -a

# Remove a container
docker rm container-name

# Pull an image
docker pull redis

# View available images
docker images
```

---

## 📁 Project Structure

```
harbor-docker-learning/
├── app.py                      # Main Streamlit application
├── requirements.txt            # Python dependencies
├── Dockerfile                  # Container configuration for deployment
├── LICENSE                     # MIT License
├── README.md                   # This file
│
├── data/                       # Database and data models
│   ├── __init__.py
│   ├── database.py            # SQLite database setup
│   ├── models.py              # Data models and schemas
│   ├── db_access.py           # Database access layer
│   ├── seed_data.py           # Tutorial content and initial data
│   └── tutorials.sqlite       # SQLite database (created on init)
│
├── utils/                      # Utility modules
│   ├── __init__.py
│   ├── command_parser.py      # Docker CLI command parser
│   ├── visualizations.py      # Visual components and diagrams
│   └── animations.py          # Harbor-themed animations
│
└── docs/                       # Documentation
    ├── TUTORIAL_GUIDE.md      # Detailed tutorial usage guide
    ├── EXAMPLE_COMMANDS.md    # Example Docker command sessions
    ├── DEPLOYMENT.md          # Deployment instructions
    └── PHASE4_TESTING.md      # Testing documentation
```

---

## 🎯 Learning Objectives

### For Students

After completing Harbor Docker Learning, you will:

- ✅ **Understand Docker fundamentals** - images, containers, lifecycle
- ✅ **Master basic Docker CLI commands** - run, stop, remove, inspect
- ✅ **Grasp container states** - created, running, paused, stopped
- ✅ **Learn best practices** - naming conventions, port mapping, cleanup
- ✅ **Build confidence** to work with real Docker environments
- ✅ **Think in metaphors** - connecting abstract concepts to concrete analogies

### For Educators

Harbor Docker Learning provides:

- 📚 **Structured curriculum** - sequential tutorials with clear progression
- 🎨 **Visual teaching aids** - metaphors and diagrams enhance comprehension
- 🔄 **Interactive practice** - learn by doing in a safe environment
- 📊 **Progress tracking** - monitor student advancement
- 🎓 **Scaffolded learning** - tooltips and hints support independent learning

---

## 🛠️ Technology Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Frontend** | Streamlit | Interactive web interface |
| **Backend** | Python 3.8+ | Application logic |
| **Database** | SQLite | Tutorial content & progress storage |
| **Data Processing** | Pandas | Tutorial data manipulation |
| **Deployment** | Docker | Containerized deployment option |

### Why These Technologies?

- **Streamlit**: Rapid development, Python-native, excellent for data apps
- **SQLite**: Zero-configuration, embedded, perfect for single-user apps
- **Python**: Beginner-friendly, extensive libraries, great for education
- **Docker**: Ironic meta-learning - deploy a Docker learning app in Docker!

---

## 📚 Documentation

- **[Tutorial Usage Guide](docs/TUTORIAL_GUIDE.md)** - Detailed walkthrough of all tutorials
- **[Example Commands](docs/EXAMPLE_COMMANDS.md)** - Sample Docker CLI sessions
- **[Deployment Guide](docs/DEPLOYMENT.md)** - How to deploy the app
- **[Testing Documentation](PHASE4_TESTING.md)** - Testing procedures and results

---

## 🏗️ Development Phases

This project was built in 5 phases over 50 structured steps:

1. **Phase 1: Foundations & Setup** (Steps 1-10)
   - Project initialization, database setup, basic UI

2. **Phase 2: Core Functionality** (Steps 11-20)
   - Tutorial navigation, CLI simulation, state management

3. **Phase 3: Additional Features** (Steps 21-30)
   - Multiple sections, progress tracking, advanced visuals

4. **Phase 4: Polish & Testing** (Steps 31-40)
   - Input validation, error handling, optimization, responsiveness

5. **Phase 5: Documentation & Deployment** (Steps 41-50)
   - Documentation, examples, containerization, final polish

See the original PRD section below for complete implementation details.

---

## 🐳 Running with Docker

The easiest way to run Harbor Docker Learning is with Docker! Perfect for Windows, macOS, and Linux.

### Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running
- For Windows users: See [WINDOWS_SETUP.md](WINDOWS_SETUP.md) for detailed instructions

### Option 1: Docker Compose (Recommended) ⭐

The simplest way to run the application:

```bash
# Start the application
docker-compose up -d

# View logs
docker-compose logs -f

# Stop the application
docker-compose down
```

**Windows users**: Double-click `start.bat` or `start.ps1` for an even easier experience!

Access the app at **http://localhost:8501**

### Option 2: Docker CLI

```bash
# Build the Docker image
docker build -t harbor-docker-learning .

# Run the container
docker run -d -p 8501:8501 --name harbor-app harbor-docker-learning

# View logs
docker logs -f harbor-app

# Stop the container
docker stop harbor-app
```

### Quick Start Scripts (Windows)

For Windows users, we provide convenient scripts:

- **start.bat** / **start.ps1** - Start the application
- **stop.bat** / **stop.ps1** - Stop the application

Just double-click to run!

### Docker Benefits

- ✅ No Python installation required
- ✅ No dependency management needed
- ✅ Works identically on all platforms
- ✅ Isolated environment
- ✅ One command to start
- ✅ Easy to update and remove

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Report Bugs** - Open an issue with details
2. **Suggest Features** - Share ideas for improvements
3. **Improve Documentation** - Fix typos, add examples
4. **Add Tutorials** - Create new learning content
5. **Enhance UI** - Improve visuals and animations

### Development Setup

```bash
# Fork and clone the repository
git clone https://github.com/yourusername/harbor-docker-learning.git

# Create a feature branch
git checkout -b feature/your-feature-name

# Make your changes and test thoroughly
streamlit run app.py

# Commit with clear messages
git commit -m "Add: description of your changes"

# Push and create a pull request
git push origin feature/your-feature-name
```

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **Streamlit** - For the amazing framework
- **Docker** - For revolutionizing containerization
- **The Open Source Community** - For inspiration and support

---

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/yourusername/harbor-docker-learning/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/harbor-docker-learning/discussions)
- **Email**: your.email@example.com

---

## 🌟 Star History

If you find this project helpful, please consider giving it a star! ⭐

---

# Original Project Requirements Document

<details>
<summary>Click to expand full PRD with implementation details</summary>

## Overview

**Harbor Docker Learning** is an innovative, beginner-friendly Streamlit application designed to teach foundational Docker container concepts through an engaging harbor and ship metaphor. Just as harbor workers manage ships docking, sailing, and leaving port, users explore Docker containers' lifecycle with relatable, thematic visuals and interactive tutorials. This approach demystifies container basics by linking technical ideas to familiar, concrete analogies, making learning intuitive and memorable.

The application offers step-by-step tutorials, simulated Docker CLI exercises, and dynamic visual aids that together guide users through the core lifecycle commands—such as running, stopping, and removing containers—without requiring real Docker installation. Aesthetic and usability considerations, like themed icons, backgrounds, and animations, enhance engagement and support incremental mastery.

Targeted at beginners new to Docker and containerization, this project prioritizes clarity and hands-on practice. Built entirely using Python and Streamlit, it is scoped for delivery within 1-2 weeks, focusing on core Docker concepts while explicitly excluding complex orchestration or backend integration. By the end of this program, learners will gain both conceptual understanding and practical skills relevant to their early Docker journey.

---

## Teaching Goals

### Learning Goals

- **Understand basic Docker container concepts**
  Learners will grasp the essentials of Docker images, containers, and lifecycle commands using the harbor and ship metaphor, making abstract elements concrete.

- **Develop skills in following incremental tutorials**
  Stepwise guided lessons encourage progressive learning and reinforce understanding through hands-on exercises.

- **Familiarize with Docker CLI command simulations**
  Simulated command inputs let users practice container management workflows in a risk-free environment without requiring Docker setup.

- **Experience thematic UI design for enhanced retention**
  Using metaphors tied to harbor and ship operations helps contextualize Docker functions, improving memory and comprehension.

- **Gain introductory proficiency in Streamlit app development**
  Learners see how interactive web apps are built with Python, including layout management, user input handling, and dynamic content updates.

### Technical Goals

- **Build a Streamlit UI presenting interactive Docker tutorials**
  Create themed visuals and tutorial flows that both teach and engage users through analogy.

- **Implement stepwise tutorials with instructions and interactive exercises**
  Facilitate active learning via command simulations and stateful progress tracking.

- **Develop a simulated Docker CLI parser and output system**
  Provide realistic command feedback and validation without needing Docker engine installation.

- **Design and integrate a consistent harbor and ship themed UI/UX**
  Use icons, background images, animations, and Streamlit layout features to enhance user experience and reinforce learning metaphor.

### Priority Notes

- The project focuses on **introductory Docker concepts** and avoids complex orchestration.
- It employs **Streamlit for UI** and a **SQLite database** for persisting progress.
- The simulation layer replaces actual Docker interactions to simplify setup.
- Thematic consistency and **educational scaffolding** are paramount for engagement and understanding.
- The timeline is constrained to **1-2 weeks**, emphasizing low-to-medium complexity features.

---

## Architecture Overview

The application follows a **single-page Streamlit architecture** featuring interactive components coordinating tutorial delivery, user input, and visualization:

- **Tutorial Data Layer:**
  SQLite stores tutorial steps, progress, and metadata. A database access layer abstracts read/write operations to isolate persistence logic.

- **UI Layer:**
  Streamlit renders the themed layout: header, sidebar, tutorial content area, CLI input box, and footer. It integrates harbor-themed visuals and animations reflecting container state.

- **Simulation Engine:**
  A Python module parses simulated Docker CLI commands, validates inputs against expected tutorial commands, updates container lifecycle state variables, and generates textual + visual feedback.

- **State Management:**
  Streamlit session state retains user progress, current tutorial step, and container simulation states persistently, syncing periodically with SQLite.

- **Teaching Scaffolding:**
  Tooltips, inline help sections, interactive demos, and guided walkthroughs are embedded throughout the UI to connect metaphor to Docker concepts.

```
+--------------------+
|   Streamlit Frontend|
|  - Thematic UI      |
|  - Tutorial Views   |
|  - CLI Input Box    |
+----------+---------+
           |
           v
+--------------------+
| Simulation Engine   |
| - Command Parsing   |
| - State Management  |
+----------+---------+
           |
           v
+--------------------+
| SQLite Database     |
| - Tutorial Content  |
| - User Progress     |
+--------------------+
```

---

## Implementation Plan - All 50 Steps

### Phase 1: Foundations & Setup (Steps 1-10)

**Step 1: Initialize Project Repository and Environment**
- Create project folder, initialize Git, set up Python virtual environment
- Install Streamlit, pandas, and SQLite dependencies

**Step 2: Create Basic Streamlit App Scaffold**
- Build minimal Streamlit app with welcome page and ship graphic

**Step 3: Define Data Model for Tutorial Steps**
- Design schema for tutorial content: step ID, title, description, expected commands

**Step 4: Set up SQLite Database and Tables**
- Create SQLite schema for tutorials and progress tracking

**Step 5: Seed Database with Sample Tutorial Data**
- Insert sample tutorial steps into database

**Step 6: Implement Database Access Layer**
- Create functions for CRUD operations on tutorials and progress

**Step 7: Implement Basic Thematic UI Layout**
- Develop first iteration of UI with harbor colors and ship icons

**Step 8: Load and Display First Tutorial Step**
- Configure app to fetch and render first tutorial content

**Step 9: Add Footer with Project Info and Navigation Hints**
- Create persistent footer with project info

**Step 10: Implement Basic Streamlit Page Layout Using Columns**
- Use Streamlit's column layout for tutorial text and visuals

---

### Phase 2: Core Functionality & Basic Integration (Steps 11-20)

**Step 11: Implement Next and Previous Tutorial Navigation Buttons**
- Add UI buttons to move sequentially through tutorials

**Step 12: Create a Simulated Docker CLI Input Box**
- Add text input widget for Docker-like commands

**Step 13: Develop Docker CLI Command Parser for Simulations**
- Parse command strings and interpret operations

**Step 14: Display Simulated CLI Command Output**
- Render command results with success or error messages

**Step 15: Link CLI Input Commands to Tutorial Step Validation**
- Validate user commands against expected tutorial commands

**Step 16: Create Visual Aid Placeholders for Container States**
- Add harbor-themed visuals for container lifecycle states

**Step 17: Implement State Management for Simulated Containers**
- Track and update container lifecycle states

**Step 18: Update Visual Aids Based on Container State**
- Dynamically update visuals when container state changes

**Step 19: Enhance Thematic UI with Harbor Background and Icons**
- Add scenic harbor backgrounds and ship icons

**Step 20: Implement Tutorial Completion Flag per Step**
- Mark tutorial steps as complete and show progress badges

---

### Phase 3: Additional Features & Refinements (Steps 21-30)

**Step 21: Add Multiple Tutorial Sections with Categorization**
- Organize tutorial content into labeled categories

**Step 22: Implement Section-Based Navigation in Sidebar**
- Sidebar UI for switching tutorial categories

**Step 23: Extend Command Parser to Handle Invalid Inputs**
- Improve parser with user-friendly error messages

**Step 24: Add Feedback Messages for Correct/Incorrect Commands**
- Provide immediate color-coded feedback

**Step 25: Create Progress Tracker UI Component**
- Visual progress bar showing tutorial advancement

**Step 26: Save User Progress State in SQLite**
- Persist completion and position data

**Step 27: Integrate User Progress Loading on App Start**
- Load user progress automatically

**Step 28: Add More Detailed Visual Representations of Container Lifecycle**
- Interactive diagrams with animations

**Step 29: Implement Simulated Docker Image Operations**
- Simulate image lifecycle (pull, build, tag)

**Step 30: Add Thematic Animations Using Streamlit Components**
- Subtle animations reinforcing theme

---

### Phase 4: Polish, Testing & Optimization (Steps 31-40)

**Step 31: Implement Input Validation for CLI Commands**
- Robust syntax and format validation

**Step 32: Add Exception Handling in Database Access Code**
- Graceful error management

**Step 33: Improve App Responsiveness with Streamlit Caching**
- Use caching for data and computations

**Step 34: Conduct Manual UI/UX Testing for Navigation Flow**
- Ensure smooth, consistent navigation

**Step 35: Test Command Simulation with Various Inputs**
- Verify parser robustness

**Step 36: Add Error Messages for Missing or Corrupted Data**
- Detect and inform data integrity problems

**Step 37: Refine Thematic UI Colors and Font Consistency**
- Polish UI styling

**Step 38: Optimize Image Sizes and Loading Times**
- Resize and compress assets (emoji-based design)

**Step 39: Add Tooltips and Help Text for UI Elements**
- Comprehensive contextual help

**Step 40: Perform Cross-Platform UI Check on Different Screen Sizes**
- Test and adjust layout for desktop and mobile

---

### Phase 5: Documentation, Examples & Deployment Prep (Steps 41-50)

**Step 41: Write README with Project Overview and Setup Instructions** ✅
- Create comprehensive user-facing README

**Step 42: Create Tutorial Usage Guide with Screenshots**
- Develop detailed user guide with images

**Step 43: Prepare Example Docker Command Sessions**
- Pre-written sample sessions

**Step 44: Add Inline Code Comments and Docstrings**
- Comprehensive code documentation

**Step 45: Create a LICENSE File**
- Add open-source licensing

**Step 46: Build a Requirements Freezing File**
- Generate locked dependency versions

**Step 47: Prepare Dockerfile for Containerizing the App**
- Write Dockerfile for deployment

**Step 48: Test Docker Container Build and Run Locally**
- Verify container deployment

**Step 49: Create Deployment Instructions and Environment Variables Guide**
- Write deployment documentation

**Step 50: Final Code Cleanup and Commit**
- Review and finalize codebase

---

## Global Teaching Notes

Educational scaffolding is built throughout the application to guide users interactively, centering on the harbor and ship metaphor to simplify Docker container concepts. Every UI element features explanatory tooltips connecting user actions to technical learning goals.

The app employs interactive demos, command simulation, progress tracking, and contextual feedback to support incremental discovery and hands-on practice.

</details>

---

**Built with ❤️ for Docker learners everywhere**
