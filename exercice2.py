import os
from time import sleep
from exercice1 import run


if __name__ == '__main__':

    # Pour tester la fonction run
    #cmd = 'ls -l'
    #run(cmd)

    # Pour démarrer roscore:
    # dans cet exercice, on va se passer de Gazebo qui lance roscore dans l'exercice 1
    cmd = 'roscore'
    run(cmd)
    sleep(1)

    # Pour un noeud permettant de multiplexer une commande provenant de 2 sources de contrôle différentes.
    # Appelons ces 2 entrées de commande de vitesse /cmd_local et /cmd_web. 
    cmd = 'rosrun topic_tools mux cmd_vel cmd_local cmd_web mux:=mux_cmdvel'
    run(cmd)

    # Dans un teminal, pour controller le mux, choisir : cmd_web ou cmd_local
    # rosrun topic_tools mux_select mux_cmdvel cmd_web
    # rosrun topic_tools mux_select mux_cmdvel cmd_local
    mux_select_param='cmd_web'
    cmd = 'rosrun topic_tools mux_select mux_cmdvel'+mux_select_param
    run(cmd)


    # Pour tester le mux, lancer
    # talker et lister utilise le format twist comme pour gazebo
    # ils permettent de mieux examiner les messages
    # les commandes suivantes sont utilisées dans les codes respectifs 
    # rospy.Publisher(chatter_name, Twist, queue_size=10)
    # rospy.Subscriber('/cmd_vel', Twist, callback)
    run('python3 talker.py 1')
    run('python3 talker.py 2')
    run('python3 listener.py')

    # Pour visualiser les noeuds :
    cmd = 'rosrun rqt_graph rqt_graph'
    run(cmd)

    