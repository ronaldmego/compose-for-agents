# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is the **Compose for Agents Demos** repository, containing multiple self-contained demo projects that showcase different agent frameworks running with Docker Compose. Each demo features AI agents, MCP (Model Context Protocol) integrations, and can run models either locally (using Docker Model Runner) or via cloud services.

## Development Commands

### Global Commands

```bash
# Lint Markdown files across the repository
task lint:markdown

# Lint and fix Markdown files
task lint:markdown:fix

# Run all linters
task lint
```

### Python Projects (a2a, adk, adk-cerebras, adk-sock-shop, agno/agent, crew-ai, langgraph)

```bash
# Type checking
pyright

# Code formatting and linting
ruff check
ruff format

# Run project (varies by project)
docker compose up --build

# Use OpenAI models instead of local models
docker compose -f compose.yaml -f compose.openai.yaml up
```

### Node.js/Next.js Projects (agno/agent-ui)

```bash
# Development server
pnpm dev

# Build for production
pnpm build

# Type checking
pnpm typecheck

# Linting
pnpm lint
pnpm lint:fix

# Code formatting
pnpm format
pnpm format:fix

# Run all validation checks
pnpm validate
```

### Java/Spring Projects (spring-ai)

```bash
# Build with Maven
./mvnw clean install

# Run application
./mvnw spring-boot:run

# Build Docker image
docker compose up --build
```

### Go Projects (langchaingo)

```bash
# Build and run
go run .

# Or use Docker
docker compose up --build
```

## Architecture Overview

### Project Structure

The repository contains multiple independent agent demos, each in its own directory:

- **a2a**: Agent-to-Agent multi-agent fact-checking system
- **adk**: Google's Agent Development Kit demos (fact-checking)
- **adk-cerebras**: ADK with Cerebras AI integration for Golang expertise
- **adk-sock-shop**: ADK-based e-commerce agent system
- **agno**: GitHub issue summarization agent with web UI
- **crew-ai**: Marketing strategy generation using CrewAI framework
- **langgraph**: SQL query agent using LangGraph
- **langchaingo**: Go-based DuckDuckGo search agent
- **spring-ai**: Java/Spring-based search agent
- **vercel**: Reference to external Vercel AI SDK chat UI

### Common Patterns

#### 1. Docker Compose Configuration

Each project uses Docker Compose with:
- Base `compose.yaml` for local model running
- Optional `compose.openai.yaml` for OpenAI models
- Optional `compose.offload.yaml` for Docker Offload
- Project-specific variations (e.g., `compose.gcloud.yaml`, `compose.gemini.yaml`)

#### 2. MCP (Model Context Protocol) Integration

MCP servers are configured as Docker services with standardized patterns:
```yaml
mcp-gateway:
  image: docker/mcp-gateway:latest
  command:
    - --transport=sse
    - --servers=server1,server2,server3
    - --config=/mcp_config
    - --secrets=docker-desktop:/run/secrets/mcp_secret
```

Secrets are stored in `.mcp.env` files (created from `.mcp.env.example` templates).

#### 3. Model Configuration

Models are defined in compose files using the standardized format:
```yaml
models:
  <model_name>:
    model: <model_image_ref>
```

Services that need models reference them:
```yaml
services:
  my-service:
    models:
      <model_name>:
        endpoint_var: MODEL_RUNNER_URL
        model_var: MODEL_RUNNER_MODEL
```

### Agent Framework Patterns

#### ADK (Agent Development Kit) Projects

- Use `SequentialAgent` for orchestration
- Sub-agents in `agents/sub_agents/` directories
- Implement `BaseAgent` interface
- Use LiteLLM for model abstraction

#### A2A (Agent-to-Agent) Projects

- Use specialized `AgentKit` framework
- Agents defined in YAML configuration files
- Support for proxy agents and agent IDs
- MCP tools integration via `create_mcp_toolsets()`

#### CrewAI Projects

- Agents and tasks defined in YAML configuration
- Use Poetry for dependency management
- Support for training and running modes

## Key Implementation Notes

### Python Projects

- Most use Python 3.13+ with `uv` or `poetry` for dependency management
- Common dependencies: `litellm`, `pyright`, `ruff`, `pydantic`
- FastAPI/Uvicorn for web servers when needed
- Environment variables loaded from `.env` files

### Docker Integration

- All projects containerized with multi-stage builds
- Support for both AMD64 and ARM64 architectures
- Use of Docker secrets for sensitive data (API keys, tokens)
- Health checks and restart policies configured

### MCP Servers

Common MCP servers used across projects:
- `duckduckgo`: Web search capabilities
- `brave`: Advanced web search
- `github-official`: GitHub API access
- `postgres`: Database operations
- `mongodb`: NoSQL database access
- `wikipedia-mcp`: Wikipedia content access

## Running Demos

Standard workflow for any demo:
1. Navigate to the demo directory
2. Create `.mcp.env` from `.mcp.env.example` (if exists)
3. Add any required API keys to `secret.*` files
4. Run `docker compose up --build`
5. Access the application (usually on localhost:8080 or localhost:3000)

For development with hot-reload, many Python projects support running outside Docker with proper environment setup.