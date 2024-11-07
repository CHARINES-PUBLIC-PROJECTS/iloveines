from contract_base import ContractBase
from contracts.inter_pf.validate import Validate
from contracts.inter_pf.sanitize import Sanitize

class InterPFContract(ContractBase):
    def validate(self):
        validator = Validate()
        return validator.run()

    def sanitize(self):
        sanitizer = Sanitize()
        return sanitizer.run()