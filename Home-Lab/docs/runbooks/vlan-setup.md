# Runbook: Add a New VLAN Safely


## Pre-change Checklist
- Confirm purpose, subnet, and DHCP/DNS strategy.
- Validate trunk ports/path (Brocade <-> Cisco <-> Netgear).
- Document expected reachability and segmentation.


## Change Steps
1. **Brocade** – Create VLAN and assign ports.
(vlan name tagged ethernet <UPLINK_PORTS> untagged ethernet <ACCESS_PORTS> write memory)
- Note: pfSense is always connected on **untagged VLAN**; do not configure pfSense for trunks.
2. **Cisco** – Add SVI (if routing on Cisco) and optional ACL.
(interface gi0/0. encapsulation dot1Q ip address ! optional ACL ip access-list extended VLAN_OUT 
permit udp host 192.168.20.53 eq 53
permit tcp host 192.168.20.53 eq 53 deny ip 192.168.20.0 0.0.0.255
permit ip any any interface gi0/0. ip access-group VLAN_OUT in)
3. **DHCP** – Choose DHCP server (Cisco or pfSense) and configure scope.
4. **pfSense** – Add static route (if DHCP not on pfSense) and test rules.


## Verification
- Client gets address from correct pool.
- DNS resolution works via Pi-hole.
- Segmentation rules enforced (no direct access to VLAN20 hosts unless allowed).


## Rollback
- Remove SVI and ACL from Cisco.
- Remove VLAN from Brocade.
- Remove static route/interface from pfSense.