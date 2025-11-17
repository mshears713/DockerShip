"""
Docker CLI Command Parser for Harbor Docker Learning

Educational Purpose: Simulates Docker CLI commands without requiring Docker installation.
Provides realistic feedback and validation to help users learn command syntax and behavior.

Metaphor Connection: Just as harbor masters understand ship commands, this parser
interprets Docker commands and translates them into harbor operations.
"""

import re
from dataclasses import dataclass
from typing import Optional, List, Dict, Any


@dataclass
class CommandResult:
    """
    Result of parsing and executing a simulated Docker command

    Educational Value: Provides structured feedback to guide learning

    Attributes:
        command: The original command string
        action: The Docker action (run, ps, stop, rm, images, pull, etc.)
        target: The target of the action (container name, image name, etc.)
        valid: Whether the command is syntactically valid
        success: Whether the command executed successfully
        message: Feedback message for the user
        help_hint: Optional hint for improving the command
        metaphor_explanation: Harbor metaphor explanation
        output: Simulated command output
    """
    command: str
    action: str = ""
    target: str = ""
    valid: bool = False
    success: bool = False
    message: str = ""
    help_hint: Optional[str] = None
    metaphor_explanation: Optional[str] = None
    output: str = ""
    flags: Dict[str, Any] = None

    def __post_init__(self):
        if self.flags is None:
            self.flags = {}


# Supported Docker commands and their patterns
COMMAND_PATTERNS = {
    'run': r'^docker\s+run\s+(?P<flags>(?:-[a-zA-Z]\s+\S+\s+|--[a-z-]+(?:=\S+)?\s+)*)?(?P<image>\S+)(?:\s+(?P<command>.+))?$',
    'ps': r'^docker\s+ps(?:\s+(?P<flags>-a|-all|--all))?$',
    'stop': r'^docker\s+stop\s+(?P<container>\S+)$',
    'rm': r'^docker\s+rm\s+(?P<flags>-f\s+)?(?P<container>\S+)$',
    'images': r'^docker\s+images(?:\s+(?P<flags>-a|--all))?$',
    'pull': r'^docker\s+pull\s+(?P<image>\S+)$',
    'start': r'^docker\s+start\s+(?P<container>\S+)$',
    'restart': r'^docker\s+restart\s+(?P<container>\S+)$',
    'logs': r'^docker\s+logs\s+(?P<flags>-f\s+)?(?P<container>\S+)$',
    'inspect': r'^docker\s+inspect\s+(?P<target>\S+)$',
    'build': r'^docker\s+build\s+(?P<flags>(?:-t\s+\S+\s+|--tag\s+\S+\s+)*)?(?P<path>\S+)$',
}

# Harbor metaphor explanations for each command
METAPHOR_EXPLANATIONS = {
    'run': "🚢 Running a container is like launching a new ship from a blueprint into the harbor. The ship (container) begins its voyage (execution).",
    'ps': "📋 Listing containers is like checking which ships are currently in your harbor. You can see all active vessels at a glance.",
    'stop': "⚓ Stopping a container is like anchoring a ship. It's still in the harbor but no longer actively sailing.",
    'rm': "🗑️ Removing a container is like decommissioning a ship. Once removed, it leaves the harbor completely.",
    'images': "📦 Listing images is like reviewing all ship blueprints available in your shipyard. Each blueprint can create many ships.",
    'pull': "📥 Pulling an image is like downloading a new ship blueprint from the central shipyard registry (Docker Hub).",
    'start': "⛵ Starting a stopped container is like setting a docked ship back into motion.",
    'restart': "🔄 Restarting a container is like bringing a ship back to dock and immediately sending it out again.",
    'logs': "📜 Viewing logs is like reading a ship's logbook to see what happened during its journey.",
    'inspect': "🔍 Inspecting shows detailed information about a ship (container) or blueprint (image).",
    'build': "🏗️ Building an image is like constructing a new ship blueprint from specifications.",
}


