from kivy.app import App
from kivy.config import Config
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.graphics import (Color,Rectangle,Ellipse)
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.animation import Animation
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.core.audio import SoundLoader
from kivy.clock import Clock
from kivy.uix.modalview import ModalView
from kivy.uix.textinput import TextInput

import webbrowser
import urllib.request
from bs4 import BeautifulSoup

Builder.load_string('''
<Main>:
	anima: (1,1,1,0)

	canvas:
		
		Rectangle:
			size:self.size
			pos:self.pos
			source:"Static/1.jpg"

		Color:
			rgba:self.anima
		Rectangle:
			size:self.size
			pos:self.pos
			source:"Static/2.jpg"

	orientation: "vertical"
	spacing: 0
	padding: [0,10,0,0]

<Kino>:
	angle:0
	canvas.before:
		PushMatrix
		Rotate:
			angle:self.angle			
			origin: root.center
	canvas.after:
		PopMatrix
		
'''	)
#Глобальные перменные 
click = SoundLoader.load("Static/1.ogg")
click.volume = 0.6

isWiFi = True;
MainBallance = ""
MainDogovor = ""
MainTarif = ""
Pay = ""
MainLogin = ""
MainPassword = ""

#Виджеты

class Butt (ButtonBehavior,Image):
	def __init__(self,**kwargs):
		super().__init__(**kwargs)		
		with self.canvas:
			self.source="Static/but.png"					
			self.pos_hint = {'center_x':0.5,'center_y':1}
			self.size_hint = 0.8,0.6
			

class Butt2 (ButtonBehavior,Image):
	def __init__ (self,**kwargs):
		super().__init__(**kwargs)
		with self.canvas:
			self.source="Static/but2.png"			
			self.pos_hint = {'center_x':0.5,'center_y':1}
			self.size_hint = 0.8,0.6

class Butt3 (Butt2):
	def __init__ (self,**kwargs):
		super().__init__(**kwargs)
		with self.canvas:
				self.source="Static/but5.png"



class Kino (ButtonBehavior,Image):
	def __init__ (self,**kwargs):
		super().__init__(**kwargs)
		with self.canvas:
			self.pos_hint = {'center_x':0.5,'center_y':0.5}
			self.size_hint = 0.7,0.7
			self.source = "Static/kino.png"						
							
class Lab (Label):
	def __init__(self,**kwargs):
		super().__init__(**kwargs)
		global balance
		with self.canvas:
			self.halign = "center"
			self.markup = True
			self.color = 0.19, 0.20, 0.17, 1			
			self.font_size ="25sp"
			self.pos_hint = {'center_x':0.5,'center_y':0.1}
			self.font_name = "Static/1.ttf"
			self.anim = Animation (x = 0, y =300, duration = 1)

	def Ballance (self):
		if isWiFi == True:
			try:
				temp = "http://gorodok1.ru"
				full = urllib.request.urlopen(temp).read()
				soup = BeautifulSoup(full,"html.parser")
				convert = soup.findAll ('div',{'class':'ballance_ip'})
				ballance = convert[0].text.replace("<div class=\"ballance_ip\"></div>","")

				ballance2 = convert[2].text
				ballance3 = convert[1].text			
				schet = convert[2].text.replace("\n","")
				schet2 = schet.replace("ЛИЦЕВОЙ СЧЕТ","")
				return "Ваш баланс: [size=30sp][color=#3c1f52]" + ballance + "[/size][/color]\n   Ваш лицевой счет:[size=30sp][color=#3c1f52] " + ballance2 + "[/size][/color] \
				\nВаш тариф: [size=30sp][color=#3c1f52]" + ballance3[3:] + "[/size][/color] "
		
			except Exception:
				return "Ошибка"
		elif isWiFi == False:
			try:
				ballance = MainBallance
				ballance2 = MainDogovor
				ballance3 = MainTarif

				return "Ваш баланс: [size=30sp][color=#3c1f52]" + ballance + "[/size][/color]\n   Ваш лицевой счет:[size=30sp][color=#3c1f52] " + ballance2 + "[/size][/color] \
				\nВаш тариф: [size=30sp][color=#3c1f52]" + ballance3 + "[/size][/color] "
		
			except Exception:
				return "Ошибка"

class Logo(ButtonBehavior,Image):
	def __init__ (self,*args,**kwargs):
		super().__init__(**kwargs)
		self.source = "Static/gor.png"
		self.size_hint = [1,1]
		self.pos_hint = {'center_x':0.5,'center_y':0.5}

