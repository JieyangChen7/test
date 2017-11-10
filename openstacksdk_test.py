from openstack import profile
from openstack import connection
import os
import sys
from openstack import utils


SERVER_NAME = "bee-node"
IMAGE_NAME = "Ubuntu-14-04-Docker"
FLAVOR_NAME = "baremetal"
NETWORK_NAME = "sharednet1"
KEYPAIR_NAME = "bee-test-key"
SSH_DIR = "/Users/jieyangchen/DEV/test"
PRIVATE_KEYPAIR_FILE = "bee.key"

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


def list_images(conn):
    print("List Images:")

    for image in conn.compute.images():
        print(image)


def list_flavors(conn):
    print("List Flavors:")

    for flavor in conn.compute.flavors():
        print(flavor)

def list_networks(conn):
    print("List Networks:")

    for network in conn.network.networks():
        print(network)

def create_keypair(conn):
    keypair = conn.compute.find_keypair(KEYPAIR_NAME)

    if not keypair:
        print("Create Key Pair:")

        keypair = conn.compute.create_keypair(name=KEYPAIR_NAME)

        print(keypair)

        try:
            os.mkdir(SSH_DIR)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise e

        with open(PRIVATE_KEYPAIR_FILE, 'w') as f:
            f.write("%s" % keypair.private_key)

        os.chmod(PRIVATE_KEYPAIR_FILE, 0o400)

    return keypair

def create_server(conn):
    print("Create Server:")

    image = conn.compute.find_image(IMAGE_NAME)
    flavor = conn.compute.find_flavor(FLAVOR_NAME)
    network = conn.network.find_network(NETWORK_NAME)
    keypair = create_keypair(conn)
    
    print (image.id)
    print (flavor.id)
    print (network.id)
    
    server = conn.bare_metal.create_node(
        name=SERVER_NAME, image_id=image.id, flavor_id=flavor.id,
        networks=[{"uuid": network.id}], key_name=keypair.name)

#    server = conn.compute.wait_for_server(server)

#    print("ssh -i {key} root@{ip}".format(
#        key=PRIVATE_KEYPAIR_FILE,
#        ip=server.access_ipv4))


conn = create_connection('https://chi.tacc.chameleoncloud.org:5000/v2.0',
                         'regionOne',
                         'CH-819321',
                         'cjy7117',
                         'Wait4aTrain7!')
conn.authorize()

utils.enable_logging(debug=True, stream=sys.stdout)

#list_servers(conn)
#list_images(conn)
#list_flavors(conn)
#list_networks(conn)
create_server(conn)
