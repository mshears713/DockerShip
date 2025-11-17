# Claude.md - AI Agent Programming Guide for Harbor Docker Learning

## Project Overview

**Harbor Docker Learning** is an educational Streamlit application that teaches Docker container concepts through an interactive harbor and ship metaphor. The app simulates Docker CLI operations without requiring actual Docker installation, making it perfect for beginners.

**Key Concept**: Ships in a harbor = Containers in Docker
- Ships docking = Containers starting
- Ships sailing = Containers running
- Ships leaving = Containers stopping/removing

## Project Philosophy & Core Principles

### Educational First
- **Every feature must teach**: UI elements, animations, and interactions should reinforce Docker concepts
- **Progressive disclosure**: Introduce complexity gradually through phases
- **Metaphor consistency**: Always maintain the harbor/ship analogy
- **Scaffolded learning**: Provide tooltips, hints, and contextual help throughout

### Technical Principles
- **Simplicity over complexity**: Use straightforward solutions appropriate for 1-2 week timeline
- **Simulation over integration**: Simulate Docker operations rather than requiring Docker installation
- **State management**: Use Streamlit session state + SQLite for persistence
- **Thematic coherence**: All visuals, animations, and UI elements follow harbor theme

## Technology Stack

| Component | Technology | Why |
|-----------|-----------|-----|
| Frontend/UI | Streamlit | Rapid prototyping, Python-first, minimal code for interactive apps |
| Backend | None | All logic in app; simplifies architecture |
| Database | SQLite | Lightweight, embedded, no separate server needed |
| Data Handling | pandas | Efficient data manipulation for tutorials and state |
| Language | Python 3.8+ | Accessible to beginners, extensive library support |

## Project Structure

```
/harbor-docker-learning/
├── app.py                      # Main Streamlit application entry point
├── db/
│   └── tutorials.sqlite        # SQLite database for tutorials and progress
├── data/
│   └── seed_data.py           # Database seeding scripts
├── utils/
│   └── command_parser.py      # Docker CLI command simulation parser
├── assets/
│   ├── images/                # Harbor-themed background images
│   └── icons/                 # Ship and harbor icons
├── README.md                  # Comprehensive project documentation
├── requirements.txt           # Python dependencies
├── Dockerfile                 # Container deployment configuration
└── claude.md                  # This file - AI agent guide

```

## Architecture

### Application Layers

1. **UI Layer (Streamlit)**
   - Renders themed harbor layout
   - Manages user interactions
   - Displays tutorial content
   - Shows CLI input/output
   - Presents visual aids and animations

2. **Simulation Engine**
   - Parses simulated Docker commands
   - Validates command syntax
   - Manages container lifecycle states
   - Generates feedback (text + visual)
   - Maps commands to learning objectives

3. **Data Layer (SQLite)**
   - Stores tutorial content
   - Tracks user progress
   - Persists container simulation states
   - Provides abstraction via database access layer

4. **State Management**
   - Streamlit session state for current runtime
   - Periodic sync with SQLite for persistence
   - Tracks: current step, completed steps, container states

### Data Flow

```
User Input (CLI command)
    ↓
Command Parser (validation)
    ↓
State Update (container lifecycle)
    ↓
Visual Update (animations) + Feedback (messages)
    ↓
Progress Persistence (SQLite)
```

## Development Phases

The project follows a 5-phase, 50-step implementation plan:

### Phase 1: Foundations & Setup (Steps 1-10)
- Initialize repository and environment
- Create basic Streamlit scaffold
- Define data models
- Set up SQLite database
- Implement basic themed UI
- Load first tutorial step

### Phase 2: Core Functionality (Steps 11-20)
- Tutorial navigation (next/previous)
- Simulated CLI input
- Command parser
- Command output display
- Step validation
- Visual aids for container states
- State management
- Dynamic visual updates
- Enhanced theming

### Phase 3: Additional Features (Steps 21-30)
- Multiple tutorial sections
- Section-based navigation
- Enhanced error handling
- Feedback messages
- Progress tracker UI
- Progress persistence
- Detailed lifecycle visuals
- Simulated image operations
- Thematic animations

### Phase 4: Polish & Testing (Steps 31-40)
- Input validation
- Exception handling
- Performance optimization (caching)
- UI/UX testing
- Error messages
- Theme refinement
- Image optimization
- Comprehensive tooltips
- Cross-platform testing

### Phase 5: Documentation & Deployment (Steps 41-50)
- README documentation
- Tutorial usage guide
- Example command sessions
- Code comments and docstrings
- License file
- Requirements.txt
- Dockerfile
- Container testing
- Deployment instructions
- Final cleanup

## Key Components to Implement

### 1. Command Parser (`utils/command_parser.py`)

