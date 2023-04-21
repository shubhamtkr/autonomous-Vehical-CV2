import cv2
import numpy as np
import utils


def getLaneCurve(img):
    imgThres=utils.thresholding(img)

    h , w, c =img.shape

    points = utils.valTrackbars()
    imgWrap=utils.wrapImg(img,points,w,h)
    imgWrapPoints= utils.drawPoints(img, points)

    cv2.imshow('Thres', imgThres)
    cv2.imshow('Wrap', imgWrap)
    cv2.imshow('wrap points ', imgWrapPoints)
    return None


if __name__ == '__main__':
    cap = cv2.VideoCapture('vid1.mp4')
    intialTracbarVals = [102,119,20,214]
    utils.initializeTrackbars(intialTracbarVals)
    frameCounter=0
    while True:
      frameCounter +=1
      if cap.get(cv2.CAP_PROP_FRAME_COUNT) ==frameCounter:
          cap.set(cv2.CAP_PROP_POS_FRAMES,0)
          frameCounter=0
      Success, img = cap.read()
      img =cv2.resize(img,(480,240))
      getLaneCurve(img)
      cv2.imshow('vid1',img)
      cv2.waitKey(1)
