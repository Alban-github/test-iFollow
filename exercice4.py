import numpy as np
import cv2, PIL
from cv2 import aruco
import matplotlib.pyplot as plt
import matplotlib as mpl
from tb3_pointop_xyz import GotoPoint
from exercice1 import run
from time import sleep

# Le format des tags n'étais pas précisé, par exemple artest.png utilise aruco.DICT_6X6_n
#aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_50) #DICT_6X6_50 100 250 1000 => n codes
#aruco_dict = aruco.Dictionary_get(aruco.DICT_ARUCO_ORIGINAL) # => 1024 codes
aruco_dict = aruco.Dictionary_get(aruco.DICT_APRILTAG_36h11) #DICT_APRILTAG_36h10 36h11 => h10 : 2320 codes , h11 : 587 codes

# x,y pour nos trois tags
id_vs_pos = {20:(1,0),21:(0,-1),22:(-1,1)}


def show_sample():
    # les premiers elements de aruco dict
    fig = plt.figure()
    plt.title("Sample")
    plt.axis('off')
    nx = 5#0
    ny = 2#0
    
    for i in range(0, nx*ny+0):
        ax = fig.add_subplot(ny,nx, i+1)
        img = aruco.drawMarker(aruco_dict,i, 700)
        plt.imshow(img, cmap = mpl.cm.gray, interpolation = "nearest")
        ax.axis("off")
    #plt.savefig("_data/markers.jpeg")
    #plt.show()

def ini(name=""):
    # lecture de l'image
    frame = cv2.imread("tags_test/"+name)
    plt.figure()
    plt.title("Original")
    plt.axis("off")
    plt.imshow(frame)
    #plt.show()
    return frame

def find(frame):
    # trouver les AR-tags et tous les ids
    # calculer la rotation du dernier tag trouvé

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    parameters =  aruco.DetectorParameters_create()
    corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
    frame_markers = aruco.drawDetectedMarkers(frame.copy(), corners, ids)

    plt.figure()
    plt.title("AR-tags")
    plt.imshow(frame_markers)
    
    # prend en compte si il y a plus qu'un tag
    tetha=0
    if(ids!=None):
        for i in range(len(ids)):
            c = corners[i][0]
            center=c[:, 0].mean(), c[:, 1].mean()
            front=c[2:4, 0].mean(), c[2:4, 1].mean()
            left=[c[1:3, 0].mean()], [c[1:3, 1].mean()]
            plt.plot(center[0],center[1], "o", label = "id={0}".format(ids[i]))
            plt.plot(front[0],front[1], "x", label = "front" )
            plt.plot(c[0,0],c[0,1], "s", label = "1st_corner")

            dx= c[0,0]-c[1,0]
            dy=-c[0,1]+c[1,1]
            tetha=np.rad2deg(np.arctan2(dy,dx))
            #print(dx,dy,tetha)

    plt.legend()
    #plt.show()
    return(ids,tetha)


def setup_env():
    # same method as exercice 1
    # use empty_world
    cmd_tb3_brgr= 'export TURTLEBOT3_MODEL=burger \n'
    cmd = cmd_tb3_brgr+'roslaunch turtlebot3_gazebo turtlebot3_empty_world.launch'
    run(cmd)
    sleep(1)

    cmd = 'roslaunch turtlebot3_gazebo turtlebot3_gazebo_rviz.launch'
    cmd = cmd_tb3_brgr+cmd
    run(cmd)
    sleep(1)
    
    cmd = 'rosrun rqt_graph rqt_graph'
    run(cmd)
    sleep(1)

    
def use_tag(name='',use_tetha=True):
    # use the functions above to find the tag and send velocity commands to reach the associated position
    
    show_sample()
    frame=ini(name)
    ids,tetha=find(frame)
    tetha=tetha*use_tetha
    if (ids!=None):
        #take the last id so it matches tetha
        id=ids[-1][0]
        print('id =',id)
        try:
            #print(id_vs_pos[id])
            x,y=id_vs_pos[id]
            nav_goal = [x, y, tetha]
            #print(nav_goal)
            GotoPoint(nav_goal)
        except KeyError:
            print("This tag isn't assigned to a position")

    else:
        print("No AR-tag found")
    
    print("Close the images to end the program")
    plt.show()


if __name__ == '__main__':
    # Gazebo Rviz and rqt graph
    # Do not use if they are already open
    setup_env()

    # ini() will do something like this
    #frame = cv2.imread("tags_test/artest.png")
    #frame = cv2.imread("tags_test/ar_tag_1.JPG")
    #frame = cv2.imread("tags_test/ARtag3.png")
    
    name="ar_tag_3.JPG"
    use_tetha=False
    use_tag(name,use_tetha)




    
