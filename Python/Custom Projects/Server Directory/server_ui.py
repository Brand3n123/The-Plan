from server_directory import *

main_directory = ServerDirectory()

def display_menu():
    print(" \n")
    print("Menu:\n1) Add server to directory\n2) List servers in directory\n3) Exit application")
    menu_input = 0
    menu_input += int(input("Enter your choice (1-3): "))
    if menu_input == 1:
        add_server_menu()
    elif menu_input == 2:
        list_server_menu()
    elif menu_input == 3:
        exit()
    else:
        print(" \n\n\n")
        print("Please enter a valid choice 1-3.")
        display_menu()

def add_server_menu():
    print(" \n")
    role = str(input("To add a server to the directory, please enter the type of server (web or db): ")).lower()
    if role == "web":
        hostname = str(input("Please enter the server's hostname: "))
        os = str(input("Please enter an operating system: "))
        total_users = int(input("Please enter the total amount of users for this server: "))
        web_apps = str(input("Please enter all web apps hosted on this server (app1, app2): "))
        main_directory.add(WebServer(hostname, os, role, total_users, web_apps))
        print(" \n\n")
        print(f"Server Added Successfully!\nYou added a web server running {os} called {hostname} with {total_users} total users.\nYour web server is hosting the following: {web_apps}.")
        print(" \n\n")
        display_menu()
    elif role == "db":
        hostname = str(input("Please enter the server's hostname: "))
        os = str(input("Please enter an operating system: "))
        total_users = int(input("Please enter the total amount of users for this server: "))
        db_type = str(input("Please enter the database type on this server: "))
        main_directory.add(DatabaseServer(hostname, os, role, total_users, db_type))
        print(" \n\n")
        print(f"Server Added Successfully!\nYou added a web server running {os} called {hostname} with {total_users} total users.\nYour db server is {db_type}.")
        print(" \n\n")
        display_menu()
    else:
        print("Please enter a valid option (web or db)")
        add_server_menu()

def list_server_menu():
    print(" \n")
    print("Menu:\n1) List servers by role\n2) List all servers\n3) Exit")
    menu_option = int(input("Enter your choice: "))
    if menu_option == 1:
        if len(main_directory.server_list) == 0:
            print(" \n")
            print("There are no servers listed in the directory.")
            display_menu()
        else:
            role = str(input("Enter the role of the servers you wish to see(web or db): "))
            main_directory.list_by_role(role)
            display_menu()
    elif menu_option == 2:
        if len(main_directory.server_list) == 0:
            print(" \n")
            print("There are no servers listed in the directory.")
            display_menu()
        else:
            main_directory.list_all()

display_menu()