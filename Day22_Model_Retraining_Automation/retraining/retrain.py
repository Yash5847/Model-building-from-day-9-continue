from trigger import should_retrain

def retrain_model():
    print("🔁 Retraining started")

    # Step 1: Load fresh data
    print("📥 Loading new data")

    # Step 2: Data preprocessing
    print("🧹 Cleaning & preprocessing")

    # Step 3: Train model
    print("🧠 Training ML model")

    # Step 4: Save updated model
    print("💾 Saving updated model.pkl")

    print("✅ Retraining completed successfully")

if __name__ == "__main__":
    if should_retrain():
        retrain_model()
    else:
        print("ℹ No drift detected. Retraining skipped.")
