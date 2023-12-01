from .models import City


class CityRepository:
    data = City.objects.all()

    @classmethod
    def get_city(cls, city):
        if city == '':
            return None
        try:
            c = cls.data.get(name=city)
        except City.DoesNotExist:
            return None
        return c
