# COPYRIGHT SAPPHIREKR 2024
# This client was made for tinkerers who want to play around with some code.
# Before beginning please run the setup.py file to install all required dependencies and requirments for the client.
# Have fun tinkering! :)
import webview # pip install webview
import keyboard
import sys

# Read and store the css file contents in a string called, custom_css & social_custom_css
css_file = open("customization/main_custom.css", "r")
main_custom_css = css_file.read()
css_file.close()

hub_css_file = open("customization/social_custom.css", "r")
hub_css = hub_css_file.read()
hub_css_file.close()


# This code below is only useful if the user wants to use this.
def KrunkHub():
    HubWindow = webview.create_window('Krunker Hub', 'https://krunker.io/social.html')
    # Loading the krunker hub css
    HubWindow.load_css(hub_css)

keyboard.add_hotkey('ctrl+alt+h', KrunkHub)

# Avoid using the keyboard.add_hotkey() function below in this function, it prevents the client from starting.
def TinkerClientFeatures(window):
    #window.toggle_fullscreen()
    # You can mess with this lmao
    window.load_css('''
    /* mess with these(if you want to and if you can) */
    #aContainer {
        display: none !important;
    }
    #newsHolder {
        display: none !important;
    }
    #mapInfo::after {
        content: ' - Tinker Client' !important;
        text-decoration: bold !important;
    }
    #/21823819281/frvr-krunker_io-krunker-display-banner-krunkerio_300x250_4 {
        display: none !important;
    }
    #endAContainer {
        display: none !important;
    }
    /* Hiding the krunker hub button, the client can't work with the krunker hub through the button for some reason */
    .menuItem:nth-child(4) {
        display: none !important;
    }
    ''')
    # Loading the main_custom.css file
    window.load_css(main_custom_css)
    # Javascript code that will be executed.
    main_custom_js = """
    // You can mess with these aswell, just make sure to not mess something up.
    // Changing the krunker logo
    document.getElementById('mainLogo').src = 'https://i.imgur.com/4UsICVn.png';
    // removing the face near the logo
    document.getElementById('mainLogoFace').remove();
    // removing the season label
    document.getElementById('seasonLabel').remove();
    // Removing the ads from the live now section within the in-game menu.
    document.getElementById('adCon').remove();
    """
    window.evaluate_js(main_custom_js)
    
window = webview.create_window('Tinker Client', 'https://krunker.io/', confirm_close=True, min_size=(800, 600))
webview.start(TinkerClientFeatures, window)
