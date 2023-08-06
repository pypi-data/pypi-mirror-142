import os
from collections import deque
import numpy as np
import argparse
import math
import imutils
import cv2
import matplotlib
import matplotlib.pyplot as plt
# from scipy.optimize import curve_fit
from numpy.linalg import eig, inv
from skimage.morphology import skeletonize, thin
from skimage.util import invert
from scipy.spatial import distance

from scipy import optimize
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import pairwise_distances_argmin
import matplotlib.animation as manimation
from collections import Counter

parser = argparse.ArgumentParser(description='process image to skeleton, and cluster to n-elements')
parser.add_argument('-n', type=int, help='Number of element to cluster')
parser.add_argument('-i', type=int, help='Video ID')
args = parser.parse_args()

video_id = args.i
num_seg = args.n

#process='bend'
#video_name = f'./experiment_video/batch1/post_edit/{video_id}.mp4'
process='twist'
video_name = f'./experiment_video/batch2/post_process/{video_id}.mp4'
assert os.path.exists(video_name), 'video does not exist'

log_flag=False #input("y/n to log the data? ")
record_flag=True
FFMpegWriter = manimation.writers['ffmpeg']
metadata = dict(title='Movie Test', artist='Matplotlib',
                comment='Movie support!')
writer = FFMpegWriter(fps=15, metadata=metadata)

def test_func(x, a, b, c):
    return a*x**2+b*x+c

def unit_vector(vector):
    return vector / np.linalg.norm(vector)

def angle_between(v1, v2):
    v1_u = unit_vector(v1)
    v2_u = unit_vector(v2)
    return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))

def binarize_array(numpy_array, threshold=200):
    """Binarize a numpy array."""
    for i in range(len(numpy_array)):
        for j in range(len(numpy_array[0])):
            if numpy_array[i][j] > threshold:
                numpy_array[i][j] = 255
            else:
                numpy_array[i][j] = 0
    return numpy_array


def select_ground(frame):
    while True:
        print("select ground")
        bbox = cv2.selectROI('MultiTracker', frame)
        ground_limit=[bbox[0],bbox[0]+bbox[2],bbox[1],bbox[1]+bbox[3]] #x_low x_high y_low y_high
        k = cv2.waitKey(0) & 0xFF
        if k == 32 or k == 13:  # (13: enter, 32: space)
            print("quit")
            break
    print('Selected ground {}'.format(bbox))
    return ground_limit

def frame_reduce(frame, ground_limit):
    return frame[ground_limit[2]:ground_limit[3],ground_limit[0]:ground_limit[1],:]

def erode_dilate_frame(frame, greenLower=(0, 0, 0), greenUpper=(100, 100, 100)):
    blurred = cv2.GaussianBlur(frame, (11, 11), 0)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, greenLower, greenUpper)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)
    return mask

def all_processed_fig(frame,process, choose=False,plot_fig=True):
    # plt.imshow(frame.shape)
    # if process=="twist":
    #     frame[...,0]=0
    #     frame[...,2]=0
    mask=[]
    mask1=erode_dilate_frame(frame)
    mask.append(mask1)
    print(np.min(frame[...,0]))
    print(np.max(frame[...,0]))
    print(np.min(frame[...,1]))
    print(np.max(frame[...,1]))
    print(np.min(frame[...,2]))
    print(np.max(frame[...,2]))
    if process=="twist":
        mask2 = binarize_array(frame[...,1], 70 )#frame[:,:,1],65
    else:
        mask2 = binarize_array(frame[:,:,0], 100)
    mask3 = invert(mask2)
    mask3[mask3!=0]=1

    skeleton3 = invert(skeletonize(mask3))
    mask.append(skeleton3)

    thinned2 = thin(mask2,max_iter=5)
    mask.append(thinned2)

    thinned6 = thin(skeleton3,max_iter=25)
    mask.append(thinned6)

    skeleton3 = np.array(skeleton3, dtype=np.uint8)
    thinned2 = np.array(thinned2, dtype=np.uint8)
    thinned6 = np.array(thinned6, dtype=np.uint8)
    kernel = np.ones((5,5),np.uint8)
    skeleton3 = cv2.erode(skeleton3, kernel, iterations=3)
    skeleton3 = cv2.dilate(skeleton3, kernel, iterations=3)
    thinned2 = cv2.erode(thinned2, kernel, iterations=3)
    thinned2 = cv2.dilate(thinned2, kernel, iterations=3)
    thinned6 = cv2.erode(thinned6, kernel, iterations=3)
    thinned6 = cv2.dilate(thinned6, kernel, iterations=3)
    mask.append(skeleton3)
    mask.append(thinned2)
    mask.append(thinned6)


    if plot_fig:
        fig, axes = plt.subplots(3, 3,figsize=(10,5))
        ax = axes.ravel()
        ax[0].imshow(frame)
        ax[0].text(0,0,"original")

        for i in range(len(mask)):
            ax[i+1].imshow(mask[i])
            ax[i+1].text(0,0,str(i))
        plt.show()
        plt.close("all")
    cv2.destroyAllWindows()
    if choose:
        num=int(input("enter the number of the pic you like: "))
    else:
        num=4


    return num

