from pathlib import Path

BASE_DIR = Path(__file__).parent

MODEL_PATH = BASE_DIR / "artifacts" / "best_model_lightgbm.pkl"
SCALER_PATH = BASE_DIR / "artifacts" / "scaler.pkl"
TARGET_ENCODER_PATH = BASE_DIR / "artifacts" / "target_encoder.pkl"
ENCODER_PATH = BASE_DIR / "artifacts" / "feature_label_encoders.pkl"
COLUMNS_PATH = BASE_DIR / "artifacts" / "model_columns.pkl"
