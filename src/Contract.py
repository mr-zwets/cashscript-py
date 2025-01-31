class Contract:
    def __init__(self, artifact, constructor_args, options=None):
        self.artifact = artifact
        self.constructor_args = constructor_args
        self.options = options
        self.provider = "Placeholder provider"
        self.address_type = "Placeholder addressType"
        self.encoded_constructor_args = "Placeholder encodedConstructorArgs"
        self.redeem_script = "Placeholder redeemScript"
        self.functions = "Placeholder functions"
        self.unlock = "Placeholder unlock"
        self.name = "Placeholder name"
        self.address = "Placeholder address"
        self.token_address = "Placeholder tokenAddress"
        self.bytecode = "Placeholder bytecode"
        self.bytesize = "Placeholder bytesize"
        self.opcount = "Placeholder opcount"

    async def get_balance(self):
        return "Placeholder bigint"

    async def get_utxos(self):
        return "Placeholder Utxo[]"

    def create_function(self, abi_function, selector=None):
        return "Placeholder ContractFunction"

    def create_unlocker(self, abi_function, selector=None):
        return "Placeholder ContractUnlocker"
