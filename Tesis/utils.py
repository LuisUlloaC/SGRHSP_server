from datetime import datetime


def getDateByStrig(date):
    date_time_obj = datetime.strptime(date, '%Y-%m-%d - %H:%M:%S')
    return date_time_obj


def getStringByDate(date):
    date_time = date.strftime("%Y-%m-%d - %H:%M:%S")
    return date_time


def getLoginErrorMessage() -> str:
    return 'La contraseña es incorrecta, por favor, inténtelo otra vez'


def getUserNotExistMessage(username) -> str:
    return f'No existe una cuenta con el nombre de usuario ({username}), por favor, inténtelo otra vez'


def getNoAdminDeleteMessage(username) -> str:
    message = f'Lo sentimos. El usuario {username} es el único administrador, no puede dejar el sistema sin ' \
              f'administradores'
    return message


def getDeleteErrorMessage(objectType) -> str:
    return f'No puede eliminar ciertas instancias del {objectType} porque otras entidades dependen de ella'


def getUniqueObjectErrorMessage(objectType) -> str:
    return f'Ya existe un objeto con el nombre "{objectType}"'


def getCategoryNoExistError() -> str:
    return 'Ha ocurrido un error al reconstruir la lista de los Cargos de Trabajadores, recuerde que los cargos ' \
           'dependen de las categorías ocupacionales, por favor, asegúrese de tener sincronizadas todas las ' \
           'Categorías Ocupacionales '


def getNeedCatForWorkerError() -> str:
    return f'Ha ocurrido un error. Asegúrese de que todas las Categorías Ocupacionales estén sincronizadas'

