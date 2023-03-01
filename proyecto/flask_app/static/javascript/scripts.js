
$(document).ready(function(){
    $("#busqueda_medico").on("keyup", function() {
        var value = $(this).val().toLowerCase();
        console.log(value)
        $(".medicos .medico").each(function() {
            var a = $(this).find("p").text();
            if ($(this).text().toLowerCase().search(value) > -1){
                $(this).show();
            }
            else{
                $(this).hide();
            }
        });
    });

    $("#busqueda_analisis").on("keyup", function() {
        var value = $(this).val().toLowerCase();
        console.log(value)
        $(".analisis .un_analisis").each(function() {
            var a = $(this).find("p .analisis_nombre").text();
            if ($(this).text().toLowerCase().search(value) > -1){
                $(this).show();
            }
            else{
                $(this).hide();
            }
        });
    });
});


