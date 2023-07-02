from tkinter import *







root =Tk()
root.geometry('600x450')
picture=PhotoImage(file="screenshot.png")#必须是真正的gif图片，改变图片的格式改不了图片的本质，无法运行
label3=Label(root,text='图片',image=picture,compound='left',relief=SUNKEN)
label3.grid(row=2,column=5)
entry=Entry(root,fg='blue',bg='pink',width=20,bd=4)
entry.grid()
entry.insert(1, 'Hello, World!')
def hit():
    print(entry.get())
button=Button(root,text='点击',width=12,height=2,command=hit)
button.grid()
root.mainloop()
