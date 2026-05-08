FROM vllm/vllm-openai:gemma4-cu130

# Install curl for healthcheck
RUN apt-get update && apt-get install -y --no-install-recommends curl \
    && rm -rf /var/lib/apt/lists/*

# Pin optimum to a version that still ships bettertransformer,
# then install infinity on top
RUN uv pip install --system --no-cache-dir \
    "optimum[bettertransformer]<1.23.0" \
    "infinity-emb[all]"

EXPOSE 7997

ENTRYPOINT ["infinity_emb"]