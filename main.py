import camera
import post_video
import threading

mirror = True
show = True
cam_obj = camera.Camera(mirror, 'Camera', 3)
post_cam_obj = post_video.PostVideo()


def processing(show_):
  while cam_obj.exit():
    if cam_obj.frame[0] is not None and cam_obj.frame[1] is not None:
      post_cam_obj.update(cam_obj.frame)


def main_():
  t = threading.Thread(target=processing, args=(show, ))
  t.start()

  while cam_obj.exit():
    cam_obj.update(show, False, False)


if __name__ == '__main__':
  main_()
