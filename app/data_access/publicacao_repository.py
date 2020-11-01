from .repository_base import RepositoryBase
from .models import Publicacao

class PublicacaoRepository(RepositoryBase):
    def __init__(self):
        super().__init__(Publicacao)