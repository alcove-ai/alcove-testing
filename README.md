# alcove-testing

Test repository for [Alcove](https://github.com/bmbouter/alcove) — a platform for running sandboxed AI coding agents in ephemeral containers.

This repo contains example YAML task definitions and security profiles used to validate Alcove's task repo sync, scheduling, security profile enforcement, and error handling features.

## Contents

### Task Definitions (`.alcove/tasks/`)

| File | Purpose |
|------|---------|
| `test-task.yml` | Basic task that clones this repo and reads a file — validates repo cloning and prompt execution |
| `another-task.yml` | Scheduled task (every 5 minutes) — validates cron scheduling and session tracking |
| `missing-profile-task.yml` | References a non-existent security profile — validates sync error warnings and dispatch blocking |
| `issue-greeter.yml` | Event-triggered task (GitHub `issues.opened` polling) — validates event-driven task dispatch and GitHub write access |
| `validate-repo.yml` | Repository integrity validation — validates all task definitions and security profiles for consistency |

### Security Profiles (`.alcove/security-profiles/`)

| File | Purpose |
|------|---------|
| `testing-readonly.yml` | Read-only GitHub access to this repo — validates YAML profile sync |
| `testing-writer.yml` | Read+write GitHub access to this repo — validates write-scoped profiles |

### Test Data

| File | Purpose |
|------|---------|
| `test-data/greeting.txt` | Simple text file read by the test task to verify repo cloning works |

### Validation Tools

| File | Purpose |
|------|---------|
| `scripts/validate-tasks.py` | Python script to validate task definitions, workflow definitions, and security profile references |

## Usage

Add this repo as a task repo in the Alcove dashboard:

1. Click your username in the top right, then **Task Repos**
2. Add `https://github.com/bmbouter/alcove-testing.git`
3. Click **Sync Now** on the Schedules page

The task definitions and security profiles will appear in the dashboard.
