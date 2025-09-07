# Home Lab Documentation


## Purpose
This repo documents my personal cybersecurity / IT training home lab. It demonstrates:
- Firewall, routing, and VLAN segmentation (pfSense + Cisco + Brocade + Netgear).
- Windows Active Directory deployment.
- SIEM/IDS integration with Wazuh + Suricata.
- Practical troubleshooting, change control, and runbooks.


This lab directly supports my career development toward **CompTIA PenTest+ and CySA+** certifications, while providing hands-on experience in network defense, monitoring, and system administration.


## Virtual Machines
- **pfSense v2.8.1** – Firewall, DHCP (VLAN20 only), static route to VLAN30 via Cisco; Suricata IDS.
- **Windows Server 2022 (ADDC Client)** – Active Directory Domain Controller, DNS, File Server.
- **Windows 10 Evaluation (CLIENT)** – Domain-joined test client.
- **Ubuntu Server 24.04.2 (Wazuh SIEM)** – Wazuh manager, indexer, dashboard.
- **Ubuntu Server 24.04.2 (Unifi WAP Controller)** – For wireless integration (planned).


## Physical Hardware
- **Cisco 2911/K9** – Router, SVI for VLAN20 and VLAN30, DHCP server for VLAN30, ACL enforcement.
- **Brocade X624HF** – Core switch.
- Port 1: VLAN20 untagged (pfSense host NIC)
- Port 2: Trunk VLAN20/30 (Cisco Gi0/0)
- Port 4: Trunk VLAN20/30 (Netgear p8)
- **Netgear GS108v3 (Managed)** – Access switch; Pi-hole, Kali bare-metal, Unifi WAP uplink.
- **Raspberry Pi 4** – Pi-hole DNS + Tailscale VPN.


## VLANs
- **VLAN 20 (SERVERS)** – 192.168.20.0/24
- pfSense: 192.168.20.254 (DHCP + default gateway for VLAN20)
- Cisco SVI: 192.168.20.1 (static route target)
- Pi-hole: 192.168.20.53
- AD DC: 192.168.20.10
- Wazuh: 192.168.20.15
- **VLAN 30 (CLIENTS)** – 192.168.30.0/24
- Cisco SVI: 192.168.30.1 (gateway + DHCP)
- Clients: .50+ range


## Topology Overview
Open `topology.drawio` in diagrams.net (draw.io) and export as PNG to produce `topology.png`.


## Resume Tie-in
This lab demonstrates my applied knowledge in:
- Network segmentation & ACLs
- Enterprise Windows/AD administration
- IDS/SIEM deployment
- Hands-on troubleshooting + runbooks