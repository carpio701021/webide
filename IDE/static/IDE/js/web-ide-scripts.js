var scriptPanelCounter = 0;
var reportPanelCounter = 0;
var codeEditors = {};
var hintObj =  { anicka : {}, cercado : {} };


var fun_on_contextmenu = function (invokedOn, selectedMenu) {
    /*
    var msg = "You selected the menu item '" + selectedMenu.text() +
        "' on the value '" + invokedOn.text() + "'";
    alert(msg);
    if(invokedOn.attr('db')!=undefined)
        alert("Atributo bd: "+invokedOn.attr('db'));
    */

    //aqui empieza la acción
    if (invokedOn.attr('class')!=undefined)
        if(invokedOn.attr('class')=='cm-databases'){
            if ( selectedMenu.text()=='Crear Base de datos') {
                $('#modal_cm_crear_bd').modal('show');
            }
        } else if (invokedOn.attr('class')=='cm-database'){
            if ( selectedMenu.text()=='Eliminar'){
                var codigo = 'ELIMINAR BASE_DATOS ' + invokedOn.attr('db') + ';';
                newScriptEditor(null,codigo);
            }
            if ( selectedMenu.text()=='Crear script'){
                //implementar
            }
            if ( selectedMenu.text()=='Backup'){
                //implementar
            }
            if ( selectedMenu.text()=='Restaurar'){
                //implementar
            }
            if ( selectedMenu.text()=='Asignar permisos'){
                //implementar
            }
            if ( selectedMenu.text()=='Ver código'){
                getCodigo( invokedOn.attr('db') );
            }
        } else if (invokedOn.attr('class')=='cm-tables'){
            if ( selectedMenu.text()=='Crear tabla'){
                //implementar
            }
        } else if (invokedOn.attr('class')=='cm-table'){    
            if ( selectedMenu.text()=='Asignar permisos'){
                //implementar
            } 
            if ( selectedMenu.text()=='Ver data'){
                //implementar
            }
        } else if (invokedOn.attr('class')=='cm-functions'){ 
            if ( selectedMenu.text()=='Crear función'){
                //implementar
            }
            
        } else if (invokedOn.attr('class')=='cm-function'){
            
        } else if (invokedOn.attr('class')=='cm-objects'){
            if ( selectedMenu.text()=='Crear objeto'){
                //implementar
            }
            
        } else if (invokedOn.attr('class')=='cm-object'){
            
        } else if (invokedOn.attr('class')=='cm-users'){
            if ( selectedMenu.text()=='Crear Usuario'){
                //implementar
            }
            
        } else if (invokedOn.attr('class')=='cm-user'){
            if ( selectedMenu.text()=='Eliminar Usuario'){
                //implementar
            }
            
        }

};
function cm_crear_bd (invokedOn, selectedMenu) {
    var codigo = 'CREAR BASE_DATOS ' + cm_crear_bd_nombre.value + ';';
    newScriptEditor(null,codigo);
    $('#modal_cm_crear_bd').modal('hide');
}
function cm_eliminar_bd (invokedOn, selectedMenu) {

}
function cm_crear_script_bd (invokedOn, selectedMenu) {

}
function cm_backup_bd (invokedOn, selectedMenu) {

}
function cm_restore_bd (invokedOn, selectedMenu) {

}
function cm_asignar_permisos_bd (invokedOn, selectedMenu) {

}
function cm_crear_tabla (invokedOn, selectedMenu) {

}
function cm_asignar_permisos_tabla (invokedOn, selectedMenu) {

}
function cm_ver_data_tabla (invokedOn, selectedMenu) {

}
function cm_crear_funcion (invokedOn, selectedMenu) {

}
function cm_crear_objeto (invokedOn, selectedMenu) {

}
function cm_crear_usuario (invokedOn, selectedMenu) {

}
function cm_eliminar_usuario (invokedOn, selectedMenu) {

}


