FROM vllm/vllm-openai:gemma4-cu130

# Basic utilities (curl for healthcheck)
RUN apt-get update && apt-get install -y --no-install-recommends curl \
    && rm -rf /var/lib/apt/lists/*

# Install Infinity (server/CLI)
RUN uv pip install --system --no-cache-dir "infinity-emb[all]"

EXPOSE 7997

ENTRYPOINT ["infinity_emb"]