FROM vllm/vllm-openai:gemma4-cu130

# Basic utilities (curl for healthcheck)
RUN apt-get update && apt-get install -y --no-install-recommends curl \
    && rm -rf /var/lib/apt/lists/*

# Install Infinity (server/CLI)
RUN python -m pip install --upgrade pip \
    && pip install --no-cache-dir "infinity-emb[all]"

EXPOSE 7997

ENTRYPOINT ["infinity_emb"]