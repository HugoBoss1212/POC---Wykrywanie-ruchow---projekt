import camera
import post_video
import rect
import threading

mirror = True
show = False
cam_obj = camera.Camera(mirror, 'Camera', 2)
post_cam_obj = post_video.PostVideo()
rect_obj = rect.Rect()


def processing(show_):
    while cam_obj.exit():
        cam_obj.update(show, False, False)


def rect(show_):
    while cam_obj.exit():
        rect_obj.points(post_cam_obj.frame)


def main_():
    t1 = threading.Thread(target=processing, args=(show,))
    t2 = threading.Thread(target=rect, args=(show,))
    t1.start()
    t2.start()

    while cam_obj.exit():
        if cam_obj.frame[0] is not None and cam_obj.frame[1] is not None:
            post_cam_obj.update(cam_obj.frame)


if __name__ == '__main__':
    main_()
