#! /bin/bash

# presence-detect.sh
# searches for the MAC address of known devices
#
# Use: precence-detect  [interfacename]

# do arp_scan to get connected mac addresses
connectedDevices=$(sudo arp-scan -l)

knownDevices=("d4:28:d5:37:7e:a2")

for device in "${knownDevices[@]}"
do


if [[ "$connectedDevices" = *"$device"* ]]; then
  echo "$device is NOT present!"
else
  echo "$device is NOT present!"
fi
#result=$(echo $connectedDevices | grep "$device")

#echo $result

done

