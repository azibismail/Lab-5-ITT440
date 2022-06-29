from netmiko import ConnectHandler

myserver={
	'device_type':'linux',
	'host':'10.1.1.85',
	'username':'azibismail',
	'password':'Mu@602048@!',
	'port':22,
	'secret':'',
}

net_connect=ConnectHandler(**myserver)
output=net_connect.send_command('uname -a')
print(output)
