from ultralytics import YOLO
from pathlib import Path

# paths
ROOT = Path(__file__).parent.parent
MODEL_DIR = ROOT / "model"
MODEL_DIR.mkdir(exist_ok=True) 

# model
model = YOLO(str(MODEL_DIR / "fireseg_v3.pt"))

# output
results = model.predict(
    str(ROOT / "data/input/fire_dataset/wildfire_dataset_videos/wildfire_video_76.mp4"),
    save=True,
    stream=True,
    project=str(ROOT / "data/output/fire_dataset/"),
    name="",
    conf=0.70 # confidence threshold
)

for r in results:
    pass