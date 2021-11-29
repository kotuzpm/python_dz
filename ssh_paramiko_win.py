import paramiko
ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect('51.250.8.136', username='serg', key_filename='C:\\TMP\\private.ppk')

stdin, stdout, stderr = ssh.exec_command('sudo shutdown -r +1')
print stdout.readlines()
ssh.close()









