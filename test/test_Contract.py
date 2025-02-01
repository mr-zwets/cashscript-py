import pytest
import json
import sys
sys.path.append('../src')
from src.Contract import Contract

# Load artifacts
def load_json_fixture(path):
    with open(path, "r") as file:
        return json.load(file)

p2pkhArtifact = load_json_fixture("./test/fixture/p2pkh.json")
twtArtifact = load_json_fixture("./test/fixture/transfer_with_timeout.json")
hodlVaultArtifact = load_json_fixture("./test/fixture/hodl_vault.json")
mecenasArtifact = load_json_fixture("./test/fixture/mecenas.json")
boundedBytesArtifact = load_json_fixture("./test/fixture/bounded_bytes.json")

@pytest.fixture
def contract():
    constructor_args = [placeholder(65), placeholder(65), 1000000]
    return Contract(twtArtifact, constructor_args, {"addressType": "p2sh32"})

# Helper function for simulating placeholder values of a given size
def placeholder(size):
    return "00" * size 

def placeholderBytes(size: int) -> bytearray:
    return bytearray(size)

@pytest.mark.skip(reason="Functionality not yet implemented")
def test_fail_incorrect_constructor_args():
    with pytest.raises(ValueError):
        Contract(p2pkhArtifact, [])

    with pytest.raises(ValueError):
        Contract(p2pkhArtifact, [20])

    with pytest.raises(ValueError):
        Contract(p2pkhArtifact, [placeholder(20), placeholder(20)])

    with pytest.raises(ValueError):
        Contract(p2pkhArtifact, [placeholder(19)])

    with pytest.raises(ValueError):
        Contract(p2pkhArtifact, [placeholder(21)])

def test_fail_incomplete_artifact():
    incomplete_artifacts = [
        {**p2pkhArtifact, "abi": None},
        {**p2pkhArtifact, "bytecode": None},
        {**p2pkhArtifact, "constructorInputs": None},
        {**p2pkhArtifact, "contractName": None},
    ]
    
    with pytest.raises(ValueError):
        Contract(incomplete_artifacts, [])

def test_create_p2pkh_instance():
    instance = Contract(p2pkhArtifact, [placeholder(20)], {"addressType": "p2sh20"})

    assert instance.address == "bitcoincash:pphszjt47dtl5t70ntlfmfxj23rxqklsyv94hs7vmt"
    assert instance.name == p2pkhArtifact["contractName"]

def test_create_transfer_with_timeout_instance():
    constructor_args = [placeholder(65), placeholder(65), 1000000]
    instance = Contract(twtArtifact, constructor_args, {"addressType": "p2sh20"})

    assert instance.address == "bitcoincash:pq6y95a62d597cahdaweehfrk8m920v3echjjmyf4l"
    assert instance.name == twtArtifact["contractName"]

def test_create_hodl_vault_instance():
    constructor_args = [placeholder(65), placeholder(65), 1000000, 10000]
    instance = Contract(hodlVaultArtifact, constructor_args, {"addressType": "p2sh20"})

    assert instance.address == "bitcoincash:pzj96a4mqd4mxec678nprgxshmc9egwpwg4pjexc7c"
    assert instance.name == hodlVaultArtifact["contractName"]

def test_create_mecenas_instance():
    constructor_args = [placeholder(20), placeholder(20), 1000000]
    instance = Contract(mecenasArtifact, constructor_args, {"addressType": "p2sh20"})

    assert instance.address == "bitcoincash:ppdmhypgpyl4e6mz8urrq56ur3wnr9cm45k8q5cva3"
    assert instance.name == mecenasArtifact["contractName"]

@pytest.mark.asyncio
async def test_get_balance(contract):
    assert await contract.get_balance() == "Placeholder bigint"

@pytest.mark.asyncio
async def test_get_utxos(contract):
    assert await contract.get_utxos() == "Placeholder Utxo[]"

def test_create_unlocker(contract):
    assert contract.create_unlocker("Placeholder abi_function") == "Placeholder ContractUnlocker"
