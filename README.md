# 🚀 CloudShop Lite

CloudShop Lite is a microservices-based web application deployed using Docker and Kubernetes (Minikube). It demonstrates containerization, service communication, and orchestration in a cloud-native environment.

---

## 📌 Features

* Microservices architecture (Frontend, API, Worker, Redis)
* Docker-based containerization
* Kubernetes deployment using Minikube
* Service-to-service communication
* Real-time visit counter using Redis

---

## 🧱 Architecture

Frontend (Node.js) → API (Flask) → Redis → Worker

* **Frontend**: Displays visit count
* **API**: Handles requests and updates Redis
* **Redis**: Stores visit data
* **Worker**: Background processing

---

## 🛠️ Tech Stack

* Frontend: Node.js
* Backend API: Python (Flask)
* Database: Redis
* Containerization: Docker
* Orchestration: Kubernetes (Minikube)

---

## 📂 Project Structure

```
cloudshop-lite/
│
├── frontend/
│   ├── Dockerfile
│   ├── package.json
│   └── index.js
│
├── api/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── app.py
│
├── worker/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── worker.py
│
├── k8s-manifests/
│   ├── frontend.yaml
│   ├── api.yaml
│   ├── worker.yaml
│   └── redis.yaml
│
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/cloudshop-lite.git
cd cloudshop-lite
```

---

### 2️⃣ Build Docker Images

```bash
docker build -t cloudshop-frontend ./frontend
docker build -t cloudshop-api ./api
docker build -t cloudshop-worker ./worker
```

---

### 3️⃣ Start Minikube

```bash
minikube start
```

---

### 4️⃣ Load Images into Minikube

```bash
minikube image load cloudshop-frontend
minikube image load cloudshop-api
minikube image load cloudshop-worker
```

---

### 5️⃣ Deploy to Kubernetes

```bash
kubectl apply -f k8s-manifests/
```

---

### 6️⃣ Check Pods

```bash
kubectl get pods
```

---

### 7️⃣ Access Application

```bash
minikube service frontend
```

Open the URL in browser 🚀

---

## 🧪 Testing

* Verify all pods are running
* Check logs using:

  ```bash
  kubectl logs <pod-name>
  ```
* Test API internally:

  ```bash
  kubectl exec -it <frontend-pod> -- curl http://api:5000
  ```

---

## 🎯 Output

The application displays:

```
CloudShop Lite
Visits: X
```

---

## 🚀 Future Improvements

* Add Ingress for custom domain
* Deploy on AWS (EKS/EC2)
* Add CI/CD pipeline
* Implement monitoring (Prometheus + Grafana)

---

## 👨‍💻 Author

Abhishek Singh

---

## ⭐ Acknowledgment

This project demonstrates real-world cloud-native development using Docker and Kubernetes.
