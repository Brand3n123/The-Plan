class Service:
    def __init__(self, name, svc_type, port):
        self.name = name
        self.svc_type = svc_type
        self.port = port

    def __repr__(self):
        return f"Service {self.name} is running service type {self.svc_type} on port {self.port}."

class Host:
    def __init__(self, hostname, os, services = None):
        self.hostname = hostname
        self.os = os
        self.services = services or []

    def __repr__(self):
        return f"Host {self.hostname} is running services {self.services} on {self.os}."

class ServiceRegistry:
    def __init__(self):
        self.hosts_list = []

    def add_host(self, host):
        if len(self.hosts_list) == 0:
            self.hosts_list.append(host)
            print(f"Host {host.hostname} successfully added to the empty registry.")
            return
        for h in self.hosts_list:
            if h.hostname.lower() == host.hostname.lower():
                print(f"This hostname {host.hostname} already exists in the registry.")
                return
        self.hosts_list.append(host)
        print(f"Host {host.hostname} successfully added to the registry.")

    def add_service(self, hostname, service):
        for h in self.hosts_list:
                if h.hostname.lower() == hostname.lower():
                    if len(h.services) == 0:
                        h.services.append(service)
                        print("Services added to host with no existing services.")
                    elif len(h.services) != 0:
                        for s in h.services:
                            if str(s.svc_type).lower() == str(service.svc_type).lower():
                                print("This service already exists for this host.")
                                return
                            elif int(s.port) == int(service.port):
                                print("A service on that port for this host already exists.")
                                return
                        h.services.append(service)
                        print("Services added to host.")
                        return
        raise LookupError(f"Host {hostname} does not exist in the registry.")
            
    
    def list_services(self, hostname):
        for h in self.hosts_list:
            if h.hostname.lower() == hostname.lower():
                print(f"The services for {hostname} are: {h.services}.")
                return h.services

    def hosts_running(self, svc_type):
        running_hosts = []
        for h in self.hosts_list:
            for s in h.services:
                if s.svc_type.lower() == svc_type.lower():
                    running_hosts.append(h.hostname)
                    break
        if running_hosts:
            print(f"The follow hosts are running {svc_type}: {running_hosts}")
        else:
            print(f"There are no hosts running {svc_type}.")
        return running_hosts
    
    def services_on_port(self, port):
        port_services = {}
        for h in self.hosts_list:
            for s in h.services:
                if int(s.port) == int(port):
                    if h.hostname in port_services:
                        port_services[h.hostname].append(s.name)
                    else:
                        port_services[h.hostname] = [s.name]
        print(f"The hosts:services running on {port} are {port_services}")
        return port_services





service1 = Service("pfSense", "DHCP", 68)
service2 = Service("Pi-Hole", "DNS", 53)
host1 = Host("Lenovo", "Windows", None)
host2 = Host("510s", "Kali", None)
registry1 = ServiceRegistry()
#registry1.add_host(host1)
#registry1.add_host(host2)
#registry1.add_service("510s", service1)
#registry1.add_service("abcd", service2)
registry1.list_services("510s")
registry1.hosts_running("DNS")
#print(registry1.hosts_list)
registry1.services_on_port(68)