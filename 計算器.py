# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import tkinter as tk
window=tk.Tk()
window.title("計算器")
window.geometry("300x300")
btn=tk.Button(window,text='0',height=2,width=25,fg='black',font=('標楷體',15))
btn.place(rely=0.13,relx=0.5,anchor='center')

btn=tk.Button(window,text='C',width=5,fg='blue',font=('標楷體',15))
btn.place(rely=0.3,relx=0.15,anchor='center')
btn=tk.Button(window,text='DEL',width=5,fg='black',font=('標楷體',15))
btn.place(rely=0.3,relx=0.38,anchor='center')
btn=tk.Button(window,text='%',width=5,fg='black',font=('標楷體',15))
btn.place(rely=0.3,relx=0.61,anchor='center')
btn=tk.Button(window,text='/',width=5,fg='black',font=('標楷體',15))
btn.place(rely=0.3,relx=0.84,anchor='center')

btn=tk.Button(window,text='7',width=5,fg='black',font=('標楷體',15))
btn.place(rely=0.45,relx=0.15,anchor='center')
btn=tk.Button(window,text='8',width=5,fg='black',font=('標楷體',15))
btn.place(rely=0.45,relx=0.38,anchor='center')
btn=tk.Button(window,text='9',width=5,fg='black',font=('標楷體',15))
btn.place(rely=0.45,relx=0.61,anchor='center')
btn=tk.Button(window,text='*',width=5,fg='black',font=('標楷體',15))
btn.place(rely=0.45,relx=0.84,anchor='center')

btn=tk.Button(window,text='4',width=5,fg='black',font=('標楷體',15))
btn.place(rely=0.6,relx=0.15,anchor='center')
btn=tk.Button(window,text='5',width=5,fg='black',font=('標楷體',15))
btn.place(rely=0.6,relx=0.38,anchor='center')
btn=tk.Button(window,text='6',width=5,fg='black',font=('標楷體',15))
btn.place(rely=0.6,relx=0.61,anchor='center')
btn=tk.Button(window,text='-',width=5,fg='black',font=('標楷體',15))
btn.place(rely=0.6,relx=0.84,anchor='center')

btn=tk.Button(window,text='1',width=5,fg='black',font=('標楷體',15))
btn.place(rely=0.75,relx=0.15,anchor='center')
btn=tk.Button(window,text='2',width=5,fg='black',font=('標楷體',15))
btn.place(rely=0.75,relx=0.38,anchor='center')
btn=tk.Button(window,text='3',width=5,fg='black',font=('標楷體',15))
btn.place(rely=0.75,relx=0.61,anchor='center')
btn=tk.Button(window,text='+',width=5,fg='black',font=('標楷體',15))
btn.place(rely=0.75,relx=0.84,anchor='center')

btn=tk.Button(window,text='0',width=12,fg='black',font=('標楷體',15))
btn.place(rely=0.9,relx=0.26,anchor='center')

btn=tk.Button(window,text='.',width=5,fg='black',font=('標楷體',15))
btn.place(rely=0.9,relx=0.61,anchor='center')
btn=tk.Button(window,text='=',width=5,bg='yellow',fg='black',font=('標楷體',15))
btn.place(rely=0.9,relx=0.84,anchor='center')

window.mainloop()
