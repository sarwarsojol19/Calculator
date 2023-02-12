from tkinter import *

class calculator:
    def __init__(self, root):
        self.root = root
        self.root.geometry("500x570+100+200")
        self.root.title("Simple Calculator")
        self.root.resizable(False,False)
        self.root.configure(bg="#17161b")
        
        
        self.var_cal_input = StringVar()
        
        #======display result======
    
        self.text_cal_input=Entry(root,textvariable=self.var_cal_input,font=("arial",30,"bold"),width=20,bd=10,relief=SUNKEN,state="readonly",justify=RIGHT)
        self.text_cal_input.place(x=15,y=5,)
        
        #====Calculatorrs Buttons====
        
        #====Row01====
        btn_clear=Button(root,text="C",font=("arial",25,"bold"),command=self.clear_cal,cursor="hand2",bd=5,width=5,height=1,bg="#3697f5",fg="#fff")
        btn_clear.place(x=10,y=100)
        
        btn_div=Button(root,text="/",font=("arial",25,"bold"),command=lambda:self.get_input('/'),cursor="hand2",bd=5,height=1,width=5,bg="#2a2d36",fg="#fff")
        btn_div.place(x=250,y=100)
        
        btn_mult=Button(root,text="*",font=("arial",25,"bold"),command=lambda:self.get_input('*'),cursor="hand2",bd=5,width=5,bg="#2a2d36",fg="#fff")
        btn_mult.place(x=370,y=100)
        
        #====Row02====
        
        btn_7=Button(root,text="7",font=("arial",25,"bold"),command=lambda:self.get_input(7),cursor="hand2",bd=5,width=5,height=1,bg="#2a2d36",fg="#fff")
        btn_7.place(x=10,y=180)
        
        btn_8=Button(root,text="8",font=("arial",25,"bold"),command=lambda:self.get_input(8),cursor="hand2",bd=5,width=5,height=1,bg="#2a2d36",fg="#fff")
        btn_8.place(x=130,y=180)
        
        btn_9=Button(root,text="9",font=("arial",25,"bold"),command=lambda:self.get_input(9),cursor="hand2",bd=5,width=5,height=1,bg="#2a2d36",fg="#fff")
        btn_9.place(x=250,y=180)
        
        btn_sub=Button(root,text="-",font=("arial",25,"bold"),command=lambda:self.get_input('-'),cursor="hand2",bd=5,width=5,bg="#2a2d36",fg="#fff")
        btn_sub.place(x=370,y=180)
        
        # #====Row03====
        
        # btn_5=Button(root,text="4",font=("arial",25,"bold"),command=lambda:self.get_input(4),cursor="hand2",bd=5,width=5,bg="#2a2d36",fg="#fff").grid(row=3,column=0)
        # btn_5=Button(root,text="5",font=("arial",25,"bold"),command=lambda:self.get_input(5),cursor="hand2",bd=5,width=5,bg="#2a2d36",fg="#fff").grid(row=3,column=1)
        # btn_6=Button(root,text="6",font=("arial",25,"bold"),command=lambda:self.get_input(6),cursor="hand2",bd=5,width=5,bg="#2a2d36",fg="#fff").grid(row=3,column=2)
        # btn_sub=Button(root,text="-",font=("arial",25,"bold"),command=lambda:self.get_input('-'),cursor="hand2",bd=5,width=5,bg="#2a2d36",fg="#fff").grid(row=3,column=3)
        
        # #====Row04====
        
        # btn_3=Button(root,text="3",font=("arial",25,"bold"),command=lambda:self.get_input(3),cursor="hand2",bd=5,width=5,bg="#2a2d36",fg="#fff").grid(row=4,column=0)
        # btn_2=Button(root,text="2",font=("arial",25,"bold"),command=lambda:self.get_input(2),cursor="hand2",bd=5,width=5,bg="#2a2d36",fg="#fff").grid(row=4,column=1)
        # btn_1=Button(root,text="1",font=("arial",25,"bold"),command=lambda:self.get_input(1),cursor="hand2",bd=5,width=5,bg="#2a2d36",fg="#fff").grid(row=4,column=2)
        
        
        # #====Row05====
        
        # btn_0=Button(root,text="0",font=("arial",25,"bold"),command=lambda:self.get_input(0),cursor="hand2",bd=5,width=10,bg="#2a2d36",fg="#fff",pady=16).grid(row=5, rowspan=2,column=0)
        # btn_eq=Button(root,text="=",font=("arial",25,"bold"),command=self.perform_cal,cursor="hand2",bd=5,width=5,bg="#fe9037",fg="#fff",pady=16).grid(row=5,column=2)
        # btn_sum=Button(root,text="+",font=("arial",25,"bold"),command=lambda:self.get_input('+'),cursor="hand2",bd=5,bg="#2a2d36",fg="#fff",width=5).grid(row=5,column=3)
        
    def get_input(self,num):
        xnum=self.var_cal_input.get()+str(num)
        self.var_cal_input.set(xnum)
        
    def clear_cal(self):
        self.var_cal_input.set('')
        
    def perform_cal(self):
        result=self.var_cal_input.get()
        self.var_cal_input.set(eval(result))
        
if __name__ == "__main__":
    root = Tk()
    obj = calculator(root)
    root.mainloop()