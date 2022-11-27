from exercice4 import use_tag,setup_env


if __name__ == '__main__':
    # Gazebo Rviz and rqt graph
    # Do not use if they are already open
    setup_env()

    # ini() will do something like this
    #frame = cv2.imread("tags_test/artest.png")
    #frame = cv2.imread("tags_test/ar_tag_1.JPG")
    #frame = cv2.imread("tags_test/ARtag3.png")
    
    name="ar_tag_1.JPG"
    use_tetha=True  #this is the only difference with exercice4
    use_tag(name,use_tetha)

