from contract_base import ContractBase
from contracts.itau_pj.validate import Validate
from contracts.itau_pj.sanitize import Sanitize

class ItauPJContract(ContractBase):
    def validate(self):
        validator = Validate()
        return validator.run()

    def sanitize(self):
        sanitizer = Sanitize()
        return sanitizer.run()