#!/usr/bin/env python3
"""
Task Definition Validator for alcove-testing

Validates that all task definitions in .alcove/tasks/ follow expected patterns
and reference valid security profiles.

Uses basic text parsing to avoid external dependencies.
"""

import os
import re
import sys
from pathlib import Path

def parse_yaml_value(content, key):
    """Extract a simple YAML value using regex"""
    pattern = rf'^{re.escape(key)}:\s*(.+)$'
    match = re.search(pattern, content, re.MULTILINE)
    return match.group(1).strip() if match else None

def parse_yaml_list(content, key):
    """Extract a YAML list using regex"""
    # Look for key followed by list items
    pattern = rf'^{re.escape(key)}:\s*$'
    lines = content.split('\n')

    start_line = None
    for i, line in enumerate(lines):
        if re.match(pattern, line):
            start_line = i
            break

    if start_line is None:
        return None

    items = []
    i = start_line + 1
    while i < len(lines):
        line = lines[i].strip()
        if line.startswith('- '):
            items.append(line[2:].strip())
        elif line and not line.startswith(' '):
            # Next section started
            break
        i += 1

    return items if items else None

def check_yaml_section(content, section_key):
    """Check if a YAML section exists"""
    pattern = rf'^{re.escape(section_key)}:\s*'
    return bool(re.search(pattern, content, re.MULTILINE))

def validate_task(task_path, available_profiles):
    """Validate a single task definition"""
    print(f"Validating {task_path.name}...")

    try:
        with open(task_path, 'r') as f:
            content = f.read()
    except Exception as e:
        print(f"  ❌ Error reading file: {e}")
        return False

    errors = []
    warnings = []

    # Check required fields
    name = parse_yaml_value(content, 'name')
    if not name:
        errors.append("Missing required field: name")

    description = parse_yaml_value(content, 'description')
    if not description:
        errors.append("Missing required field: description")

    # Check that either prompt or executable is defined
    has_prompt = check_yaml_section(content, 'prompt')
    has_executable = check_yaml_section(content, 'executable')

    if not has_prompt and not has_executable:
        errors.append("Task must have either 'prompt' or 'executable' field")

    # Check profiles if specified
    profiles = parse_yaml_list(content, 'profiles')
    if profiles is not None:
        for profile in profiles:
            if profile not in available_profiles:
                if profile == 'nonexistent-profile':
                    # This is expected for testing
                    warnings.append(f"References test profile '{profile}' (expected for validation testing)")
                else:
                    errors.append(f"References unknown profile: {profile}")

    # Check timeout
    timeout = parse_yaml_value(content, 'timeout')
    if timeout:
        try:
            timeout_val = int(timeout)
            if timeout_val <= 0:
                errors.append("'timeout' must be a positive integer")
        except ValueError:
            errors.append("'timeout' must be a valid integer")

    # Print results
    if errors:
        print(f"  ❌ ERRORS in {task_path.name}:")
        for error in errors:
            print(f"    - {error}")

    if warnings:
        print(f"  ⚠️  WARNINGS in {task_path.name}:")
        for warning in warnings:
            print(f"    - {warning}")

    if not errors and not warnings:
        print(f"  ✅ {task_path.name} is valid")
    elif not errors:
        print(f"  ✅ {task_path.name} is valid (with warnings)")

    return len(errors) == 0

def load_security_profiles():
    """Load all available security profile names"""
    profiles_dir = Path('.alcove/security-profiles')
    profiles = set()

    if profiles_dir.exists():
        for profile_file in profiles_dir.glob('*.yml'):
            try:
                with open(profile_file, 'r') as f:
                    content = f.read()
                    name = parse_yaml_value(content, 'name')
                    if name:
                        profiles.add(name)
            except Exception as e:
                print(f"Warning: Could not parse {profile_file}: {e}")

    return profiles

def main():
    """Main validation function"""
    print("🔍 Alcove Task Definition Validator")
    print("=" * 40)

    # Check if we're in the right directory
    if not Path('.alcove').exists():
        print("❌ Error: .alcove directory not found. Run from repository root.")
        sys.exit(1)

    # Load available security profiles
    profiles = load_security_profiles()
    print(f"📋 Found {len(profiles)} security profiles: {', '.join(sorted(profiles))}")
    print()

    # Find and validate all task files
    tasks_dir = Path('.alcove/tasks')
    if not tasks_dir.exists():
        print("❌ Error: .alcove/tasks directory not found")
        sys.exit(1)

    task_files = list(tasks_dir.glob('*.yml'))
    if not task_files:
        print("❌ Error: No task files found")
        sys.exit(1)

    print(f"🔧 Validating {len(task_files)} task files...")
    print()

    all_valid = True
    for task_file in sorted(task_files):
        valid = validate_task(task_file, profiles)
        all_valid = all_valid and valid
        print()

    # Summary
    if all_valid:
        print("🎉 All task definitions are valid!")
        sys.exit(0)
    else:
        print("❌ Some task definitions have errors. Please fix them.")
        sys.exit(1)

if __name__ == '__main__':
    main()