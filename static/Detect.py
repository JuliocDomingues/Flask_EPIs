import yolov5


def detect(source,
           imgsz=(640, 640),
           conf_thres=0.58,
           save_txt=False,
           save_conf=False,
           nosave=True,
           name='Results_Flask',
           line_thickness=1,
           model=None,
           weights='yolov5n.pt'):

    if model is None:
        raise Exception("Model is None!")

    return yolov5.detect.run(source=source, imgsz=imgsz, conf_thres=conf_thres, save_txt=save_txt, save_conf=save_conf,
                             nosave=nosave, name=name, line_thickness=line_thickness, model=model, weights=weights)
