class SignatureTemplate:
    def __init__(self, signer, hashtype="Placeholder HashType", signature_algorithm="Placeholder SignatureAlgorithm"):
        self.private_key = "Placeholder privateKey"

    def generate_signature(self, payload, bch_fork_id=None):
        return "Placeholder Uint8Array"

    def get_hash_type(self, bch_fork_id=True):
        return "Placeholder number"

    def get_signature_algorithm(self):
        return "Placeholder SignatureAlgorithm"

    def get_public_key(self):
        return "Placeholder Uint8Array"

    def unlock_p2pkh(self):
        return {
            "generateLockingBytecode":"test",
            "generateUnlockingBytecode": "test",
        }
