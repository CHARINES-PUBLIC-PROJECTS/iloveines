from contract_base import ContractBase
from contracts.inter_pj.validate import Validate
from contracts.inter_pj.sanitize import Sanitize

class InterPJContract(ContractBase):
    def validate(self):
        validator = Validate()
        return validator.run()

    def sanitize(self):
        sanitizer = Sanitize()
        return sanitizer.run()