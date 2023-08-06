# -*- coding: utf-8 -*-
import platform
import arcgis

from datetime import datetime
from ImportarSurvey.Utiles import ToolboxLogger, Configuracion
from ImportarSurvey.DataAccess import QueryItem, QueryList
from ImportarSurvey.ArcGISPythonApiDataAccess import ArcGISPythonApiDataAccess

class ProcesarEncuestas : 

    def __init__ (self, 
        rutaConfiguracion, 
        portal = None, 
        usuario = None, 
        clave = None, 
        servicioFuente = None, 
        servicioDestino = None, 
        versionFuente = None, 
        versionDestino = None, 
        usuarioCampo = None) :
       
        self.rutaConfiguracion = rutaConfiguracion
        self.config = Configuracion(rutaConfiguracion)

        self.portal = portal
        self.usuario = usuario
        self.usuario_campo = usuarioCampo if usuarioCampo != None else usuario
        self.clave = clave
        self.servicioFuente = servicioFuente
        self.versionDestino = versionDestino
        self.servicioDestino = servicioDestino
        self.versionDestino = versionDestino
        self.versionFuente = versionFuente

        self.destino_da = None
        self.fuente_da = None
        self.importarDatos = None

    @ToolboxLogger.log_method
    def inicializarProceso(self) :
        
        self.gis = ArcGISPythonApiDataAccess.getGIS(self.portal, self.usuario, self.clave)
        if (self.gis != None) :
            self.portal = self.gis.url
            self.usuario = self.gis.users.me.username
            self.usuario_campo = self.usuario_campo if self.usuario_campo != None else self.usuario
            self.nombreCompleto = self.gis.users.me.fullName
        
        self.plataforma = platform.platform()
        self.system, self.node, self.release, self.version, self.machine, self.processor  = platform.uname()

        self.python_impl = platform.python_implementation()
        self.python_rev = platform.python_revision()
        self.python_ver = platform.python_version()
        self.arcgis_ver = arcgis.__version__

        ToolboxLogger.info("Plataforma: {}".format(self.plataforma))
        ToolboxLogger.info("Ejecutando desde: {}".format(self.node))
        ToolboxLogger.info("Sistema Operativo: {} {} Versión: {}".format(self.system, self.release, self.version))
        ToolboxLogger.info("Tipo máquina: {} Procesador: {}".format(self.machine, self.processor))

        ToolboxLogger.info("Python ver: {} rev: {} impl: {}".format(self.python_ver, self.python_rev, self.python_impl))
        ToolboxLogger.info("arcgis ver: {}".format(self.arcgis_ver))
        return

    @ToolboxLogger.log_method
    def limpiarProceso(self):
        return

    @ToolboxLogger.log_method
    def calcularConsultaInicial(self) :
        return 

    @ToolboxLogger.log_method
    def crearVersion(self, da, nombre_formulario) :
        fecha_hora = datetime.now()
        nombre_version = "{}_{}".format(nombre_formulario, fecha_hora.strftime("%Y%m%d%H%M%S"))
        descripcion = "Carga Formulario Survey {}, {}".format(nombre_formulario, fecha_hora.strftime("%Y-%m-%d %H:%M"))
        
        return da.createVersion(nombre_version, "Protected", descripcion)

    @ToolboxLogger.log_method
    def obtenerConsultaInicial(self, campos, valores) :
        ToolboxLogger.debug("campos : '{}'".format(campos))
        ToolboxLogger.debug("valores: '{}'".format(valores))

        self.consultaInicial = QueryList()
        self.consultaInicial.addQuery(QueryItem(campos, valores))

    def registroEjecucion(self) :
        registro = {}
        registro["modulo"] = self.__module__
        registro["portal"] = self.portal
        registro["usuario"] = self.usuario
        registro["usuario_campo"] = self.usuario_campo
        registro["servicio_fuente"] = self.servicioFuente
        registro["version_fuente"] = self.versionFuente
        registro["servicio_destino"] = self.servicioDestino
        registro["version_destino"] = self.versionDestino
        registro["nodo"] = self.node
        registro["plataforma"] = self.plataforma
        registro["sistema"] = self.system
        registro["release"] = self.release
        registro["version"] = self.version
        registro["machine"] = self.machine
        registro["python_impl"] = self.python_impl
        registro["python_rev"] = self.python_rev
        registro["python_ver"] = self.python_ver
        registro["arcgis_ver"] = self.arcgis_ver
        registro["total_tablas"] = self.importarDatos.estadisticas.obtenerTotalTablas()
        registro["total_encuestas"] = self.importarDatos.estadisticas.obtenerNumeroEstadisticas()
        registro["total_creados"] = self.importarDatos.estadisticas.obtenerTotalEstadisticas("C")
        registro["total_actualizados"] = self.importarDatos.estadisticas.obtenerTotalEstadisticas("U")
        registro["total_no_actualizados"] = self.importarDatos.estadisticas.obtenerTotalEstadisticas("NU")
        registro["total_errores"] = self.importarDatos.estadisticas.obtenerTotalEstadisticas("E")
        registro["total_registros"] = self.importarDatos.estadisticas.obtenerTotalRegistros()
        registro["total_operaciones"] = self.importarDatos.estadisticas.obtenerTotalOperaciones()
        registro["inicio"] = "{}".format(self.importarDatos.estadisticas.timer.startTime)
        registro["fin"] = "{}".format(self.importarDatos.estadisticas.timer.endTime)
        registro["duracion_total"] = "{}".format(self.importarDatos.estadisticas.timer.timeSpan)

        if self.importarDatos.estadisticas.obtenerTotalRegistros() > 0:
            registro["duracion_por_encuesta"] = "{}".format(self.importarDatos.estadisticas.duracionPorEstadistica())
            registro["duracion_por_registro"] = "{}".format(self.importarDatos.estadisticas.duracionPorRegistro())
            registro["duracion_por_operacion"] = "{}".format(self.importarDatos.estadisticas.duracionPorOperacion())
            registro["minutos_por_encuesta"] = self.importarDatos.estadisticas.minutosPorEstadistica()
            registro["minutos_por_registro"] = self.importarDatos.estadisticas.minutosPorRegistro()
            registro["minutos_por_operacion"] = self.importarDatos.estadisticas.minutosPorOperacion()
            registro["encuestas_por_minuto"] = self.importarDatos.estadisticas.estadisticasPorMinuto()
            registro["registros_por_minuto"] = self.importarDatos.estadisticas.registrosPorMinuto()
            registro["operaciones_por_minuto"] = self.importarDatos.estadisticas.operacionesPorMinuto()
        
        return registro

    @ToolboxLogger.log_method
    def Ejecutar(self) :
        total_encuestas = 0
        total_registros = 0
        total_errores = 0
        patron_fecha_hora = "%Y-%m-%d %H:%M:%S"
        try: 
            ToolboxLogger.info("Iniciado: {}".format(datetime.now().strftime(patron_fecha_hora)))
            self.inicializarProceso()
            if self.importarDatos :
                mapeos = self.config.getConfigKey("mapeos")
                for mapeo in mapeos :
                    self.calcularConsultaInicial()
                    encuestas, registros, errores = self.importarDatos.procesarMapeo(mapeo, self.consultaInicial)
                    total_encuestas += encuestas
                    total_registros += registros
                    total_errores += errores 
            self.limpiarProceso()
        except Exception as e:
            ToolboxLogger.info("Error: {}".format(e))
        finally :
            ToolboxLogger.info("Terminado: {}".format(datetime.now().strftime(patron_fecha_hora)))
            
        return total_encuestas, total_registros, total_errores