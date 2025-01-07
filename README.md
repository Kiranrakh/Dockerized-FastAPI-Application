# docker-fastapi-test

# Dockerized FastAPI Application with Monitoring and CI/CD Pipeline

This project demonstrates a Dockerized FastAPI application integrated with a Jenkins CI/CD pipeline and monitored using Prometheus and Grafana.

---

## **Project Overview**
This application:
- Implements a simple FastAPI application with endpoints:
  - `GET /`: Returns a hello message.
  - `GET /users`: Fetches a list of users from a JSON file.
  - `POST /users`: Adds a user to the JSON file.
- Uses `docker-compose` to orchestrate the application, Prometheus, and Grafana.
- Provides a Jenkins pipeline for automated deployment.
- Includes Prometheus and Grafana for monitoring.

---

## **1. How to Build and Run the Application**

### **Prerequisites**
- Install [Docker](https://www.docker.com/products/docker-desktop).
- Install [Docker Compose](https://docs.docker.com/compose/install/).
- Ensure Python (for local testing) is installed (optional).

### **Steps**
1. **Clone the Repository**
   ```bash
   git clone <repository_url>
   cd docker-fastapi-test

Build and Run the Application

bash
Copy code
docker-compose up --build
This command:

Builds the FastAPI application.
Starts the application, Prometheus, and Grafana containers.
Access the Application

FastAPI application: http://localhost:8000/docs (API documentation).
Prometheus: http://localhost:9090.
Grafana: http://localhost:3000.

Install Jenkins and configure Docker inside the Jenkins server.

Configure Jenkins

Create a new pipeline job.

Run the Pipeline

Trigger the pipeline from the Jenkins dashboard.
Monitor logs to ensure the application is deployed successfully.
Validate Deployment

Verify the application is running at http://localhost:8000.

*Access Prometheus*

Visit http://localhost:9090 to view metrics.

*Grafana*
Login

Default credentials: admin/admin.
Add Prometheus Data Source

URL: http://prometheus:9090.
Import Dashboard

Use an existing FastAPI/Prometheus dashboard template or create a new one.