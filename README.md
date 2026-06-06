

# 📌 DevOps GitOps CI

## About
This repository demonstrates a **GitOps‑driven CI/CD workflow** for deploying containerized applications on Kubernetes. It integrates **GitHub, Docker, and Kubernetes manifests** to automate builds, deployments, and service management in a reproducible, version‑controlled manner.  

The project is designed for **hands‑on DevOps labs, interviews, and real‑world workflows**, focusing on automation, reproducibility, and cloud‑native best practices.

---

## 🚀 Features
- **Infrastructure as Code (IaC):** Kubernetes manifests (`deployment.yaml`, `service.yaml`) define application state declaratively.  
- **Automated Builds:** Dockerfile + GitHub integration for container image creation.  
- **Continuous Deployment:** GitOps workflow ensures changes in Git trigger updates in Kubernetes.  
- **Reproducibility:** Version‑controlled infrastructure and application code.  
- **Minimal Setup:** Lightweight FastAPI app (`app.py`) with requirements tracked in `requirements.txt`.

---

## 📂 Repository Structure
| File/Folder        | Purpose |
|--------------------|---------|
| `app.py`           | Sample FastAPI application |
| `requirements.txt` | Python dependencies |
| `Dockerfile`       | Containerization instructions |
| `deployment.yaml`  | Kubernetes Deployment manifest |
| `service.yaml`     | Kubernetes Service manifest |

---

## 🛠️ Prerequisites
- **Ubuntu/Linux system**  
- **Docker** installed and running  
- **Kubernetes cluster** (local via Minikube or cloud)  
- **kubectl** configured  
- **GitHub account** for GitOps integration  
- **Internet access**  

---

## ⚡ Quick Start
1. **Clone the repo**  
   ```bash
   git clone https://github.com/RenoX23/devops-gitops-ci.git
   cd devops-gitops-ci
   ```

2. **Build Docker image**  
   ```bash
   docker build -t fastapi-app:latest .
   ```

3. **Apply Kubernetes manifests**  
   ```bash
   kubectl apply -f deployment.yaml
   kubectl apply -f service.yaml
   ```

4. **Access the app**  
   ```bash
   kubectl get svc
   ```
   Use the external IP/NodePort to reach the FastAPI service.

---

## 🔁 GitOps Workflow
- **Push changes** → GitHub repository  
- **CI/CD pipeline** builds Docker image and updates manifests  
- **Kubernetes cluster** reconciles desired state with actual state  
- **Zero‑downtime updates** via rolling deployments  

---

## 🎯 Use Cases
- Lab exams and hands‑on DevOps practice  
- Demonstrating GitOps principles in interviews  
- Real‑world CI/CD pipeline setup for containerized apps  

---

