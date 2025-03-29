import os
import sys
import getopt

def add_service(serviceFilePath, serviceFileContent):
    fileExist = False
    serviceName = serviceFilePath.split('/')[-1]
    if os.path.exists(serviceFilePath):
        fileExist = True
        print(f'stop existing service : {serviceName}')
        os.system(f'sudo systemctl stop {serviceName}')

    with open(serviceFilePath, 'w') as file:
        file.write(serviceFileContent)

    print(f'enable service : {serviceName}')
    os.system(f'sudo systemctl enable {serviceName}')
    print(f'start service : {serviceName}')
    os.system(f'systemctl daemon-reload')
    os.system(f'sudo systemctl start {serviceName}')
    
def disable_bt():
	os.system('sudo systemctl disable hciuart')
	os.system('sudo systemctl stop hciuart')
	

#cpuinfo = os.system('cat /proc/cpuinfo')
#cpuinfo = os.system('cat /proc/device-tree/model')
cpuinfo = os.popen('cat /sys/firmware/devicetree/base/model').read()
arch = os.popen('uname -m').read()

print(cpuinfo)
if ('Raspberry Pi 4' not in cpuinfo) or ('aarch64' not in arch):
    print('This script is only for Raspberry Pi 4 (x64)')
    sys.exit(2)


argv = sys.argv[1:]
print('Number of arguments : ' , len(argv))
for arg in argv:
    print("provided arguments : ", arg)

#default values 
ip = ''
app = ''
#both parameters shall exist
if len(argv) != 2 :
    print('please enter ip and application name to the scipt')
    sys.exit(2)

# parse command line options:
try:
    opts, args = getopt.getopt(argv,'x',['ip=','app='])
    print('The existing options are : ', opts)
except getopt.GetoptError:
    print('python3 install.py --ip=192.168.178.20 --app=arducopter')
    sys.exit(2)

for opt, arg in opts:
    if opt in ("-i", "--ip"):
        #ip address for the machine that has mission planner
        ip = arg
    elif opt in ("-a", "--app"):
        #name of the application (arducopter,arduplane,..etc)
        app  = arg.lower()

APPS = ['arducopter','arduplane','rover',]


#check if the user selected an app from the list and this app exists in current folder
if (app not in APPS) or (not os.path.exists(app)) or (ip == '') or (app == ''):
    sys.exit(2)

cwd = os.getcwd() + '/'

appPath = cwd + app


paramFile= 'ardupilot.parm'
paramFileContent = '''
SYSID_THISMAV 1
FRAME_CLASS 1
FRAME_TYPE  1
'''

if app == 'arducopter':
    with open(paramFile, 'w') as file:
        file.write(paramFileContent)

#service file path
serviceFilePath = '/lib/systemd/system/ardupilot.service'
#service file content
serviceFileContent =f'''
[Unit]
Description=Autopilot service
After=systemd-modules-load.service

[Service]
Type=simple
ExecStart={appPath} --serial0 udp:{ip}:14550:bcast --serial4 /dev/ttyAMA4
Restart=on-failure
CPUAffinity=3
IOSchedulingClass=real-time
IOSchedulingPriority=0
LimitNICE=-10

[Install]
WantedBy=multi-user.target
'''

add_service(serviceFilePath, serviceFileContent)

#service file path
serviceFilePath = '/lib/systemd/system/picamera.service'
#service file content
serviceFileContent =f'''
[Unit]
Description=Run Pi Camera as Webcam
After=network.target

[Service]
Type=simple
Restart=on-failure
ExecStart=/bin/sh -c "rpicam-vid -n --width 1280 --height 720 -b 1000000 --framerate 15 -t 0 -o - | gst-launch-1.0 -v fdsrc ! h264parse ! rtph264pay config-interval=10 pt=96 ! udpsink host={ip} port=9000"
CPUAffinity=2
Restart=on-failure

[Install]
WantedBy=default.target
'''

add_service(serviceFilePath, serviceFileContent)

print('Disable Bluetooth')
disable_bt()

configFile = '/boot/firmware/config.txt'

lines = [
	'dtparam=i2c_arm=on', #Enable I2C
	'dtparam=i2c_arm_baudrate=400000', #enable I2C speed
	'dtparam=spi=on', #Enable SPI
	'enable_uart=1', #Enable UART
	'dtoverlay=uart4', #Enable UART4 on GPIO 8, 9
]

with open(configFile) as f:
    datafile = f.readlines()
    for l in datafile:
        l = l[0:-1] #remove new line from l 
        if l in lines:
            print(f"found in {configFile} : ", l)
            #remove found lines from list of lines to be appended
            lines.remove(l) 
            

with open(configFile,'+a') as f:
    for l in lines:
        f.write(l+'\n')
        

file = '/boot/firmware/cmdline.txt'

print('remove the console serial prints')
os.system(f'sed -i -e "s/console=serial0,115200//g" {file}')
os.system(f"sudo grep -qxF 'isolcpus' {file} || sed -i 's/$/ isolcpus=2,3/' {file}")

#load the i2c dev to the modules at startup
#or user must use "sudo modprobe i2c-dev" for each boot-up
file = '/etc/modules'
os.system(f'sudo chmod 777 {file}')
os.system(f'sudo grep -qxF "i2c-dev" {file} || echo "i2c-dev" >> {file}')

print("please restart your PI : sudo reboot now")



