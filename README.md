# ASCENDING Cloudera Data Engineer Hub

## Cloudera Manager Instance

### Login in Cloudera Manager Instance

```
http://:7180
https://data.ascendingdc.com
```

### SSH into Cloudera Manager Instance

```sh
ssh ec2-user@
```

You will login in as ec2-user and you have root privilege, you can use sudo command without password

## Cloudera Nodes Types and Number

### 3 MasterNodes

```
master-1: ip-10-0-7-212.ec2.internal
master-2: ip-10-0-1-51.ec2.internal
master-3: ip-10-0-2-172.ec2.internal
```
### 3 WorkerNodes

```
worker-1: ip-10-0-8-55.ec2.internal
worker-2: ip-10-0-1-181.ec2.internal
worker-3: ip-10-0-9-146.ec2.internal
```

### 1 UtilityNode

```
utility-1: ip-10-0-14-225.ec2.internal
```

### 1 GatewayNode

```
gateway-1: ip-10-0-4-177.ec2.internal
```

### SSH into Node Instance

After you ssh into Cloudera Manager Instance, use following command line

```sh
ssh -i ~/.ssh/jumpbox.pem ec2-user@${private_DNS}
```

## Start&Stop Node Instances

### Start All Node Instances

In lambda function cloudera-lambda-SwitchClouderaInstances-4JoNeLuISoq1, run the test with content:

```
{"status": "on"}
```

### Stop All Node Instances

In lambda function cloudera-lambda-SwitchClouderaInstances-4JoNeLuISoq1, run the test with content:

```
{"status": "off"}
```

### Create Jumpbox Linux User with Ansible

```sh
ansible-playbook CreateUser.yaml -e @/Users/yi/Documents/Data-Engineer/ansible/UserInfo.yaml
```

## Login in database

### Method 1: Login in via Cloudera Manager Instance

ssh into Cloudera Manager Instance first, then input 

```sh
mysql --host=wordpress.c6tqxth4eafz.us-east-1.rds.amazonaws.com --user=root --password
```

enter correct password and you will login in databse

### Method 2: SSH port forwarding

run following command line in your local machine

```sh
ssh -L 3306:cloudera.cpnxuicfyso5.us-east-1.rds.amazonaws.com:3306 ec2-user@
```

Then you can visit database in localhost:3306 with your own mysql client tool.

## Cloudera Monitor Website

### Hbase

```
https://hbase-1.ascendingdc.com/master-status
https://hbase-2.ascendingdc.com/master-status
https://hbase-3.ascendingdc.com/master-status
```

### HDFS

```
https://hdfs.ascendingdc.com
```

### Hive

```
https://hive.ascendingdc.com
```

### Hue

```
https://hue.ascendingdc.com
```

### Impala

```
https://impala-state.ascendingdc.com
https://impala-catalog.ascendingdc.com
```

### Impala Daemon
```
https://impala-daemon-1.ascendingdc.com
https://impala-daemon-2.ascendingdc.com
https://impala-daemon-3.ascendingdc.com
```

### Oozie

```
https://oozie.ascendingdc.com
```

### Spark

```
https://spark.ascendingdc.com
```

### Yarn

```
https://yarn.ascendingdc.com/cluster
https://yarn-history.ascendingdc.com
```

### Kudu

```
https://kudu-master-1.ascendingdc.com
https://kudu-master-2.ascendingdc.com
https://kudu-master-3.ascendingdc.com
```

```bash
ansible-playbook --connection=local --inventory 127.0.0.1, Keypair.yaml -e @/home/ec2-user/ansible/UserInfo.yaml

ansible-playbook CreateUser.yaml -e @/home/ec2-user/ansible/UserInfo2.yaml
```


### Cloudera Settings Troubleshooting

#### Settings for Cloudera manager referring

```
# Cloudera Manager Error: Rejecting request originating from x.x.x.x for http://xxx/cmf/services/landingPageStatusContent with referrer https://xxx.com/cmf/home

cd /opt/cloudera/cm/webapp/WEB-INF/spring/mvc-config.xml

# Comment CsrfRefererInterceptor

<!-- <bean class="com.cloudera.server.web.cmf.csrf.CsrfRefererInterceptor"/> -->

# Restart server

sudo service cloudera-scm-server restart
```

#### Settings for instances ip addresses changing

```
# stop scm agent on each instance
sudo service cloudera-scm-agent stop

# stop scm server on cloudera manager instance (jumpbox)
sudo service cloudera-scm-server stop

# on each cloudera instances except jumpbox, change the ip address for server ip address
sudo vi /etc/cloudera-scm-agent/config.ini

# check its own ip adress
sudo vi /etc/hosts

# restart agent on each instance
sudo service cloudera-scm-agent restart

# restart server on jumpbox
sudo service cloudera-scm-server restart
```

#### HDFS has two standby namenode but zero active namenode

reset zookeeper format in each namenode instance and restart hdfs service.

```
hdfs zkfc -formatZK
```

#### Kudu instances has different ip addresses in settings

remove setting files in each kudu master instance

```
rm -rf /data/kudu/master_xx
```

#### HDFS check point error

remove folders under /dfs/snn on active HDFS namenode.

```
rm -rf /dfs/snn/current
```