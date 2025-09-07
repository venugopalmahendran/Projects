from ultralytics import YOLO

model=YOLO("yolov8n.pt")

for result in model.predict(source=0,show=True,stream=True):
    boxes=result.boxes
    for box in boxes:
        cls=int(box.cls[0])
        conf=float(box.conf[0])
        print(model.names[cls],conf)