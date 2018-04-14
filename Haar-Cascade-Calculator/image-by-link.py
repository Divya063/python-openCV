import urllib.request
import cv2
import numpy as np
import os

def store_raw_images():

    #http://image-net.org/api/text/imagenet.synset.geturls?wnid=n07942152

    neg_images_link = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n00523513'   
    neg_image_urls = urllib.request.urlopen(neg_images_link).read().decode()
    pic_num = 440
    
    if not os.path.exists('neg'):
        os.makedirs('neg')
        
    for i in neg_image_urls.split('\n'):
        try:
            print(i)
            urllib.request.urlretrieve(i, "neg/"+str(pic_num)+".jpg")
            img = cv2.imread("neg/"+str(pic_num)+".jpg",cv2.IMREAD_GRAYSCALE)
            # should be larger than samples / pos pic (so we can place our image on it)
            resized_image = cv2.resize(img, (100, 100))
            cv2.imwrite("neg/"+str(pic_num)+".jpg",resized_image)
            pic_num += 1
            
        except Exception as e:
            print(str(e)) 


#store_raw_images()

def find_images_not_found():
    match = False
    for file_type in ['neg']:
        for img in os.listdir(file_type):
            for not_found in os.listdir('images_not_found'):
                try:
                    current_image_path = str(file_type)+'/'+str(img)
                    not_found = cv2.imread('images_not_found/'+str(not_found))
                    question = cv2.imread(current_image_path)
                    if not_found.shape == question.shape and not(np.bitwise_xor(not_found,question).any()):
                        print('That is not original pic! Deleting!')
                        print(current_image_path)
                        os.remove(current_image_path)
                except Exception as e:
                    print(str(e))

def create_pos_n_neg():
    for file_type in ['neg']:
        
        for img in os.listdir(file_type):

            if file_type == 'pos':
                line = file_type+'/'+img+' 1 0 0 50 50\n'
                with open('info.dat','a') as f:
                    f.write(line)
            elif file_type == 'neg':
                line = file_type+'/'+img+'\n'
                with open('bg.txt','a') as f:
                    f.write(line)

create_pos_n_neg()

#find_images_not_found()