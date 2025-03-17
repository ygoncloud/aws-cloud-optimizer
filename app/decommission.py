from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient
from app.database import SessionLocal, CloudResource
from config import subscription_id
from app.logging_config import logger

credential = DefaultAzureCredential()
compute_client = ComputeManagementClient(credential, subscription_id)

def deallocate_vm(vm_id, resource_group, vm_name):
    """Deallocate (stop) the unused VM."""
    compute_client.virtual_machines.begin_deallocate(resource_group_name=resource_group, vm_name=vm_name)

def delete_vm(vm_id, resource_group, vm_name):
    """Delete the unused VM."""
    compute_client.virtual_machines.begin_delete(resource_group_name=resource_group, vm_name=vm_name)

def decommission_resources():
    """Deallocate or delete unused Azure VM."""
    db = SessionLocal()
    unused_resources = db.query(CloudResource).filter(CloudResource.status == "deallocated").all()

    for res in unused_resources:
        # Extract resource group and VM name from resource_id
        parts = res.resource_id.split("/")
        try:
            rg_index = parts.index("resourceGroups") + 1
            resource_group = parts[rg_index]
            vm_name = parts[-1]

            # Deallocate or Delete the VM
            delete_vm(res.resource_id, resource_group, vm_name)

            # Remove from database
            db.delete(res)
            db.commit()
        except Exception as e:
            print(f"Error processing resource {res.resource_id}: {e}")

    db.close()
    return {"message": "Unused Azure resources decommissioned successfully."}

if __name__ == "__main__":
    print(decommission_resources())
