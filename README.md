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

**Donation**

Please consider donating for the project. There were tremendous effort added in this project. 
Many prototype boards were built and a lot of tools were purchased to make this project become true.

click image below to start donating :

[
![Donate with PayPal](https://github.com/akhodeir/OBAL_V2/blob/main/photo/paypal-donate-button.png)
](https://www.paypal.com/donate/?hosted_button_id=LGAC3VKW2A8ZA)

**Important**

Use this project at your own risc. The authors and contributors will not be able to provide any help if PayPal complains about usage.
