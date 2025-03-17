import pytest
from unittest.mock import patch, MagicMock
from app.scanner import get_unused_vms

def test_get_unused_vms():
    with patch("app.scanner.compute_client.virtual_machines.list_all") as mock_list_all, \
         patch("app.scanner.compute_client.virtual_machines.instance_view") as mock_instance_view:

        mock_vm = MagicMock()
        mock_vm.id = "/subscriptions/sub-id/resourceGroups/test-rg/provides/Microsoft.Compute/virtualMachines/test-vm"
        mock_vm.name = "test-vm"
        mock_list_all.return_value = [mock_vm]

        mock_instance_view.return_value.statuses = [MagicMock(code="PowerState/deallocated")]

        result = get_unused_vms()
        assert len(result) == 1
        assert result[0]["name"] == "test-vm"
        assert result[0]["status"] == "deallocated"
