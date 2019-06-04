import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.textinput import TextInput 
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager,Screen
import os



kivy.require("1.11.0")

class ConnectPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2

        if os.path.isfile("saved_details.txt"):
        	with open("saved_details.txt", "r") as f:
        		s = f.read.split(",")
        		
        		saved_ip = s[0]
        		saved_port = s[1]
        		saved_username = s[2]
        else:
        	saved_ip = ""
        	saved_port = ""
        	saved_username = ""

        #Entering IP
        self.add_widget(Label(text="IP:"))
        self.ip = TextInput(text=saved_ip,multiline=False)
        self.add_widget(self.ip)
        #Entering Port
        self.add_widget(Label(text="Port:"))
        self.port = TextInput(text=saved_port,multiline=False)
        self.add_widget(self.port)
        #Entering Username
        self.add_widget(Label(text="Username:"))
        self.username = TextInput(text=saved_username,multiline=False)
        self.add_widget(self.username)
        #Join Button
        self.join = Button(text="Join")
        self.join.bind(on_press=self.join_button_action)
        self.add_widget(Label())
        self.add_widget(self.join)

    def join_button_action(self,instance):
    	port = self.port.text
    	ip = self.ip.text
    	username = self.username.text

    	with open("saved_details.txt", "w") as f:
    		f.write(f"{ip},{port},{username}")

    	info =f"Attempting to join {ip}:{port} as {username}"
    	chat_app.info_page.update_info(info)
    	chat_app.screen_manager.current= "Info"


class InfoPage(GridLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.cols=1
		self.message = Label(halign="center" , valign="middle", font_size =30)
		self.message.bind(width=self.update_text_width)
		self.add_widget(self.message)

	def update_info(self,message):
		self.message.text = message

	def update_text_width(self,*_):
		self.message.text_size = (self.message.width*0.9,None)





class MainApp(App):
    def build(self):
        self.screen_manager = ScreenManager()
        
        self.connect_page = ConnectPage()
        screen = Screen(name="Connect")
        screen.add_widget(self.connect_page)
        self.screen_manager.add_widget(screen)

        self.info_page = InfoPage()
        screen = Screen(name="Info")
        screen.add_widget(self.info_page)
        self.screen_manager.add_widget(screen)

        return self.screen_manager

if __name__ == "__main__":
    chat_app=MainApp()
    chat_app.run() 