The parser simulates Docker CLI commands. Key functions:

```python
def parse_command(command_str):
    """
    Parse and validate simulated Docker command

    Supported commands:
    - docker run <image>
    - docker ps
    - docker stop <container>
    - docker rm <container>
    - docker images
    - docker pull <image>

    Returns:
        dict: {
            'command': str,
            'action': str,
            'target': str,
            'valid': bool,
            'message': str
        }
    """
```

**Implementation Notes**:
- Use regex for command parsing
- Validate command structure
- Provide helpful error messages
- Map commands to lifecycle states
- Include educational context in responses

### 2. Database Schema

**Tables**:

```sql
CREATE TABLE tutorials (
    id INTEGER PRIMARY KEY,
    section TEXT NOT NULL,
    step_number INTEGER NOT NULL,
    title TEXT NOT NULL,
    description TEXT,
    expected_command TEXT,
    visual_state TEXT,
    help_text TEXT
);

CREATE TABLE user_progress (
    id INTEGER PRIMARY KEY,
    tutorial_id INTEGER,
    completed BOOLEAN DEFAULT 0,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (tutorial_id) REFERENCES tutorials(id)
);

CREATE TABLE container_states (
    id INTEGER PRIMARY KEY,
    container_name TEXT UNIQUE,
    state TEXT, -- 'running', 'stopped', 'removed'
    image TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

### 3. State Management Pattern

Use Streamlit session state for runtime + SQLite for persistence:

```python
# Initialize session state
if 'current_tutorial_id' not in st.session_state:
    st.session_state.current_tutorial_id = 1

if 'containers' not in st.session_state:
    st.session_state.containers = {}

if 'completed_steps' not in st.session_state:
    st.session_state.completed_steps = load_progress_from_db()

# Update and persist
def complete_step(tutorial_id):
    st.session_state.completed_steps.add(tutorial_id)
    save_progress_to_db(tutorial_id)
```

### 4. Visual State Mapping

Map container states to harbor visuals:

| Container State | Harbor Visual | Animation |
|----------------|---------------|-----------|
| Creating | Ship approaching dock | Fade in |
| Running | Ship docked, active | Gentle rocking |
| Stopped | Ship docked, inactive | Static, dimmed |
| Removing | Ship leaving port | Fade out |

## Coding Conventions

### Python Style
- Follow PEP 8
- Use type hints where helpful
- Write docstrings for all functions
- Keep functions small and focused
- Use meaningful variable names that reflect the harbor metaphor

### Streamlit Best Practices
- Use `@st.cache_data` for data loading
- Use `@st.cache_resource` for expensive computations
- Minimize reruns with session state
- Use columns for layout
- Implement sidebar for navigation

### Educational Code Comments
Every component should include:
1. **Purpose**: What does this do?
2. **Educational value**: How does this teach Docker concepts?
3. **Metaphor connection**: How does this relate to the harbor theme?

Example:
```python
def dock_container(container_name):
    """
    Simulate starting a Docker container (ship docking in harbor)

    Educational value: Demonstrates 'docker run' command
    Metaphor: A ship arriving and docking at the harbor

    Args:
        container_name: Name of container/ship to dock
    """
```

## Working with the Codebase

### Adding a New Tutorial Step

1. **Define content** in seed data or database
2. **Create expected command** validation
3. **Design visual state** for the step
4. **Write help text** with metaphor explanation
5. **Add tooltips** for UI elements
6. **Test navigation** flow

### Implementing a New Docker Command

1. **Add parser logic** in `command_parser.py`
2. **Define expected output** format
3. **Update state management** for command effects
4. **Create visual feedback** (animation/icon change)
5. **Write validation logic** for tutorial steps
6. **Add error handling** for invalid syntax

### Adding Visual Elements

1. **Choose harbor-appropriate** imagery/icons
2. **Implement in themed colors** (blues, teals, nautical palette)
3. **Add hover tooltips** explaining metaphor
4. **Create smooth transitions** using Streamlit components
5. **Ensure responsive design** across screen sizes
6. **Test accessibility** (alt text, contrast)

## Testing Guidelines

### Manual Testing Checklist
- [ ] All tutorial steps load correctly
- [ ] Navigation flows smoothly (next/previous)
- [ ] CLI parser handles valid commands
- [ ] CLI parser rejects invalid commands gracefully
- [ ] Visual states update on command execution
- [ ] Progress saves and loads correctly
- [ ] UI is responsive on different screen sizes
- [ ] All tooltips display correctly
- [ ] Animations are smooth and meaningful
- [ ] Theme consistency throughout app

### Command Parser Test Cases
- Valid commands: `docker run nginx`, `docker ps`, `docker stop mycontainer`
- Invalid commands: `docker ren`, `doker run`, `docker` (incomplete)
- Edge cases: Extra whitespace, case sensitivity, special characters

### Data Integrity Tests
- Database connection handling
- Missing tutorial data
- Corrupted progress data
- Multiple simultaneous sessions

## Performance Considerations

### Caching Strategy
```python
@st.cache_data(ttl=3600)
def load_tutorials():
    """Cache tutorial data for 1 hour"""
    return fetch_from_database()

