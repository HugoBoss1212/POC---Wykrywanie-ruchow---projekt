import camera

mirror = True
cam_obj = camera.Camera(500, mirror, 3)


def main_():
    while cam_obj.exit():
        cam_obj.update()


if __name__ == '__main__':
    main_()
