from cutImagesClass import cutImages
from cutImagesClass import createImagesFromVideo
import os


def startingDialog():
    print('Welcome to the Video/Images cutter...')
    print('Do you want to start with a Video or just cut immages: (write the number)')
    print('1. For Video cutter')
    print('2. For Images cutter')
    print('3. For Video cutter following by Images cutter')
    choice = input()
    if choice != '1' and choice != '2'and choice != '3':
        print('You typed wrong number... goodbye')
        exit(0)
    return choice


def videoCutterDialog():
    print('Video Cutter App!')
    path_to_video = input(
        "what's the video full (not relative) folde path name (english path only)?")
    path_folder_images_to_save = input(
        "what's the full (not relative) folder path (english path only) you want to save the images to?")
    image_starting_with = input("what's the starting images name?")
    save_every_frame = input(
        "what's the frame rate you want saving picture (number)? - press ENTER for the default 10")
    if save_every_frame == '':
        save_every_frame = 10
    else:
        save_every_frame = int(save_every_frame)
    videoCutter = createImagesFromVideo(path_to_video,
                                        path_folder_images_to_save,
                                        image_starting_with,
                                        save_every_frame,
                                        verbos=1)
    videoCutter.start_cutting_video()


def imagesCutterDialog():
    print('Image Cutter App!')
    path_folder_images_to_upload = input(
        "what's the images full (not relative) folder path name (english path only)?")
    path_folder_images_to_save = input(
        "what's the full (not relative) folder path (english path only) you want to save the images to?")
    image_starting_with = input("what's the starting images name?")
    final_image_size = input(
        "what's the images final dimention (number)? - press ENTER for the default 252")
    print(final_image_size)
    if final_image_size == '':
        final_image_size = 252
    else:
        final_image_size = int(final_image_size)
    imagesCutter = cutImages(path_folder_images_to_upload,
                             path_folder_images_to_save,
                             image_starting_with,
                             final_image_size,
                             verbos=1)
    imagesCutter.start_cutting()


def VideoImageDialog():
    print('Video and Image Cutter App!')
    path_to_video = input(
        "what's the video full (not relative) path name (english path only)?")
    path_folder_images_to_save_video = input(
        "what's the full (not relative) folder path (english path only) you want to save the images out of the video?")
    path_folder_images_to_save_cutted_images = input(
        "what's the full (not relative) folder path (english path only) you want to save the cutted images?")
    image_starting_with = input("what's the starting images name?")
    save_every_frame = input(
        "what's the frame rate you want saving picture (number)? - press ENTER for the default 10")
    if save_every_frame == '':
        save_every_frame = 10
    else:
        save_every_frame = int(save_every_frame)
    final_image_size = input(
        "what's the images final dimention (number)? - press ENTER for the default 252")
    if final_image_size == '':
        final_image_size = 252
    else:
        final_image_size = int(final_image_size)

    files = []
    for r, _, f in os.walk(path_to_video):
        for file in f:
            files.append(os.path.join(r, file))

    print(files)
    for videoFile in files:
        videoCutter = createImagesFromVideo(videoFile,
                                            path_folder_images_to_save_video,
                                            image_starting_with,
                                            save_every_frame,
                                            verbos=1)
        videoCutter.start_cutting_video()
        imagesCutter = cutImages(path_folder_images_to_save_video,
                                 path_folder_images_to_save_cutted_images,
                                 image_starting_with,
                                 final_image_size,
                                 verbos=1)
        imagesCutter.start_cutting()


if __name__ == "__main__":
    userChoice = startingDialog()
    if userChoice == '1':
        videoCutterDialog()
        exit(0)
    elif userChoice == '2':
        imagesCutterDialog()
        exit(0)
    elif userChoice == '3':
        VideoImageDialog()
        exit(0)
