# Service Registry
Basic DHCP-type host/service registry
Track hosts and the services running on them with basic OOP structures.

## Usage
```bash
python ServiceRegistry.py
```

## Notes
```bash
Classes:

Service(name, svc_type, port)  
Host(hostname, os, services)  
ServiceRegistry for managing hosts and queries    

Duplicate protection:  
Prevents duplicate hostnames  
Prevents duplicate services (same type + port) on a host  

Queries:  
list_services(hostname) → services for a host  
hosts_running(svc_type) → hosts with a given service type  
services_on_port(port) → dict of hosts:services using a port  
Raises LookupError if adding a service to an unknown host  
```

## Example snippet:
```bash
registry = ServiceRegistry()
registry.add_host(Host("Lenovo", "Windows"))
registry.add_service("Lenovo", Service("pfSense", "DHCP", 68))
registry.hosts_running("dhcp")
```
## Example Output
```bash
Host Lenovo successfully added to the empty registry.
Service added to host with no existing services.
The following hosts are running dhcp: ['Lenovo']
The hosts:services running on 68 are {'Lenovo': ['pfSense']}
```
