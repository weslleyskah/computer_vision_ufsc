from ultralytics import YOLO
from pathlib import Path

# paths
ROOT = Path(__file__).parent.parent
MODEL_DIR = ROOT / "model"
MODEL_DIR.mkdir(exist_ok=True) 

# model
model = YOLO(str(MODEL_DIR / "best.pt"))

# output
results = model.predict(
    str(ROOT / "data/input/fire_dataset/wildfire_dataset_videos/"),
    save=True,
    stream=True,
    project=str(ROOT / "data/output/fire_dataset/wildfire_dataset/"),
    name=""
)

for r in results:
    pass