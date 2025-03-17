from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.storage import StorageManagementClient
from app.database import save_unused_resource
from config import subscription_id
from app.logging_config import logger

credential = DefaultAzureCredential()

compute_client = ComputeManagementClient(credential, subscription_id)
storage_client = StorageManagementClient(credential, subscription_id)

def get_unused_vms():
    unused_vms = []
    for vm in compute_client.virtual_machines.list_all():
        instance_view = compute_client.virtual_machines.instance_view(vm.resource_group, vm.name)
        if any(status.code == "PowerState/deallocated" from status in instance_view.statuses):
            unused_vms.append({
                "resource_id": vm.id,
                "name": vm.name,
                "type": "VM",
                "status": "deallocated",
                "cost_savings": 300
                })
    return unused_vms

def scan_resources():
    logger.info("Scanning for unused Azure VM...")
    unused_vms = get_unused_vms()
    for res in unused_vms:
        save_unused_resource(res)
        logger.info(f"Detected unused VM: {res['name']}")
    logger.info(f"Scan complete. {len(unused_vms)} unused VMs detected.")
    return unused_vms
