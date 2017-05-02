#Get Model and Manufacture for DELL, HP and FUJITSU Servers
def model_manufacture(self, ipmi_ip, ipmi_username, ipmi_password):
	cmd1= 'ipmitool -I lanplus -H '+ipmi_ip+' -U '+ipmi_username+' -P '+ipmi_password+' fru print'
	check = linux.SSH.Command(cmd1)
	if 'FUJITSU' in check:
		cmd = 'ipmitool -I lanplus -H '+ipmi_ip+' -U '+ipmi_username+' -P '+ipmi_password+' fru print'
		#print cmd
		manufacture = ''
		model = ''
		ipmi = self.SSH.Command(cmd)
		for line in ipmi.split('\n'):
			if 'Product Manufacturer' in line:
				manufacture = line.split(':', 1)[-1].strip()
		for line in ipmi.split('\n'):
			if 'Product Name' in line:
				model = line.split(':', 1)[-1].strip()
		print "Manufacture: %s" % manufacture
		print "Model: %s" % model
	else:
		cmd = 'ipmitool -I lanplus -H '+ipmi_ip+' -U '+ipmi_username+' -P '+ipmi_password+' fru print ID 0'
		#print cmd
		manufacture = ''
		model = ''
		ipmi = self.SSH.Command(cmd)
		for line in ipmi.split('\n'):
			if 'Product Manufacturer' in line:
				manufacture = line.split(':', 1)[-1].strip()
		for line in ipmi.split('\n'):
			if 'Product Name' in line:
				model = line.split(':', 1)[-1].strip()
		print "Manufacture: %s" % manufacture
		print "Model: %s" % model
		
def getOS(self, IP, username, password):
	cmd1= 'vmware -vl'
	cmd2= 'cat /etc/*release'
	cmd3= 'cat /etc/os-release'
	esx = linux.SSH.Command(cmd1)
	suse = linux.SSH.Command(cmd3)
	rhel = linux.SSH.Command(cmd2)
	if 'VMware ESXi' in suse: print suse
	elif 'VMware ESXi' in esx: print esx
	elif 'VMware ESXi' in rhel : print rhel
	elif 'PRETTY_NAME' in suse:
		for line in suse.split('\n'):
			if 'PRETTY_NAME' in line:
				sles_ver = line.split('=', 1)[-1].strip()
				break
		print "OS: %s" % sles_ver
	elif 'PRETTY_NAME' in esx:
		for line in esx.split('\n'):
			if 'PRETTY_NAME' in line:
				sles_ver = line.split('=', 1)[-1].strip()
				break
		print "OS: %s" % sles_ver
	elif 'PRETTY_NAME' in rhel:
		for line in rhel.split('\n'):
			if 'PRETTY_NAME' in line:
				sles_ver = line.split('=', 1)[-1].strip()
				break
		print "OS: %s" % sles_ver
	elif "Red Hat" in suse:
		for line in suse.split('\n'):
			if "Red Hat" in line:
				redhat = line.strip('\n')
				break
		print "OS: %s" % redhat
	elif "Red Hat" in esx:
		for line in esx.split('\n'):
			if "Red Hat" in line:
				redhat = line.strip('\n')
				break
		print "OS: %s" % redhat
	elif "Red Hat" in rhel:
		for line in rhel.split('\n'):
			if "Red Hat" in line:
				redhat = line.strip('\n')
				break
		print "OS: %s" % redhat
		