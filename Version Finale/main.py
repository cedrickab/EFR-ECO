
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
import mysql.connector as mysql
from kivy.uix.popup import Popup
from kivy.uix.label import Label




class FirstWindow(Screen):
    pass
class SecondWindow(Screen):
    pass
class ThirdWindow(Screen):
    def verify(self):
        con = mysql.connect(host = "localhost",user="root", password= "",database ="eco" )
        cur = con.cursor()
        user = self.ids["login"].text
        pswd = self.ids["passw"].text
        sql = 'SELECT IdUtilisateur,Password FROM utilisateur WHERE IdUtilisateur=%s AND Password=%s'
        val = [user,pswd]
        cur.execute(sql,val)
        if cur.fetchall():
            self.manager.current = "Accueil Membre"
        else:
            pop = Popup(title='Invalid Login',
                            content=Label(text='Invalid username or password.'),
                            size_hint=(None, None), 
                            size=(250, 100))

            pop.open()


class Second2Window(Screen):
    def soumettre(self):
        con = mysql.connect(host = "localhost",user="root", password= "",database ="eco" )
        cur = con.cursor()
        commentaire = self.ids["commentaire"].text
        sql = "INSERT INTO Commentaire  values(%s)"
        val = [commentaire]
        cur.execute(sql,val)
        con.commit()
        pop = Popup(title='Commentaire soumis',
                            content=Label(text='Commentaire envoyé dans la Base De Donnée.'),
                            size_hint=(None, None), 
                            size=(350, 150))

        pop.open()

    def change_screen(self, screen_name):
        screen_manager = self.root.ids['screen_manager']
        screen_manager.current = screen_name

class MainWindow(Screen):
    #id = commentaire
    def consulter(self):
        con = mysql.connect(host = "localhost",user="root", password= "",database ="eco" )
        cur = con.cursor()
        sql = 'SELECT * from commentaire'
        cur.execute(sql)
        a = cur.fetchall()
        #print(a)
        label = Label(text=str(a)) 
        print(label)
        pop = Popup(title='Commentaire soumis',
                            content=Label(text=str(a)),
                            size_hint=(None, None), 
                            size=(600, 200))

        pop.open()

class WindowManager(ScreenManager):
    pass
class MyLayout(Widget):
    pass

kv = Builder.load_file('fenetre.kv')

class EfrEco(App):
    def build(self):
        Window.clearcolor=(1,1,1,1)
        return kv


if __name__=='__main__':
    EfrEco().run()


