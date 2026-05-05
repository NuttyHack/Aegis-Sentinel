# Aegis-Sentinel 🛡️
A Local LLM Security Gateway designed to detect and mitigate Prompt Injection attacks.

## 🚀 Overview
Aegis-Sentinel acts as a middleware firewall between users and LLMs. It uses a quantized **Llama 3.2 1B** model to perform semantic analysis on incoming prompts, scoring them for malicious intent before they reach the core system.

## 🛠️ Tech Stack
- **Language:** Python 3.11+
- **Brain:** Llama 3.2 1B (via Ollama)
- **Framework:** FastAPI / Uvicorn
- **Security:** Adversarial Red-Teaming Suite included.

## 📈 Performance Optimization
Optimized for resource-constrained environments (VMs/Edge) using:
- Context Window Sharding (`num_ctx: 256`)
- CPU Thread Pinning
- Model Warm-start strategies
