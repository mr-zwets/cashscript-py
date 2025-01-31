class TransactionBuilder:
    def __init__(self, options):
        self.provider = options["provider"]
        self.inputs = []
        self.outputs = []
        self.locktime = "Placeholder locktime"
        self.max_fee = "Placeholder maxFee"

    def add_input(self, utxo, unlocker, options=None):
        return "Placeholder TransactionBuilder"

    def add_inputs(self, utxos, unlocker=None, options=None):
        return "Placeholder TransactionBuilder"

    def add_output(self, output):
        return "Placeholder TransactionBuilder"

    def add_outputs(self, outputs):
        return "Placeholder TransactionBuilder"

    def add_op_return_output(self, chunks):
        return "Placeholder TransactionBuilder"

    def set_locktime(self, locktime):
        return "Placeholder TransactionBuilder"

    def set_max_fee(self, max_fee):
        return "Placeholder TransactionBuilder"

    def check_max_fee(self):
        return "Placeholder void"

    def build(self):
        return "Placeholder transaction hex"

    async def send(self, raw=False):
        return "Placeholder TransactionDetails or string"

    async def get_tx_details(self, txid, raw=False):
        return "Placeholder TransactionDetails or string"
