import camera


def main(mirror=False):
    cam_obj = camera.Camera(mirror, 'Camera', 3)

    while cam_obj.exit():
        cam_obj.update(True, False, False)


main()
