# Runbook: SIEM/IDS Integration


## Current State
- Wazuh SIEM on Ubuntu; agents on Win10 + AD DC.
- Suricata on pfSense (LAN + WAN).
- No SPAN/port mirror yet on Brocade.


## Next Steps
1. **Expand Agents**
- Install Wazuh agent on pfSense, Ubuntu servers, and Raspberry Pi.
2. **Forward Suricata to Wazuh**
- Configure eve.json forwarding to Wazuh manager (Filebeat/agent module).
3. **Optional: Brocade SPAN**
(monitor session 1 source vlan 20,30 both monitor session 1 destination ethernet write memory)
4. **Dashboards and Alerts**
- Build DNS anomaly and ACL violation views.


## Validation
- Trigger test events from Kali (port scan, bad DNS) and verify appearance in Wazuh.