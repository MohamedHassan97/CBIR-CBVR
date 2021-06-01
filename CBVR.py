from cv2 import cv2
import numpy as np

def keyframe(name,threshold=0.3):
    ''' 
    parameters
        name: string path of processed video
        threshold: float value control the threshold of comparison bet. frames
    extract keyframes from a video
    return: np.array of keyframes 
    '''

    cap = cv2.VideoCapture(name)
    frameCount = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))-1
    frameWidth = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frameHeight = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    ret,current = cap.read()
    prev = current
    prevHist = np.array([cv2.calcHist([prev],[i],None,[256],[0,256]) for i in [0,1,2]])
    prevHist = prevHist / (frameHeight*frameWidth)
    keyframes = [prevHist]

    for dummy in range(1,frameCount):
        if ret:
            ret, current = cap.read()
            currentHist = np.array([cv2.calcHist([current],[i],None,[256],[0,256]) for i in [0,1,2]])
            currentHist = currentHist / (frameHeight*frameWidth)
            dif = np.sum(np.abs(prevHist-currentHist))/3
            if dif > threshold:
                keyframes.append(currentHist)
            prev = current
            prevHist = currentHist

    cap.release()
    return np.array(keyframes)

def video_distance(dbHist,queryHist,threshold=0.5):
    '''
    parameters
        dbHist: np.array of keyframes Histograms of video from the database
        queryHist: np.array of keyframes Histograms of query video
        threshold: float value control the threshold of comparison bet. keyframes
    computer similarity bet. 2 videos
    return: similarity percentage
    '''

    Match = 0
    for hist in range(len(queryHist)):
        for h in range(len(dbHist)):
            dif = np.sum(np.abs(dbHist[h]-queryHist[hist]))/3
            if dif <= threshold:
                Match += 1
                break
    return Match/len(queryHist)