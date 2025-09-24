class Server:
    def __init__(self, hostname, os, role, total_users):
        self.hostname = hostname
        self.os = os
        self.role = role
        self.total_users = total_users
    
    def __repr__(self):
        return f"Server {self.hostname} running {self.os} (role: {self.role}) with {self.total_users} users."

class WebServer(Server):
    def __init__(self, hostname, os, role, total_users, *web_apps):
        super().__init__(hostname, os, role, total_users)
        self.web_apps = list(web_apps)

    def __repr__(self):
        repr = super().__repr__()
        return f"{repr}\nHosts web apps: {self.web_apps}"
    
class DatabaseServer(Server):
    def __init__(self, hostname, os, role, total_users, db_type):
        super().__init__(hostname, os, role, total_users)
        self.db_type = db_type
    
    def __repr__(self):
        repr = super().__repr__()
        return f"{repr}\nDatabase: {self.db_type}"
    
class ServerDirectory:
    def __init__(self):
        self.server_list = []
        self.total_users = 0

    def add(self, server):
        self.server_list.append(server)
        self.total_users += server.total_users
    
    def gather_all(self):
        return list(self.server_list)
    
    def list_all(self):
        print("Servers:\n")
        for server in self.gather_all():
            print(f"-{server}")

    def list_by_role(self, role):
        matches = []
        print(f"Servers with the role {role}:\n")
        for server in self.server_list:
            if server.role == role:
                print(f"{server}\n")
                matches.append(server)
        return matches