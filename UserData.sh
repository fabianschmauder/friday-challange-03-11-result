pip3 install flask boto3
cd /home/ec2-user
aws s3 cp s3://bucket-api-code-package-42/app-code.zip app-code.zip
unzip app-code.zip -d app-code
cd app-code
unzip app-code.zip -d app-code
cd app-code
sh run-api.sh 