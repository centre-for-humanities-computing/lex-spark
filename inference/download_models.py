from huggingface_hub import snapshot_download
import os

if __name__ == "__main__":
    token = os.environ["HF_TOKEN"]
    cache = "./models"

    models = [
        # Gemma 4 models (served via vllm/vllm-openai:gemma4-cu130)
        "bg-digitalservices/Gemma-4-26B-A4B-it-NVFP4A16",
        "google/gemma-4-E2B-it",
        # Embedding models (served via nvcr.io/nvidia/vllm:26.02-py3)
        "intfloat/multilingual-e5-large",
        "jinaai/jina-embeddings-v5-text-small-retrieval",

        # ── Experimental models (for docker-compose.experimental.yml) ──────
        # Quantized Gemma 4 E2B (replaces google/gemma-4-E2B-it)
        "bg-digitalservices/Gemma-4-E2B-it-NVFP4A16",
        # DiffusionGemma 26B (replaces bg-digitalservices/Gemma-4-26B-A4B-it-NVFP4A16)
        "nvidia/diffusiongemma-26B-A4B-it-NVFP4",
        # Gemma 4 E2B MTP assistant checkpoint (speculative decoding)
        "gg-hf-am/gemma-4-E2B-it-assistant",
    ]

    for model in models:
        print(f"Downloading {model}...")
        snapshot_download(repo_id=model, token=token, cache_dir=cache)
        print(f"  ✓ Done")