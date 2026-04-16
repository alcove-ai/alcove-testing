#!/bin/bash

# Test script to validate alcove-testing repository structure
# This ensures all required files and configurations are present

set -e

echo "🧪 Running alcove-testing structure validation..."

# Test 1: Check required directories exist
echo "✓ Checking required directories..."
required_dirs=(".alcove" ".alcove/tasks" ".alcove/security-profiles" ".alcove/workflows" "test-data")
for dir in "${required_dirs[@]}"; do
    if [[ -d "$dir" ]]; then
        echo "  ✓ $dir exists"
    else
        echo "  ❌ $dir missing"
        exit 1
    fi
done

# Test 2: Check required files exist
echo "✓ Checking required files..."
required_files=("README.md" "test-data/greeting.txt" ".alcove/workflows/sdlc-pipeline.yml")
for file in "${required_files[@]}"; do
    if [[ -f "$file" ]]; then
        echo "  ✓ $file exists"
    else
        echo "  ❌ $file missing"
        exit 1
    fi
done

# Test 3: Check YAML files syntax
echo "✓ Checking YAML files syntax..."
yaml_files=($(find .alcove -name "*.yml" -type f))
for file in "${yaml_files[@]}"; do
    # Basic YAML syntax check - look for common issues
    if [[ -f "$file" ]] && [[ -s "$file" ]]; then
        # Check for basic YAML structure (colon after key, proper indentation start)
        if grep -q ": " "$file" || grep -q "^[a-zA-Z]" "$file"; then
            echo "  ✓ $file appears to be valid YAML"
        else
            echo "  ❌ $file may have YAML syntax issues"
            exit 1
        fi
    else
        echo "  ❌ $file is empty or unreadable"
        exit 1
    fi
done

# Test 4: Check task definitions have required fields
echo "✓ Validating task definitions..."
for task_file in .alcove/tasks/*.yml; do
    if [[ -f "$task_file" ]]; then
        if grep -q "^name:" "$task_file" && grep -q "^description:" "$task_file"; then
            echo "  ✓ $(basename "$task_file") has required fields"
        else
            echo "  ❌ $(basename "$task_file") missing required fields (name/description)"
            exit 1
        fi
    fi
done

# Test 5: Check security profiles have required fields
echo "✓ Validating security profiles..."
for profile_file in .alcove/security-profiles/*.yml; do
    if [[ -f "$profile_file" ]]; then
        if grep -q "tools:" "$profile_file" && grep -q "github:" "$profile_file"; then
            echo "  ✓ $(basename "$profile_file") has github configuration"
        else
            echo "  ❌ $(basename "$profile_file") missing github configuration"
            exit 1
        fi
    fi
done

# Test 6: Check test data is readable
echo "✓ Validating test data..."
if [[ -r "test-data/greeting.txt" ]] && [[ -s "test-data/greeting.txt" ]]; then
    echo "  ✓ test-data/greeting.txt is readable and non-empty"
else
    echo "  ❌ test-data/greeting.txt is not readable or empty"
    exit 1
fi

echo "🎉 All structure validation tests passed!"
