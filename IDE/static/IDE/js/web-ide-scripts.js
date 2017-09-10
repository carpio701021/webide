var scriptPanelCounter = 0;
var codeEditors = {};

function updateDbTree(){
    $.get("/ide/getDbTree", function(data, status){
        json = data;
        var $tree = $('#treeview12').treeview({
            data: json,
            showBorder: false
        });
    
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
        mode: "text/x-mysql",//mode: "javascript",
        keyMap: "sublime",
        autoCloseBrackets: true,
        matchBrackets: true,
        showCursorWhenSelecting: true,
        theme: "monokai",
        tabSize: 4,
        extraKeys: {"Ctrl-Space": "autocomplete"},
        hintOptions: {tables: {
          users: {name: null, score: null, birthDate: null},
          countries: {name: null, population: null, size: null}
        }}
    });
    codeEditors[article_id] = editor;
}


// Funcion que se ejecuta al cargar la pagina
$(function() {
    updateDbTree();

    var value = "// The bindings asdf defined specifically in the Sublime Text mode\nvar bindings = {\n";
    
    value += "}\n\n// Theasdf implementation of joinLines javier\n";
    value += CodeMirror.commands.joinLines.toString().replace(/^function\s*\(/, "function joinLines(").replace(/\n  /g, "\n") + "\n";
    
    init_codemirror_editor('txtScript_sql', value);
});


/* Agrega nueva pestaña a los editores de scripts */
$('#btnNewScriptEditor').click(function() {
    $.get("/ide/newScriptPanel?numPanel="+scriptPanelCounter, function(data, status){
        $('#myEditorsTabContent').append(data);
        $.get("/ide/newScriptPanelTab?numPanel="+scriptPanelCounter, function(data, status){
            $('#ul-container-editors-tabs').append(data);
            init_codemirror_editor('txtScript'+scriptPanelCounter,'Hola script ' + scriptPanelCounter);
            scriptPanelCounter++;
        });
    });
});

// manda el codigo de un editor a ser analizado y devuelve la respuesta a los outputs
function executeScript(scriptPanelNum){
    //var editor = document.querySelector('#txtScript'+scriptPanelNum + ' + .codeMirror');
    //alert( editor.getValue() );
    $.post("/ide/executeScript", 
    {
        scriptPanelNum: scriptPanelNum,
        sqlcode: codeEditors['txtScript'+scriptPanelNum].getValue()
    })
        .done(function(json_respuesta, status){
            $('#output-datos').val($('#output-datos').val()+json_respuesta['salida']);
            $('#output-plan').val($('#output-plan').val()+json_respuesta['plan']);
            $('#output-mensajes').val($('#output-mensajes').val()+json_respuesta['mensajes']);
            $('#output-historial').val($('#output-historial').val()+json_respuesta['historial']);
            updateDbTree();
        });
    
}




