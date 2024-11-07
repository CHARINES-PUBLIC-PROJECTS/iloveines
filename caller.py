from contracts.inter_pj.contract import InterPJContract
from contracts.itau_pj.contract import ItauPJContract
from contracts.inter_pf.contract import InterPFContract

class Caller:
    def __init__(self, contract_type):
        self.contract = self._load_contract(contract_type)

    def _load_contract(self, contract_type):
        if contract_type == "itau":
            return ItauPJContract()
        elif contract_type == "interpj":
            return InterPJContract()
        elif contract_type == "interpf":
            return InterPFContract()
        else:
            raise ValueError(f"Unknown contract type: {contract_type}")

    def execute(self):
        print(self.contract.validate())
        print(self.contract.sanitize())

# Exemplo de uso
caller = Caller("interpj")
caller.execute()
