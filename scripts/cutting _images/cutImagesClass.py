import os
import uuid
import cv2


class cutImages():
    '''
        path_folder_images_to_upload, path_folder_images_to_save => Full not relative path!!!
        image_starting_with => for classification purposes man or not wearing a hat or not
        image_format = > not supported at the moment
        verbos => 0-> no explainings outputs, ->outputs explainings
    '''

    def __init__(self, path_folder_images_to_upload, path_folder_images_to_save, image_starting_with, final_image_size=252, image_format='PNG', verbos=0):
        self.path_folder_images_to_upload = path_folder_images_to_upload.strip()
        self.path_folder_images_to_save = path_folder_images_to_save.strip()
        self.image_starting_with = image_starting_with.strip()
        self.final_image_size = final_image_size
        self.image_format = image_format
        self.verbos = verbos
        self.all_photos_list = []

    def get_images_list(self):
        count = 0
        if self.verbos == 1:
            print('Start extracting images from folder: {} .'.format(
                self.path_folder_images_to_upload))

        # r=root, d=directories, f = files
        for r, _, f in os.walk(self.path_folder_images_to_upload):
            for file in f:
                count += 1
                if '.'+self.image_format.upper() in file or '.'+self.image_format.lower() in file:
                    self.all_photos_list.append(os.path.join(r, file))
        if self.verbos == 1:
            print('Done extracting {0} photos.'.format(count))

    def cut_images_and_save_them(self):
        count = 0
        if self.verbos == 1:
            print('Start cutting images', end=' ')

        for img_path in self.all_photos_list:
            img = cv2.imread(img_path)
            h, w, _ = img.shape
            self.final_image_size = 252

            hight_to_cut_final_image = int((h - self.final_image_size)/2.0)
            width_to_cut_final_image = int((w - self.final_image_size)/2.0)
            # For 252x252 px image
            # y_0 = 234
            # y_f = 486
            # x_0 = 514
            # x_f = 766
            y_0 = hight_to_cut_final_image
            y_f = hight_to_cut_final_image + self.final_image_size
            x_0 = width_to_cut_final_image
            x_f = width_to_cut_final_image + self.final_image_size

            crop_img = img[y_0:y_f, x_0:x_f]
            old_name = img_path.split("/")[-1]
            cv2.imwrite(self.path_folder_images_to_save+'/'+self.image_starting_with +
                        ''+str(uuid.uuid4())+''+old_name, crop_img, [cv2.IMWRITE_PNG_COMPRESSION, 0])
            count += 1
            if self.verbos == 1:
                if count % 10 == 0:
                    print('.', end=' ')
        if self.verbos == 1:
            print('\nDone cutting and saving images!')

    def start_cutting(self):
        self.get_images_list()
        self.cut_images_and_save_them()
        print('Done dealing with images')


class createImagesFromVideo():
    '''
        path_folder_video_upload, path_folder_images_to_save => Full not relative path!!!
        image_starting_with => for classification purposes man or not wearing a hat or not
        save_every_frame => save the images on the x'th frame - where x = save_every_frame argument
        image_format = > not supported at the moment
        verbos => 0-> no explainings outputs, ->outputs explainings
    '''

    def __init__(self, path_video_upload, path_folder_images_to_save, image_starting_with, save_every_frame=10, image_format='PNG', verbos=0):
        self.path_video_upload = path_video_upload.strip()
        self.path_folder_images_to_save = path_folder_images_to_save.strip()
        self.image_starting_with = image_starting_with.strip()
        self.save_every_frame = save_every_frame
        self.image_format = image_format
        self.verbos = verbos
        self.all_photos_list = []

    def start_cutting_video(self):
        cap = cv2.VideoCapture(self.path_video_upload)
        index = 0
        if self.verbos == 1:
            print('Start cutting images out of the video every {0} frames.'.format(
                self.save_every_frame))
            print('Working', end=' ')
        while True:
            _, frame = cap.read()
            if frame is None:
                break
            # cv2.imshow('app', frame)
            if index % self.save_every_frame == 0:
                cv2.imwrite(self.path_folder_images_to_save+'/'+self.image_starting_with +
                            ''+str(uuid.uuid4()), frame, [cv2.IMWRITE_PNG_COMPRESSION, 0])
                print('.', end=' ')
            index += 1
        cap.release()
        if self.verbos == 1:
            print('\nDone cutting and saving images!')
