# README.md

# Azure Cloud Resource Optimizer

Automated detection and decommissioning of unused Azure cloud resources.

## 🚀 Overview
This project provides a framework to help Azure users automatically:

- Detect unused or deallocated Azure Virtual Machines (VMs).
- Log and store resource information.
- Decommission (delete) unused resources.
- Schedule regular scans and cleanup using GitHub Actions.

**Tech Stack:**
- Python 3.9
- Azure SDK (Azure Identity, Compute)
- FastAPI (API endpoints)
- SQLAlchemy (SQLite/PostgreSQL)
- GitHub Actions (CI/CD automation)

---

## 🛠️ Setup Instructions

### 1️⃣ Clone Repository
```bash
git clone https://github.com/your-username/azure-cloud-optimizer.git
cd azure-cloud-optimizer
```

### 2️⃣ Configure Azure Credentials

This project uses **Azure Default Credentials**:
- **Locally**: Set environment variables or use Azure CLI authenticated session.
- **GitHub Actions**: Add secrets under repository settings:

| Secret Name             | Value                                      |
|------------------------|--------------------------------------------|
| `AZURE_CLIENT_ID`      | Your Azure Client ID                       |
| `AZURE_CLIENT_SECRET`  | Your Azure Client Secret                   |
| `AZURE_TENANT_ID`      | Your Azure Tenant ID                       |
| `AZURE_SUBSCRIPTION_ID`| Your Azure Subscription ID                 |

Also create a `.env` file for local development:
```bash
AZURE_SUBSCRIPTION_ID=your-subscription-id
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

### Manual Run (Local)
```bash
# Run scan
PYTHONPATH=. python scripts/run_scan.py

# Run decommission
PYTHONPATH=. python app/decommission.py
```

### API Server (Optional)
```bash
uvicorn app.main:app --reload
```
Then visit `http://127.0.0.1:8000/docs` for API endpoints.

### GitHub Actions Automation

Pre-configured `.github/workflows/cron-job.yml` runs:
- Daily scan and decommission jobs.

Customize schedule as needed:
```yaml
schedule:
  - cron: '0 3 * * *'  # Runs daily at 3 AM UTC
```

---

## ✅ Features
- Detect **deallocated** Azure VMs.
- Store detected unused resources in **SQLite/PostgreSQL**.
- Decommission resources with **safe deletion** logic.
- Extensible to include Storage Accounts, Disks, Databases.
- Works with **GitHub Actions** (fully automated) or manual triggers.
- Easy integration with dashboards or alerts (Slack, Email).

---

## 🔥 Next Steps
- [ ] Extend detection logic to more Azure resource types.
- [ ] Add notification integrations (Slack/Email).
- [ ] Provide a Streamlit dashboard for reporting.
- [ ] Support PostgreSQL backend for production use.

---

## 🤝 Contributions
This framework is intentionally designed to be extendable by other Azure users! Feel free to:
- Fork it.
- Customize scanning logic.
- Add resource types or cost estimations.
- Submit PRs! 🚀

---

## 📄 License
MIT License.