def chosen_process(num,frame):
    if num==0:
        frame=erode_dilate_frame(frame)
    elif num==1 or num==4:
        if process=="twist":
            mask2 = binarize_array(frame[...,1], 60)
        else:
            mask2 = binarize_array(frame[:,:,0], 100)
        mask3 = invert(mask2)
        mask3[mask3!=0]=1
        frame= invert(skeletonize(mask3))
    elif num==2 or num==5:
        if process=="twist":
            mask2 = binarize_array(frame[...,1], 70)
        else:
            mask2 = binarize_array(frame[:,:,0], 100)
        frame = thin(mask2,max_iter=5)
    elif num==3 or num==6:
        if process=="twist":
            mask2 = binarize_array(frame[:,:,1], 50)
        else:
            mask2 = binarize_array(frame[:,:,0], 100)
        mask3 = invert(mask2)
        mask3[mask3!=0]=1
        skeleton3 = invert(skeletonize(mask3))
        frame = thin(skeleton3,max_iter=25)
    if num==4:
        frame = np.array(frame, dtype=np.uint8)
        kernel = np.ones((5,5),np.uint8)
        frame= cv2.erode(frame, kernel, iterations=3)
        frame = cv2.dilate(frame, kernel, iterations=3)
    return frame

def cluster_segment(frame,num_seg,plot_flag=False):
    frame=frame[5:-5][5:-5]

    if process=="bend":
        frame=binarize_array(frame[:,:,0], 100)
    else:
        frame=binarize_array(frame, 0.5)

    # data=np.where(arr!=255)
    data=np.where(frame==0)


    X=np.flip(np.array(data).T,1)

    k_means = KMeans(n_clusters=num_seg).fit(X)

    colors = ['b','g','deeppink','c','m','y','k','olive','limegreen','lightcoral','deepskyblue']
    k_means_cluster_centers = k_means.cluster_centers_

    k_means_labels = pairwise_distances_argmin(X, k_means_cluster_centers)

    #y_pred = KMeans(n_clusters=num_seg).fit_predict(X) 
    #plt.scatter(X[:,0], X[:,1], c=y_pred)
    #plt.show()

    ends=[]
    for k, col in zip(range(num_seg), colors):
        # plt.imshow(frame)
        my_members = k_means_labels == k
        cluster_center = k_means_cluster_centers[k]
        if process=="bend":
            params, _ = optimize.curve_fit(test_func, X[my_members, 0], X[my_members, 1], p0=[2, 2, 2])
            y_fit=test_func(X[my_members, 0], params[0], params[1], params[2])

        plt.plot(X[my_members, 0], X[my_members, 1],
                markerfacecolor=col, marker='.')
        plt.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col,
                markeredgecolor='k', markersize=6,label='cluster center')

        if plot_flag:
            if process=="bend":
                plt.plot(X[my_members, 0],y_fit,'r.',label='Fitted function')
            else:
                plt.show()
                flag=input("this is (0 center/ 1 edge/ 2 other): ")

        if process=="bend":
            x=np.array([np.min(X[my_members, 0]),np.max(X[my_members, 0])])
            y=np.array([y_fit[np.where(X[my_members, 0]==np.min(X[my_members, 0]))[0][0]],y_fit[np.where(X[my_members, 0]==np.max(X[my_members, 0]))[0][0]]])
            ends.append((x[1],y[1]))
        else:
            try:
                ends.append([flag,(cluster_center[0],cluster_center[1])])
            except:
                ends.append((cluster_center[0],cluster_center[1]))
    if plot_flag:
        plt.show()
    if process=="bend":
        # sort ends first : old document in abunis
        dis=distance.cdist(ends, ends, 'euclidean')
        dis=np.diag(dis[1:])
    else:
        ends=np.array(ends)
        ends=ends[ends[:,0].argsort()]
        dis=ends

    return dis, k_means_cluster_centers

