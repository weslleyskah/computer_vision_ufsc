# VISIA

Repository to study object detection at the UFSC VISIA Lab.

## Fire Detection

### Detections

![Wildfire Detection Model](data/output/fire_dataset/wildfire_59.gif)

![Wildfire Detection Model](data/output/fire_dataset/wildfire_63.gif)

![Wildfire Detection Model](data/output/fire_dataset/wildfire_17.gif)

### Datasets

- Wildfire Images: [dataset I](https://universe.roboflow.com/roboflow-universe-projects/fire-and-smoke-segmentation), [dataset II](https://universe.roboflow.com/uzai-kha-s-workspace/forest_fire-aggsg)

- Wildfire Videos: [dataset I](https://www.kaggle.com/datasets/weslleyskah/wildfire-dataset)

## Notes

| Dependencies |  |
| --- | --- |
| [uv](https://github.com/astral-sh/uv) | Python package manager |
| [opencv](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html) | Image manipulation |
| ultralytics | Detection with YOLO |

| Datasets |  |
| --- | --- |
| Sites | [roboflow](https://roboflow.com/), [open images v7](https://storage.googleapis.com/openimages/web/index.html), [aws open data](https://registry.opendata.aws/), [huggingface](https://huggingface.co/datasets), kaggle, flickr |
| Annotations | [CVAT](https://app.cvat.ai) |

## Setup

```bash
uv venv
uv pip install ultralytics
uv run src/main.py
```