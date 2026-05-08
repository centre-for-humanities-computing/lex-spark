from huggingface_hub import snapshot_download
import os

if __name__ == "__main__":
    token = os.environ["HF_TOKEN"]
    cache = "./models"

    models = [
        "bg-digitalservices/Gemma-4-26B-A4B-it-NVFP4A16",
        "google/gemma-4-E4B-it",
        "google/gemma-4-E2B-it",
        "intfloat/multilingual-e5-large",
        # TEI requires the task-specific merged variant of jina-v5-small,
        # NOT the base model. The base model uses LoRA adapters which TEI
        # does not support. Use the retrieval variant for RAG/search use cases.
        "jinaai/jina-embeddings-v5-text-small-retrieval",
    ]

    for model in models:
        print(f"Downloading {model}...")
        snapshot_download(repo_id=model, token=token, cache_dir=cache)
        print(f"  ✓ Done")