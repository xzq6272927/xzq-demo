"""开发记事本软件的菜单"""
import tkinter
from tkinter.filedialog import *
from tkinter.colorchooser import *
from tkinter import *
import codecs,chardet#设置编码格式
class Application(Frame):
    def __init__(self,master=None):
        super(Application,self).__init__(master)
        self.master=master
        self.pack()
        self.createWidget()
    def createWidget(self):
        #创建主菜单栏
        menubar=Menu(root)
        #创建子菜单
        menuFile=Menu(menubar)
        menuEdit=Menu(menubar)
        menuHelp=Menu(menubar)
        #将子菜单加入到主菜单栏
        menubar.add_cascade(label="新建(F)",menu=menuFile)
        menubar.add_cascade(label="编辑(E)",menu=menuEdit)
        menubar.add_cascade(label="帮助(H)",menu=menuHelp)
        #添加菜单项
        menuFile.add_command(label="新建",accelerator="ctrl+n",command=self.newfile)
        menuFile.add_command(label="打开",accelerator="ctrl+o",command=self.openfile)
        menuFile.add_command(label="保存",accelerator="ctrl+s",command=self.savefile)
        menuFile.add_separator()#添加分割线
        menuFile.add_command(label="退出",accelerator="ctrl+q",command=self.exit)
        #将主菜单栏加到根窗口
        root["menu"]=menubar
        root.bind("<Control-n>",lambda event:self.newfile())
        root.bind("<Control-o>",lambda event:self.openfile())
        root.bind("<Control-s>",lambda event:self.savefile())
        root.bind("<Control-q>",lambda event:self.exit())
        #创建快捷菜单
        self.menubars=Menu(root)
        self.menubars.add_command(label="背景颜色",command=self.openAskColor)
        menubarit=Menu(self.menubars,tearoff=0)
        menubarit.add_command(label="剪切")
        menubarit.add_command(label="复制")
        menubarit.add_command(label="粘贴")
        self.menubars.add_cascade(label="编辑",menu=menubarit)
        #文本编辑区
        self.pastext=Text(root,width=50,height=30)
        self.pastext.bind("<Button-3>",self.tests)
        self.pastext.pack()
    def tests(self,event):
        #菜单在鼠标右键单击的坐标处显示
        self.menubars.post(event.x_root,event.y_root)
    def openAskColor(self):
        f=askcolor(color="green",title="选择背景色")
        self.pastext.config(bg=f[1])
    def newfile(self):
        self.pastext.delete(1.0,END)
        self.filename=asksaveasfilename(title="另存为",initialfile="未命名.txt",filetypes=[("文本文件","*.txt")],defaultextension=".txt")
        print(self.filename)
        self.savefile()
    def openfile(self):
        self.pastext.delete(1.0,END)
        try:
            with codecs.open(askopenfilename(title="打开文件",filetypes=[("纯文本文件",".txt")]),"r",encoding="gbk") as f:
                self.pastext.insert(INSERT,f.read())
                self.filename=f.name
                print(f.name)
        except:
            with codecs.open(askopenfilename(title="打开文件",filetypes=[("纯文本文件",".txt")]),"r",encoding="utf-8") as f:
                self.pastext.insert(INSERT,f.read())
                self.filename=f.name
                print(f.name)
    def savefile(self):
        try:
            with open(self.filename,"w",encoding="utf-8") as f:
                text=self.pastext.get(1.0,END)
                f.write(text)
        except BaseException as e:
            print("无文件!")
    def exit(self):
        root.quit()
if __name__ == "__main__":
    root=Tk()
    root.geometry("400x400-300+300")
    root.title("记事本")
    app=Application(master=root)
    root.mainloop()