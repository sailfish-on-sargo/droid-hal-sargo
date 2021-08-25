# These and other macros are documented in dhd/droid-hal-device.inc
# Feel free to cleanup this file by removing comments, once you have memorised them ;)

%define device sargo
%define vendor google

%define vendor_pretty Google
%define device_pretty Pixel 3a

%define installable_zip 1
%define droid_target_aarch64 1

%define straggler_files \
/setup_fake_cache.sh \
/bugreports \
   /cache \
   /d \
   /dsp \
   /firmware \
   /persist \
   /product \
   /sdcard \
%{nil}

%include rpm/dhd/droid-hal-device.inc

# IMPORTANT if you want to comment out any macros in your .spec, delete the %
# sign, otherwise they will remain defined! E.g.:
#define some_macro "I'll not be defined because I don't have % in front"

