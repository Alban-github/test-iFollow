import os
from time import sleep

def run(cmd):
    os.system("gnome-terminal -e 'bash -c \""+cmd+";bash\"'")


if __name__ == '__main__':

    # Pour tester la fonction run
    #cmd = 'ls -l'
    #run(cmd)

    # choix du model burger qui sera fait quand necessaire
    cmd_tb3_brgr= 'export TURTLEBOT3_MODEL=burger \n'
    # alternativement il est possible de fixer le choix
    # gedit ~/.bashrc
    # ajout de 'export TURTLEBOT3_MODEL=burger' en fin de texte
    # source ~/.bashrc

    # Visualisation du robot dans Gazebo
    # A cause des limitations de la VM, il faut aussi activer View→Collision
    cmd = cmd_tb3_brgr+'roslaunch turtlebot3_gazebo turtlebot3_world.launch'
    #cmd = cmd_tb3_brgr+'roslaunch turtlebot3_gazebo turtlebot3_empty_world.launch'
    run(cmd)
    sleep(3)

    # Map dans Rviz
    # cas simple :
    #cmd = 'roslaunch turtlebot3_gazebo turtlebot3_gazebo_rviz.launch'
    # cas avec une carte déjà existante dans le dossier (ex: genérée avec slam) :
    cmd = 'roslaunch turtlebot3_navigation turtlebot3_navigation.launch' #+' map_file:=$HOME/map.yaml' si on veut une autre carte
    cmd = cmd_tb3_brgr+cmd
    run(cmd)

    # Il y a deux boutons dans Rviz permettant au robot de se localiser et de se déplacer dans cette map, 
    # 2D Pose Estimate et 
    # 2D Nav Goal respectivement.

    # Contrôler le robot 
    # les instructions s'afficherons sur le terminal
    # Attention, il faut choisir un seul controleur ou Nav goal
    # car leurs consignes sont en conflits

    # en téléopération (clavier) :
    cmd = cmd_tb3_brgr+'roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch'
    run(cmd)

    # en lui donnant un nav goal 2D :
    # les obstacles sont moins bien geres qu’avec « 2D Nav Goal » de Rviz
    cmd = cmd_tb3_brgr+'roslaunch turtlebot3_example turtlebot3_pointop_key.launch'
    #run(cmd)


