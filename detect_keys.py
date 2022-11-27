import sys,tty,termios

# Commands and escape codes
END_OF_TEXT = chr(3)  # CTRL+C (prints nothing)
END_OF_FILE = chr(4)  # CTRL+D (prints nothing)
CANCEL      = chr(24) # CTRL+X
ESCAPE      = chr(27) # Escape
CONTROL     = ESCAPE +'['

# Escape sequences for terminal keyboard navigation
ARROW_UP    = CONTROL+'A'
ARROW_DOWN  = CONTROL+'B'
ARROW_RIGHT = CONTROL+'C'
ARROW_LEFT  = CONTROL+'D'
KEY_END     = CONTROL+'F'
KEY_HOME    = CONTROL+'H'
PAGE_UP     = CONTROL+'5~'
PAGE_DOWN   = CONTROL+'6~'

# Escape sequences to match
commands = {
    ARROW_UP   :'up arrow',
    ARROW_DOWN :'down arrow',
    ARROW_RIGHT:'right arrow',
    ARROW_LEFT :'left arrow',
    KEY_END    :'end',
    KEY_HOME   :'home',
    PAGE_UP    :'page up',
    PAGE_DOWN  :'page down',
}

# Blocking read of one input character, detecting appropriate interrupts
def getch():
    k = sys.stdin.read(1)[0]
    if k in {END_OF_TEXT, END_OF_FILE, CANCEL}: raise KeyboardInterrupt
    #print('raw input 0x%X'%ord(k),end='\r\n')
    return k

# Println for raw terminal mode
def println(*args):
    print(*args,end='\r\n',flush=True)

def read_key():
    # Parse known command escape sequences
    read = getch()
    while any(k.startswith(read) for k in commands.keys()): 
        if read in commands: 
            #println('detected command (%s)'%commands[read])
            #read = ''
            break
        read += getch()
    return read

def setraw():
    tty.setraw(sys.stdin.fileno())

def ini():
    # Preserve current terminal settings (we will restore these before exiting)
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    return fd,old_settings

def end(fd,old_settings):
    # clean up
    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings) 
    println('')
    sys.exit(0)


# Main loop to use  
def detect():
    fd,old_settings=ini()
    try:
        # Enter raw mode (key events sent directly as characters)
        setraw()

        # Loop, waiting for keyboard input
        while 1:
            read = read_key()
            if read in commands: 
                println('detected command (%s)'%commands[read])

            # Interpret all other inputs as text input
            #for c in read:
            #    println('detected character 0x%X %c'%(ord(c),c))
            

    # Always clean up
    finally:
        end(fd,old_settings)

if __name__ == '__main__':
    detect()