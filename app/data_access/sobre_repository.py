from .repository_base import RepositoryBase
from .models import Sobre

class SobreRepository(RepositoryBase):
    def __init__(self):
        super().__init__(Sobre)