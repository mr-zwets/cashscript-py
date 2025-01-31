import pytest
import sys
sys.path.append('../src')
from src.SignatureTemplate import SignatureTemplate

def test_generate_signature():
    obj = SignatureTemplate("Placeholder signer")
    assert obj.generate_signature("Placeholder payload") == "Placeholder Uint8Array"

def test_get_hash_type():
    obj = SignatureTemplate("Placeholder signer")
    assert obj.get_hash_type() == "Placeholder number"

def test_get_signature_algorithm():
    obj = SignatureTemplate("Placeholder signer")
    assert obj.get_signature_algorithm() == "Placeholder SignatureAlgorithm"

def test_get_public_key():
    obj = SignatureTemplate("Placeholder signer")
    assert obj.get_public_key() == "Placeholder Uint8Array"

def test_unlock_p2pkh():
    obj = SignatureTemplate("Placeholder signer")
    unlocker = obj.unlock_p2pkh()
    assert unlocker["generateLockingBytecode"] == "test"
    assert unlocker["generateUnlockingBytecode"]     == "test"