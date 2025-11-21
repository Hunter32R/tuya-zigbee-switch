# Supported devices

Note that rebranded versions may have different internals, requiring different pinouts (and therefore custom builds).  
**Zigbee Manufacturer** is the most reliable device identifier.

If your device contains a **supported Tuya Zigbee module** (ZTU, ZT2S, ZT3L), porting is relatively simple.  
It consists of tracing (or guessing) the **board pinout**, adding an entry in the `device_db.yaml` file and running the build action. 

Also read:  
- [porting_to_new_device.md](./porting_to_new_device.md)
- [recommended_devices.md](./recommended_devices.md)
- [not_recommended_devices.md](./not_recommended_devices.md)

| Z2M device name | Vendor name | Zigbee Manufacturer | Type | Status | Issue |
| --- | --- | --- | --- | --- | --- |
| [TS0004_switch_module_2](https://www.zigbee2mqtt.io/devices/TS0004_switch_module_2.html) | TS0004  | _TZ3000_18ejxno1 | router | Supported |    -  | 
| [TS0004_switch_module_3](https://www.zigbee2mqtt.io/devices/TS0004_switch_module_3.html) | TS0014  | _TZ3000_18ejxno2 | router | Supported |    -  | 

