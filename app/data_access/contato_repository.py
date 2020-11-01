from .repository_base import RepositoryBase
from .models import Contato

class ContatoRepository(RepositoryBase):
    def __init__(self):
        super().__init__(Contato)