import tkinter as tk
from tkinter import filedialog
from tkinter import *
from tkinter.ttk import Combobox
import pandas as pd
import plotly
import numpy as np
from plotly.offline import iplot, init_notebook_mode
import plotly.graph_objects as go

def fOpen(): 
    print(filedialog.askopenfilename(initialdir = "/",title = "Open file",filetypes = (("Python files","*.py;*.pyw"),("All files","*.*"))))
def ExitF(): 
    window.destroy()
def fSave(): 
    print(filedialog.asksaveasfilename(initialdir = "/",title = "Save as",filetypes = (("Python files","*.py;*.pyw"),("All files","*.*"))))
def browse():
    print(filedialog.asksaveasfilename(initialdir = "/",title = "Browse",filetypes = (("Python files","*.py;*.pyw"),("All files","*.*"))))
    

window = tk.Tk()
window.title("MS(DS) Big Data Analytics")
window.configure(bg = "white")
window.geometry("1500x1500")


def configure_plotly_browser_state():
  import IPython
  display(IPython.core.display.HTML('''
        <script src="static/components/requirejs/require.js"></script>
        <script>
          requirejs.config({
            paths:{
              base:'/static/base',
              plotly:'https:cdn.plot.ly/plotly-1.5.1.min.js/noext'

            },
          });
         </script>
      
 ''' ))


### IMPORT FILES ASSIGNMENT 1

df = pd.read_csv('age_vs_user_activity_data.csv')

## TOP LABEL
photo1 = tk.PhotoImage(file='C:\\Users\\Haier\\Desktop\\SNAP.GIF', master=window)
img = tk.Label(window, image= photo1, width=1650, height=150,bg="#43d5c3", ) 
img.grid(row = 0, column = 0, columnspan = 2)



##RIGHT FRAME
frame = Frame(window, width=1000,height=1350,bg="white")
frame.grid(row= 1,column = 0, sticky = 'ne')


label2 = tk.Label(frame, text="Pokec social network", bg= "white", fg= "#3e679e", font= "none 22 bold") 
label2.grid(row = 1, column = 0)

label1 = tk.Label(frame, text= "\nPokec is the most popular on-line social network in Slovakia. \nThe popularity of network has not changed even after the coming of Facebook.\n Pokec has been provided for more than 10 years and connects more than 1.6 million people.\nDatasets contains anonymized data of the whole network.\n Profile data contains gender, age, hobbies, interest, education etc.\nProfile data are in Slovak language.\nFriendships in Pokec are oriented.", bg= "white", fg= "black" ,font= "none 12 ")
label1.grid(row = 2, column = 0) 

#DATASET PHOTO
photo2 = tk.PhotoImage(file='C:\\Users\\Haier\\Desktop\\Dataset.gif', master=window)
img = tk.Label(frame, image=photo2, width=400, height=350, bg= "white") 
img.grid(row = 3, column = 0)

##LEFT FRAME
frame2 = Frame(window, width=300,height=1350,bg="#3e679e")
frame2.grid(row= 1,column = 0, sticky = 'w')