class LogoShadow(ButtonBehavior,Image):
	def __init__ (self,*args,**kwargs):
		super().__init__(**kwargs)
		self.source = "Static/gor2.png"
		self.color = [1,1,1,0]
		self.size_hint = 1,1
		self.pos_hint = {'center_x':0.5,'center_y':0.5}
		

class Logo2(Image):
	def __init__ (self,*args,**kwargs):
		super().__init__(**kwargs)
		self.source = "Static/tel.png"
		self.size_hint = 1,1

class Logo3(Image):
	def __init__ (self,*args,**kwargs):
		super().__init__(**kwargs)
		self.source = "Static/whats.png"
		self.size_hint = 1,1

class Background (Image):
	def __init__ (self,**kwargs):
		super().__init__(**kwargs)
		self.source = "Static/2.jpg"

class Main (BoxLayout):
	def __init__ (self,**kwargs):
		super().__init__ (**kwargs)
	
		self.butt = Butt()
		self.butt2 = Butt2()
		self.butt3 = Butt3()
		self.lab = Lab()
		self.logo = Logo()
		self.logoSh = LogoShadow()
		self.tel = Logo2()
		self.whats = Logo3()
		self.back = Background()
		self.kino = Kino()
		
												
# Слой с логотипом вверху
		FloatLogo = FloatLayout(size_hint=[1,0.7],pos_hint = {'center_x':0.5,'center_y':0.5})
		FloatLogo.add_widget(self.logo)
		FloatLogo.add_widget(self.logoSh)
		self.add_widget(FloatLogo)

# Слой с кнопками
		BoxButton = BoxLayout(size_hint=[1,1],pos_hint = {'center_x':0.5,'center_y':0.5},padding=[0,-50,0,0],orientation="vertical",spacing= -50)		
		BoxButton.add_widget(self.butt)
		BoxButton.add_widget(self.butt2)
		BoxButton.add_widget(self.butt3)
		self.add_widget(BoxButton)

# Вывод баланса
		
		self.add_widget(self.lab)

# Слой с телефонами внизу
		KinoLayout = FloatLayout(size_hint=[1,1],pos_hint = {'center_x':0.5,'center_y':0.5})
		KinoLayout.add_widget(self.kino)		
		
		GridTele = GridLayout(cols=3,size_hint=[1,0.6],pos_hint = {'center_x':0.5,'center_y':0.1})
		GridTele.add_widget(self.tel)
		GridTele.add_widget(KinoLayout)
		GridTele.add_widget(self.whats)	
		self.add_widget(GridTele)
		
		self.butt.bind(on_press = self.press)
		self.butt.bind(on_release = self.release)
		self.butt2.bind (on_press = self.press2)
		self.butt2.bind (on_release = self.oplata)
		self.butt3.bind (on_press = self.press3)
		self.butt3.bind (on_release = self.kabinet)
		self.kino.bind (on_press = self.press4)
		self.kino.bind (on_release = self.Kinozal)
		self.logoSh.bind (on_press=self.press5)
		self.logoSh.bind (on_release=self.site)

			
# Обработка нажатий на кнопки
	def press(self,instance):		
		click.play()
		self.butt.source="Static/but3.png"

	def press2 (self,instance):
		click.play()
		self.butt2.source="Static/but4.png"

	def press3 (self,instance):
		click.play()
		self.butt3.source="Static/but6.png"

	def press4 (self,instance):
		click.play()
		self.kino.source="Static/kino2.png"

	def press5 (self,instance):
		click.play()
		self.logoSh.source="Static/logoclick.png"

# Узнать баланс
	def release (self,value):
		self.butt.source="Static/but.png"
		self.lab.text = self.lab.Ballance();
		self.lab.anim.start(self.lab)
# Оплата			
	def oplata (self,value):
		if isWiFi == True:
			self.butt2.source="Static/but2.png"
			webbrowser.open_new ("http://www.gorodok1.ru/pay.php")
		elif isWiFi == False:
			self.butt2.source="Static/but2.png"
			webbrowser.open_new ("http://www.gorodok1.ru/pay.php")


# Кинозал
	def Kinozal (self,value):
		self.kino.source="Static/kino.png"
		webbrowser.open_new ("http://kino2.gorodok1.ru/")

	def site (self,value):
		self.logoSh.source = "Static/gor2.png"
		webbrowser.open_new ("http://www.gorodok1.ru/")

# Личный кабинет 
	def kabinet (self,value):
		self.butt3.source = "Static/but5.png"
		
