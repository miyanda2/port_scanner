import tkinter.ttk, socket,sys
import threading
from tkinter import messagebox, Label, Spinbox, Tk, Entry, E, W, END, WORD, Button, Text
# creates a dic of common service's
def commonPortDef(port):
    try:
       commonPortDic = {80: "http", 443: "https", 53: "dns", 21: "ftp", 22: "ssh", 25:"smtp",  110: "pop3"}
       return commonPortDic[port]
    except KeyError:
        return "Unknown service"


class PortScanner:
    def __init__(self):
            mGUI = Tk() #create tk reference object AKA Make A Window/Frame
            self.srvr = Entry(mGUI,textvariable="server")
            self.srvr.setvar(name="server",value='127.0.0.1')
            self.srvr.grid(row=0,column=1,sticky=W)
            lbl = Label(mGUI,text="Target Address:")
            lbl.grid(row=0,column=0,sticky=W)
            self.spnr = Spinbox(mGUI,from_=1,to=49152,value=1)
            self.spnr.grid(row=1,column=1,sticky=W)
            lbl2 = Label(mGUI,text="Starting Port:")
            lbl2.grid(row=1,column=0,sticky=W)
            self.spnr.grid(row=1,column=1,sticky=W)
            self.spnr2 = Spinbox(mGUI,from_=1,to=49152,value=49152)
            self.spnr2.grid(row=2,column=1,sticky=W)
            lbl3 = Label(mGUI,text="Ending Port")
            lbl3.grid(row=2,column=0,sticky=W)
            mGUI.resizable(width=False,height=False) #Make Window Size Static (Not Resizeable)
            btn = Button(mGUI,text="Commence Port Scan!",command=self.scan)
            btn.grid(row=3,column=1,sticky=W)
            self.txt = Text(mGUI,width=70,height=40,wrap=WORD)
            self.txt.grid(row=4,column=0,columnspan=2,sticky=W)
            mGUI.title('Network PortScanner dev by MICHEAL IYANDA!') #set Title Of Window
            self.txt.insert(0.0,'Open Ports Will Appear Here After Scan Completes!')

            mGUI.mainloop() #Show GUI Window


    def pscan(self,port):
            try:
                target = self.srvr.get()
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s.connect((target,port))
                return True
            except:
                return False

    def scan(self):
        self.txt.delete(0.0, END)
        print('Scanning', self.srvr.get())
        for num in range(int(self.spnr.get()), int(self.spnr2.get())+1):
            if self.pscan(num):
                print('Port: ',num,'Is Open!')
                msg = "Port "+str(num)+" Is Open!-------" "Port %d is normally used for " % num + commonPortDef(num)
                self.txt.insert(0.0,msg)
            else:
                print('port: ',num,'Is Closed!')
                #msg = "Port "+str(x)+" Is Closed!\n"
                #txt.insert(0.0,msg)


        messagebox.showinfo(title="PyPortScanner!", message="Scan Completed!")

ps = PortScanner()
