import os
from fileinput import filename

from ImportarSurvey.Utiles import FILE_HANDLER, STREAM_HANDLER, JsonFile, ToolboxLogger
from ImportarSurvey.PrecargarEncuestas import PrecargarEncuestas
from ImportarSurvey.InyectarEncuestas import InyectarEncuestas
from ImportarSurvey.ArcGISPythonApiDataAccess import ArcGISPythonApiDataAccess

STATISTICS_FILE = "__estadisticas.json"

class ProcesarEncuestas :

    @staticmethod 
    def BorrarEncuestas(
        portal = None, 
        usuario = None, 
        clave = None, 
        servicioEncuesta = None, 
        debug = False,
        rutaSalida = '', 
        salidaRelativa = False) :

        LOG_FILE = "__logBorrarEncuestasVSCode"
        alias = "LogBorrarEncuestasVSCode"

        folder_path = os.path.dirname(os.path.realpath(__file__))
        log_path = os.path.normpath(os.path.join(folder_path, rutaSalida)) if salidaRelativa else rutaSalida

        ToolboxLogger.initLogger(source=alias, log_path=log_path, log_file=LOG_FILE)
        ToolboxLogger.setDebugLevel() if debug else ToolboxLogger.setInfoLevel()

        ToolboxLogger.info("Iniciando {}".format(alias))
        ToolboxLogger.info("Ruta Salida: {}".format(log_path)) if rutaSalida != '' else None

        fuente_da = ArcGISPythonApiDataAccess(portal, usuario, clave)
        fuente_da.setFeatureService(servicioEncuesta)

        numRegistros = 0

        for tabla in fuente_da.getServiceTables() :
            registros = fuente_da.query(tabla, [tabla.properties.objectIdField])
            fuente_da.delete(tabla, registros)
            numRegistros += len(registros)
            ToolboxLogger.debug("Tabla: {} Borrados: {}".format(tabla.properties.name, len(registros)))

        for capa in fuente_da.getServiceLayers() :
            registros = fuente_da.query(capa, [capa.properties.objectIdField])
            fuente_da.delete(capa, registros)
            numRegistros += len(registros)
            ToolboxLogger.debug("Capa: {} Borrados: {}".format(capa.properties.name, len(registros)))

        ToolboxLogger.info("Total Borrados: {}".format(numRegistros))

    @staticmethod
    def Precargar(alias = '',
        archivoLog = '',
        portal = None, 
        usuario = None, 
        clave = None, 
        usuarioCampo = None,
        servicioFuente = None, 
        versionFuente = None, 
        servicioDestino = None, 
        idsPrecarga = None, 
        debug = False, 
        tipoRegistro = (FILE_HANDLER | STREAM_HANDLER),
        rutaSalida = '', 
        salidaRelativa = False, 
        agregarEstadistica = True) :

        CONFIG_BACKWARD_PATH = "_precarga_geo.json"
        LOG_BACKWARD_FILE = "__logPrecargarEncuestasVsCode" if archivoLog == '' else archivoLog
        alias = "PrecargarEncuestasVSCode" if alias == '' else alias

        folder_path = os.path.dirname(os.path.realpath(__file__))
        config_path = os.path.join(folder_path, CONFIG_BACKWARD_PATH)
        log_path = os.path.normpath(os.path.join(folder_path, rutaSalida)) if salidaRelativa else rutaSalida

        ToolboxLogger.initLogger(source = alias, log_path = log_path, log_file = LOG_BACKWARD_FILE, handler_type = tipoRegistro)
        ToolboxLogger.setDebugLevel() if debug else ToolboxLogger.setInfoLevel()

        encuestas = 0
        registros = 0
        errores = 0
        version = ''

        usuario_valido = (portal and usuario and clave) or (not portal and not usuario and not clave)
        if servicioFuente and versionFuente and servicioDestino and idsPrecarga and usuario_valido:
            ToolboxLogger.info("Iniciando {}".format(alias))
            ToolboxLogger.info("Ruta Salida: {}".format(log_path)) if rutaSalida != '' else None

            preloader = PrecargarEncuestas(config_path, 
                portal, 
                usuario, 
                clave,
                servicioFuente, 
                servicioDestino, 
                usuarioCampo= usuarioCampo,
                versionFuente = versionFuente,
                idsPrecarga = idsPrecarga
            )

            resultado  = preloader.Ejecutar()
            if resultado: 
                encuestas = resultado[0]
                registros = resultado[1]
                errores = resultado[2]
                version = preloader.versionFuente

            ToolboxLogger.info("Versión: {}".format(version))
            ToolboxLogger.info("Encuestas: {}".format(encuestas))
            ToolboxLogger.info("Registros: {}".format(registros))
            ToolboxLogger.info("Errores: {}".format(errores))

            if agregarEstadistica:
                filename = os.path.join(log_path, STATISTICS_FILE)
                estadisticas = JsonFile.readFile(filename)
                estadisticas.append(preloader.registroEjecucion())
                JsonFile.writeFile(filename, estadisticas)

        else:
            if not portal:
                ToolboxLogger.info("No se definió Portal")
            if not usuario:
                ToolboxLogger.info("No se definió Usuario")
            if not clave:
                ToolboxLogger.info("No se definió Clave")
            if not servicioFuente:
                ToolboxLogger.info("No se definió Servicio Fuente")
            if not versionFuente:
                ToolboxLogger.info("No se definió Versión Fuente")
            if not servicioDestino:
                ToolboxLogger.info("No se definió Servicio Destino")
            if not idsPrecarga:
                ToolboxLogger.info("No se definieron IDs de Precarga")

        return encuestas, registros, errores, version

    @staticmethod
    def Inyectar(alias = '',
        archivoLog = '',
        portal = None, 
        usuario = None, 
        clave = None, 
        usuarioCampo = None,
        servicioFuente = None, 
        servicioDestino = None,
        versionDestino = None, 
        debug = False, 
        tipoRegistro = (FILE_HANDLER | STREAM_HANDLER),
        rutaSalida = '', 
        salidaRelativa = False, 
        agregarEstadistica = True) :

        CONFIG_PATH = "_inyeccion_geo.json"
        LOG_FILE = "__logInyectarEncuestasVSCode" if archivoLog == '' else archivoLog
        alias = "LogInyectarEncuestasVSCode" if alias == '' else alias

        folder_path = os.path.dirname(os.path.realpath(__file__))
        config_path = os.path.join(folder_path, CONFIG_PATH)
        log_path = os.path.normpath(os.path.join(folder_path, rutaSalida)) if salidaRelativa else rutaSalida

        ToolboxLogger.initLogger(source = alias, log_path = log_path, log_file = LOG_FILE, handler_type = tipoRegistro)
        ToolboxLogger.setDebugLevel() if debug else ToolboxLogger.setInfoLevel()

        encuestas = 0
        registros = 0
        errores = 0
        versionFinal = ''

        usuario_valido = (portal and usuario and clave) or (not portal and not usuario and not clave)
        if servicioFuente and versionDestino and servicioDestino and usuario_valido:
            ToolboxLogger.info("Iniciando {}".format(alias))
            ToolboxLogger.info("Ruta Salida: {}".format(log_path)) if rutaSalida != '' else None

            inyector = InyectarEncuestas(
                config_path, 
                portal, 
                usuario, 
                clave, 
                servicioFuente, 
                servicioDestino, 
                usuarioCampo = usuarioCampo,
                versionDestino = versionDestino
            )
            resultado  = inyector.Ejecutar()
            if resultado: 
                encuestas = resultado[0]
                registros = resultado[1]
                errores = resultado[2]
                versionFinal = inyector.versionDestino
            
            ToolboxLogger.info("Version Final: {}".format(versionFinal))
            ToolboxLogger.info("Encuestas: {}".format(encuestas))
            ToolboxLogger.info("Registros: {}".format(registros))
            ToolboxLogger.info("Errores: {}".format(errores))

            if agregarEstadistica:
                filename = os.path.join(log_path, STATISTICS_FILE)
                estadisticas = JsonFile.readFile(filename)

                estadisticas.append(inyector.registroEjecucion())
                JsonFile.writeFile(filename, estadisticas)
        else:
            if not portal:
                ToolboxLogger.info("No se definió Portal")
            if not usuario:
                ToolboxLogger.info("No se definió Usuario")
            if not clave:
                ToolboxLogger.info("No se definió Clave")
            if not servicioFuente:
                ToolboxLogger.info("No se definió Servicio Fuente")
            if not servicioDestino:
                ToolboxLogger.info("No se definió Servicio Destino")
            if not versionDestino:
                ToolboxLogger.info("No se definió Versión Destino")

        return encuestas, registros, errores, versionFinal
