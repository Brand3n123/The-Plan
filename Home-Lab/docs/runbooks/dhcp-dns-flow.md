# Runbook: DHCP/DNS Flow Verification


## VLAN 20 (SERVERS)
- DHCP: pfSense (192.168.20.254)
- DNS: Pi-hole (192.168.20.53)
- Validate:
- `ipconfig /all` or `nmcli` shows correct DHCP/DNS
- `nslookup example.com 192.168.20.53`


## VLAN 30 (CLIENTS)
- DHCP: Cisco 2911 (192.168.30.1)
- Pool: 192.168.30.50+
- DNS handed out: 192.168.20.53 (primary), 1.1.1.1 (secondary)
- Validate:
- `ipconfig /all` shows DHCP server 192.168.30.1
- `nslookup example.com 192.168.20.53`
- Cisco: `show ip dhcp binding`


## Failure Modes
- **No lease**: check Cisco `show run | section dhcp`, bindings; pfSense packet capture 67/68 (VLAN20 only).
- **DNS blocked**: confirm Cisco ACL permits only DNS to 192.168.20.53.
- **Wrong DNS**: verify DHCP option values and Pi-hole availability.