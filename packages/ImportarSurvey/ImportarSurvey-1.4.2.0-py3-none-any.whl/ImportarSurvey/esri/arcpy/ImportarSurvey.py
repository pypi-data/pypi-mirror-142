# -*- coding: utf-8 -*-
r""""""
__all__ = ['HerramientaInyectarEncuestas', 'HerramientaPrecargarEncuestas']
__alias__ = 'ImportarSurvey'
from arcpy.geoprocessing._base import gptooldoc, gp, gp_fixargs
from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject

# Tools
@gptooldoc('HerramientaInyectarEncuestas_ImportarSurvey', None)
def HerramientaInyectarEncuestas(portal=None, usuario=None, clave=None, servicioFuente=None, servicioDestino=None, versionDestino=None, usuarioCampo=None, informeDetallado=None):
    """HerramientaInyectarEncuestas_ImportarSurvey(portal, usuario, clave, servicioFuente, servicioDestino, {versionDestino}, usuarioCampo, {informeDetallado})

     INPUTS:
      portal (Cadena):
          URL del Portal: 
      usuario (Cadena):
          Usuario: 
      clave (Cadena de caracteres oculta):
          Clave: 
      servicioFuente (Cadena):
          Servicio Fuente (Encuesta Survey123):
      servicioDestino (Cadena):
          Servicio Destino (SubModelo Levantamiento Catastral):
      versionDestino {Cadena}:
          Versión Destino: 
      usuarioCampo (Cadena):
          Usuario Reconocedor: 
      informeDetallado {Booleano}:
          Informe Detallado:"""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.HerramientaInyectarEncuestas_ImportarSurvey(*gp_fixargs((portal, usuario, clave, servicioFuente, servicioDestino, versionDestino, usuarioCampo, informeDetallado), True)))
        return retval
    except Exception as e:
        raise e

@gptooldoc('HerramientaPrecargarEncuestas_ImportarSurvey', None)
def HerramientaPrecargarEncuestas(portal=None, usuario=None, clave=None, servicioFuente=None, versionFuente=None, servicioDestino=None, usuarioCampo=None, idsPrecarga=None, informeDetallado=None):
    """HerramientaPrecargarEncuestas_ImportarSurvey(portal, usuario, clave, servicioFuente, {versionFuente}, servicioDestino, usuarioCampo, idsPrecarga;idsPrecarga..., {informeDetallado})

     INPUTS:
      portal (Cadena):
          URL del Portal: 
      usuario (Cadena):
          Usuario: 
      clave (Cadena de caracteres oculta):
          Clave: 
      servicioFuente (Cadena):
          Servicio Fuente (SubModelo Levantamiento Catastral):
      versionFuente {Cadena}:
          Versión Fuente:
      servicioDestino (Cadena):
          Servicio Destino (Encuesta Survey123):
      usuarioCampo (Cadena):
          Usuario Reconocedor: 
      idsPrecarga (Cadena):
          Números Prediales a cargar:
      informeDetallado {Booleano}:
          Informe Detallado:"""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.HerramientaPrecargarEncuestas_ImportarSurvey(*gp_fixargs((portal, usuario, clave, servicioFuente, versionFuente, servicioDestino, usuarioCampo, idsPrecarga, informeDetallado), True)))
        return retval
    except Exception as e:
        raise e


# End of generated toolbox code
del gptooldoc, gp, gp_fixargs, convertArcObjectToPythonObject