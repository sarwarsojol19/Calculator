from tkinter import *

class calculator:
    def __init__(self, root):
        self.root = root
        self.root.geometry("600x550+100+200")
        self.root.title("Simple Calculator")
        self.root.resizable(False,False)
        self.root.configure(bg="#17161b")
        
        
        self.var_cal_input = StringVar()
        
        #======display result======
    
        self.text_cal_input=Entry(root,textvariable=self.var_cal_input,font=("arial",30,"bold"),width=25,bd=10,relief=SUNKEN,state="readonly",justify=RIGHT)
        self.text_cal_input.grid(row=0,columnspan=4,padx=10,pady=10)
        
        #====Calculatorrs Buttons====
        
        #====Row01====
        
        btn_7=Button(root,text="7",font=("arial",30,"bold"),command=lambda:self.get_input(7),cursor="hand2",bd=5,width=5,pady=10).grid(row=1,column=0)
        btn_8=Button(root,text="8",font=("arial",30,"bold"),command=lambda:self.get_input(8),cursor="hand2",bd=5,width=5,pady=10).grid(row=1,column=1)
        btn_9=Button(root,text="9",font=("arial",30,"bold"),command=lambda:self.get_input(9),cursor="hand2",bd=5,width=5,pady=10).grid(row=1,column=2)
        btn_sum=Button(root,text="+",font=("arial",30,"bold"),command=lambda:self.get_input('+'),cursor="hand2",bd=5,width=5,pady=10).grid(row=1,column=3)
        
        #====Row02====
        
        btn_5=Button(root,text="4",font=("arial",30,"bold"),command=lambda:self.get_input(4),cursor="hand2",bd=5,width=5,pady=10).grid(row=2,column=0)
        btn_5=Button(root,text="5",font=("arial",30,"bold"),command=lambda:self.get_input(5),cursor="hand2",bd=5,width=5,pady=10).grid(row=2,column=1)
        btn_6=Button(root,text="6",font=("arial",30,"bold"),command=lambda:self.get_input(6),cursor="hand2",bd=5,width=5,pady=10).grid(row=2,column=2)
        btn_sub=Button(root,text="-",font=("arial",30,"bold"),command=lambda:self.get_input('-'),cursor="hand2",bd=5,width=5,pady=10).grid(row=2,column=3)
        
        #====Row03====
        
        btn_3=Button(root,text="3",font=("arial",30,"bold"),command=lambda:self.get_input(3),cursor="hand2",bd=5,width=5,pady=10).grid(row=3,column=0)
        btn_2=Button(root,text="2",font=("arial",30,"bold"),command=lambda:self.get_input(2),cursor="hand2",bd=5,width=5,pady=10).grid(row=3,column=1)
        btn_1=Button(root,text="1",font=("arial",30,"bold"),command=lambda:self.get_input(1),cursor="hand2",bd=5,width=5,pady=10).grid(row=3,column=2)
        btn_mul=Button(root,text="*",font=("arial",30,"bold"),command=lambda:self.get_input('*'),cursor="hand2",bd=5,width=5,pady=10).grid(row=3,column=3)
        
        #====Row04====
        
        btn_0=Button(root,text="0",font=("arial",30,"bold"),command=lambda:self.get_input(0),cursor="hand2",bd=5,width=5,pady=16).grid(row=4,column=0)
        btn_c=Button(root,text="C",font=("arial",30,"bold"),command=self.clear_cal,cursor="hand2",bg="#3697f5",bd=5,width=5,pady=16).grid(row=4,column=1)
        btn_eq=Button(root,text="=",font=("arial",30,"bold"),command=self.perform_cal,cursor="hand2",bd=5,width=5,pady=16).grid(row=4,column=2)
        btn_div=Button(root,text="/",font=("arial",30,"bold"),command=lambda:self.get_input('/'),cursor="hand2",bd=5,width=5,pady=16).grid(row=4,column=3)
        
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