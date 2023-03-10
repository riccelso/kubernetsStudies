### Building image with Dockerfile and send to repo in DockerHub
```
docker build -t rc-spark-operator-image:3.1.1 -f spark/DockerFile

docker tag rc-spark-operator-image:3.1.1 riccelso/spark-k8s-test:3.1.1

docker push riccelso/spark-k8s-test:3.1.1

```

### Installing HELM if necessary

```bash
cd /tmp
https://get.helm.sh/helm-v3.11.1-linux-amd64.tar.gz

tar xfz helm-v3.11.1-linux-amd64.tar.gz 

sudo mv linux-amd64/helm /usr/local/bin/helm
```

### ADD PERMISSIONS ON K8S and IN HELM ADD A REPO AND INSTALL
```
k create clusterrolebinding spark-operator-role --clusterrole=get,edit --serviceaccount=spark-operator:spark

helm repo add spark-operator https://googlecloudplatform.github.io/spark-on-k8s-operator
helm install my-release spark-operator/spark-operator --namespace spark-operator --create-namespace --set enableWebhook=true,serviceAccounts.spark.name=spark,sparkJobNamespace=spark-operator,logLevel=3
helm ls -n spark-operator
```

### INSIDE SPECIFIC NAMESPACE
```
kubens spark-operator

k apply -f k8s-files/spark-k8s.yaml
```