def parse_command(command_str: str) -> CommandResult:
    """
    Parse and validate a simulated Docker command

    Educational Purpose: Helps users learn correct Docker command syntax through
    interactive feedback and validation.

    Args:
        command_str: The Docker command string to parse

    Returns:
        CommandResult: Structured result with validation and feedback

    Example:
        >>> result = parse_command("docker run nginx")
        >>> print(result.valid)  # True
        >>> print(result.action)  # "run"
        >>> print(result.target)  # "nginx"
    """
    # Step 31: Enhanced Input Validation
    # Validate input is not None or non-string
    if command_str is None or not isinstance(command_str, str):
        return CommandResult(
            command=str(command_str) if command_str else "",
            valid=False,
            message="❌ Invalid command input. Please enter a valid Docker command.",
            help_hint="Commands must be text strings starting with 'docker'"
        )

    # Clean and normalize the command
    command_str = command_str.strip()

    # Empty command check
    if not command_str:
        return CommandResult(
            command=command_str,
            valid=False,
            message="❌ No command entered. Try typing a Docker command!",
            help_hint="Start with: docker ps"
        )

    # Maximum length validation (prevent extremely long inputs)
    MAX_COMMAND_LENGTH = 500
    if len(command_str) > MAX_COMMAND_LENGTH:
        return CommandResult(
            command=command_str[:50] + "...",
            valid=False,
            message=f"❌ Command too long ({len(command_str)} characters). Maximum allowed: {MAX_COMMAND_LENGTH}",
            help_hint="Docker commands should be concise. Check for errors or unnecessary repetition."
        )

    # Check for potentially dangerous characters (educational security note)
    # While this is a simulation, we teach good input validation practices
    dangerous_patterns = [';', '&&', '||', '|', '`', '$(' , '$(', '>${', '<(']
    if any(pattern in command_str for pattern in dangerous_patterns):
        return CommandResult(
            command=command_str,
            valid=False,
            message="❌ Invalid characters detected in command",
            help_hint="Docker commands should not contain shell operators like ;, &&, ||, or backticks. Use simple Docker command syntax."
        )

    # Check for excessive whitespace or control characters
    if any(ord(char) < 32 and char not in ['\t', '\n'] for char in command_str):
        return CommandResult(
            command=command_str,
            valid=False,
            message="❌ Invalid control characters in command",
            help_hint="Please use only printable characters in Docker commands."
        )

    # Check if command starts with 'docker'
    if not command_str.lower().startswith('docker'):
        return CommandResult(
            command=command_str,
            valid=False,
            message="❌ Commands must start with 'docker'",
            help_hint=f"Did you mean: docker {command_str}?"
        )

    # Try to match against known command patterns
    for action, pattern in COMMAND_PATTERNS.items():
        match = re.match(pattern, command_str, re.IGNORECASE)
        if match:
            return _handle_matched_command(command_str, action, match)

    # Command not recognized
    return _handle_unknown_command(command_str)


def _handle_matched_command(command_str: str, action: str, match: re.Match) -> CommandResult:
    """
    Handle a successfully matched command

    Educational Purpose: Provides success feedback and metaphor explanation
    """
    groups = match.groupdict()

    # Extract target based on command type
    target = ""
    if 'container' in groups:
        target = groups['container'] or ""
    elif 'image' in groups:
        target = groups['image'] or ""
    elif 'target' in groups:
        target = groups['target'] or ""
    elif 'path' in groups:
        target = groups['path'] or ""

    # Extract flags if present
    flags = {}
    if 'flags' in groups and groups['flags']:
        flags = _parse_flags(groups['flags'])

    # Build success message
    message = _build_success_message(action, target, flags)

    # Generate simulated output
    output = _generate_simulated_output(action, target, flags)

    return CommandResult(
        command=command_str,
        action=action,
        target=target,
        valid=True,
        success=True,
        message=message,
        metaphor_explanation=METAPHOR_EXPLANATIONS.get(action, ""),
        output=output,
        flags=flags
    )


def _handle_unknown_command(command_str: str) -> CommandResult:
    """
    Handle an unrecognized Docker command

    Educational Purpose: Provides helpful suggestions for typos or unknown commands
    """
    # Extract the attempted action
    parts = command_str.split()
    attempted_action = parts[1] if len(parts) > 1 else ""

    # Find similar commands (simple edit distance)
    suggestions = _find_similar_commands(attempted_action)

    message = f"❌ Unknown Docker command: '{attempted_action}'"
    help_hint = None

    if suggestions:
        help_hint = f"Did you mean: {', '.join(suggestions)}?"
    else:
        help_hint = "Supported commands: run, ps, stop, rm, images, pull, start, restart, logs, inspect, build"

    return CommandResult(
        command=command_str,
        valid=False,
        message=message,
        help_hint=help_hint
    )


