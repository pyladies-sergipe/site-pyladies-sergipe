from .repository_base import RepositoryBase
from .models import Eventos

class EventosRepository(RepositoryBase):
    def __init__(self):
        super().__init__(Eventos)