@st.cache_resource
def get_database_connection():
    """Singleton database connection"""
    return sqlite3.connect('db/tutorials.sqlite')
```

### Image Optimization
- Use WebP format for smaller file sizes
- Compress images to < 100KB each
- Lazy load images not immediately visible
- Use appropriate resolution (no higher than needed)

### Database Optimization
- Index frequently queried fields
- Use prepared statements
- Batch progress updates
- Close connections properly

## Common Development Patterns

### Navigation Pattern
```python
col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    if st.button("← Previous") and st.session_state.current_step > 1:
        st.session_state.current_step -= 1
        st.rerun()

with col3:
    if st.button("Next →"):
        st.session_state.current_step += 1
        st.rerun()
```

### Command Input Pattern
```python
command = st.text_input(
    "Enter Docker command:",
    placeholder="e.g., docker run nginx",
    help="Try the command shown in the tutorial above"
)

if command:
    result = parse_command(command)
    if result['valid']:
        st.success(result['message'])
        update_container_state(result)
        update_visuals()
    else:
        st.error(result['message'])
```

### Progress Tracking Pattern
```python
total_steps = len(get_all_tutorials())
completed = len(st.session_state.completed_steps)
progress = completed / total_steps

st.progress(progress)
st.caption(f"Progress: {completed}/{total_steps} steps completed")
```

## Theming Guidelines

### Color Palette
- **Primary**: Navy blue (#1E3A5F) - Deep water
- **Secondary**: Teal (#20B2AA) - Harbor water
- **Accent**: Coral (#FF7F50) - Harbor lights
- **Success**: Sea green (#2E8B57) - Go signal
- **Warning**: Amber (#FFB347) - Caution
- **Error**: Red (#DC143C) - Stop signal
- **Background**: Light blue-gray (#F0F4F8) - Sky

### Typography
- **Headers**: Bold, nautical-inspired
- **Body**: Clear, readable (14-16px)
- **Code**: Monospace for commands
- **Tooltips**: Smaller, italic for hints

### Icon Usage
- 🚢 Ships for containers
- ⚓ Anchors for stopped containers
- 🌊 Waves for running processes
- 🏗️ Cranes for building images
- 📦 Boxes for images
- 🎯 Targets for learning objectives

## Common Pitfalls to Avoid

### 1. Breaking the Metaphor
❌ Bad: "Click to initialize container instance"
✅ Good: "Click to dock the ship in harbor"

### 2. Over-complicating State
❌ Bad: Complex state machines with many substates
✅ Good: Simple states mapped to Docker lifecycle (created, running, stopped, removed)

### 3. Ignoring Educational Value
❌ Bad: Just simulating commands without explanation
✅ Good: Each command includes tooltip explaining what it does in Docker

### 4. Poor Error Messages
❌ Bad: "Invalid input"
✅ Good: "The command 'docker ren' is not recognized. Did you mean 'docker run'?"

### 5. Inconsistent Theme
❌ Bad: Mixing metaphors (harbor, space, road trips)
✅ Good: Consistently using harbor/ship/maritime terminology

## Debugging Tips

### Streamlit State Issues
```python
# Add debug panel in development
if st.checkbox("Show Debug Info"):
    st.write("Session State:", st.session_state)
    st.write("Current Tutorial:", get_current_tutorial())
```

### Database Issues
```python
# Add connection testing
try:
    conn = get_database_connection()
    st.success("Database connected")
except Exception as e:
    st.error(f"Database error: {e}")
```

### Parser Issues
```python
# Log parsed commands for debugging
import logging
logging.basicConfig(level=logging.DEBUG)

def parse_command(cmd):
    logging.debug(f"Parsing command: {cmd}")
    # ... parsing logic
