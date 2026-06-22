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

        # ─────────────────────────────────────────────────────────────────
        # Benchmark configs (docker-compose.alt{1,2,3,4}.yml)
        # ─────────────────────────────────────────────────────────────────

        # ── Config 1 — Community NVFP4 (W4A4), no speculative decoding ──────
        # 26B requires gemma4_patched.py + VLLM_NVFP4_GEMM_BACKEND=marlin.
        "bg-digitalservices/Gemma-4-26B-A4B-it-NVFP4",
        # E2B W4A4 — no patch needed (vanilla handles it).
        "bg-digitalservices/Gemma-4-E2B-it-NVFP4",

        # ── Config 2 — MTP speculative decoding ────────────────────────────
        "nvidia/Gemma-4-26B-A4B-NVFP4",
        "google/gemma-4-26B-A4B-it-assistant",
        "google/gemma-4-E2B-it-qat-w4a16-ct", 
        "google/gemma-4-E2B-it-qat-q4_0-unquantized-assistant",

        # ── Config 3 — DFlash (26B) + ParoQuant (E2B) ──────────────────────
        # DFlash target = google/gemma-4-26B-A4B-it (bf16 repo). FP8 is applied
        # ONLINE at load via --quantization fp8, so we download the bf16 weights.
        "google/gemma-4-26B-A4B-it",
        # DFlash drafter (~0.4B block-diffusion model, shares target embeddings).
        "z-lab/gemma-4-26B-A4B-it-DFlash",
        # ParoQuant INT4 E2B (VLM checkpoint; served --language-model-only).
        "z-lab/gemma-4-E2B-it-PARO",

        # ── Config 4 — DiffusionGemma (26B) + QAT compressed-tensors E2B ───
        # DiffusionGemma NVFP4 (block-diffusion, served via vllm/vllm-openai:gemma).
        "nvidia/diffusiongemma-26B-A4B-it-NVFP4",
        # E2B QAT = google/gemma-4-E2B-it-qat-w4a16-ct (already listed above).
    ]

    for model in models:
        print(f"Downloading {model}...")
        snapshot_download(repo_id=model, token=token)
        print(f"  ✓ Done")