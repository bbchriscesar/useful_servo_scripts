import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Replace the following values with your own information
host = "192.168.20.103"
username = "pi"
password = "gp"
command = "python /home/pi/Robotics/sample.py"

ssh.connect(host, username=username, password=password)
stdin, stdout, stderr = ssh.exec_command(command)
# print(stdout.read().decode())
# print(stderr.read().decode())

ssh.close()
