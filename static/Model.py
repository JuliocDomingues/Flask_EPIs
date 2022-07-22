import torch
from yolov5.models.common import DetectMultiBackend


def load_model(weights='yolov5n.pt', device=torch.device('cpu'), dnn=False, data=None, fp16=False):

    if data is None:
        from pathlib import Path
        import yolov5
        ROOT = Path(yolov5.__file__).parents[0]
        data = ROOT / 'data/coco128.yaml'

    return DetectMultiBackend(weights=weights, device=device, dnn=dnn, data=data, fp16=fp16)
