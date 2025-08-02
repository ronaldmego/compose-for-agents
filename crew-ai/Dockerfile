FROM python:3.12-slim

RUN apt-get update && apt-get install -y build-essential && \
    rm -rf /var/lib/apt/lists/*
RUN pip install poetry
WORKDIR /app
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-interaction --no-root
COPY . .
RUN poetry install
COPY <<EOF /entrypoint.sh
#!/bin/sh

if [ "\${LLM_PROVIDER}" = "gemini" ]; then
    echo "Using Gemini with \${GEMINI_MODEL_NAME}"
    export GEMINI_API_KEY=$(cat /run/secrets/gemini-api-key)
elif [ "\${LLM_PROVIDER}" = "openai" ]; then
    echo "Using OpenAI with \${OPENAI_MODEL_NAME}"
    export OPENAI_API_KEY=$(cat /run/secrets/openai-api-key)
else
    echo "Using Docker Model Runner with \${MODEL_RUNNER_MODEL}"
    export OPENAI_BASE_URL=\${MODEL_RUNNER_URL}
    export OPENAI_MODEL_NAME=openai/\${MODEL_RUNNER_MODEL}
    export OPENAI_API_KEY=cannot_be_empty
fi

exec poetry run marketing_posts
EOF
RUN chmod +x /entrypoint.sh
CMD ["/entrypoint.sh"]
