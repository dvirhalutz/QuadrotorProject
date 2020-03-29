from cutImagesClass import cutImages
from cutImagesClass import createImagesFromVideo
import os
import random


def startingDialog():
    print('Welcome to the Video/Images cutter...')
    print('Do you want to start with a Video or just cut immages: (write the number)')
    print('1. For Video cutter')
    print('2. For Images cutter')
    print('3. For Video cutter following by Images cutter')
    print('4. Arranging images in folders')
    choice = input()
    if choice != '1' and choice != '2'and choice != '3' and choice != '4':
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
    is_without_man = input('Is it without man? (y/n)')
    if is_without_man == 'y':
        isWithoutMan = True
    else:
        isWithoutMan = False
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
                             verbos=1,
                             isWithoutMan=isWithoutMan)
    imagesCutter.start_cutting()


def VideoImageDialog():
    print('Video and Image Cutter App!')
    path_to_video = input(
        "what's the video full (not relative) directory path name (english path only)?")

    files = []
    for r, _, f in os.walk(path_to_video):
        print(r)
        for file in f:
            if file.endswith('.mp4'):
                files.append(os.path.join(r, file))

    print(files)

    path_folder_images_to_save_video = input(
        "what's the full (not relative) folder path (english path only) you want to save the images out of the video?")
    path_folder_images_to_save_cutted_images = input(
        "what's the full (not relative) folder path (english path only) you want to save the cutted images?")
    image_starting_with = input("what's the starting images name?")
    is_without_man = input('Is it without man? (y/n)')
    if is_without_man == 'y':
        isWithoutMan = True
    else:
        isWithoutMan = False

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
                                 verbos=1,
                                 isWithoutMan=isWithoutMan)
        imagesCutter.start_cutting()

# Creating dataset folder in that order:
    # data_set
    # ----> train
    #       |----> withHat
    #       |----> withOutHat
    #       |----> withOutMan
    # ----> val
    #       |----> withHat
    #       |----> withOutHat
    #       |----> withOutMan
    # ----> test
    #       |----> withHat
    #       |----> withOutHat
    #       |----> withOutMan


def createFolderHierarchy(path_to_save_photo):
    os.mkdir(path_to_save_photo + '/data_set')
    os.mkdir(path_to_save_photo + '/data_set/train')
    os.mkdir(path_to_save_photo + '/data_set/train/withHat')
    os.mkdir(path_to_save_photo + '/data_set/train/withOutHat')
    os.mkdir(path_to_save_photo + '/data_set/train/withOutMan')

    os.mkdir(path_to_save_photo + '/data_set/val')
    os.mkdir(path_to_save_photo + '/data_set/val/withHat')
    os.mkdir(path_to_save_photo + '/data_set/val/withOutHat')
    os.mkdir(path_to_save_photo + '/data_set/val/withOutMan')

    os.mkdir(path_to_save_photo + '/data_set/test')
    os.mkdir(path_to_save_photo + '/data_set/test/withHat')
    os.mkdir(path_to_save_photo + '/data_set/test/withOutHat')
    os.mkdir(path_to_save_photo + '/data_set/test/withOutMan')


