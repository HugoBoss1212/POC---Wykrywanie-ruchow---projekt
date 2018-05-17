import camera


def main(mirror=False):
    cam_obj = camera.Camera(mirror, 'Camera')

    while cam_obj.exit():
        cam_obj.update(show=True, fps=False, avg_fps=True)


main()
