from sortClasses import alerts, buttons, sortClasses


def form():
    response = {
        "notification_windows": []
    }
    window = {

    }
    sortClasses()
    for name, coord in alerts.items():
        window = {
            "type": name,
            "coordinate": {
                "top_left": {
                    "x": int(coord[0]),
                    "y": int(coord[1])
                },
                "bottom_right": {
                    "x": int(coord[2]),
                    "y": int(coord[3])
                }
            },
            "buttons": []
        }
        response["notification_windows"].append(window)

    for name, coord in buttons.items():
        button = {
            "name": name,
            "content": "",  # Замените эту строку на ваш текст кнопки
            "coordinate": {
                "top_left": {
                    "x": int(coord[0]),
                    "y": int(coord[1])
                },
                "bottom_right": {
                    "x": int(coord[2]),
                    "y": int(coord[3])
                }
            }
        }
        window["buttons"].append(button)
    return response