```

## Git Workflow

### Branch Strategy
- `main` - Production-ready code
- `develop` - Integration branch
- `feature/*` - Feature branches
- `bugfix/*` - Bug fix branches
- `claude/*` - AI agent working branches

### Commit Messages
Follow conventional commits:
- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation changes
- `style:` - Code style changes
- `refactor:` - Code refactoring
- `test:` - Test additions/changes
- `chore:` - Maintenance tasks

Examples:
```
feat: add docker run command simulation
fix: correct container state transition on stop
docs: update README with setup instructions
style: apply harbor theme to tutorial cards
refactor: extract command parser into utils module
```

## Extension Opportunities

### Future Enhancements
1. **Advanced Docker Concepts**
   - Docker networks simulation
   - Volume mounting metaphor (cargo loading)
   - Multi-container scenarios (fleet management)

2. **Interactive Features**
   - Drag-and-drop ship/container management
   - Real-time collaboration (multiple users in harbor)
   - Achievement system (sailor ranks)

3. **Content Expansion**
   - Docker Compose tutorials (fleet coordination)
   - Dockerfile creation lessons (shipbuilding)
   - Registry operations (port-to-port shipping)

4. **Technical Improvements**
   - Real Docker engine integration option
   - Export progress reports
   - Social sharing of achievements
   - Integration with Docker Hub API

## Security Considerations

### Input Validation
- **Sanitize all user inputs** before parsing
- **Prevent command injection** in simulated CLI
- **Validate file paths** if file operations added
- **Escape special characters** in database queries

### Database Security
- Use **parameterized queries** (no string concatenation)
- **Validate data types** before insertion
- **Handle errors gracefully** without exposing internals
- **Back up database** regularly

### Deployment Security
- **Use environment variables** for sensitive config
- **Don't commit secrets** to version control
- **Set proper file permissions** in Docker container
- **Use HTTPS** in production deployment

## FAQ for AI Agents

### Q: How do I add a new tutorial section?
A:
1. Add section data to database seed file
2. Update section navigation in sidebar
3. Create tutorial steps for the section
4. Add section-specific visual elements
5. Update progress tracking to include section

### Q: How do I simulate a new Docker command?
A:
1. Add command pattern to parser regex
2. Define expected behavior and output
3. Update container state management
4. Create visual feedback for command
5. Add command to tutorial steps where relevant

### Q: What if Streamlit doesn't support an animation I need?
A:
- Use `st.markdown()` with HTML/CSS
- Try Streamlit components library
- Create custom component if necessary
- Use image sequences for frame-by-frame animation
- Consider Lottie animations via streamlit-lottie

### Q: How do I test without a database?
A:
- Create mock database functions
- Use in-memory SQLite (`:memory:`)
- Provide sample data in JSON format
- Use Streamlit session state only (no persistence)

### Q: Should I implement real Docker integration?
A: **Not in the initial scope**. The project explicitly focuses on simulation to avoid Docker installation requirements. This can be added as an advanced opt-in feature later.

### Q: How detailed should tooltips be?
A:
- **Concise but informative** (1-2 sentences)
- **Connect to metaphor** explicitly
- **Link to Docker concept** being taught
- **Actionable** when relevant (e.g., "Try running: docker ps")

### Q: When should I use animations vs. static visuals?
A:
- **Animations**: State transitions (docking, sailing, removing)
- **Static**: Current state display, icons, backgrounds
- **Balance**: Don't overdo animations - use purposefully for teaching

## Resources & References

### Streamlit Documentation
- [Streamlit API Reference](https://docs.streamlit.io/)
- [Session State Guide](https://docs.streamlit.io/library/api-reference/session-state)
- [Caching Guide](https://docs.streamlit.io/library/advanced-features/caching)

### Docker Concepts
- Docker CLI command reference
- Container lifecycle documentation
- Image vs. Container distinction

### Design Inspiration
- Nautical/maritime color palettes
- Harbor and port illustrations
- Educational app UX patterns

## Contact & Contributions

When working on this project:
- **Stay focused** on educational goals
- **Maintain metaphor** consistency
- **Document thoroughly** with educational context
- **Test incrementally** after each feature
- **Seek feedback** on learning effectiveness

## Quick Reference Commands

### Run the app
```bash
streamlit run app.py
```

### Initialize database
```bash
python data/seed_data.py
```

### Install dependencies
```bash
pip install -r requirements.txt
```

### Build Docker image
```bash
docker build -t harbor-docker-learning .
```

### Run in container
```bash
docker run -p 8501:8501 harbor-docker-learning
```

---

## Final Notes for AI Agents

When working on this project, always ask yourself:

1. **Does this teach Docker concepts effectively?**
2. **Does this maintain the harbor metaphor?**
3. **Is this appropriate for beginners?**
4. **Will users understand this intuitively?**
5. **Does this fit the 1-2 week timeline?**

Remember: The goal is **education through engaging simulation**, not building a production Docker management tool. Prioritize clarity, usability, and the learning experience above technical sophistication.

Keep the harbor theme consistent, make learning fun, and help users build confidence with Docker fundamentals through the ship and harbor analogy.

---

**Document Version**: 1.0
**Last Updated**: 2025-11-17
**Project Phase**: Documentation
**Status**: Active Development
