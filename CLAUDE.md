# alcove-testing

Test fixtures and agent definitions for the Alcove platform.

## Repository Structure

- `.alcove/tasks/` — agent definitions (YAML)
- `.alcove/workflows/` — workflow pipelines (YAML)
- `.alcove/security-profiles/` — security profiles
- `test-data/` — test projects and fixtures
- `scripts/` — test scripts

## Dev Container

When a dev container is available, use it to build and test code. The dev
container shares a `/workspace` volume with your working directory — files
you edit are immediately visible inside the dev container.

### Checking if a dev container is available

If the `DEV_CONTAINER_HOST` and `DEV_TOKEN` environment variables are set,
a dev container is running.

### Health check

```bash
curl -s http://$DEV_CONTAINER_HOST/healthz
```

Returns `{"status":"ok"}` when ready.

### Running commands in the dev container

```bash
curl -s -X POST http://$DEV_CONTAINER_HOST/exec \
  -H "Authorization: Bearer $DEV_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"cmd": "your-command-here", "timeout": 30}'
```

The response is NDJSON with `stdout`, `stderr`, and `exit` stream types.
Check the `exit` line for the exit code.

### Workflow

1. Edit code in your working directory (it's on the shared volume)
2. Run build/test commands via the dev container exec endpoint
3. Read the output, fix issues, repeat
4. Push when tests pass

## Go Test Project

The `test-data/go-project/` directory contains a small Go project for testing.

To run tests:

```bash
curl -s -X POST http://$DEV_CONTAINER_HOST/exec \
  -H "Authorization: Bearer $DEV_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"cmd": "cd /workspace/test-data/go-project && go test -v ./...", "timeout": 30}'
```
