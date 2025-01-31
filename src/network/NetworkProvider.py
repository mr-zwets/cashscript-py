from typing import List

class NetworkProvider:
    def __init__(self):
        self.network = "Placeholder Network"

    async def get_utxos(self, address: str) -> List[str]:
        return "Placeholder Utxo[]"

    async def get_block_height(self) -> int:
        return "Placeholder number"

    async def get_raw_transaction(self, txid: str) -> str:
        return "Placeholder hex transaction"

    async def send_raw_transaction(self, tx_hex: str) -> str:
        return "Placeholder transaction ID"
