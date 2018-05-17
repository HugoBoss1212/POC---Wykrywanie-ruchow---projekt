import camera
import post_video
import _thread

mirror = True
show = True
cam_obj = camera.Camera(mirror, 'Camera', 3)


def live_feed(show_, null02):
    while cam_obj.exit():
        cam_obj.update(show_, False, False)


def processing(show_, null02):
    post_cam_obj = post_video.PostVideo(mirror, 'Camera')

    while cam_obj.exit():
        post_cam_obj.update(cam_obj.pass_frame(), show_)


_thread.start_new_thread(live_feed, (show, 0))
_thread.start_new_thread(processing, (show, 0))
