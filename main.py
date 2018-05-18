import camera
import post_video
import threading
import matplotlib.pyplot as plt
import matplotlib.animation as animation

mirror = True
show = True
cam_obj = camera.Camera(mirror, 'Camera', 1)
post_cam_obj = post_video.PostVideo()


def processing(show_):
    while cam_obj.exit():
        if cam_obj.frame[0] is not None and cam_obj.frame[1] is not None:
            # fig = plt.figure()
            # ims = []
            # for i in range(300):
                post_cam_obj.update(cam_obj.frame)
            #     ims.append([plt.imshow(post_cam_obj.frame, animated=True)])
            #
            #     ani = animation.ArtistAnimation(fig, ims, interval=0, blit=True)
            # plt.show()


def main_():
    t = threading.Thread(target=processing, args=(show, ))
    t.start()

    while cam_obj.exit():
        cam_obj.update(show, False, False)


main_()
