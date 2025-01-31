import pytest
import sys
sys.path.append('../src')
from src.TransactionBuilder import TransactionBuilder

@pytest.fixture
def transaction_builder():
    return TransactionBuilder({"provider": "Placeholder provider"})

def test_add_input(transaction_builder):
    assert transaction_builder.add_input("Placeholder utxo", "Placeholder unlocker") == "Placeholder TransactionBuilder"

def test_add_inputs(transaction_builder):
    assert transaction_builder.add_inputs(["Placeholder utxo"]) == "Placeholder TransactionBuilder"

def test_add_output(transaction_builder):
    assert transaction_builder.add_output("Placeholder output") == "Placeholder TransactionBuilder"

def test_add_outputs(transaction_builder):
    assert transaction_builder.add_outputs(["Placeholder output"]) == "Placeholder TransactionBuilder"

def test_add_op_return_output(transaction_builder):
    assert transaction_builder.add_op_return_output(["Placeholder chunks"]) == "Placeholder TransactionBuilder"

def test_set_locktime(transaction_builder):
    assert transaction_builder.set_locktime("Placeholder locktime") == "Placeholder TransactionBuilder"

def test_set_max_fee(transaction_builder):
    assert transaction_builder.set_max_fee("Placeholder maxFee") == "Placeholder TransactionBuilder"

def test_check_max_fee(transaction_builder):
    assert transaction_builder.check_max_fee() == "Placeholder void"

def test_build(transaction_builder):
    assert transaction_builder.build() == "Placeholder transaction hex"

@pytest.mark.asyncio
async def test_send(transaction_builder):
    assert await transaction_builder.send() == "Placeholder TransactionDetails or string"

@pytest.mark.asyncio
async def test_get_tx_details(transaction_builder):
    assert await transaction_builder.get_tx_details("Placeholder txid") == "Placeholder TransactionDetails or string"
