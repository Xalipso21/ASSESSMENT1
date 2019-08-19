from question4.orm import ORM


class Branch(ORM):

    tablename = 'branchs'
    fields = ['city', 'state', 'zipcode']

    def __init__(self, **kwargs):
        self.pk = kwargs.get('pk')
        self.city = kwargs.get('city')
        self.state = kwargs.get('state')
        self.zipcode = kwargs.get('zipcode')


        