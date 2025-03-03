# OBAL_V2
Significant improvement to OBAL (Open Board Ardupilot Linux)

|  | OBAL | OBAL_V2 | Navio2
|--|---|--|--|
|Linux Kernel |Bulleyes |Bookworm | Raspbian + ROS
|Ardupilot | 32-bit | 64-bit | ?
|Linux Configuration|Manual | Automatic via script | Manual 
|Rx Protocol| PPM | IBUS and SBUS | PPM and SBUS
|Flight controller | prototype | complete system | complete system
|IMU | GY-91 | GY-91 ,GY-912,..+more| MPU9250, LSM9DS1
|Display | No | yes | No
|Power moddule | No | Yes | Yes
|License | Open source | Open source | Proprietary 
|Price | < $40 | < $40 | $199
|Link | [here](https://github.com/HefnySco/OBAL) | here | [here](https://navio2.hipi.io/)

  
Cons with initial OBAL:
  1. Use analog Rx protocol (PPM)
  2. Limited to GY-91 (only possible IMU)
  3. Safety switch has electronic issue
  4. No proper logic conversion (use mix of 5v and 3.3v with RPI)
  5. Use old linux version which require re-compile to disable CONFIG_STRICT_DEVMEM
  6. Use 32-bit Ardupilot applications


![image](https://github.com/user-attachments/assets/bde9b66d-7c74-42ae-bda8-1ca1fce99bd3)
