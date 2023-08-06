import time
import cv2
import random
from shutil import copyfile
import threading
import ntpath
import subprocess

import sys, os, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
sys.path.insert(0, currentdir)
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

import main_paras
from main_paras import queueForGui, queueForResult, queueForCom

from define import *
from calibration import crop_rotate, final_save
from qr_identify import qrIdentify
from algorithm import alg

def camInstCreate(cameraIndex):
    try:
        device="/dev/video"+str(cameraIndex)
        print(device)
        camInst=cv2.VideoCapture(device)
        #time.sleep(1)
        camInst.set(cv2.CAP_PROP_FRAME_WIDTH,  MAX_CAMERA_RESOLUTION_WIDTH)
        camInst.set(cv2.CAP_PROP_FRAME_HEIGHT, MAX_CAMERA_RESOLUTION_HEIGHT)
        print (camInst)
        return camInst
    except Exception as camErr:
        print("Camera create exception:",camErr)
        return None;
    

camera_sem = threading.Semaphore()


def takePhoto(cameraIndex,qrCode, ext, event, callBack):
    s = False
    img =None
    for i in range(5):
        camera_sem.acquire()    
        try:
            cam=camInstCreate(cameraIndex)
            s, img=cam.read()
            if s:
                cam.release()
                camera_sem.release()
                break;
        except cv2.error as cv2Error:
            print("takePhoto cv2 Error: ", cv2Error)
        except Exception as e:
            print("takePhoto Exception: ", e)
    
        camera_sem.release()            
        if cam !=None:
            cam.release()
        event.wait(2)
        if event.isSet():
            break;
    if s:
        print('got image')
        #cv2.imwrite(str(int(time.time())) + '_'+time.strftime('%Y%m%d%H%M%S')+'.png', img)
        if qrCode == None:
            #cv2.imwrite(str(int(time.time())) + '_'+time.strftime('%Y%m%d%H%M%S')+'.png', img)
            qrCode = qrIdentify(img)
            if qrCode == None:
                return NO_ID
            callBack(qrCode)

        
            
        
        photo=qrCode+ext+'_'+str(int(time.time())) + '_'+time.strftime('%Y%m%d%H%M%S')+'.png'

        identifier, final_img = alg.target_cut(img)
        if identifier == INVALID:
            return INVALID
            #print('image deal done')
        imageFile=IMG_PATH+photo
        if final_save(final_img,imageFile):
            return photo
    else:
        print("Photo taking failed!",qrCode, time.strftime('%Y%m%d%H%M%S'))
        
    return None
    
    
# def takePhoto(cameraIndex, qrCode, ext, event):
#     rtn = None
#     print('in takePhoto')
# #     #fswebcam -v --no-banner -d /dev/video0 -r 1600x1200 -p YUYV -S 10 test.png
# #     cmd = 'fswebcam -v --no-banner -d /dev/video'+str(cameraIndex)+' -r 1600x1200 -p YUYV -S 10 test.png'
# #     result=subprocess.check_output([cmd], shell=True).decode("utf-8")
# #     print('result:',result)
# #     return
#     rtn=cv_camera(cameraIndex,qrCode, ext, event);
#     #rtn=fsw_camera(cameraIndex,qrCode,event);
#     
#     print('takePhoto return')
#     return rtn

class TakePhotoProcedure(threading.Thread):
    def __init__(self, slotIndex, qrCode, camera, qCom, stopTakingPhoto):
        threading.Thread.__init__(self)
        self.slotIndex=slotIndex
        self.qrCode=qrCode
        self.camera = camera
        self.qCom = qCom
       
        self.timerParaIndex = 0
        self.taskStop=False
        self.event=stopTakingPhoto
        
        self.adjustment = 0

    def run(self):
        while True:
            if main_paras.info.getTestMode()==TEST_MODE_SPEED:
                self.procedure(0)
                break;
            else:
                if self.timerParaIndex < len(PHOTO_TAKING_GAPS):
                    delay=PHOTO_TAKING_GAPS[self.timerParaIndex] - self.adjustment
                    self.timerParaIndex += 1
                    #print('taking photo set delay:',delay)
                    if delay > 0:
                        self.event.wait(delay)
                    #print('taking photo delay time out')
                else:
                    self.timerParaIndex = 0
                    break;

                begin=time.time()
#                self.procedure(self.timerParaIndex)
                self.procedure(0)
                end=time.time()
                self.adjustment = end - begin;
            
            if self.event.isSet():
                #print(time.strftime('%Y%m%d%H%M%S'), "got stop command")
                break;
    def takePhotoCallBack(self, new_qr):
        self.qrCode = new_qr
        item=[self.slotIndex, DEVICE_STATE_TAKING_PHOTO, self.qrCode, '']
        queueForGui.put(item)
        
            
    def procedure(self,photoIndex):
        photoFile=takePhoto(self.camera, self.qrCode, '_'+str(self.slotIndex)+'_'+str(photoIndex), self.event, self.takePhotoCallBack)
        print('in take_photo, procedure:',photoFile)
        if(photoFile ==None ):
            item=[self.slotIndex, Taking_picture_fail, self.qrCode, '']
        elif photoFile == NO_ID:
            item=[self.slotIndex, Wrong_cassette, self.qrCode, '']
        elif photoFile == INVALID:
            item=[self.slotIndex, Invalid_image_identifier, self.qrCode, '']
        else: 
            item=[]
        if item == []:
            self.qCom.put(photoFile)
        else:
            queueForGui.put(item)
        
    
    
if __name__ == "__main__":
    takePhoto_test()
          
