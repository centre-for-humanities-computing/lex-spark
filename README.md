# lex-spark
Configuration for using the Spark DGX as an inference server for Lex

## Running the stack
### 1. Verify NVIDIA Container Toolkit is set up
nvidia-smi
docker run --rm --gpus all nvidia/cuda:12.0-base nvidia-smi

### 2. (Optional) Pull images and models ahead of time
uv run download_models.py
docker compose pull

### 3. Launch everything
docker compose up -d

### 4. Watch logs (all services)
docker compose logs -f

### 5. Watch a specific service
docker compose logs -f vllm-gemma-large

### 6. Check health status
docker compose ps

## Useful management commands
### Restart a single service without taking down others
docker compose restart vllm-gemma-large

### Scale down (e.g., free memory during testing)
docker compose stop vllm-gemma-large

### View resource usage
docker stats

### Update a single image and restart
docker compose pull vllm-gemma-large && docker compose up -d vllm-gemma-large

### Full teardown (keeps model cache)
docker compose down

# Nuclear option (removes volumes too — loses model cache)
docker compose down -v