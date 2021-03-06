class RepositoryBase:
    def __init__(self, model):
        self.model = model

    def update(self, obj, updated_data={}):
        return obj.save(**updated_data)

    def delete(self, obj):
        obj.delete()

    def create(self, obj):
        return self.model.objects.get_or_create(**obj)

    def get_all(self, query_params={}, orderby=[], select_related=[], values=[], flat=False):
        return self.model.objects.select_related(*select_related).filter(**query_params).order_by(*orderby)

    def get(self, query_params={}, select_related=[]):
        return self.model.objects.select_related(*select_related).get(**query_params)

    def exists(self, query_params={}):
        return self.model.objects.filter(**query_params).exists()