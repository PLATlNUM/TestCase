from ultralytics import YOLO


def detect():
    model = YOLO('runs/detect/train/weights/best.pt')
    source = 'uploads/uploaded_image.jpg'
    return model(source)
