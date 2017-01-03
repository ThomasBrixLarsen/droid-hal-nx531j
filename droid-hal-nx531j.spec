# These and other macros are documented in dhd/droid-hal-device.inc
%define device nx531j
%define vendor nubia
%define vendor_pretty Nubia
%define device_pretty Nubia Z11
%define installable_zip 1
%define straggler_files \
/init.mdm.sh\
/init.nubia.sh\
/init.qcom.early_boot.sh\
/init.qcom.sh\
/init.qcom.syspart_fixup.sh\
/init.qcom.usb.sh\
/verity_key\
%{nil}
%include rpm/dhd/droid-hal-device.inc
