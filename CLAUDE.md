# alcove-testing

Test fixtures and agent definitions for the Alcove platform.

## Repository Structure

- `.alcove/tasks/` — agent definitions (YAML)
- `.alcove/workflows/` — workflow pipelines (YAML)
- `.alcove/security-profiles/` — security profiles
- `test-data/` — test projects and fixtures
- `scripts/` — test scripts

## Dev Container

This project uses a dev container for building and testing code. Do NOT run
build or test commands directly — always use the dev container, which has the
correct toolchain and dependencies.

### Checking availability

The dev container is available when the `DEV_CONTAINER_HOST` and `DEV_TOKEN`
environment variables are set.

### Health check

```bash
curl -s http://$DEV_CONTAINER_HOST/healthz
```

Returns `{"status":"ok"}` when ready.

### Running commands

All build and test commands must be run via the dev container exec endpoint:

```bash
curl -s -X POST http://$DEV_CONTAINER_HOST/exec \
  -H "Authorization: Bearer $DEV_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"cmd": "your-command-here", "timeout": 30}'
```

The response is NDJSON. Each line is JSON with a `stream` field (`stdout`,
`stderr`, or `exit`). The `exit` line has the exit `code`.

### Workflow

1. Edit code in your working directory (it's on the shared volume)
2. Run build/test commands via the dev container exec endpoint
3. Read the NDJSON output to check results
4. Fix issues and repeat until tests pass

## Go Test Project

`test-data/go-project/` contains a Go project. Run its tests with:

```bash
curl -s -X POST http://$DEV_CONTAINER_HOST/exec \
  -H "Authorization: Bearer $DEV_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"cmd": "cd /workspace/test-data/go-project && go test -v ./...", "timeout": 30}'
```
