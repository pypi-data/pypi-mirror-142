
import ipywidgets as widgets

from  IPython.display import display
from ImportarSurvey.ImportarSurvey import ProcesarEncuestas
from ImportarSurvey.Utiles import ToolboxLogger

class Precarga :

    @classmethod
    def Mostrar(cls, 
        portal = None, 
        usuario = None, 
        clave = None, 
        usuarioCampo = None,
        servicioFuente = None, 
        versionFuente = None, 
        servicioDestino = None, 
        idsPrecarga = None, 
        salidaRelativa = False, 
        rutaSalida = '') :

        def btn_eventhandler(obj):

            portal_value = portal_text.value if portal_text.value != '' or portal_text.value != None else None
            usuario_value = usuario_text.value if usuario_text.value != '' or portal_text.value != None else None
            clave_value = clave_password.value if clave_password.value != '' or clave_password.value != None else None

            print("portal: {}".format(portal_value))
            print("usuario: {}".format(usuario_value))
            print("clave: {}".format(clave_value))

            try :
                ProcesarEncuestas.Precargar( 
                    portal = portal_value, 
                    usuario = usuario_value, 
                    clave = clave_value, 
                    servicioFuente = servicio_fuente_text.value, 
                    versionFuente = version_fuente_text.value, 
                    servicioDestino = servicio_destino_text.value, 
                    idsPrecarga = id_textarea.value, 
                    salidaRelativa = salidaRelativa,
                    rutaSalida = rutaSalida)
            except Exception as e:
                ToolboxLogger.error(e)

        layout = widgets.Layout(
            width = 'max_width'
        )

        style = {'description_width': 'max_width'}

        titulo_html = widgets.HTML(
            value="<h1><b>Precarga de Encuestas Catastrales</b></h1>",
        )        
        display(titulo_html)

        portal_text = widgets.Text(
            value = portal,
            description='Url del Portal:',
            style = style,
            disabled=False)
        display(portal_text)

        usuario_text = widgets.Text(
            value = usuario,
            description='Usuario:',
            style = style,
            disabled=False)
        display(usuario_text)

        clave_password = widgets.Password(
            value = clave,
            description='Clave:',
            style = style,
            disabled=False)
        display(clave_password)

        servicio_fuente_text = widgets.Text(
            value = servicioFuente,
            description='Servicio Fuente:',
            style = style,
            disabled=False)
        display(servicio_fuente_text)

        version_fuente_text = widgets.Text(
            value = versionFuente,
            description='Versión Fuente:',
            style = style,
            disabled=False)
        display(version_fuente_text)

        servicio_destino_text = widgets.Text(
            value = servicioDestino,
            description='Servicio Destino:',
            style = style,
            layout = layout,
            disabled=False)
        display(servicio_destino_text)

        id_textarea = widgets.Textarea(
            value = idsPrecarga,
            description='Números Prediales a cargar:',
            style = style,
            disabled=False)
        display(id_textarea)

        usuario_reconocedor_text = widgets.Text(
            value = usuarioCampo,
            description='Usuario Reconocedor:',
            style = style,
            disabled=False)
        display(usuario_reconocedor_text)

        informe_detallado_checkbox = widgets.Checkbox(
            value = False,
            description='Informe Detallado:',
            disabled=False)
        display(informe_detallado_checkbox)

        ejecutar_button = widgets.Button(description ="Ejecutar")
        display(ejecutar_button)

        ejecutar_button.on_click(btn_eventhandler)
    
class Inyeccion :

    @classmethod
    def Mostrar(cls, 
        portal = None, 
        usuario = None, 
        clave = None, 
        usuarioCampo = None,
        servicioFuente = None, 
        servicioDestino = None, 
        versionDestino = None,
        idsPrecarga = None, 
        salidaRelativa = False, 
        rutaSalida = '') :

        def btn_eventhandler(obj):

            portal_value = portal_text.value if portal_text.value != '' or portal_text.value != None else None
            usuario_value = usuario_text.value if usuario_text.value != '' or portal_text.value != None else None
            clave_value = clave_password.value if clave_password.value != '' or clave_password.value != None else None

            print("portal: {}".format(portal_value))
            print("usuario: {}".format(usuario_value))
            print("clave: {}".format(clave_value))

            try :
                ProcesarEncuestas.Inyectar( 
                    portal = portal_value, 
                    usuario = usuario_value, 
                    clave = clave_value, 
                    servicioFuente = servicio_fuente_text.value, 
                    versionDestino = version_destino_text.value, 
                    servicioDestino = servicio_destino_text.value, 
                    salidaRelativa = salidaRelativa,
                    rutaSalida = rutaSalida)
            except Exception as e:
                ToolboxLogger.error(e)

        layout = widgets.Layout(
            width = 'max_width'
        )

        style = {'description_width': 'max_width'}

        titulo_html = widgets.HTML(
            value="<h1><b>Precarga de Encuestas Catastrales</b></h1>",
        )        
        display(titulo_html)

        portal_text = widgets.Text(
            value = portal,
            description='Url del Portal:',
            style = style,
            disabled=False)
        display(portal_text)

        usuario_text = widgets.Text(
            value = usuario,
            description='Usuario:',
            style = style,
            disabled=False)
        display(usuario_text)

        clave_password = widgets.Password(
            value = clave,
            description='Clave:',
            style = style,
            disabled=False)
        display(clave_password)

        servicio_fuente_text = widgets.Text(
            value = servicioFuente,
            description='Servicio Fuente:',
            style = style,
            disabled=False)
        display(servicio_fuente_text)

        servicio_destino_text = widgets.Text(
            value = servicioDestino,
            description='Servicio Destino:',
            style = style,
            layout = layout,
            disabled=False)
        display(servicio_destino_text)

        version_destino_text = widgets.Text(
            value = versionDestino,
            description='Versión Destino:',
            style = style,
            disabled=False)
        display(version_destino_text)

        id_textarea = widgets.Textarea(
            value = idsPrecarga,
            description='Números Prediales a cargar:',
            style = style,
            disabled=False)
        display(id_textarea)

        usuario_reconocedor_text = widgets.Text(
            value = usuarioCampo,
            description='Usuario Reconocedor:',
            style = style,
            disabled=False)
        display(usuario_reconocedor_text)

        informe_detallado_checkbox = widgets.Checkbox(
            value = False,
            description='Informe Detallado:',
            disabled=False)
        display(informe_detallado_checkbox)

        ejecutar_button = widgets.Button(description ="Ejecutar")
        display(ejecutar_button)

        ejecutar_button.on_click(btn_eventhandler)
