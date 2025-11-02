class Permission:
    def __init__(self, action, resource, deny=False):
        self.action = action
        self.resource = resource
        self.deny = deny

    def __repr__(self):
        return f"{self.action} access on {self.resource} resource"
    
class Role:
    def __init__(self, name, permissions = None):
        self.name = name
        self.permissions = permissions or []
    
    def __repr__(self):
        return f"The {self.name} role has the following permissions: {self.permissions}"

class User:
    def __init__(self, username, roles = None):
        self.username = username
        self.roles = roles or []

    def __repr__(self):
        role_names = [role.name for role in self.roles]
        return f"User {self.username} has the following roles: {role_names}"
    

def can(user, action, resource):
    allow = False
    for role in user.roles:
        for permission in role.permissions:
            if permission.action.lower().strip() == str(action.lower().strip()) and permission.resource.lower().strip() == str(resource.lower().strip()):
                if permission.deny:
                    return False
                allow = True
    return allow

def list_permissions(user):
    perms = []
    for role in user.roles:
        for permission in role.permissions:
            perms.append(("DENY:" if permission.deny else "ALLOW:", permission.action, permission.resource))
    return perms

reboot_server_perm = Permission("Reboot", "Server")
reboot_server_block = Permission("Reboot", "Server", deny=True)
read_user_perm = Permission("Read", "User")
read_user_block = Permission("Read", "User", deny=True)
read_server_perm = Permission("Read", "Server")
read_server_block = Permission("Read", "Server", deny=True)

helpdesk_role = Role("Helpdesk", [read_user_perm])
ops_admin_role = Role("Ops_admin", [reboot_server_perm])
security_readonly_role = Role("Security_readonly", [read_server_perm])

helpdesk_user1 = User("Helpdesk.1", [helpdesk_role])
ops_admin_user1 = User("Ops Admin.1", [ops_admin_role])
security_readonly_user1 = User("Security_(readonly).1", [security_readonly_role])

test_user = User("TestUser", [helpdesk_role])