#Tyler Heller 
# Import the Portal object.
import geni.portal as portal

# Import the ProtoGENI library.
import geni.rspec.pg as pg

# Create a portal context.
pc = portal.Context()

# Create a Request object to start building the RSpec.
request = pc.makeRequestRSpec()
 
# loop to Add 4 raw PC's

for i in range(1, 5)
    node = request.XenVM("node-" + str(i)) #creates a node with name node- +the looping counter
    node.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:CENTOS7-64-STD" 
    interfaceip = node.addInterface("interface" + str(i)) #source 8.8
    interfaceip.component_id = "eth1" #source 8.6
    interfaceip.(rspec.IPv4Address("192.168.1.1", "192.168.1.4")) #source 8.6
    link.addInterface(interfaceip) # source 8.6
    if(i == 1)
        node.routable_control_ip = "true" #source example with use of routable_control_ip

# Install and execute a script that is contained in the repository.
node.addService(pg.Execute(shell="sh", command="/local/repository/silly.sh"))

# Print the RSpec to the enclosing page.
pc.printRequestRSpec(request)