def _parse_flags(flags_str: str) -> Dict[str, Any]:
    """Parse command line flags"""
    flags = {}

    # Common flags
    if '-a' in flags_str or '--all' in flags_str:
        flags['all'] = True
    if '-f' in flags_str or '--force' in flags_str:
        flags['force'] = True
    if '-d' in flags_str or '--detach' in flags_str:
        flags['detach'] = True

    # Port mapping (-p flag)
    port_match = re.search(r'-p\s+(\d+):(\d+)', flags_str)
    if port_match:
        flags['port'] = f"{port_match.group(1)}:{port_match.group(2)}"

    # Name flag (--name)
    name_match = re.search(r'--name[=\s]+(\S+)', flags_str)
    if name_match:
        flags['name'] = name_match.group(1)

    # Tag flag (-t or --tag)
    tag_match = re.search(r'(?:-t|--tag)[=\s]+(\S+)', flags_str)
    if tag_match:
        flags['tag'] = tag_match.group(1)

    return flags


def _build_success_message(action: str, target: str, flags: Dict) -> str:
    """Build a success message for a valid command"""
    messages = {
        'run': f"✅ Launching container from image '{target}'",
        'ps': "✅ Listing containers in your harbor",
        'stop': f"✅ Anchoring container '{target}'",
        'rm': f"✅ Removing container '{target}' from harbor",
        'images': "✅ Showing available ship blueprints",
        'pull': f"✅ Downloading image '{target}' from registry",
        'start': f"✅ Starting container '{target}'",
        'restart': f"✅ Restarting container '{target}'",
        'logs': f"✅ Reading logbook of '{target}'",
        'inspect': f"✅ Inspecting '{target}'",
        'build': f"✅ Building image from '{target}'",
    }

    base_message = messages.get(action, f"✅ Executing {action}")

    # Add flag information
    if flags.get('all'):
        base_message += " (including stopped)"
    if flags.get('detach'):
        base_message += " in background mode"
    if flags.get('port'):
        base_message += f" with port mapping {flags['port']}"
    if flags.get('name'):
        base_message += f" with name '{flags['name']}'"

    return base_message


def _generate_simulated_output(action: str, target: str, flags: Dict) -> str:
    """Generate realistic simulated Docker command output"""
    import random
    import string

    def random_id(length=12):
        return ''.join(random.choices(string.hexdigits.lower(), k=length))

    outputs = {
        'run': f"{random_id()}\n🚢 Container is now sailing in the harbor!",
        'ps': """CONTAINER ID   IMAGE     COMMAND     STATUS       PORTS     NAMES
{id}   nginx     "nginx"     Up 2 hours   80/tcp    harbor-web
{id2}   redis     "redis"     Up 1 hour    6379/tcp  harbor-cache""".format(
            id=random_id(12),
            id2=random_id(12)
        ),
        'stop': f"{target}\n⚓ Container has been anchored.",
        'rm': f"{target}\n🗑️ Container has left the harbor.",
        'images': """REPOSITORY   TAG       IMAGE ID       CREATED        SIZE
nginx        latest    {id}   2 days ago     142MB
redis        latest    {id2}   1 week ago     117MB""".format(
            id=random_id(12),
            id2=random_id(12)
        ),
        'pull': f"""Pulling from library/{target}
latest: Pulling from library/{target}
Digest: sha256:{random_id(64)}
Status: Downloaded newer image for {target}:latest
📥 Blueprint added to your shipyard!""",
        'start': f"{target}\n⛵ Container is sailing again!",
        'restart': f"{target}\n🔄 Container has been restarted.",
        'logs': f"""[{target}] 2025-11-17 12:00:00 Starting service...
[{target}] 2025-11-17 12:00:01 Service ready!
[{target}] 2025-11-17 12:00:02 Handling requests...""",
        'inspect': f"""[
    {{
        "Id": "{random_id(64)}",
        "Name": "{target}",
        "State": "running",
        "Image": "nginx:latest"
    }}
]""",
        'build': f"""Step 1/3 : FROM alpine:latest
 ---> {random_id(12)}
Step 2/3 : RUN echo "Building..."
 ---> {random_id(12)}
Step 3/3 : CMD ["echo", "Hello Harbor!"]
 ---> {random_id(12)}
Successfully built {random_id(12)}
🏗️ New ship blueprint created!""",
    }

    output = outputs.get(action, f"Simulated output for {action}")

    # Adjust for flags
    if action == 'ps' and flags.get('all'):
        output += f"\n{random_id(12)}   mysql     \"mysql\"     Exited       3306/tcp  harbor-db"

    return output


