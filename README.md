# OBAL_V2
Significant improvement to OBAL (Open Board Ardupilot Linux)

Initial OBAl was using old linux kernel that has 'CONFIG_STRICT_DEVMEM=y' and to overcome this issue, the kernel must be recompiled with 'CONFIG_STRICT_DEVMEM=n'. That was a big headache.

Currently, the new releases of RPI operating system "Bookworm" has CONFIG_STRICT_DEVMEM set to "no" by default. To verify this please try on your RPI : 

    $ sudo modprobe configs
    $ zcat /proc/config.gz | grep STRICT_DEVMEM
    # CONFIG_STRICT_DEVMEM is not set
  
