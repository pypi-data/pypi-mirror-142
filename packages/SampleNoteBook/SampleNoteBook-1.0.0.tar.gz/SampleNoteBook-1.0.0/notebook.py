'''利用Menu创建一个记事本程序'''

from datetime import datetime
from sqlite3 import Date
import time
from tkinter import *
from tkinter import messagebox
from tkinter.colorchooser import askcolor
from tkinter.filedialog import askopenfile, askopenfilename, asksaveasfile
import webbrowser
from xmlrpc.client import DateTime

class Application(Frame):
    def __init__(self,master=None):
        super().__init__(master);
        self.master=master
        self.newFile=TRUE            #给是否新建的文档定义一个变量
        self.pack()
        
        self.createWidget()
        
    #新建文件  
    def addFile(self):
       self.text.delete('1.0',END)     #每次打开都先清除文字
       self.master.title('无标题文档')
    
    #打开文件
    def openFile(self): 
        with askopenfile(title='选择文件',initialdir='C',filetypes=[('Text Files','*txt')]) as f:
            self.text.delete('1.0',END)     #每次打开都先清除文字
            self.text.insert(INSERT,f.read())  #插入文件
            self.filename=f.name
            ff= f.name.split('/')              #分割文件名
            self.master.title(ff[-1])          #修改打开窗口标题
            self.newFile=False
    
    #保存文件      
    def saveFile(self):
        if(self.newFile==False):
            with open(self.filename,'w') as f:
               f.write(self.text.get('1.0',END))
        else: 
            with asksaveasfile(title='保存文件',initialdir='C',initialfile='无标题文档.txt',filetypes=[('text file','*txt')]) as f:
                self.filename=f.name
                ff= f.name.split('/')              #分割文件名
                self.master.title(ff[-1])          #修改打开窗口标题
                self.newFile=False
                self.saveFile()
        
    #退出窗口
    def exitFile(self):
        self.master.destroy()                #关闭主窗口
    
    #改变背景色
    def changeMeun(self,event):
        self.zimenu=Menu(self.menubar,tearoff='off')
        self.zimenu.add_command(label='更换背景颜色',command=self.changeBG)
        self.zimenu.add_command(label='粘贴',command=self.changeBG)
        self.zimenu.add_command(label='全选（A）',command=self.changeBG)
        self.zimenu.post(event.x_root,event.y_root)
    
    #改变背景色    
    def changeBG(self):
        self.bgc=askcolor(title='选择颜色',color='gray')
        self.text.config(bg=self.bgc[1])
     
    #得到当前的事件并输出到当前文档上   
    def getDate(self):
        self.nowTimeText=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
        self.text.insert(END,self.nowTimeText)
        
    #查看帮助    
    def lookHelp(self):
       url = 'www.baidu.com'
       webbrowser.open_new_tab(url)  #打开网址
       
    #关于记事本
    def aboutText(self):
        messagebox.showinfo('关于记事本','当前记事本版本号为:v 1.0.0')
        
    #创建组件
    def createWidget(self):
        #导入菜单模块模板
        self.menubar=Menu(root)
        
        #创建文件模块子菜单
        self.filebar=Menu(self.menubar,tearoff='FALSE')  
        self.filebar.add_command(label='新建(N)',accelerator='Ctrl+N',command=self.addFile)
        self.filebar.add_command(label='打开(N)',accelerator='Ctrl+O',command=self.openFile)
        self.filebar.add_command(label='保存(N)',accelerator='Ctrl+S',command=self.saveFile)
        self.filebar.add_separator()
        self.filebar.add_command(label='退出(X)',command=self.exitFile)
        
        #创建格式子菜单
        self.editbar=Menu(self.menubar,tearoff='off')
        self.editbar.add_command(label='时间/日期(D)',accelerator='F5',command=self.getDate)
        self.editbar.add_separator()
        self.editbar.add_command(label='复制(C)')
        self.editbar.add_command(label='粘贴(P)')
        self.editbar.add_command(label='删除(L)')
        self.editbar.add_command(label='剪切(T)')
        
        #创建格式子菜单
        self.gebar=Menu(self.menubar,tearoff='off')
        self.gebar.add_command(label='自动换行(W)')
        self.gebar.add_command(label='字体(F)...')
        
        #创建查看子菜单
        self.viewbar=Menu(self.menubar,tearoff='off')
        self.viewbar.add_command(label='状态栏(S)')
        
        #创建帮助子菜单
        self.helpbar=Menu(self.menubar,tearoff='off')
        self.helpbar.add_command(label='查看帮助(H)',command=self.lookHelp)
        self.helpbar.add_command(label='关于记事本(A)',command=self.aboutText)
        
        
        #创建主菜单
        self.menubar.add_cascade(label='文件(F)',menu=self.filebar)   #利用cascade绑定子菜单
        self.menubar.add_cascade(label='编辑(E)',menu=self.editbar)
        self.menubar.add_cascade(label='格式(O)',menu=self.gebar)
        self.menubar.add_cascade(label='查看(V)',menu=self.viewbar)
        self.menubar.add_cascade(label='帮助(H)',menu=self.helpbar)
       
        #显示菜单栏
        self.master.config(menu=self.menubar)
        
        #创建编辑栏
        self.text=Text(self,width=800,height=500)
        self.text.pack()
        
        #右键出现菜单更换背景
        self.text.bind('<Button-3>',self.changeMeun)
        
        #添加键盘操作快捷键
        root.bind('<Control-KeyPress-s>',lambda event:self.saveFile())
        root.bind('<Control-KeyPress-o>',lambda event:self.openFile())
        root.bind('<Control-KeyPress-F5>',lambda event:self.getDate())
    
    
    
root=Tk()
app=Application(master=root)
root.title('记事本-无标题')
root.geometry('800x500+200+100')



root.mainloop()