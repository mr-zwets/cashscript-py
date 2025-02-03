from src.helpers.utils import *

class Contract:
    def __init__(self, artifact: dict, constructor_args, options=None):
        self.artifact = artifact
        self.constructor_args = constructor_args
        self.options = options
        self.provider = "Placeholder self.provider"
        self.address_type = options.get("addressType", "p2sh32") if options else "p2sh32"
        expected_properties = ["abi", "bytecode", "constructorInputs", "contractName", "compiler"]
        if not all(prop in artifact for prop in expected_properties):
            raise ValueError("Invalid or incomplete artifact provided")

        if len(artifact["constructorInputs"]) != len(constructor_args):
            expected_types = [input["type"] for input in artifact["constructorInputs"]]
            raise ValueError(
                f"Incorrect number of arguments passed to {artifact['contractName']} constructor. "
                f"Expected {len(artifact['constructorInputs'])} arguments ({expected_types}) "
                f"but got {len(constructor_args)}"
            )

        self.encoded_constructor_args = encode_constructor_args(constructor_args, artifact)
        self.redeem_script = generate_redeem_script(asm_to_script(artifact['bytecode']), self.encoded_constructor_args)

        self.name = artifact["contractName"]
        self.address = script_to_address(self.redeem_script, self.address_type, False)
        self.token_address = script_to_address(self.redeem_script, self.address_type, True)
        # self.address = scriptToAddress(self.redeem_script, self.provider.network, self.address_type, false)
        # self.token_address = scriptToAddress(self.redeem_script, self.provider.network, self.address_type, true)
        self.bytecode = script_to_bytecode(self.redeem_script).hex()
        self.bytesize = calculate_bytesize(self.redeem_script)
        self.opcount = count_opcodes(self.redeem_script)
        self.unlock = {}

        if len(artifact["abi"]) == 1:
            f = artifact["abi"][0]
            self.unlock[f["name"]] = self._create_unlocker(f)
        else:
            for i, f in enumerate(artifact["abi"]):
                self.unlock[f["name"]] = self._create_unlocker(f, i)

    def _create_unlocker(self, abiFunction, selector=None):
        def unlocker(*args):
            if len(abi_function["inputs"]) != len(args):
                expected_types = [input["type"] for input in abi_function["inputs"]]
                raise ValueError(
                    f"Incorrect number of arguments passed to function {abi_function['name']}. "
                    f"Expected {len(abi_function['inputs'])} arguments ({expected_types}) "
                    f"but got {len(args)}"
                )
            
            # TODO: Implement generate_unlocking_bytecode
            def generate_unlocking_bytecode():
                return "Placeholder"
            
            def generate_locking_bytecode():
                return address_to_lock_script(self.address)

            return {
                "generateUnlockingBytecode": generate_unlocking_bytecode,
                "generateLockingBytecode": generate_locking_bytecode
            }
        return unlocker


    async def get_balance(self):
        return "Placeholder bigint"

    async def get_utxos(self):
        return "Placeholder Utxo[]"
