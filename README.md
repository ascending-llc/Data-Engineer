# ASCENDING Cloudera Data Engineer Hub

## Cloudera Manager Instance

### Login in Cloudera Manager Instance

```
http://54.86.193.122:7180
```

Currently you may have some problems viewing charts and tables in https://data.ascendingdc.com please use ip address above.

### SSH into Cloudera Manager Instance

```sh
ssh ec2-user@54.86.193.122
```

You will login in as ec2-user and you have root privilege, you can use sudo command without password

## Cloudera Nodes Types and Number

### 3 MasterNodes

```
master-1: ip-172-31-86-198.ec2.internal
master-2: ip-172-31-93-228.ec2.internal
master-3: ip-172-31-89-172.ec2.internal
```
### 3 WorkerNodes

```
worker-1: ip-172-31-94-165.ec2.internal
worker-2: ip-172-31-89-11.ec2.internal
worker-3: ip-172-31-91-232.ec2.internal
```

### 1 UtilityNode

```
utility-1: ip-172-31-91-213.ec2.internal
```

### 1 GatewayNode

```
gateway-1: ip-172-31-92-98.ec2.internal
```

### SSH into Node Instance

After you ssh into Cloudera Manager Instance, use following command line

```sh
ssh -i ~/.ssh/jumpbox.pem ec2-user@${private_DNS}
```

## Start&Stop Node Instances

### Start All Node Instances

```sh
aws lambda invoke --function-name arn:aws:lambda:us-east-1:595312265488:function:cloudera-lambda-SwitchClouderaInstances-1NEWLX6F20VFK --payload '{ "status": "on" }' response.json
```

### Stop All Node Instances

```sh
aws lambda invoke --function-name arn:aws:lambda:us-east-1:595312265488:function:cloudera-lambda-SwitchClouderaInstances-1NEWLX6F20VFK --payload '{ "status": "off" }' response.json
```

### Create AWS User

```sh
aws lambda invoke --function-name cloudera-lambda-CreateIamUser-1APZ0OUSDRPIS --payload '{ "username": "test0730", "group": "student", "email": "leyi@frugalops.com" }' response.json
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
ssh -L 3306:wordpress.c6tqxth4eafz.us-east-1.rds.amazonaws.com:3306 ec2-user@54.86.193.122
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