from huggingface_hub import snapshot_download
import os

if __name__ == "__main__":
    token = os.environ["HF_TOKEN"]
    os.environ.setdefault("HF_HOME", os.path.abspath("./models"))

    models = [
        # Gemma 4 models (served via vllm/vllm-openai:gemma4-cu130)
        "bg-digitalservices/Gemma-4-26B-A4B-it-NVFP4A16",
        "google/gemma-4-E2B-it",
        # Embedding models (served via nvcr.io/nvidia/vllm:26.02-py3)
        "intfloat/multilingual-e5-large",
        "jinaai/jina-embeddings-v5-text-small-retrieval",

        # ── Experimental models (for docker-compose.experimental.yml) ──────
        # QAT E2B (w4a16 compressed-tensors, vLLM-native)
        "google/gemma-4-E2B-it-qat-w4a16-ct",
        # QAT E2B MTP assistant (unquantized, gemma4_assistant arch)
        "google/gemma-4-E2B-it-qat-q4_0-unquantized-assistant",
        # QAT 26B A4B MoE (w4a16 compressed-tensors, vLLM-native)
        "google/gemma-4-26B-A4B-it-qat-w4a16-ct",
        # QAT 26B A4B MoE MTP assistant (unquantized, gemma4_assistant arch)
        "google/gemma-4-26B-A4B-it-qat-q4_0-unquantized-assistant",

        # ── DiffusionGemma (commented out — kept for future experimentation)
        # "nvidia/diffusiongemma-26B-A4B-it-NVFP4",
    ]

    for model in models:
        print(f"Downloading {model}...")
        snapshot_download(repo_id=model, token=token)
        print(f"  ✓ Done")