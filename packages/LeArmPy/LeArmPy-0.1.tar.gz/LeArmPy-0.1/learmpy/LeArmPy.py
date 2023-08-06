import serial
import serial.tools.list_ports
import time
port_list = list(serial.tools.list_ports.comports())

def check_port():
    if len(port_list) <= 0:
        print ("The Serial port can't find!")
        return None
    else:
        for port_list_0 in port_list:
            port_serial = port_list_0[0]
            ser=serial.Serial(port_serial,115200,timeout = 1)
            time.sleep(2)
            ser.write(b'CHK');
            time.sleep(0.5)
            if ser.readline().decode().strip()=='LEARM0.1':
                return ser
            ser.close()
    return None

def send(port,cmd):
    port.write(cmd.encode())
    time.sleep(0.1)
def read(port):
    return port.readline().decode().strip()

class learm:
    ser=None
    Pa="000"
    Npa="000"
    Pb="000"
    Npb="000"
    Pc="000"
    Npc="000"
    AMaxPs=""
    BMaxPs=""
    CMaxPs=""
    MaxSP=""
    ArmSet=""
    def __init__(self,port=None):
        if port==None:
            port=check_port()
        if port==None:
            print("无法连接")
        else:
            self.ser=port
            print("连接成功")
            send(self.ser,'ARMSET')
            time.sleep(0.1)
            self.ArmSet=read(self.ser)
            self.AMaxPs=self.ArmSet.split(',')[0]
            self.BMaxPs=self.ArmSet.split(',')[1]
            self.CMaxPs=self.ArmSet.split(',')[2]
            self.MaxSP=self.ArmSet.split(',')[3]
            print("AMaxPs:%s\n"%(self.AMaxPs))
            print("BMaxPs:%s\n"%(self.BMaxPs))
            print("CMaxPs:%s\n"%(self.CMaxPs))
            print("MaxSP:%s\n"%(self.MaxSP))
    def get_sensor(self):
        if self.ser==None:
            print("无法连接")
        else:
            send(self.ser,'ISensor')
            time.sleep(0.1)
            return int(read(self.ser))
    def motor(self,switch):
        if self.ser==None:
            print("无法连接")
        else:
            if switch==0:
                print("已发送指令 "+'CTRLCL'+" 气泵关闭")
                send(self.ser,'CTRLCL')
            else:
                print("已发送指令 "+'CTRLOP'+" 气泵开启")
                send(self.ser,'CTRLOP')
    def move(self):
        if self.ser==None:
            print("无法连接")
        else:
            self.get_state()
            self.get_prestate()
            Pa=int(self.Pa)
            Pb=int(self.Pb)
            Pc=int(self.Pc)
            Npa=int(self.Npa)
            Npb=int(self.Npb)
            Npc=int(self.Npc)
            maxdis=max(abs(Pa-Npa)*int(self.AMaxPs)/1000,abs(Pb-Npb)*int(self.BMaxPs)/1000,abs(Pc-Npc)*int(self.CMaxPs)/1000)
            maxtime=maxdis/int(self.MaxSP)        

            send(self.ser,"M"+"A"+self.Pa+"99"+"B"+self.Pb+"99"+"C"+self.Pc+"99")
            time.sleep(maxtime)    
    def init_arm(self,a=None):
        if self.ser==None:
            print("无法连接")
        else:
            print("已发送初始化指令，正在初始化")
            send(self.ser,"INIT")
            while(read(self.ser)!="INITOK"):{
                }
            self.get_state()
    def get_state(self,a=None):
        if self.ser==None:
            print("无法连接")
        else:
            send(self.ser,'STATE')
            time.sleep(0.1)
            msg=read(self.ser)
            self.Npa=self.ps_change_str(msg.split(',')[0],self.AMaxPs)
            self.Npb=self.ps_change_str(msg.split(',')[1],self.BMaxPs)
            self.Npc=self.ps_change_str(msg.split(',')[2],self.CMaxPs)
            return print("当前实际位置为：A:%.3s B:%.3s C:%.3s"%(self.Npa,self.Npb,self.Npc))
    def ps_change_str(self,ps,maxps):
        res=str(int(int(ps)/int(maxps)*1000))
        res=int(res)
        if 10<=res<100:
            res="0"+str(res)
        elif res<10:
            res="00"+str(res)
        return res
    def set_pos(self,pa,pb,pc,direct=False):
        self.set_pa(pa)
        self.set_pb(pb)
        self.set_pc(pc)
        if direct:
            self.move()
    def set_pa(self,pos,direct=False):
        if 10<=pos<100:
            self.Pa="0"+str(pos)
        elif pos<10:
            self.Pa="00"+str(pos)
        else:
            self.Pa=str(pos)
        if direct:
            self.move()
    def set_pb(self,pos,direct=False):
        if 10<=pos<100:
            self.Pb="0"+str(pos)
        elif pos<10:
            self.Pb="00"+str(pos)
        else:
            self.Pb=str(pos)
        if direct:
            self.move()
    def set_pc(self,pos,direct=False):
        if 10<=pos<100:
            self.Pc="0"+str(pos)
        elif pos<10:
            self.Pc="00"+str(pos)
        else:
            self.Pc=str(pos)
        if direct:
            self.move()
    def get_prestate(self):
        print("当前目标位置为：A:%s B:%s C:%s"%(self.Pa,self.Pb,self.Pc))
    def get_armset(self):
        if self.ser==None:
            print("无法连接")
        else:
            print("AMaxPs:%s\n"%(self.AMaxPs))
            print("BMaxPs:%s\n"%(self.BMaxPs))
            print("CMaxPs:%s\n"%(self.CMaxPs))
            print("MaxSP:%s\n"%(self.MaxSP))
