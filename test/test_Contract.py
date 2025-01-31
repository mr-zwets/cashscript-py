import pytest
import sys
sys.path.append('../src')
from src.Contract import Contract

@pytest.fixture
def contract():
    return Contract("Placeholder artifact", "Placeholder constructor_args", "Placeholder options")

@pytest.mark.asyncio
async def test_get_balance(contract):
    assert await contract.get_balance() == "Placeholder bigint"

@pytest.mark.asyncio
async def test_get_utxos(contract):
    assert await contract.get_utxos() == "Placeholder Utxo[]"

def test_create_function(contract):
    assert contract.create_function("Placeholder abi_function") == "Placeholder ContractFunction"

def test_create_unlocker(contract):
    assert contract.create_unlocker("Placeholder abi_function") == "Placeholder ContractUnlocker"
