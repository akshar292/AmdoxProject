import subprocess
import sys


def run(cmd):
    print(f"\n▶️ Running: {cmd}\n")

    result = subprocess.run(cmd, shell=True)

    if result.returncode != 0:
        print(f"❌ ERROR while running: {cmd}")
        sys.exit(1)   # stop pipeline if something fails


def main():
    print("\n🚀 NEURAL RETAIL FULL PIPELINE STARTED")

    # -----------------------------
    # 🔹 STEP 1: DATA PIPELINE
    # -----------------------------
    run("python backend/pipeline.py")
    run("python backend/feature_store_pipeline.py")

    # -----------------------------
    # 🔹 STEP 2: CORE MODEL
    # -----------------------------
    run("python backend/train_pipeline.py")  # demand model

    # -----------------------------
    # 🔹 STEP 3: ADVANCED MODELS
    # -----------------------------
    run("python -m backend.models.train_lstm")
    run("python -m backend.models.prophet_model")

    # -----------------------------
    # 🔹 STEP 4: BUSINESS MODELS
    # -----------------------------
    run("python -m backend.churn.pipeline")
    run("python -m backend.segmentation.pipeline")
    run("python -m backend.pricing.pipeline")

    print("\n✅ ALL PIPELINES COMPLETED SUCCESSFULLY")


if __name__ == "__main__":
    main()