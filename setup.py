# COPYRIGHT SAPPHIREKR 2023
# You can tinker with this file aswell, just make sure not to break everything.
# You can use this file to distribute your modified client without the entire customization folder.
import os

try:
    os.system('mkdir customization')
    main_css = open("customization/main_custom.css", "x")
    social_css = open("customization/social_custom.css", "x")
    main_css.close()
    social_css.close()
except:
    print("\033[0;31m Setup Failed, Please create a new folder within this folder called: customization. \033[1;37m")
    print("Library installation will continue as normal")
    os.system('pip install pywebview==4.0.1')
    os.system('pip install keyboard')

os.system('pip install pywebview==4.0.1')
os.system('pip install keyboard')


print("""\n \033[0;32m 
Installation Complete! The Client has setup now!
To use Custom Css Please insert code of your css in your main_custom.css file and social_custom.css file in the customization folder \033[1;37m""")
input("Press Enter to exit")