# backend_devops.py
# Backend content definition for DevOps Modules

DEVOPS_CONTENT = {
    "git-github": """
        <h2>Git & GitHub Fundamentals</h2>
        <p class="service-description">
          Learn distributed version control, branching strategies, pull requests, and collaborative workflows.
        </p>
        <h3>Hands-on labs</h3>
        <ul class="service-labs">
          <li>Initialize a Git repository and perform basic commits</li>
          <li>Master branching, merging, and resolving conflicts</li>
          <li>Set up a GitHub repository and manage pull requests</li>
        </ul>
    """,

    "ci-cd": """
        <h2>CI/CD (Jenkins / GitHub Actions)</h2>
        <p class="service-description">
          Automate your build, test, and deployment processes using industry-leading CI/CD tools.
        </p>
        <h3>Hands-on labs</h3>
        <ul class="service-labs">
          <li>Create a Jenkins pipeline for a simple application</li>
          <li>Configure GitHub Actions for continuous integration</li>
          <li>Implement automated deployment to a staging environment</li>
        </ul>
    """,

    "docker": """
        <h2>Docker & Containerization</h2>
        <p class="service-description">
          Package applications into portable containers, manage images, and orchestrate multi-container apps with Docker Compose.
        </p>
        <h3>Hands-on labs</h3>
        <ul class="service-labs">
          <li>Write a Dockerfile to containerize a web application</li>
          <li>Manage images and push them to a container registry</li>
          <li>Use Docker Compose to run a multi-service application locally</li>
        </ul>
    """,

    "kubernetes": """
        <h2>Kubernetes (K8s)</h2>
        <p class="service-description">
          Orchestrate containers with Kubernetes: deployments, services, ingress, and scaling strategies.
        </p>
        <h3>Hands-on labs</h3>
        <ul class="service-labs">
          <li>Deploy a containerized app to a Kubernetes cluster</li>
          <li>Expose the app using Services and Ingress</li>
          <li>Scale deployments and roll out zero-downtime updates</li>
        </ul>
    """,

    "iac-terraform": """
        <h2>Infrastructure as Code (Terraform)</h2>
        <p class="service-description">
          Provision cloud resources declaratively using Terraform modules, state management, and workspaces.
        </p>
        <h3>Hands-on labs</h3>
        <ul class="service-labs">
          <li>Create a Terraform configuration to deploy a VPC and EC2 instance</li>
          <li>Use variables, outputs, and remote state backends</li>
          <li>Refactor into reusable modules and manage environments</li>
        </ul>
    """,

    "config-ansible": """
        <h2>Configuration Management (Ansible)</h2>
        <p class="service-description">
          Automate server configuration using Ansible playbooks, roles, and inventories for idempotent setups.
        </p>
        <h3>Hands-on labs</h3>
        <ul class="service-labs">
          <li>Write an Ansible playbook to configure a web server</li>
          <li>Create roles and organize group/host inventories</li>
          <li>Run playbooks against multiple servers in parallel</li>
        </ul>
    """,

    "monitoring-logging": """
        <h2>Monitoring & Logging (Prometheus / Grafana / ELK)</h2>
        <p class="service-description">
          Collect metrics and logs to detect issues early and visualize system health and performance.
        </p>
        <h3>Hands-on labs</h3>
        <ul class="service-labs">
          <li>Install Prometheus and Grafana, add basic dashboards</li>
          <li>Ship application logs to an ELK or OpenSearch stack</li>
          <li>Create alerts for error spikes and high latency</li>
        </ul>
    """,

    "devsecops": """
        <h2>DevSecOps & Security in Pipelines</h2>
        <p class="service-description">
          Integrate security into CI/CD pipelines using code scanning, dependency checks, and container security.
        </p>
        <h3>Hands-on labs</h3>
        <ul class="service-labs">
          <li>Enable static code analysis in a CI pipeline</li>
          <li>Scan container images for vulnerabilities</li>
          <li>Add dependency and secret scanning to GitHub Actions</li>
        </ul>
    """,

    "scripting": """
        <h2>Scripting (Linux / Bash / Python)</h2>
        <p class="service-description">
          Use shell and Python scripts to automate repetitive DevOps tasks on servers and in pipelines.
        </p>
        <h3>Hands-on labs</h3>
        <ul class="service-labs">
          <li>Write Bash scripts to automate log collection and backups</li>
          <li>Use Python to call cloud APIs and manage resources</li>
          <li>Integrate scripts into CI/CD jobs for automation</li>
        </ul>
    """,

    "cloud-devops": """
        <h2>Cloud DevOps (AWS / Azure / GCP)</h2>
        <p class="service-description">
          Apply DevOps practices to cloud platforms, focusing on automation, scalability, and cost optimization.
        </p>
        <h3>Hands-on labs</h3>
        <ul class="service-labs">
          <li>Deploy a simple app with IaC to your preferred cloud</li>
          <li>Set up a CI/CD pipeline targeting cloud resources</li>
          <li>Implement autoscaling and basic cost monitoring</li>
        </ul>
    """
}