function getCodigo(nombre){
    $.get("/ide/getCodigo?nombre="+nombre, function(data, status){
        var cod = data['codigo'];
        codeEditors['txtScript_sql'].setValue(cod);
    });
}

function updateDbTree(){
    $.get("/ide/getDbTree", function(data, status){
        var json = data['arbol'];
        var $tree = $('#treeview12').treeview({
            data: json,
            showBorder: false,
            contextMenuSelector: {
                'cm-databases'   : '#cm_databases',
                'cm-database'   : '#cm_database',
                'cm-tables'     : '#cm_tables',
                'cm-table'      : '#cm_table',
                'cm-functions'  : '#cm_functions',
                'cm-objects'     : '#cm_objects',
                'cm-users'     : '#cm_users',
                'cm-user'     : '#cm_user'
            },
            onContextMenu: fun_on_contextmenu 
        });
        hintObj = data['tables'] ;
        reiniciar_editores();
    });
}

function eliminarEditor(editorId){
    document.getElementById("script-editor-"+editorId).remove();
    document.getElementById("script-editor-"+editorId+"-li-tab").remove();
    $('#sql').tab('show');
}

function reiniciar_editores(){
    Object.keys(codeEditors).forEach(function(key) {
        var editor = codeEditors[key];
        var contenido = editor.getValue();
        document.getElementById(key).innerHTML = "";
        init_codemirror_editor(key,contenido)
    });
}

function init_codemirror_editor(article_id,value){
    var editor = CodeMirror($('#'+article_id)[0], {
        value: value,
        lineNumbers: true,
        indentWithTabs: true,
        smartIndent: true,
        autofocus: true,
        viewportMargin: Infinity,
        mode: "text/usql",//mode: "javascript",
        keyMap: "sublime",
        autoCloseBrackets: true,
        matchBrackets: true,
        showCursorWhenSelecting: true,
        theme: "material",// "monokai",
        tabSize: 4,
        extraKeys: {"Ctrl-Space": "autocomplete"},
        hintOptions: {
            tables: hintObj
            //tables: {'anicka':{}}
        }
    });
    codeEditors[article_id] = editor;
}


