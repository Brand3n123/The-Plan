# Troubleshooting Guide


## DHCP Issues
- VLAN20: verify pfSense DHCP leases.
- VLAN30: verify Cisco DHCP bindings (`show ip dhcp binding`).
- pfSense: packet capture on LAN (ports 67/68).


## DNS Issues
- `nslookup example.com 192.168.20.53` to test Pi-hole.
- Check Pi-hole query logs and Cisco ACL hits.


## Segmentation Tests
- VLAN30 -> VLAN20 host ping: should fail (blocked by ACL).
- VLAN30 -> 192.168.20.53 DNS: should succeed.


## Virtualization Checks
- VirtualBox NICs = Bridged, Promiscuous = Allow All.
- pfSense static route to 192.168.30.0/24 via 192.168.20.1 present.