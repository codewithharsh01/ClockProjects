from tkinter import * 
from time import strftime 
digital_clock = Tk()
digital_clock.geometry("600x300")
digital_clock.title('Digital Clock') 
def time():
    string = strftime('%H:%M:%S %p')  
    lable.config(text = string)
    lable.after(1000, time) 
lable = Label(digital_clock, font = ('calibri', 40, 'bold'),
            background = '#AA0000',
            foreground = 'white')
lable.pack(anchor = 'center')
time() 

mainloop()