// Funcion que se ejecuta al cargar la pagina
$(function() {
    updateDbTree();

    //texto de prueba, borrar si es necesario
    var value = 'CREAR BASE_DATOS prueba;\n\nUSAR prueba;\n\nCREAR PROCEDIMIENTO crear_inicial (){\n\n	#falta crear usuario usuario_calificacion\n\n	CREAR OBJETO T_DIRECCION(\n		INTEGER avenida, \n		INTEGER calle, \n		TEXT nombre, \n		TEXT descripcion\n	);\n\n	CREAR TABLA estudiante(\n		INTEGER carnet LLAVE_PRIMARIA,\n		INTEGER dpi UNICO,\n		TEXT nombre NO NULO,\n		T_DIRECCION direccion,\n		DATE fh_nac NO NULO,\n		DATETIME fh_creacion NO NULO\n	);\n\n	CREAR TABLA curso(\n		INTEGER codigo_curso LLAVE_PRIMARIA,\n		TEXT nombre NO NULO,\n		INTEGER creditos  NO NULO,\n		INTEGER creditos_prerrequisito\n	);\n\n\n	CREAR TABLA asignacion(\n		INTEGER codigo_curso NO NULO LLAVE_FORANEA curso codigo_curso,\n		INTEGER carnet NO NULO LLAVE_FORANEA estudiante carnet,\n		DATETIME fh_asignacion NO NULO,\n		CHAR estado\n	);\n\n	CREAR FUNCTION T_DIRECCION_TO_TEXT (T_DIRECCION) TEXT{\n		RETORNAR T_DIRECCION.calle + \' calle, \' + T_DIRECCION.avenida + \' avenida, \' + T_DIRECCION.nombre + T_DIRECCION.descripcion;\n	}\n}\n\n\n\n\nCREAR PROCEDIMIENTO insertar_inicial (){\n\n	INSERTAR EN TABLA estudiante (201403001, 2950130000101,\'alumno 1\', \'direccion 1\',\'1996-01-19\',\'2017-08-17\');\n	INSERTAR EN TABLA estudiante (201403002, 2950130001101,\'alumno 2\', \'direccion 2\',\'1990-02-07\',\'2017-08-17\');\n	INSERTAR EN TABLA estudiante (201403003, 2950130002101,\'alumno 3\', \'direccion 3\',\'1994-12-29\',\'2017-08-17\');\n	INSERTAR EN TABLA estudiante (201403004, 2950130003101,\'Alumno 4\', \'direccion 4\',\'1993-03-02\',\'2017-08-17\');\n	#este no se debe de insertar\n	INSERTAR EN TABLA estudiante (201403017, 2950130000101,\'Repetido - Error\', \'7 av 1-48 zona 1, Guatemala\',\'1996-11-02\',\'2017-08-17\');\n\n\n	INSERTAR EN TABLA curso (1, \'clase 1\', 5, NULO);\n	INSERTAR EN TABLA curso (2, \'clase 2\', 5, NULO);\n	INSERTAR EN TABLA curso (3, \'clase 3\', 5, NULO);\n	INSERTAR EN TABLA curso (4, \'clase 4\', 5, NULO);\n}\n\n\n\nCREAR PROCEDIMIENTO insertar_primer_semestre (){\n\n	#El 17 de enero del 2017 se asignan unos estudiantes a Estructuras de Datos\n	INSERTAR EN TABLA asignacion (1, 201403002, \'2017-01-17\', \'C\');\n	INSERTAR EN TABLA asignacion (1, 201403003, \'2017-01-17\', \'C\');\n	INSERTAR EN TABLA asignacion (1, 201403004, \'2017-01-17\', \'C\');\n\n	#El 17 de enero del 2017 se asignan unos estudiantes a curso 2\n	INSERTAR EN TABLA asignacion (2, 201403001, \'2017-01-17\', \'C\');\n	INSERTAR EN TABLA asignacion (2, 201403002, \'2017-01-17\', \'C\');\n	INSERTAR EN TABLA asignacion (2, 201403004, \'2017-01-17\', \'C\');\n\n}\n\n\n\nCREAR PROCEDIMIENTO finalizar_primer_semestre (){\n\n	#Se cambia el estado de los alumnos que ganaron EDD y Compiladores 1;\n	ACTUALIZAR asignacion set estado = \'A\' DONDE carnet = 201403002 && (codigo_curso = 1 || codigo_curso = 2);\n	ACTUALIZAR asignacion set estado = \'A\' DONDE carnet = 201403001 && codigo_curso = 2;\n\n	#Se cambia de estado a los alumnos que perdieron EDD y Compiladores 1\n	ACTUALIZAR asignacion set estado = \'R\' DONDE estado = \'C\' && (codigo_curso = 1 || codigo_curso = 2);\n\n}\n\n\nCREAR PROCEDIMIENTO insertar_segundo_semestre (){\n\n	#El 12 de julio del 2017 se asignan al curso 2 los alumnos que ya ganaron curso 1 y curso 2\n	INSERTAR EN TABLA asignacion (781, 201403002, \'2017-07-12\', \'C\');\n\n}\n\n\nCREAR PROCEDIMIENTO insertar_tercer_semestre (){\n\n	SELECCIONAR * DE estudiante;\n\n	SELECCIONAR * DE curso;\n\n	SELECCIONAR * DE prerrequisito;\n\n	SELECCIONAR * DE asignacion;\n\n\n	#Alumnos asignados al curso 1\n	SELECCIONAR curso.nombre, estudiante.nombre, asignacion.estado \n	DE curso, asignacion, estudiante \n	DONDE asignacion.codigo_curso = 1 \n	&& asignacion.carnet = estudiante.carnet \n	&& asignacion.codigo_curso = curso.codigo_curso;\n\n	#Alumnos asignados al curso 2\n	SELECCIONAR curso.nombre, estudiante.nombre, asignacion.estado \n	DE curso, asignacion, estudiante \n	DONDE asignacion.codigo_curso = 2 \n	&& asignacion.carnet = estudiante.carnet \n	&& asignacion.codigo_curso = curso.codigo_curso;\n\n\n	#Asignaciones despues de la fecha de hoy\n	SELECCIONAR curso.nombre, estudiante.nombre, asignacion.estado \n	DE curso, asignacion, estudiante \n	DONDE asignacion.carnet = estudiante.carnet \n	&& asignacion.codigo_curso = curso.codigo_curso\n	&& asignacion.fh_asignacion >= FECHA_HORA();\n\n}\n\n\nCREAR PROCEDIMIENTO funcionamientos(INTEGER @variable1, INTEGER @variable2){\n\n	SI(@var2 > @var1){\n		IMPRIMIR("variable 2 es mayor");\n	}SINO{\n		SI(@variable2 < @variable1){\n			IMPRIMIR("variable 1 es mayor");\n		}SINO{\n			IMPRIMIR("los prarmentros son iguales");\n		}\n	}\n\n	DECLARAR @contador INTEGER= 0;\n	DECLARAR @bandera BOOL= (((5>10)||(15<25))&&(@contador == 0));\n\n\n	MIENTRAS(@contador < 10||@bandera == false){\n\n		SELECCIONAR (@contador){\n			CASO 0: IMPRIMIR(" cero\n"); DETENER;\n			CASO 1: IMPRIMIR (" uno\n"); DETENER;\n			CASO 2: IMPRIMIR (" dos\n"); DETENER;\n			CASO 3: IMPRIMIR (" tres\n"); DETENER;\n			CASO 4: IMPRIMIR(" cuatro\n"); DETENER;\n			CASO 5: IMPRIMIR (" cinco\n"); DETENER;\n			CASO 6: IMPRIMIR (" seis\n"); DETENER;\n			CASO 7: IMPRIMIR (" siete\n"); DETENER;\n			CASO 8: IMPRIMIR(" ocho\n"); DETENER;\n			CASO 9: IMPRIMIR (" nueve\n"); DETENER;\n		}\n		@contador = @contado + 1;\n	}\n\n\n	DECLARAR miDirec T_DIRECCION;\n	miDirec.calle = 15;\n	miDirec.avenida = 2;\n	miDirec.nombre = \'Residenciales el casas bellas\';\n	miDirec.descripcion = \'casa 18\';\n	IMPRIMIR(miDirec.calle + " calle y " + miDirec.avenida + " avenida, " + miDirec.nombre + " " + miDirec.descripcion);\n}\n\n\nCREAR PROCEDIMIENTO ejecutar(){\n	crear_inicial();\n	insertar_inicial();\n	funcionamientos((15+2/2)*2-10, 5+(28/4)*2);\n	insertar_primer_semestre();\n	finalizar_primer_semestre();\n	insertar_segundo_semestre();\n	consultas();\n}\n\nejecutar();\n\n\n\n\n	#*\n	Reporte 1 \n	<html>\n		<body>\n			<h1> Reporte 1 </h1>\n			<usql> SELECCIONAR * DE estudiante</usql>\n		</body>\n	</html>\n	*#\n\n\n	#*\n	Reporte 2\n	<html>\n		<body>\n			<h1> Reporte 2 </h1>\n			<usql> SELECCIONAR * DE curso</usql>\n		</body>\n	</html>\n	*#';
    
    init_codemirror_editor('txtScript_sql', value);
});


