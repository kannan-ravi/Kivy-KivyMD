# Calculator Designed in Python(Kivy) by Kannan Ravindran

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput


	
class MainLayout(Widget):
	def button_clear(self):
		self.ids.text_input.text= '0'
	
	def decimal_dot(self):
		previous= self.ids.text_input.text
		plus= previous.split('+')
		minus = plus[-1].split('-')
		multiply = minus[-1].split('x')
		divide = multiply[-1].split('÷')
		
		
		if '.' not in divide[-1]:
			previous= f'{previous}.'
			self.ids.text_input.text = previous
		elif '.' in previous:
			pass
		else:
			previous= f'{previous}.'
			self.ids.text_input.text = previous
	
			
	def button_delete(self):
		previous= self.ids.text_input.text
		previous= previous[:-1]
		self.ids.text_input.text = previous
		
	
	
	def button_plus_minus(self):
		previous= self.ids.text_input.text
		if '-' in previous:
			previous = previous.replace('-','')
			self.ids.text_input.text = f'{previous}'
		else:
			self.ids.text_input.text= f'-{previous}'
	
	def button_click(self, number):
		previous= self.ids.text_input.text
		
			
		if previous == '0' or previous == "Can't do that for you":
			self.ids.text_input.text = ''
			self.ids.text_input.text = f'{number}'
		else:
			self.ids.text_input.text = f'{previous}{number}'
		
	def button_clicks(self, symbol):
		previous= self.ids.text_input.text
		text_input_list= list(previous)
		
		if '+' == str(text_input_list[-1]):
			pass
		elif '-' == str(text_input_list[-1]):
			pass
		elif 'xx' == ''.join(text_input_list[-2:]):
			pass
		elif '÷÷' == ''.join(text_input_list[-2:]):
			pass
			
		else:
			self.ids.text_input.text= f'{previous}{symbol}'
	
	def button_equal(self):
		previous= self.ids.text_input.text
		if 'x' in previous:
			previous= previous.replace('x', '*')
		elif "÷" in previous:
			previous= previous.replace('÷', '/')
		try:
			solution= eval(previous)
			self.ids.text_input.text = f'{solution}'
		except:
			self.ids.text_input.text = "Can't do that for you"
		
class Simple_CalculatorApp(App):
	pass
	
Simple_CalculatorApp().run()
