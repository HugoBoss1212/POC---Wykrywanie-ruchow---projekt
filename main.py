import camera

mirror = True
cam_obj = camera.Camera(10, mirror, 10)


def main_():
    while cam_obj.exit():
        cam_obj.update()


if __name__ == '__main__':
    main_()
