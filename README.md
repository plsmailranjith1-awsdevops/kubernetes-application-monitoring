# Kubernetes-Based Application Deployment & Monitoring

A production-style DevOps portfolio project demonstrating containerization,
Kubernetes orchestration, CI validation, container security scanning,
autoscaling, Helm packaging, and observability.

## Architecture

GitHub -> GitHub Actions -> Docker Build -> Trivy Scan -> Kubernetes

Kubernetes:
- Deployment
- Service
- NGINX Ingress
- ConfigMap
- Secret
- Liveness/Readiness probes
- Resource requests/limits
- Horizontal Pod Autoscaler

Monitoring:
- Prometheus
- Grafana

## Technologies

Docker, Kubernetes, Minikube, Helm, GitHub Actions, Prometheus, Grafana,
Trivy, Python Flask, Linux and Bash.

## Features

- Containerized Flask application
- Two-replica Kubernetes Deployment
- Rolling updates
- Self-healing
- Readiness and liveness probes
- CPU/memory resource controls
- Horizontal Pod Autoscaler
- Ingress routing
- Helm chart
- GitHub Actions CI
- Trivy image scanning
- Prometheus/Grafana monitoring

## Quick Start

### 1. Start Minikube

```bash
minikube start
minikube addons enable ingress
```

### 2. Build the application

```bash
docker build -t devops-k8s-app:latest ./app
minikube image load devops-k8s-app:latest
```

For local Minikube use, update `kubernetes/deployment.yaml` to:
`devops-k8s-app:latest` and set `imagePullPolicy: IfNotPresent`.

### 3. Deploy

```bash
chmod +x scripts/*.sh
./scripts/deploy.sh
```

### 4. Verify

```bash
kubectl get pods -n devops-demo
kubectl get svc -n devops-demo
kubectl get ingress -n devops-demo
kubectl get hpa -n devops-demo
```

## Helm

Validate the chart:

```bash
helm lint helm/devops-app
helm template devops-demo helm/devops-app
```

Install it after configuring the image repository:

```bash
helm upgrade --install devops-demo helm/devops-app   --namespace devops-demo   --create-namespace
```

## Monitoring

The repository includes `monitoring/prometheus-values.yaml` for installing
the kube-prometheus-stack with Helm.

Example:

```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update

helm upgrade --install monitoring prometheus-community/kube-prometheus-stack   --namespace monitoring   --create-namespace   -f monitoring/prometheus-values.yaml
```

For a portfolio/demo environment, change the sample Grafana password before use.

## Self-Healing Demo

```bash
kubectl get pods -n devops-demo
kubectl delete pod <pod-name> -n devops-demo
kubectl get pods -n devops-demo
```

A replacement pod should be created by the Deployment controller.

## Rolling Update Demo

Change `APP_VERSION` in the ConfigMap and restart the deployment:

```bash
kubectl apply -f kubernetes/configmap.yaml
kubectl rollout restart deployment/devops-app -n devops-demo
kubectl rollout status deployment/devops-app -n devops-demo
```

## Security

- Non-root Docker user
- Trivy container image scanning
- Kubernetes Secret example
- Resource limits
- Health probes

Do not commit real credentials or secrets. For production, use a dedicated
secret-management system such as AWS Secrets Manager or an external-secrets
solution.

## Screenshots

Add real screenshots after deployment:

- GitHub Actions successful pipeline
- Kubernetes pods
- Services and Ingress
- HPA
- Grafana dashboard
- Prometheus targets
- Self-healing test
- Rolling update

Store them under `screenshots/`.

## Learning Outcomes

This project demonstrates practical understanding of:

- Kubernetes workloads and networking
- Docker containerization
- Helm
- CI/CD fundamentals
- Container security
- Kubernetes health management
- Autoscaling
- Monitoring and observability
- Linux/Bash automation

## Future Improvements

- AWS EKS deployment
- Argo CD GitOps
- AWS Secrets Manager
- Loki centralized logging
- cert-manager and HTTPS
- Terraform-based EKS infrastructure
- Automated deployment to a staging environment