def ArrangeAllFoldersAndPhotos(train_ratio, val_ratio, test_ratio):
    """ train_ratio = 60%, val_ratio = 25% test_ratio = 15% """
    print('Arranging Photos App!')
    path_to_with_out_man_folder = input(
        "what's the withOutMan directory full (not relative) path name (english path only)?")
    path_to_with_out_hat_folder = input(
        "what's the withOutHat directory full (not relative) path name (english path only)?")
    path_to_with_hat_folder = input(
        "what's the withHat directory full (not relative) path name (english path only)?")
    path_to_save_photo = input(
        "Where do you want to save the photos as a dataset folder - provide directory full (not relative) path name (english path only)")

    files_with_hat_folder = []
    files_without_hat_folder = []
    files_without_man_folder = []
    for r, _, f in os.walk(path_to_with_hat_folder):
        for file in f:
            if file.endswith(".png"):
                files_with_hat_folder.append(os.path.join(r, file))
    random.shuffle(files_with_hat_folder)

    for r, _, f in os.walk(path_to_with_out_hat_folder):
        for file in f:
            if file.endswith(".png"):
                files_without_hat_folder.append(os.path.join(r, file))
    random.shuffle(files_without_hat_folder)

    for r, _, f in os.walk(path_to_with_out_man_folder):
        for file in f:
            if file.endswith(".png"):
                files_without_man_folder.append(os.path.join(r, file))
    random.shuffle(files_without_man_folder)

    with_hat_number = len(files_with_hat_folder)
    with_out_hat_number = len(files_without_hat_folder)
    with_out_man_number = len(files_without_man_folder)

    print("with hat - ", with_hat_number)
    print("with out hat - ", with_out_hat_number)
    print("with out man - ", with_out_man_number)

    # Creating dataset folder in that order:
    # data_set
    # ----> train
    #       |----> withHat
    #       |----> withOutHat
    #       |----> withOutMan
    # ----> val
    #       |----> withHat
    #       |----> withOutHat
    #       |----> withOutMan
    createFolderHierarchy(path_to_save_photo)
    # with hat
    with_hat_train = files_with_hat_folder[0:int(with_hat_number*train_ratio)]
    next_number = int(with_hat_number*train_ratio)
    with_hat_val = files_with_hat_folder[(
        next_number+1):next_number+int(with_hat_number*val_ratio)]
    next_number = next_number+int(with_hat_number*val_ratio)
    with_hat_test = files_with_hat_folder[next_number:]
    # without hat
    without_hat_train = files_without_hat_folder[0:int(
        with_out_hat_number*train_ratio)]
    next_number = int(with_out_hat_number*train_ratio)
    without_hat_val = files_without_hat_folder[(
        next_number+1):next_number+int(with_out_hat_number*val_ratio)]
    next_number = next_number+int(with_out_hat_number*val_ratio)
    without_hat_test = files_without_hat_folder[next_number:]
    # without man
    without_man_train = files_without_man_folder[0:int(
        with_out_man_number*train_ratio)]
    next_number = int(with_out_man_number*train_ratio)
    without_man_val = files_without_man_folder[(
        next_number+1):next_number+int(with_out_man_number*val_ratio)]
    next_number = next_number+int(with_out_man_number*val_ratio)
    without_man_test = files_without_man_folder[next_number:]

    print(without_man_train)

    [os.rename(f, path_to_save_photo+'/data_set/train/withHat/'+str(index)+'.png')
     for index, f in enumerate(with_hat_train)]
    [os.rename(f, path_to_save_photo+'/data_set/val/withHat/'+str(index)+'.png')
     for index, f in enumerate(with_hat_val)]
    [os.rename(f, path_to_save_photo+'/data_set/test/withHat/'+str(index)+'.png')
     for index, f in enumerate(with_hat_test)]

    [os.rename(f, path_to_save_photo+'/data_set/train/withOutHat/'+str(index)+'.png')
     for index, f in enumerate(without_hat_train)]
    [os.rename(f, path_to_save_photo+'/data_set/val/withOutHat/'+str(index)+'.png')
     for index, f in enumerate(without_hat_val)]
    [os.rename(f, path_to_save_photo+'/data_set/test/withOutHat/'+str(index)+'.png')
     for index, f in enumerate(without_hat_test)]

    [os.rename(f, path_to_save_photo+'/data_set/train/withOutMan/'+str(index)+'.png')
     for index, f in enumerate(without_man_train)]
    [os.rename(f, path_to_save_photo+'/data_set/val/withOutMan/'+str(index)+'.png')
     for index, f in enumerate(without_man_val)]
    [os.rename(f, path_to_save_photo+'/data_set/test/withOutMan/'+str(index)+'.png')
     for index, f in enumerate(without_man_test)]


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
    elif userChoice == '4':
        ArrangeAllFoldersAndPhotos(0.6, 0.25, 0.15)
        exit(0)
