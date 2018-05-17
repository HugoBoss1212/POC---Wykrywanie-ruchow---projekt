import camera


def main(mirror=False):
    cam_obj = camera.Camera(mirror, 'Camera', 5)

    while cam_obj.exit():
        cam_obj.update(True, True, False)
        cam_obj.show_processing()


main()
