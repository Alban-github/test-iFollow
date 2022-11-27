from exercice1 import run
from time import sleep

if __name__ == '__main__':
        
    run_gazebo=1
    use_mux=1

    # ini ROS comme exrecice 1 et 2
    # pour aleger les tests mqtt desactiver gazebo
    if (not run_gazebo):
        cmd = 'roscore'
        run(cmd)
        sleep(1)
        run('python3 listener.py')
    else:
        cmd_tb3_brgr= 'export TURTLEBOT3_MODEL=burger \n'
        cmd = cmd_tb3_brgr+'roslaunch turtlebot3_gazebo turtlebot3_world.launch'
        run(cmd)
        sleep(3)
        cmd = 'roslaunch turtlebot3_navigation turtlebot3_navigation.launch'
        cmd = cmd_tb3_brgr+cmd
        #run(cmd)


    if not use_mux:
        # sans le mux, connecter le noeud mqtt à turtlebot
        chatter_name= '/cmd_vel'
    else:
        # comme exercice 2
        chatter_name= '/cmd_web'
        cmd = 'rosrun topic_tools mux cmd_vel cmd_local cmd_web mux:=mux_cmdvel'
        run(cmd)
        mux_select_param='cmd_web'
        cmd = 'rosrun topic_tools mux_select mux_cmdvel '+mux_select_param
        run(cmd)


    # Pour tester les fonctions de detection clavier
    #run('python3 detect_keys.py')    
    
    # Les 2 blocs principaux :
    run('python3 mqtt_publish.py')
    run('python3 mqtt_subscribe.py '+chatter_name)


    # Pour visualiser les noeuds :
    cmd = 'rosrun rqt_graph rqt_graph'
    run(cmd)

    
