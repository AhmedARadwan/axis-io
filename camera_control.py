import requests
import time

# TODO:
# get camera model
# from the dictionary, get the configuration of IOs

class AxisIO:
    def __init__(self, camera_ip, username, password, delay=5) -> None:
        self.camera_ip = camera_ip
        self.username = username
        self.password = password
        self.flag = [False, False, False, False]
        self.time_on = [0, 0, 0, 0]
        self.delay = delay

    def turn_on(self, port_num):
        url = "http://{}/axis-cgi/param.cgi?action=update&root.IOPort.I{}.Output.Active=open".format(self.camera_ip, port_num)
        response = requests.get(url, auth=(self.username, self.password))
        self.time_on[port_num] = time.time()
        self.flag[port_num] = True
        if response.status_code == 200:
            print("Port state changed to ON successfully.")
            return True
        else:
            print("Failed to change port state to ON")
            return False
    
    def turn_off(self, port_num):
        url = "http://{}/axis-cgi/param.cgi?action=update&root.IOPort.I{}.Output.Active=closed".format(self.camera_ip, port_num)
        response = requests.get(url, auth=(self.username, self.password))
        if response.status_code == 200:
            print("Port state changed to OFF successfully.")
            return True
        else:
            print("Failed to change port state to OFF")
            return False

    def check_port_state(self):
        for port in range(4):
            if self.flag[port] and ((time.time() - self.time_on[port]) > self.delay):
                self.turn_off(port)
                self.flag[port] = False
    
    def get_port_state(self, port_num):
        pass

    def send_pulse(self, port_num, pulse_time):
        url = "http://{}/axis-cgi/param.cgi?action=update&root.IOPort.I{}.Output.PulseTime={}".format(self.camera_ip, port_num, pulse_time)
        response = requests.get(url, auth=(self.username, self.password))
        if response.status_code == 200:
            print("PulseTime set to {} successfully.".format(pulse_time))
            return True
        else:
            print("Failed to set PulseTime")
            return False
        
    def get_port_info(self, port_num):
        url = "http://{}/axis-cgi/param.cgi?action=list&group=IOPort.I{}".format(self.camera_ip, port_num)
        response = requests.get(url, auth=(self.username, self.password))
        



    



if __name__=="__main__":
    camera = AxisIO("192.168.1.94", "root", "pass", 3)
    camera.turn_off(1)
    camera.send_pulse(1, 200)
    camera.turn_on(1)