def _find_similar_commands(attempted: str) -> List[str]:
    """Find similar command names (simple Levenshtein-like matching)"""
    known_commands = list(COMMAND_PATTERNS.keys())
    suggestions = []

    for cmd in known_commands:
        # Simple similarity: check if strings share common characters
        if _similarity(attempted.lower(), cmd) > 0.5:
            suggestions.append(cmd)

    return suggestions[:3]  # Return top 3 suggestions


def _similarity(s1: str, s2: str) -> float:
    """Calculate simple similarity between two strings"""
    if not s1 or not s2:
        return 0.0

    # Count matching characters
    matches = sum(1 for c in s1 if c in s2)
    return matches / max(len(s1), len(s2))


def validate_docker_command(command: str, expected_command: str) -> bool:
    """
    Validate if a command matches the expected command for a tutorial step

    Educational Purpose: Checks if the user entered the correct command for learning

    Args:
        command: The command entered by the user
        expected_command: The expected command for this tutorial step

    Returns:
        bool: True if commands match (allowing for minor variations)
    """
    # Parse both commands
    user_result = parse_command(command)
    expected_result = parse_command(expected_command)

    # Both must be valid
    if not user_result.valid or not expected_result.valid:
        return False

    # Actions must match
    if user_result.action != expected_result.action:
        return False

    # Targets must match (if expected has a target)
    if expected_result.target and user_result.target != expected_result.target:
        return False

    return True


def get_command_help(action: str) -> str:
    """
    Get help text for a specific Docker command

    Educational Purpose: Provides quick reference for command syntax

    Args:
        action: The Docker action (run, ps, stop, etc.)

    Returns:
        str: Help text with examples
    """
    help_texts = {
        'run': """docker run [OPTIONS] IMAGE [COMMAND]

Create and start a new container from an image.

Examples:
  docker run nginx
  docker run -d -p 8080:80 --name my-web nginx

Options:
  -d, --detach       Run container in background
  -p, --publish      Publish container ports to host
  --name            Assign a name to the container""",

        'ps': """docker ps [OPTIONS]

List running containers.

Examples:
  docker ps
  docker ps -a

Options:
  -a, --all         Show all containers (including stopped)""",

        'stop': """docker stop CONTAINER

Stop one or more running containers.

Examples:
  docker stop my-container
  docker stop container-id""",

        'rm': """docker rm [OPTIONS] CONTAINER

Remove one or more containers.

Examples:
  docker rm my-container
  docker rm -f my-container

Options:
  -f, --force       Force removal of running container""",

        'images': """docker images [OPTIONS]

List available images.

Examples:
  docker images
  docker images -a

Options:
  -a, --all         Show all images""",

        'pull': """docker pull IMAGE[:TAG]

Download an image from a registry.

Examples:
  docker pull nginx
  docker pull nginx:alpine""",
    }

    return help_texts.get(action, f"No help available for '{action}'")


# Example usage and testing
if __name__ == "__main__":
    print("Harbor Docker Learning - Command Parser")
    print("=" * 60)

    # Test various commands
    test_commands = [
        "docker run nginx",
        "docker ps",
        "docker ps -a",
        "docker stop my-container",
        "docker rm my-container",
        "docker images",
        "docker pull redis",
        "docker ren nginx",  # Typo
        "run nginx",  # Missing 'docker'
        "",  # Empty
    ]

    print("\n🧪 Testing command parser:\n")
    for cmd in test_commands:
        result = parse_command(cmd)
        print(f"Command: '{cmd}'")
        print(f"  Valid: {result.valid}")
        print(f"  Action: {result.action}")
        print(f"  Message: {result.message}")
        if result.help_hint:
            print(f"  Hint: {result.help_hint}")
        print()

    print("=" * 60)
    print("✅ Command parser ready for use!")
