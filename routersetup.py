#ConnectionHandler
from netmiko import Netmiko

cisco_serial = {
    "device_type": "cisco_ios_serial",
    "serial_settings":{'port':'COM4'},
    "username": "Router",
    "password": "cisco",
    "secret":"cisco",
    'global_delay_factor':3,
    }

#Connection to router
connection = Netmiko(**cisco_serial)
connection.enable()


#Selection menu
print("###############################")
print("1) Show running-configuration")
print("2) Standard configuration")
print("3) Save running-config")
print("###############################")

#Bool used in while loops that gets set to false, once the specific paremeter has
#been set/filled out.
validation_bool = True

commands = []

#Commands used mulitple times
login = "login"
_exit = "exit"

chosen = int(input("Choose desired route:"))
if(chosen==1):
    output = connection.send_command("sh run")
    print(output)
elif(chosen==2):
    
    #hostname
    while(validation_bool):
        hostname = str(input("Hostname:"))
        if(hostname == ""):
            print("Empty")
        else:
            validation_bool = False
            final_hostname = "hostname "
            final_hostname += hostname
    validation_bool = True
    #enable secret
    while(validation_bool):
        enable_secret = str(input("Choose password:"))
        if(enable_secret ==""):
            print("Empty")
        else:
            validation_bool = False
            final_enable_secret = "enable secret "
            final_enable_secret += enable_secret
    validation_bool = True
    #line vty
    while(validation_bool):
        line_vty = "line vty 0 15"
        
        line_vty_pass = str(input("Choose line vty password:"))
        if(line_vty_pass ==""):
            print("Empty")
        else:
            validation_bool = False
            final_line_vty_pass = "password "
            final_line_vty_pass += line_vty_pass
    validation_bool = True
    #line console
    while(validation_bool):
        line_console = "line console 0"
        
        line_console_pass = str(input("Choose console line password:"))
        if(line_console_pass ==""):
            print("Empty")
        else:
            validation_bool = False
            final_line_console_pass = "password "
            final_line_console_pass += line_console_pass
    validation_bool = True
    #Some       
    
    
    #Above commands getting send as config commands for the configuration
    #of the switch
    cfg_commands = [
        #Hostname cmds
        final_hostname,
        #Enable secret cmds
        final_enable_secret, 
        #Line vty cmds
        line_vty,final_line_vty_pass,login,_exit,
        #Line console cmds
        line_console,final_line_console_pass,login,_exit
        ]
    
    connection.send_config_set()
    output = connection.send_config_set(cfg_commands)
    print(output)
    print("Done!")
      
elif(chosen==3):
    output = connection.save_config()
    print(output)


connection.disconnect()


# Automatically cleans-up the output so that only the show output is returned
print()
   
            

             

        