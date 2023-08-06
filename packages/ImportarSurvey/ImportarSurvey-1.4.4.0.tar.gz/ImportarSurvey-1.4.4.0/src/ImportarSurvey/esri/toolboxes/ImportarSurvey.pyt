# -*- coding: utf-8 -*-
import arcpy

from ImportarSurvey.Utiles import ARCGIS_HANDLER
from ImportarSurvey.ImportarSurvey import ProcesarEncuestas

class Toolbox(object):
    
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Importar Encuestas Actualización"
        self.alias = "ImportarSurvey"
        
        # List of tool classes associated with this toolbox
        self.tools = [HerramientaInyectarEncuestas, HerramientaPrecargarEncuestas]

class HerramientaInyectarEncuestas(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Inyectar Encuesta Catastral"
        self.description = "Inyectar Encuesta Catastral"
        self.alias = "InyectarEncuestasPro"
        
        self.canRunInBackground = True
        self.Params = {"portal": 0, 
                        "usuario": 1, 
                        "clave": 2, 
                        "servicioFuente": 3, 
                        "servicioDestino": 4,
                        "versionDestino": 5,
                        "usuarioCampo": 6,
                        "informeDetallado": 7,
                        "versionFinal": 8, 
                        "encuestas": 9, 
                        "registros": 10, 
                        "errores": 11}

    def getParameterInfo(self):
        """Define parameter definitions"""
        params = []

        param = arcpy.Parameter(
            displayName="URL del Portal: ",
            name="portal",
            datatype="GPString",
            parameterType="Required",
            direction="Input",
        )
        params.insert(self.Params["portal"], param)

        param = arcpy.Parameter(
            displayName="Usuario: ",
            name="usuario",
            datatype="GPString",
            parameterType="Required",
            direction="Input",
        )
        params.insert(self.Params["usuario"], param)

        param = arcpy.Parameter(
            displayName="Clave: ",
            name="clave",
            datatype="GPStringHidden",
            parameterType="Required",
            direction="Input",
        )
        params.insert(self.Params["clave"], param)

        param = arcpy.Parameter(
            displayName="Servicio Fuente (Encuesta Survey123):",
            name="servicioFuente",
            datatype="GPString",
            parameterType="Required",
            direction="Input",
        )
        params.insert(self.Params["servicioFuente"], param)

        param = arcpy.Parameter(
            displayName="Servicio Destino (SubModelo Levantamiento Catastral):",
            name="servicioDestino",
            datatype="GPString",
            parameterType="Required",
            direction="Input",
        )
        params.insert(self.Params["servicioDestino"], param)

        param = arcpy.Parameter(
            displayName="Versión Destino: ",
            name="versionDestino",
            datatype="GPString",
            parameterType="Optional",
            direction="Input",
        )
        params.insert(self.Params["versionDestino"], param)

        param = arcpy.Parameter(
            displayName="Usuario Reconocedor: ",
            name="usuarioCampo",
            datatype="GPString",
            parameterType="Required",
            direction="Input",
        )
        params.insert(self.Params["usuarioCampo"], param)

        param = arcpy.Parameter(
            displayName="Informe Detallado: ",
            name="informeDetallado",
            datatype="GPBoolean",
            parameterType="Optional",
            direction="Input",
        )
        param.value = False
        params.insert(self.Params["informeDetallado"], param)

        param = arcpy.Parameter(
            displayName="Versión Final: ",
            name="versionFinal",
            datatype="GPString",
            parameterType="Derived",
            direction="Output",
        )
        params.insert(self.Params["versionFinal"], param)

        param = arcpy.Parameter(
            displayName="Encuestas: ",
            name="encuestas",
            datatype="GPLong",
            parameterType="Derived",
            direction="Output",
        )
        params.insert(self.Params["encuestas"], param)

        param = arcpy.Parameter(
            displayName="Registros: ",
            name="registros",
            datatype="GPLong",
            parameterType="Derived",
            direction="Output",
        )
        params.insert(self.Params["registros"], param)

        param = arcpy.Parameter(
            displayName="Errores: ",
            name="errores",
            datatype="GPLong",
            parameterType="Derived",
            direction="Output",
        )
        params.insert(self.Params["errores"], param)

        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""

        portal = parameters[self.Params["portal"]].valueAsText
        usuario = parameters[self.Params["usuario"]].valueAsText
        clave = parameters[self.Params["clave"]].valueAsText
        servicioFuente = parameters[self.Params["servicioFuente"]].valueAsText
        servicioDestino = parameters[self.Params["servicioDestino"]].valueAsText
        versionDestino = parameters[self.Params["versionDestino"]].valueAsText
        usuarioCampo = parameters[self.Params["usuarioCampo"]].valueAsText
        informeDetallado = parameters[self.Params["informeDetallado"]].value

        resultado = ProcesarEncuestas.Inyectar( 
            alias = self.alias,
            portal = portal,
            usuario = usuario, 
            clave = clave, 
            servicioFuente = servicioFuente, 
            servicioDestino = servicioDestino, 
            versionDestino = versionDestino,
            usuarioCampo = usuarioCampo,
            debug = informeDetallado,
            agregarEstadistica = False,
            tipoRegistro = ARCGIS_HANDLER 
        )

        arcpy.SetParameter(self.Params["encuestas"], resultado[0])
        arcpy.SetParameter(self.Params["registros"], resultado[1])
        arcpy.SetParameter(self.Params["errores"], resultado[2])
        arcpy.SetParameter(self.Params["versionFinal"], resultado[3])

        return

class HerramientaPrecargarEncuestas(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Precargar Encuesta Catastral"
        self.description = "Precargar Encuesta Catastral"
        self.alias = "PrecargarEncuestasPro"
        self.description = "Realiza una precarga de datos desde la base de datos central al servicio de survey"
        self.canRunInBackground = True

        self.Params = {"portal": 0, 
                        "usuario": 1, 
                        "clave": 2, 
                        "servicioFuente": 3, 
                        "versionFuente": 4,
                        "servicioDestino": 5, 
                        "usuarioCampo": 6, 
                        "idsPrecarga": 7,
                        "informeDetallado": 8,
                        "versionFinal": 9,
                        "encuestas": 10, 
                        "registros": 11, 
                        "errores": 12}

    def getParameterInfo(self):
        """Define parameter definitions"""
        params = []

        param = arcpy.Parameter(
            displayName="URL del Portal: ",
            name="portal",
            datatype="GPString",
            parameterType="Required",
            direction="Input",
        )
        params.insert(self.Params["portal"], param)

        param = arcpy.Parameter(
            displayName="Usuario: ",
            name="usuario",
            datatype="GPString",
            parameterType="Required",
            direction="Input",
        )
        params.insert(self.Params["usuario"], param)

        param = arcpy.Parameter(
            displayName="Clave: ",
            name="clave",
            datatype="GPStringHidden",
            parameterType="Required",
            direction="Input",
        )
        params.insert(self.Params["clave"], param)

        param = arcpy.Parameter(
            displayName="Servicio Fuente (SubModelo Levantamiento Catastral):",
            name="servicioFuente",
            datatype="GPString",
            parameterType="Required",
            direction="Input",
        )
        params.insert(self.Params["servicioFuente"], param)

        param = arcpy.Parameter(
             displayName="Versión Fuente:",
             name="versionFuente",
             datatype="GPString",
             parameterType="Optional",
             direction="Input",
        )
        params.insert(self.Params["versionFuente"], param)

        param = arcpy.Parameter(
            displayName="Servicio Destino (Encuesta Survey123):",
            name="servicioDestino",
            datatype="GPString",
            parameterType="Required",
            direction="Input",
        )
        params.insert(self.Params["servicioDestino"], param)

        param = arcpy.Parameter(
            displayName="Números Prediales a cargar:",
            name="idsPrecarga",
            datatype="GPString",
            parameterType="Required",
            direction="Input",
            multiValue=True,
        )
        params.insert(self.Params["idsPrecarga"], param)

        param = arcpy.Parameter(
            displayName="Usuario Reconocedor: ",
            name="usuarioCampo",
            datatype="GPString",
            parameterType="Required",
            direction="Input",
        )
        params.insert(self.Params["usuarioCampo"], param)

        param = arcpy.Parameter(
            displayName="Informe Detallado: ",
            name="informeDetallado",
            datatype="GPBoolean",
            parameterType="Optional",
            direction="Input",
        )
        param.value = False
        params.insert(self.Params["informeDetallado"], param)

        param = arcpy.Parameter(
            displayName="Versión Final: ",
            name="versionFinal",
            datatype="GPString",
            parameterType="Derived",
            direction="Output",
        )
        params.insert(self.Params["versionFinal"], param)

        param = arcpy.Parameter(
            displayName="Encuestas: ",
            name="encuestas",
            datatype="GPLong",
            parameterType="Derived",
            direction="Output",
        )
        params.insert(self.Params["encuestas"], param)

        param = arcpy.Parameter(
            displayName="Registros: ",
            name="registros",
            datatype="GPLong",
            parameterType="Derived",
            direction="Output",
        )
        params.insert(self.Params["registros"], param)

        param = arcpy.Parameter(
            displayName="Errores: ",
            name="errores",
            datatype="GPLong",
            parameterType="Derived",
            direction="Output",
        )
        params.insert(self.Params["errores"], param)

        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""

        portal = parameters[self.Params["portal"]].valueAsText
        usuario = parameters[self.Params["usuario"]].valueAsText
        clave = parameters[self.Params["clave"]].valueAsText
        servicioFuente = parameters[self.Params["servicioFuente"]].valueAsText
        versionFuente = parameters[self.Params["versionFuente"]].valueAsText
        servicioDestino = parameters[self.Params["servicioDestino"]].valueAsText
        idsPrecarga = parameters[self.Params["idsPrecarga"]].valueAsText
        usuarioCampo = parameters[self.Params["usuarioCampo"]].valueAsText
        informeDetallado = parameters[self.Params["informeDetallado"]].value


        resultado = ProcesarEncuestas.Precargar(
            alias = self.alias,
            portal = portal,
            usuario = usuario, 
            clave = clave, 
            servicioFuente = servicioFuente, 
            versionFuente = versionFuente, 
            servicioDestino = servicioDestino, 
            idsPrecarga = idsPrecarga,
            usuarioCampo = usuarioCampo,
            debug = informeDetallado,
            agregarEstadistica = False,
            tipoRegistro = ARCGIS_HANDLER
        )

        arcpy.SetParameter(self.Params["encuestas"], resultado[0])
        arcpy.SetParameter(self.Params["registros"], resultado[1])
        arcpy.SetParameter(self.Params["errores"], resultado[2])
        arcpy.SetParameter(self.Params["versionFinal"], resultado[3])

        return
