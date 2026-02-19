# 3D Data Processing Pipeline – Documentation

## 1. Overview

This repository contains a prototype automated 3D data processing workflow designed to evaluate whether a workflow engine can improve:

- automation

- processing time

- ease of use

- integration with external tools

- parallel processing

- fault handling

The pipeline is orchestrated using Argo Workflows and integrates containerized processing steps for handling 3D data.

The project demonstrates how modern data engineering tools such as Kubernetes, Docker, and object storage can be combined into a reproducible 3D processing pipeline.


## 2. Architecture

Core Components

| Component      | Purpose                               |
| -------------- | ------------------------------------- |
| Argo Workflows | Orchestrates the pipeline steps       |
| Kubernetes     | Executes containerized tasks          |
| Docker         | Provides reproducible environments    |
| MinIO          | Object storage for input/output files |
| Python scripts | Perform 3D processing tasks           |

High-level Flow

````
Input 3D data
   ↓
Upload to object storage (MinIO)
   ↓
Argo workflow triggers processing steps
   ↓
Parallel processing of meshes
   ↓
Results stored back in storage
   ↓
Outputs ready for visualization or analysis
````


## 3. Repository Structure

````
3D-data-processing-pipeline/
│
├── 3d_pipeline.yaml        # Argo workflow definition
├── mesh-test.py            # Example mesh processing script
├── README.md               # Basic project description
├── Final Presentation.pdf  # Project presentation
└── .gitignore
````


### File descriptions

3d_pipeline.yaml <- Defines the workflow executed by Argo.

Contains:

- workflow templates

- container steps

- dependencies between tasks

- storage configuration

This file is the main orchestration logic of the pipeline.

Final Presentation - Final.pdf

Explains:

project motivation

architecture decisions

evaluation criteria

results of automation tests

Useful for understanding design choices.

## 4. Workflow Execution Prerequisites

Install:

- Docker Desktop

- Kubernetes (Minikube or cluster)

- Argo Workflows

- MinIO (object storage)

- Python 3.9+

Optional:

WSL Ubuntu (if running on Windows)

### Step 1: Start Kubernetes

````
Start Docker Desktop
````

### Step 2: Install Argo

````
kubectl create namespace argo
kubectl apply -n argo -f https://raw.githubusercontent.com/argoproj/argo-workflows/stable/manifests/install.yaml
````

Verify:

````

kubectl get pods -n argo

````

Run:

````
argo submit 3d_pipeline.yaml
````


*** docker repo: https://hub.docker.com/repositories/ifte110