def fit_whole(frame,i):
    y_data=(-np.array(np.where(frame<1)[0]))
    x_data=np.where(frame<1)[1]
    params, params_covariance = optimize.curve_fit(test_func, x_data, y_data, p0=[2, 2, 2])
    y_fit=test_func(x_data, params[0], params[1], params[2])

    plt.imshow(frame)
    plt.scatter(x_data, -y_data,s=1.0, label='Data')
    plt.plot(x_data, -y_fit,'ro', markersize=1.0, label='Fitted function')
    # plt.legend(loc='upper right')
    plt.ylim([0,ground_limit[3]-ground_limit[2]])
    plt.xlim([0,ground_limit[1]-ground_limit[0]])
    plt.text(0,0,"frame "+str(i))

def log_data(x,y,itr,start_itr,end_itr):
    if itr>start_itr and itr<end_itr:
        file="./x"+"{:02d}".format(i-211)+".txt"
        f2= open(file,"a+")
        for j in range(0,len(x),100):
            f2.write(str(x[j])+'\n')
        f2.close()
        file="./y"+"{:02d}".format(i-211)+".txt"
        f2= open(file,"a+")
        for j in range(0,len(y),100):
            f2.write(str(y[j])+'\n')
        f2.close()

def process_bend(
    camera,
    frame,
    ground_limit,
    log_flag,
    record_flag,
    num_seg=11,
):
    # print out all processed figs and pick the best process for the video
    num=4#all_processed_fig(frame,choose=False,plot_fig=False)

    dis, k_means_center =cluster_segment(frame,num_seg)


    if log_flag:
        start_itr=input("starting frame is: ")
        end_itr=input("ending frame is: ")

    eps_record=[]
    k_means_center_record = [k_means_center]
    fig = plt.figure()
    i=0
    with writer.saving(fig, f"{video_id}_n{num_seg}.mp4", 100):
        while True:
            i+=1
            # grab the current frame
            (grabbed, frame0) = camera.read()
            if grabbed is False:
                break
            frame0 = frame_reduce(frame0, ground_limit)

            dis_old=dis
            dis, k_means_center =cluster_segment(frame0,num_seg)
            eps=(dis-dis_old)/dis_old
            eps_record.append(eps)
            k_means_center_record.append(k_means_center)

            # need to write function to scale, something like
                    # y=(-np.array(np.where(mask>0)[0])+8)/1200+0.35
                    # x=(np.where(mask>0)[1]-248)/1200

            if record_flag:
                frame=chosen_process(num,frame0)
                fit_whole(frame,i)
                writer.grab_frame()
                fig.clf()
            if log_flag:
                log_data(x_data,y_fit,i,start_itr,end_itr)
    np.save(f"eps_{video_id}_n{num_seg}",eps_record)
    np.save(f"centers_{video_id}_n{num_seg}",np.array(k_means_center_record))

