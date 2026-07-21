from ultralytics import YOLO
from pathlib import Path

# paths
ROOT = Path(__file__).parent.parent
#MODEL_DIR = ROOT / "models"
#MODEL_DIR.mkdir(exist_ok=True) 

# model
model = YOLO(str("C:/Users/weslley/Desktop/work/computer_vision_ufsc/models/firesmoke_4_2_yolo26n-seg/weights/best.pt"))

# output
results = model.predict(
    str(ROOT / "C:/Users/weslley/Desktop/work/computer_vision_ufsc/data/datasets/notredame"),
    save=True,
    stream=True,
    project=str(ROOT / "data/"),
    name="",
    # conf=0.70 # confidence threshold
)

for r in results:
    pass