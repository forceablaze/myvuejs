
class NoFileIdFoundMessage:

    @staticmethod
    def getMessage(id): 
        return {'message': 'No such file id ({}) found.'.format(id)}
