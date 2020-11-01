from .repository_base import RepositoryBase
from .models import Ladies

class LadiesRepository(RepositoryBase):
    def __init__(self):
        super().__init__(Ladies)