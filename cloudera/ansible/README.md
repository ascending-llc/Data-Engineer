## Create AWS Console User and Jumpbox Linux User with Ansible

### Step 1: Change to /ansible Directory

### Step 2: Fill Information in UserInfo.yaml

### Step 3: Run register.py script

```sh
python register.py
```

## Run in Jumpbox

```bash
ansible-playbook --connection=local --inventory 127.0.0.1, Keypair.yaml -e @/home/ec2-user/ansible/UserInfo.yaml

ansible-playbook CreateUser.yaml -e @/home/ec2-user/ansible/UserInfo2.yaml
```