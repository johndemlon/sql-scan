# -*- coding: utf-8 -*-
# Date: 12/28/2018
# Author: Mohamed
# Description: Constants

# Limits
max_time_to_wait = 15
max_active_browsers = 256

# Misc
debug = False
version = '1.0.1'
sql_log = 'sql_vuln.txt'

# Art
banners = [
    '''
  ██████   █████   ██▓         ██████  ▄████▄   ▄▄▄       ███▄    █  ███▄    █ ▓█████  ██▀███  
▒██    ▒ ▒██▓  ██▒▓██▒       ▒██    ▒ ▒██▀ ▀█  ▒████▄     ██ ▀█   █  ██ ▀█   █ ▓█   ▀ ▓██ ▒ ██▒
░ ▓██▄   ▒██▒  ██░▒██░       ░ ▓██▄   ▒▓█    ▄ ▒██  ▀█▄  ▓██  ▀█ ██▒▓██  ▀█ ██▒▒███   ▓██ ░▄█ ▒
  ▒   ██▒░██  █▀ ░▒██░         ▒   ██▒▒▓▓▄ ▄██▒░██▄▄▄▄██ ▓██▒  ▐▌██▒▓██▒  ▐▌██▒▒▓█  ▄ ▒██▀▀█▄  
▒██████▒▒░▒███▒█▄ ░██████▒   ▒██████▒▒▒ ▓███▀ ░ ▓█   ▓██▒▒██░   ▓██░▒██░   ▓██░░▒████▒░██▓ ▒██▒
▒ ▒▓▒ ▒ ░░░ ▒▒░ ▒ ░ ▒░▓  ░   ▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒ ░ ▒░   ▒ ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
░ ░▒  ░ ░ ░ ▒░  ░ ░ ░ ▒  ░   ░ ░▒  ░ ░  ░  ▒     ▒   ▒▒ ░░ ░░   ░ ▒░░ ░░   ░ ▒░ ░ ░  ░  ░▒ ░ ▒░
░  ░  ░     ░   ░   ░ ░      ░  ░  ░  ░          ░   ▒      ░   ░ ░    ░   ░ ░    ░     ░░   ░ 
      ░      ░        ░  ░         ░  ░ ░            ░  ░         ░          ░    ░  ░   ░     
                                      ░                                                                                                                                            
                                                                                                    {}    
''',

    '''

███████╗ ██████╗ ██╗         ███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗ 
██╔════╝██╔═══██╗██║         ██╔════╝██╔════╝██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗
███████╗██║   ██║██║         ███████╗██║     ███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝
╚════██║██║▄▄ ██║██║         ╚════██║██║     ██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗
███████║╚██████╔╝███████╗    ███████║╚██████╗██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║
╚══════╝ ╚══▀▀═╝ ╚══════╝    ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
                                                                                                {}
''',

    '''

   ▄████████ ████████▄    ▄█               ▄████████  ▄████████    ▄████████ ███▄▄▄▄   ███▄▄▄▄      ▄████████    ▄████████ 
  ███    ███ ███    ███  ███              ███    ███ ███    ███   ███    ███ ███▀▀▀██▄ ███▀▀▀██▄   ███    ███   ███    ███ 
  ███    █▀  ███    ███  ███              ███    █▀  ███    █▀    ███    ███ ███   ███ ███   ███   ███    █▀    ███    ███ 
  ███        ███    ███  ███              ███        ███          ███    ███ ███   ███ ███   ███  ▄███▄▄▄      ▄███▄▄▄▄██▀ 
▀███████████ ███    ███  ███            ▀███████████ ███        ▀███████████ ███   ███ ███   ███ ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   
         ███ ███    ███  ███                     ███ ███    █▄    ███    ███ ███   ███ ███   ███   ███    █▄  ▀███████████ 
   ▄█    ███ ███  ▀ ███  ███▌    ▄         ▄█    ███ ███    ███   ███    ███ ███   ███ ███   ███   ███    ███   ███    ███ 
 ▄████████▀   ▀██████▀▄█ █████▄▄██       ▄████████▀  ████████▀    ███    █▀   ▀█   █▀   ▀█   █▀    ██████████   ███    ███ 
                         ▀                                                                                      ███    ███ 
                                                                                                                                {}
''',

    '''
 ▄▀▀▀▀▄  ▄▀▀▀▀▄   ▄▀▀▀▀▄          ▄▀▀▀▀▄  ▄▀▄▄▄▄   ▄▀▀█▄   ▄▀▀▄ ▀▄  ▄▀▀▄ ▀▄  ▄▀▀█▄▄▄▄  ▄▀▀▄▀▀▀▄ 
█ █   ▐ █      █ █    █          █ █   ▐ █ █    ▌ ▐ ▄▀ ▀▄ █  █ █ █ █  █ █ █ ▐  ▄▀   ▐ █   █   █ 
   ▀▄   █      █ ▐    █             ▀▄   ▐ █        █▄▄▄█ ▐  █  ▀█ ▐  █  ▀█   █▄▄▄▄▄  ▐  █▀▀█▀  
▀▄   █   ▀▄▄▄▄▀▄     █           ▀▄   █    █       ▄▀   █   █   █    █   █    █    ▌   ▄▀    █  
 █▀▀▀           █  ▄▀▄▄▄▄▄▄▀      █▀▀▀    ▄▀▄▄▄▄▀ █   ▄▀  ▄▀   █   ▄▀   █    ▄▀▄▄▄▄   █     █   
 ▐              ▐  █              ▐      █     ▐  ▐   ▐   █    ▐   █    ▐    █    ▐   ▐     ▐   
                   ▐                     ▐                ▐        ▐         ▐                  
                                                                                                    {}
''',

    '''
   ▄▄▄▄▄    ▄▄ █ █            ▄▄▄▄▄   ▄█▄    ██      ▄      ▄   ▄███▄   █▄▄▄▄ 
  █     ▀▄ █   █ █           █     ▀▄ █▀ ▀▄  █ █      █      █  █▀   ▀  █  ▄▀ 
▄  ▀▀▀▀▄    ▀▀▀█ █         ▄  ▀▀▀▀▄   █   ▀  █▄▄█ ██   █ ██   █ ██▄▄    █▀▀▌  
 ▀▄▄▄▄▀        █ ███▄       ▀▄▄▄▄▀    █▄  ▄▀ █  █ █ █  █ █ █  █ █▄   ▄▀ █  █  
                █    ▀                ▀███▀     █ █  █ █ █  █ █ ▀███▀     █   
                 ▀                             █  █   ██ █   ██          ▀    
                                              ▀                               
                                                                                {}
'''
]