/* Agrega nueva pestaña a los editores de scripts */
var newScriptEditor = function(event,contenido_codigo) {
    $.get("/ide/newScriptPanel?numPanel="+scriptPanelCounter, function(data, status){
        $('#myEditorsTabContent').append(data);
        $.get("/ide/newScriptPanelTab?numPanel="+scriptPanelCounter, function(data, status){
            $('#ul-container-editors-tabs').append(data);
            init_codemirror_editor('txtScript'+scriptPanelCounter,(contenido_codigo===undefined)?'Nuevo script ' + scriptPanelCounter : contenido_codigo );
            $('#script-editor-txtScript'+scriptPanelCounter+"-tab").tab('show');
            scriptPanelCounter++;
        });
    });
}
$('#btnNewScriptEditor').click(newScriptEditor);

// manda el codigo de un editor a ser analizado y devuelve la respuesta a los outputs
function executeScript(scriptPanelNum){
    $.post("/ide/executeScript", 
    {
        scriptPanelNum: scriptPanelNum,
        sqlcode: codeEditors['txtScript'+scriptPanelNum].getValue()
    })
        .done(function(json_respuesta, status){
            document.getElementById('output-datos').innerHTML = json_respuesta['salida']
            //$('#output-datos').val($('#output-datos').val()+json_respuesta['salida']);
            $('#output-plan').val($('#output-plan').val()+json_respuesta['plan']);
            $('#output-mensajes').val($('#output-mensajes').val()+json_respuesta['mensajes']);
            $('#output-historial').val($('#output-historial').val()+json_respuesta['historial']);
            updateDbTree();
        });
    
}