#EDA WINDOW FUNCTION
def second_window():
    window2 = tk.Tk()
    window2.title("MS(DS) Big Data Analytics")
    window2.configure(bg = "white")
    window2.geometry("1500x1500")
    
    #TOP LABEL
    Top2 = tk.Label(window2, text="Exploratory Data Analysis".center(48), width=80, height=4,bg="#43d5c3" , font= "Ariel 20 bold") 
    Top2.grid(row = 0, column = 0, sticky = 'n')
    
    #FRAME LEFT
    frame2 = Frame(window2, width=320,height=1350,bg="#438a5d")
    frame2.grid(row= 1,column = 0, sticky = 'w')
    
    #DROPDOWN IN LEFT FRAME
    lab = tk.Label(frame2, text ="Select Visulization :",bg="#438a5d", font= "none 14 bold")
    lab.place(x=65, y=30)
    
    #COMBOBOX IN LEFT FRAME
    C1= Combobox(frame2, width= 25, height= 30, font= "none 13")
    C1['values'] = ('Active and Inactive Users', 'Spoken Languages Distribution' ,'Top 5 Languages Spoken ' )
    C1.current(0)
    C1.place(x=55, y= 65)
    
    #FRAME RIGHT
    frame22 = Frame(window2, width=1050,height=1350,bg="white")
    frame22.grid(row= 1,column = 0, sticky = 'e')
    
    
    
    def display_graph():
        data1 = C1.get()
        
        if data1 == "Active and Inactive Users":
            photo3 = tk.PhotoImage(file='C:\\Users\\Haier\\Desktop\\active.png', master = frame22)
            img1 = tk.Label(frame22, image=photo3) 
            img1.place(x= 20, y=40)
            
        if data1 == "Spoken Languages Distribution":
            photo4 = tk.PhotoImage(file='C:\\Users\\Haier\\Desktop\\s_lang.png', master = frame22)
            img2 = tk.Label(frame22, image=photo4) 
            img2.place(x= 20, y=40)
            
        if data1 == "Top 5 Languages Spoken ":
            photo5 = tk.PhotoImage(file='C:\\Users\\Haier\\Desktop\\5_lang.png', master = frame22)
            img3 = tk.Label(frame22, image=photo5) 
            img3.place(x= 20, y=40)
            

        
    
    ##Exploratory Data Analysis ##DISPLAY GRAPH BUTTON
    EDA_graph_Button = Button(frame2, text= 'Display Graph', bg="#438a5d", command = display_graph, font= "none 14 bold", width = 20)
    EDA_graph_Button.place(x=55, y=300)

   


##Exploratory Data Analysis Button
EDA_Button = Button(frame2, text= 'Exploratory Data Analysis', command= second_window, fg="#43d5c3", bg="#3e679e", font= "none 14 bold", width = 20)
EDA_Button.place(x= 35, y=30)


#EDA WINDOW FUNCTION
def third_window():
    window3 = tk.Tk()
    window3.title("MS(DS) Big Data Analytics")
    window3.configure(bg = "white")
    window3.geometry("1500x1500")
    
    #TOP LABEL
    Top3 = tk.Label(window3, text="Frequency Pattern Mining".center(48), width=80, height=4,bg="#43d5c3" , font= "Ariel 20 bold")
    Top3.grid(row = 0, column = 0, sticky = 'n')
    
    #FRAME LEFT
    frame2 = Frame(window3, width=320,height=1350,bg="#438a5d")
    frame2.grid(row= 1,column = 0, sticky = 'w')
    
    #DROPDOWN IN LEFT FRAME
    lab = tk.Label(frame2, text ="Select Visulization :",bg="#438a5d", font= "none 14 bold")
    lab.place(x=65, y=30)
    
    #COMBOBOX IN LEFT FRAME
    C1= Combobox(frame2, width= 25, height= 30, font= "none 13")
    C1['values'] = ('A Priori', 'PCY' ,'F P Growth ' )
    C1.current(0)
    C1.place(x=55, y= 65)
    
    
    #FRAME RIGHT
    frame23 = Frame(window3, width=1050,height=1350,bg="white")
    frame23.grid(row= 1,column = 0, sticky = 'e')
    
    def display_graph():
        data = C1.get()
        
        if data1 == "A Priori":
            photo3 = tk.PhotoImage(file='C:\\Users\\Haier\\Desktop\\Region.png', master = frame22)
            img1 = tk.Label(frame22, image=photo3) 
            img1.place(x= 20, y=40)
            
        if data1 == "PCY":
            photo4 = tk.PhotoImage(file='C:\\Users\\Haier\\Desktop\\s_lang.png', master = frame22)
            img2 = tk.Label(frame22, image=photo4) 
            img2.place(x= 20, y=40)
            
        if data1 == "F P Growth ":
            photo5 = tk.PhotoImage(file='C:\\Users\\Haier\\Desktop\\5_lang.png', master = frame22)
            img3 = tk.Label(frame22, image=photo5) 
            img3.place(x= 20, y=40)
        
        
        
    
    ##Frequency Pattern Mining's ##DISPLAY GRAPH BUTTON
    EDA_graph_Button = Button(frame2, text= 'Display Graph', bg="#438a5d", command = display_graph, font= "none 14 bold", width = 20)
    EDA_graph_Button.place(x=55, y=300)


    
#Frequency Pattern Mining button
FPM_Button = Button(frame2, text= 'Frequency Pattern Mining', command= third_window, fg="#43d5c3", bg="#3e679e", font= "Ariel 14 bold", width = 20)
FPM_Button.place(x=35, y=180)




window.mainloop()