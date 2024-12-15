import paramiko

# Corrected connection parameters
hostname = "192.168.0.124"  # IP address of the remote server
username = "root"           # Username to authenticate as
password = "Winteck@2023"   # Password for authentication

# Create an SSH client object
client = paramiko.SSHClient()

# Automatically add the server's host key (not recommended for production use)
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # Establish the connection
    client.connect(hostname=hostname, username=username, password=password)

    # Execute a command on the remote server
    _stdin, _stdout, _stderr = client.exec_command("lsblk")

    # Read the output from stdout
    print(_stdout.read().decode())

    # Optionally, handle any errors
    error_output = _stderr.read().decode()
    if error_output:
        print(f"Error: {error_output}")

finally:
    # Close the connection
    client.close()



