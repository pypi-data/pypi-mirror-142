from pymongo import MongoClient,errors
import logging as log
from abc import ABC, abstractmethod

class MongoDB(ABC):
    #
    # Credenciales de Conexión a MongoDB
    #
    host = ''
    user = ''
    password = ''
    dbname = ''
    port = 27017
    options = "authSource=admin&replicaSet=atlas-of1upp-shard-0&w=majority&readPreference=primary&appname=MongoDB%20Compass&retryWrites=true&ssl=true"
    #
    # Otras Propiedades relevantes
    #
    collection = ''  # Nombre de la colección a consultar
    client = None  # Cliente MongoDB
    conn = None  # Conexión a MongoDB
    projection = {}  # Diccionario con los campos seleccionados (projection MongoDB)
    filters = {}  # Diccionario con los filtros (por lo general por Fecha)
    metadata = None  # Dataframe con la metadata
    campos_disponibles = {}  # Campos que estan disponibles para ser seleccionados (obtenidos de la metadata)
    field_date = ''  # Campo de fecha que se utiliza para realizar los filtros

    def getMongoClient(self):
        return MongoClient(f'mongodb://{self.user}:{self.password}@{self.host}/{self.dbname}?{self.options}')

    def getMongoDb(self):
        """Genera la conexión a MongoDB"""
        self.client = MongoClient(f'mongodb://{self.user}:{self.password}@{self.host}/{self.dbname}?{self.options}')
        self.conn = self.client[self.dbname][self.collection]
        return self.conn

    def helper_rangedate(self, fecha):
        """Genera un filtro por fecha"""
        log.debug(f"Generando filtro por fecha helper_rangedate: {fecha}")
        from datetime import datetime
        return {
            '$gte': datetime.strptime(f"{fecha} 00:00:00", '%Y-%m-%d %H:%M:%S'),
            '$lt': datetime.strptime(f"{fecha} 23:59:59", '%Y-%m-%d %H:%M:%S')
        }

    def filtro_fecha(self, fecha):
        """
        Incorpora un filtro por fecha a la Query MongoDB

        :param fecha: Fecha en formato YYYY-MM-DD
        :return:
        """
        log.debug(f"Generando filtro MongoDB por fecha: {fecha}")
        from datetime import datetime
        filter = {
            self.field_date: {
                '$gte': datetime.strptime(f"{fecha} 00:00:00", '%Y-%m-%d %H:%M:%S'),
                '$lt': datetime.strptime(f"{fecha} 23:59:59", '%Y-%m-%d %H:%M:%S')
            }
        }
        self.filters.update(filter)
        return self

    def filtro_simple(self, field_name, value):
        """Incorpora un filtro por _id del documento"""
        log.debug(f"Generando filtro simple en MongoDB por campo {field_name}: {value}")

        filter = {
            field_name: {
                '$eq': value
            }
        }
        self.filters.update(filter)
        return self

    def filtro_id(self, id, field_name='_id'):
        """Incorpora un filtro por _id del documento"""
        log.debug(f"Generando filtro MongoDB por id: {id}")

        filter = {
            '_id': {
                '$eq': id
            }
        }
        self.filters.update(filter)
        return self

    def execute(self, limit=5, timeout_seconds=3):
        """Consulta la la base de datos MongoDB, se obtiene un cursor (la data todavía no viaja)"""
        db = self.getMongoDb()
        try:
            result = db.find(
                filter=self.filters,
                projection=self.projection,
                limit=limit,
                max_time_ms=timeout_seconds * 1000
            )
        except errors.ExecutionTimeout as e:
            log.error('Timeout')
            raise Exception("La consulta fue abortada por un Timeout")
        except Exception as e:
            log.error(e)
            raise Exception(e)
        return result

    def cantidad_registros(self, fecha=None, timeout_seconds=3):
        """Consulta la la base de datos MongoDB, se obtiene un cursor (la data todavía no viaja)"""
        db = self.getMongoDb()
        try:
            if fecha:
                self.filtro_fecha(fecha)
            result = db.find(
                filter=self.filters,
                projection=self.projection,
                limit=0,
                max_time_ms=timeout_seconds * 1000
            )
            return result.count()
        except errors.ExecutionTimeout as e:
            log.error('Timeout')
            raise Exception("La consulta fue abortada por un Timeout")
        except Exception as e:
            log.error(e)
            raise Exception(e)

    def to_df(self, limit=0, timeout_seconds=60, normalize_level=0):
        """Carga el resultado de la Query en un Dataframe pandas.
        Retorna el dataframe.

        **limit**           : El limite de registros a cargar, si es 0 es infinito.
        **timeout_seconds** : Cantidad de segundos antes que la Query sea abortada por timeout
        **normalize_level** : Indica el nivel de profundidad para normalizar las subestructuras hacia columnas dataframe
        """
        data = self.execute(limit, timeout_seconds)
        import pandas as pd
        df = pd.json_normalize(data, max_level=normalize_level)
        return df

    def select(self, campos_seleccionados='*'):
        """
        Campos a seleccionar en la salida del dataframe.
        **campos_seleccionados**: Puede ser un string separado por comas o un objeto list.
        En caso de querer todos los campos prioritarios, se debe poner un asteristo '*'.
        """
        if isinstance(campos_seleccionados, str):
            campos_seleccionados = campos_seleccionados.split(",")

        if not isinstance(campos_seleccionados, list):
            raise Exception('Se requiere ingresar los campos como lista o string separado por comas')

        campos_disponibles = self.campos_disponibles
        for campo in campos_disponibles:
            if campo in campos_seleccionados or '*' in campos_seleccionados:
                codigo = campos_disponibles[campo]
                if codigo[0] == '$':
                    valor = codigo
                elif codigo[0] in ["'", '"', '{']:
                    valor = eval(codigo)
                else:
                    msg = f"valor de celda projection es desconocido: {codigo}"
                    log.error(msg)
                    raise Exception(msg)
                llave = campo
                self.projection.update({llave: valor})
        return self

    def where(self, filtros_seleccionados):  # @todo Mejorar
        """
        Filtros a incorporar en la consulta, debe ser alguno de los predefinidos.
        Son de uso netamente de desarrollo para hacer Data Profiling
        """
        if isinstance(filtros_seleccionados, str):
            filtros_seleccionados = filtros_seleccionados.split(",")

        if not isinstance(filtros_seleccionados, list):
            raise Exception('Se requiere ingresar los nombres de filtros como lista o string separado por comas')

        filtros_disponibles = self.get_filtros_disponibles()
        for filter in filtros_disponibles:
            if filter in filtros_seleccionados:
                self.filters.update(filtros_disponibles[filter])
        return self

    @abstractmethod
    def get_filtros_disponibles(self):
        """Son los filtros disponibles para aplicar a la Query MongoDB, utilizarlos con cuidado,
        solo son para desarrollo y Data Profiling"""
        pass
