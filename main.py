
import sys

#clients = 'pablo,ricardo,'
clients = ['pablo', 'rikardo']

def create_client(client_name):
    global clients #para poer utilizar las variables globales
    if client_name not in clients:
        clients.append(client_name)
    else:
        print('Client already is in the cliente \'s list')

def  _get_client_name():
    client_name = None
    while not client_name:
        client_name = input('What is the cliente name?')
        if client_name =='exit':
            client_name = None
            break

    if not client_name:
        sys.exit()

    return client_name

def _add_coma():
    global clients
    clients +=','

def list_clients():
    global clients
    for idx, client in enumerate(clients):
        print('{}:{}'.format(idx,client))
    


def search_client(client_name):
    global clients
    client_list = clients.split(',')
    for client in client_list:
        if client != client_name:
            continue
        else:
            return True



def update_client(client_name,update_client_name):
    global clients
    if client_name in clients:
        clients = clients.replace( client_name +',', update_client_name)
    else:
        print('Client is not exist in clients list')


def delete_clients(client_name):
    global clients
    if client_name in clients:
        clients = clients.replace(client_name +',' , '')
    else:
        print('Client is not in clients list')

def _print_welcome():
    """ Como utlizar el sistema """ #comentario de ayuda para estuiar el sistema
    print('WELCOME TO PLATZI VENTAS')
    print('*' * 50)
    print('What would you like to do today?')
    print('[C]reate client')
    print('[D]elete client')
    print('[U]pdate client')
    print('[S]earch client')

if __name__ == '__main__':
    _print_welcome()
    command = input()
    command = command.upper()

    if command =='C':
        client_name = _get_client_name()
        create_client(client_name)
        list_clients()
    elif command == 'D':
        client_name = _get_client_name()
        delete_clients(client_name)
        list_clients()
    elif command == 'U':
        client_name = _get_client_name()
        update_client_name= input('What is the updated client name')
        update_client(client_name,update_client_name)
        list_clients()
    elif command == 'S':
        client_name = _get_client_name()
        found = search_client(client_name)
        if found :
            print('The cliente is in the cliente\' list')
        else:
            print('the cliente:{} is not in out list'.format(client_name))
    else:
        print('Invalid comand!!')







