from detect import detect

alerts = {}
buttons = {}


def sortClasses():
    results = detect()
    alerts.clear()
    buttons.clear()
    boxes = results[0].boxes.cpu().numpy()
    for index, box in enumerate(boxes):
        coord = box.xyxy[0].astype(int)
        name = results[0].names[int(box.cls[0])]
        if name == 'sys_alert' or name == 'site_alert':
            alerts[name + str(index)] = coord
        elif name == 'button':
            buttons[name + str(index)] = coord