# Узнаем номер догоовра через сайт
		if isWiFi == True:
			try: 
				temp = "http://gorodok1.ru"
				full = urllib.request.urlopen(temp).read()
				soup = BeautifulSoup(full,"html.parser")
				convert = soup.findAll ('div',{'class':'ballance_ip'})
				ballance = convert[2].text.replace("<div class=\"ballance_ip\"></div>","")
# Находим пользователя по номеру договора и получаем информацию о нем 
				url = "http://10.0.0.17:1444/api.php?cmd=execute&proc=CLN_AUTH_LOGIN&arg1=dude&arg2=dude&arg3=0"
				urlopen = urllib.request.urlopen (url)
				soup = BeautifulSoup(urlopen,'html.parser')
				sess = soup.find_all('suid')
				suid = sess[0].text.replace("suid","")

				url2 = "http://10.0.0.17:1444/api.php?cmd=execute&proc=CLN_USR_FIND_2&arg1="+suid +"&arg2=null&arg3=null&arg4=null&arg5=null&arg6=null&arg7=null&arg8=null&arg9=null&arg10=null&arg11=null&arg12=null&arg13=null&arg14&arg15=null&arg16=null&arg17=null&arg18="+ballance+ "&arg19=null&arg20=null&arg21=null&arg22=null&arg23=null&arg24=null"
				urlopen2 = urllib.request.urlopen (url2)
				soup2 = BeautifulSoup(urlopen2,'html.parser')
				sess2 = soup2.find_all('id')
				Id = sess2[0].text.replace("id","")

				url3 = "http://10.0.0.17:1444/api.php?login=dude&password=dude&cmd=execute&proc=CLN_USR_GET&arg1=" + suid+ "&arg2=" + Id
				urlopen3 = urllib.request.urlopen(url3)
				soup3 = BeautifulSoup (urlopen3,'html.parser')
				sess3 = soup3.find_all('login')
				sess4 = soup3.find_all('gen_pwd')
				login = sess3[0].text.replace("login","")
				password = sess4[0].text.replace("gen_pwd","")

				url4 = "https://10.0.0.17/login.php?login="+login+"&password="+password
				webbrowser.open_new (url4)
			except Exception:
				self.lab.text = "Ошибка"
		elif isWiFi == False:
			try:				
				url4 = "https://31.148.3.2/login.php?login="+MainLogin+"&password="+MainPassword
				webbrowser.open_new (url4)
			except Exception:
				self.lab.text = "Ошибка"
		
# Анимация логотипа
	def AnimLogo (self,dt):
		anim = Animation (color=[1,1,1,1], duration=5) + Animation(color=[1,1,1,0], duration=5)		
		anim.start(self.logoSh)

# Анимация фона
	def AnimBack (self,dt):
		anim = Animation(anima=(1,1,1,0.2),duration=10) + Animation(anima=(1,1,1,0),duration=15)
		anim.start(self)
# Анимация иконки кинозала	
	def AnimKino (self,dt):
		anim = Animation (angle = 10, duration=10) + Animation(angle=-10,duration=10)
		anim.start(self.kino)
			
class GorodokApp (App):
# Перменные для окна при старте если подключение через мобильный интернет

	Logo = Image(source="Static/gor.png",pos_hint = {'center_x':0.5,'center_y':0.85})
	
	LoginMes = Label(text="Логин: ",halign = "center",color = [0.19, 0.20, 0.17, 1],font_size ="25sp",
	pos_hint = {'center_x':0.5,'center_y':0.75},font_name = "Static/1.ttf")
	
	PassMes = Label(text="Пароль: ",halign = "center",color = [0.19, 0.20, 0.17, 1],font_size ="25sp",
	pos_hint = {'center_x':0.5,'center_y':0.55},font_name = "Static/1.ttf")
	
	LoginTXT = TextInput(size_hint=(0.7,0.08), pos_hint = {'center_x':0.5,'center_y':0.65}, halign="center", multiline=False)
	
	PassTXT = TextInput(size_hint=(0.7,0.08), pos_hint = {'center_x':0.5,'center_y':0.45}, halign="center", multiline=False)
	
	Button = Button (size_hint=(0.5,0.08), pos_hint= {'center_x':0.5,'center_y':0.33},text="Войти",font_name = "Static/1.ttf",background_normal="", background_color=[0,0.40,0.69,1],font_size="25sp"  )
	
	Error = Label(text="",halign = "center",color = [0.19, 0.20, 0.17, 1],font_size ="25sp",
	pos_hint = {'center_x':0.5,'center_y':0.23},font_name = "Static/1.ttf")

	Tel = Image(source="Static/tel.png", pos_hint={'center_x': 0.5, 'center_y' : 0.13}, size_hint=[1,1])

	view = ModalView(size_hint=(1,1), background = "Static/1.jpg", auto_dismiss=False)