def process_twist(camera,frame,log_flag,record_flag):
    # print out all processed figs and pick the best process for the video
    num=all_processed_fig(frame,process,choose=True,plot_fig=True)
    # plt.imshow(frame)
    frame=chosen_process(num,frame)
    dis, k_means_center =cluster_segment(frame,2,plot_flag=True)
    vector_move=np.array(dis[0][1])-np.array(dis[1][1])
    vector_ref=vector_move
    angle=angle_between(vector_move,vector_ref)
    angle_record=[]
    angle_record.append(angle)
    angle1_record=[]
    angle1_record.append(angle)
    angle2_record=[]
    angle2_record.append(angle)

    if log_flag:
        start_itr=input("starting frame is: ")
        end_itr=input("ending frame is: ")

    fig = plt.figure()
    i=0
    with writer.saving(fig, "twist.mp4", 100):
        while True :#and i <5:

            i+=1

            # grab the current frame
            (grabbed, frame0) = camera.read()
            if grabbed is False:
                break
            frame0=cv2.cvtColor(frame0, cv2.COLOR_BGR2RGB)
            frame0 = frame_reduce(frame0, ground_limit)
            plt.clf()
            plt.imshow(frame0)
            frame=chosen_process(num,frame0)
            dis, k_means_center =cluster_segment(frame,2)
            vector_move=np.array(dis[0])-np.array(dis[1])
            angle1=angle_between(vector_move,vector_ref)
            angle2=angle_between(-vector_move,vector_ref)
            angle_candi=np.array([[np.abs(angle1-angle),angle1],[np.abs(angle2-angle),angle2]])
            angle_candi=angle_candi[angle_candi[:,0].argsort()]

            angle=angle_candi[0][1]
            angle_record.append(angle)
            angle1_record.append(angle1)
            angle2_record.append(angle2)

            # need to write function to scale, something like
                    # y=(-np.array(np.where(mask>0)[0])+8)/1200+0.35
                    # x=(np.where(mask>0)[1]-248)/1200

            if record_flag:
                frame=chosen_process(num,frame0)
                # fit_whole(frame)
                writer.grab_frame()
            if log_flag:
                log_data(x_data,y_fit,i,start_itr,end_itr)
    np.save("angle",angle_record)
    np.save("angle1",angle1_record)
    np.save("angle2",angle2_record)
def clean_angle():
    c=np.load("angle.npy")
    a=np.load("angle1.npy")
    b=np.load("angle2.npy")
    d=np.hstack((c[:44],a[44:351],c[351:400])) # choose basee on the result
    fig, axs = plt.subplots(5)
    axs[0].plot(range(len(a)),a,'o',label="angle1")
    axs[0].set_ylim([0,180])
    plt.legend()
    axs[1].plot(range(len(b)),b/3.14*180,'o',label="angle2")
    axs[1].set_ylim([0,180])
    plt.legend()
    axs[2].plot(range(len(c)),c/3.14*180,'o',label="angle")
    axs[2].set_ylim([0,180])
    plt.legend()
    axs[3].plot(range(len(a)),a/3.14*180,label="angle1")
    axs[3].plot(range(len(b)),b/3.14*180,label="angle2")
    axs[3].plot(range(len(c)),c/3.14*180,label="angle")
    axs[3].set_ylim([0,180])
    plt.legend()
    axs[4].plot(range(len(d)),d/3.14*180,label="angle")
    axs[4].set_ylim([0,180])
    plt.legend()
    plt.show()
    # plt.savefig("angle1N2.png")
    # #
    np.save("angle_smooth",d)

camera = cv2.VideoCapture(video_name)

(grabbed, frame) = camera.read()
# frame=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

ground_limit=select_ground(frame)
frame = frame_reduce(frame, ground_limit)

if process=="bend":
    process_bend(camera, frame, ground_limit, log_flag, record_flag, num_seg=num_seg)
else:
    process_twist(camera,frame,log_flag,record_flag)

def extract_data_video(scale):
    a=np.load("elem.npy")
    print(a.shape)

    import matplotlib.animation as manimation
    print("plot video")
    FFMpegWriter = manimation.writers['ffmpeg']
    metadata = dict(title='Movie Test', artist='Matplotlib',
                    comment='Movie support!')
    writer = FFMpegWriter(fps=30, metadata=metadata)
    fig = plt.figure()
    X=[]
    with writer.saving(fig, "test.mp4", 100):
        for time in range(len(a)):
            fig.clf()
            x=(764-a[time][:,0])*scale
            y=(a[time][:,1]-88)*scale
            plt.xlim([-0.01,0.38])
            plt.ylim([-0.1,0.1])
            plt.gca().set_aspect('equal', adjustable='box')
            plt.plot(x,y)
            writer.grab_frame()
            X.append([x,y])
    np.save("elemX",X)

# extract_data_video(0.00052)
# a=np.load("curv.npy")[:,1:,1]
# a=np.repeat(a,3,axis=1)
# k=a[:,-1].reshape((77,1))
# a=np.append(a,k,axis=1)
#
# np.save("curv.npy",a)

# # print(a.shape)
# # a=np.repeat(a,30,axis=0)
# # print(a.shape)
# # print(np.sum(a,axis=1).shape)
# plt.plot(range(len(a)),np.sum(a,axis=1)/31)
# plt.show()