function init_codemirror_report_editor(article_id,value){
    var editor = CodeMirror($('#'+article_id)[0], {
        value: value,
        lineNumbers: true,
        indentWithTabs: true,
        autofocus: true,
        viewportMargin: Infinity,
        mode: "text/html",//mode: "javascript",
        keyMap: "sublime",
        showCursorWhenSelecting: true,
        theme: "material",
        tabSize: 2,
        extraKeys: {"Ctrl-Space": "autocomplete"},
        hintOptions: {usql:'usql'}
    });
    codeEditors[article_id] = editor;
}

/* Agrega nueva pestaña a los editores de reportes */
$('#btnNewReportEditor').click(function() {
    $.get("/ide/newReportPanel?numPanel="+reportPanelCounter, function(data, status){
        $('#myEditorsTabContent').append(data);
        $.get("/ide/newReportPanelTab?numPanel="+reportPanelCounter, function(data, status){
            $('#ul-container-editors-tabs').append(data);
            init_codemirror_report_editor('txtReport'+reportPanelCounter,'Hola Report ' + reportPanelCounter);
            init_codemirror_report_editor('txtReport'+reportPanelCounter+'_results','Resultados ');
            reportPanelCounter++;
        });
    });
});


// manda el codigo de un editor a ser analizado y devuelve la respuesta a los outputs
function executeReport(reportPanelNum){
    
        //var iDiv = document.createElement('div');
        //iDiv.innerHTML = codeEditors['txtReport'+reportPanelNum].getValue();
        //var usql = iDiv.querySelector("usql");
        //var nDiv = iDiv.querySelector("usql").innerHTML(json_respuesta['resultado'])
    
        $.post("/ide/executeReport", 
        {
            reportPanelNum: reportPanelNum,
            sqlcode:codeEditors['txtReport'+reportPanelNum].getValue()// usql.innerHTML
        })
            .done(function(json_respuesta, status){
                //iDiv.querySelector("usql").innerHTML = json_respuesta['resultado'];
                
                codeEditors['txtReport'+reportPanelNum+'_results'].setValue(json_respuesta['resultado']);
            });
}
    

// Visualizar reporte
function showReport(reportPanelNum){
    submit_post_via_hidden_form(
        '/ide/showReport',
        {
            htmlcode: codeEditors['txtReport'+reportPanelNum+'_results'].getValue()
        }
    );
   
}

//para abrir ventana con metodo post con parametros
function submit_post_via_hidden_form(url, params) {
    var f = $("<form target='_blank' method='POST' style='display:none;'></form>").attr({
        action: url
    }).appendTo(document.body);
    for (var i in params) {
        if (params.hasOwnProperty(i)) {
            $('<input type="hidden" />').attr({
                name: i,
                value: params[i]
            }).appendTo(f);
        }
    }
    f.submit();
    f.remove();
}