# Окно авторизации 	
	def on_start(self):
		global isWiFi
		try:
			temp = "http://gorodok1.ru"
			full = urllib.request.urlopen(temp).read()
			soup = BeautifulSoup(full,"html.parser")
			convert = soup.findAll ('div',{'class':'ballance_ip'})
			ballance = convert[0].text.replace("<div class=\"ballance_ip\"></div>","")

			ballance2 = convert[2].text
			ballance3 = convert[1].text			
			schet = convert[2].text.replace("\n","")
			schet2 = schet.replace("ЛИЦЕВОЙ СЧЕТ","")
			return ballance2			
			
		except:			
			isWiFi = False;
			

		if isWiFi==False:			
			Box = FloatLayout()
			But = self.Button
			Tel = self.Tel
						
			But.bind(on_release=self.enter)

			Box.add_widget(self.Logo)
			Box.add_widget(self.LoginMes)
			Box.add_widget(self.LoginTXT)
			Box.add_widget(self.PassMes)
			Box.add_widget(self.PassTXT)
			Box.add_widget(But)
			Box.add_widget(self.Error)
			Box.add_widget(Tel)

			self.view.add_widget(Box)			
			self.view.open()

# Функция авторизации
	def enter(self,value):
		try:
			global MainLogin
			global MainPassword
			Log = self.LoginTXT
			Pas = self.PassTXT
			Error = self.Error
			Login = Log.text
			MainLogin = Login
			Password = Pas.text
			MainPassword = Password

			url = "http://31.148.3.2:1444/api.php?cmd=execute&proc=CLN_AUTH_LOGIN&arg1=dude&arg2=dude&arg3=0"
			urlopen = urllib.request.urlopen (url)
			soup = BeautifulSoup(urlopen,'html.parser')
			sess = soup.find_all('suid')
			suid = sess[0].text.replace("suid","")

			url2 = "http://31.148.3.2:1444/api.php?cmd=execute&proc=CLN_USR_FIND_2&arg1="+suid +"&arg2=null&arg3="+Login+"&arg4=null&arg5=null&arg6=null&arg7=null&arg8=null&arg9=null&arg10=null&arg11=null&arg12=null&arg13=null&arg14&arg15=null&arg16=null&arg17=null&arg18=null&arg19=null&arg20=null&arg21=null&arg22=null&arg23=null&arg24=null"
			urlopen2 = urllib.request.urlopen (url2)
			soup2 = BeautifulSoup(urlopen2,'html.parser')
			sess2 = soup2.find_all('id')
			Id = sess2[0].text.replace("id","")

			url3 = "http://31.148.3.2:1444/api.php?login=dude&password=dude&cmd=execute&proc=CLN_USR_GET&arg1=" + suid+ "&arg2=" + Id
			urlopen3 = urllib.request.urlopen(url3)
			soup3 = BeautifulSoup (urlopen3,'html.parser')
			dog = soup3.find_all('contract_number')
			bal = soup3.find_all('balance')
			tar = soup3.find_all('tarif_txt')
			tar2 = tar[0].text
			pas = soup3.find_all('gen_pwd')
			payment = soup3.find_all('abonent_pay')

			password = pas[0].text
			dogovor = dog[0].text
			balance = bal[0].text
			tarif = tar2[3:]
			pay = payment[0].text

			global MainBallance 
			global MainDogovor 
			global MainTarif
			global Pay 	

			MainBallance = balance
			MainDogovor = dogovor
			MainTarif = tarif
			Pay = pay				

			if password != Password:
				Error.text = "Неверный Логин или Пароль!"
				Log.text = ""
				Pas.text = ""
			elif password == Password: 
				self.view.dismiss()
									
		except:
			Error.text = "Ошибка"

	def build (self):
		self.icon = "Static/oppa.png"							
		main = Main()
		main.AnimLogo(0)
		main.AnimBack(0)
		main.AnimKino(0)	
		Clock.schedule_interval(main.AnimLogo,10)
		Clock.schedule_interval(main.AnimBack,25)
		Clock.schedule_interval(main.AnimKino,20)
	
		return main
if __name__ == "__main__":
	GorodokApp().run() 
