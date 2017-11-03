from openstack import profile
from openstack import connection

def create_connection(auth_url, region, project_name, username, password):
    #prof = profile.Profile()
    #prof.set_region(profile.Profile.ALL, region)

    return connection.Connection(
        #profile=prof,
        verify=True,
        auth_url=auth_url,
        project_name=project_name,
        username=username,
        password=password
    )

def list_servers(conn):
    print("List Servers:")

    for server in conn.compute.servers():
        print(server)

conn = create_connection('https://chi.tacc.chameleoncloud.org:5000/v2.0',
                         'regionOne',
                         'CH-819321',
                         'cjy7117',
                         'Wait4aTrain7!')
conn.authorize()

list_servers(conn)
