import tkinter as tk
import tkinter.ttk as ttk
import autoCarClass

class GUI():
    def __init__(self):
        super(GUI, self).__init__()
        text_font = ('Helvetica', '20', 'bold')
        window = tk.Tk()
        window.title('Computational Intelligence_HW1_Auto Car')
        window.geometry('660x600')
        window.configure(background='#364862')

        btn_frame = tk.Frame(window)
        btn_frame.pack(pady=120)
        btn_frame.configure(background='#364862')
        btn1 = tk.Button(btn_frame, text='case01', activebackground='#2887D8', activeforeground='#FFFFFF'
            , font=text_font, width=12, height=1, command=self.leftbtn, bg='#5BBAFA', fg='#FFFFFF')
        btn1.grid(row=0, column=0, padx=20)

        btn2 = tk.Button(btn_frame, text='case02', activebackground='#C0910D', activeforeground='#FFFFFF'
            , font=text_font, width=12, height=1, command=self.righttbn, bg='#F2C40F', fg='#FFFFFF')
        btn2.grid(row=0, column=1, padx=20)
        # btn_frame, btn1, btn2

        

        S = tk.Scrollbar(window)
        self.T = tk.Text(window, height=4, width=92)
        S.pack(side=tk.RIGHT, fill=tk.Y)
        self.T.pack(side=tk.LEFT, fill=tk.Y)
        S.config(command=self.T.yview)
        self.T.config(yscrollcommand=S.set)

        window.mainloop()


    def leftbtn(self):
        car1 = autoCarClass.autoCar()
        car1.loadMap(filename = 'case01.txt')
        car1.run()
        l, f, r = car1.retResultLFR()
        str = 'left Dist     front Dist     right Dist\n'
        for i in range(len(l)):
            str += '{:9.2f}      {:9.2f}      {:9.2f}\n'.format(l[i], f[i], r[i])
        self.T.insert(tk.END, str)
        car1.draw()
        car1.saveResult()
    
    def righttbn(self):
            car1 = autoCarClass.autoCar()
            car1.loadMap(filename = 'case02.txt')
            car1.run()
            l, f, r = car1.retResultLFR()
            str = 'left Dist     front Dist     right Dist\n'
            for i in range(len(l)):
                str += '{:9.2f}      {:9.2f}      {:9.2f}\n'.format(l[i], f[i], r[i])
            self.T.insert(tk.END, str)
            car1.draw()
            car1.saveResult()

def temp():
    text_font = ('Helvetica', '20', 'bold')
    window = tk.Tk()
    window.title('Computational Intelligence_HW1_Auto Car')
    window.geometry('660x600')
    window.configure(background='#364862')

    btn_frame = tk.Frame(window)
    btn_frame.pack(pady=120)
    btn_frame.configure(background='#364862')
    btn1 = tk.Button(btn_frame, text='case01', activebackground='#2887D8', activeforeground='#FFFFFF'
        , font=text_font, width=12, height=1, command=leftbtn, bg='#5BBAFA', fg='#FFFFFF')
    btn1.grid(row=0, column=0, padx=20)

    btn2 = tk.Button(btn_frame, text='case02', activebackground='#C0910D', activeforeground='#FFFFFF'
        , font=text_font, width=12, height=1, command=righttbn, bg='#F2C40F', fg='#FFFFFF')
    btn2.grid(row=0, column=1, padx=20)
    # btn_frame, btn1, btn2

    

    S = tk.Scrollbar(window)
    T = tk.Text(window, height=4, width=92)
    S.pack(side=tk.RIGHT, fill=tk.Y)
    T.pack(side=tk.LEFT, fill=tk.Y)
    S.config(command=T.yview)
    T.config(yscrollcommand=S.set)

    window.mainloop()

if __name__ == '__main__':
    g = GUI()
