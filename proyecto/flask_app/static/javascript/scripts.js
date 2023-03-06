
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
        $(".analisis .un_analisis").each(function() {
            var a = $(this).find(".analisis_nombre").text();
            console.log(a);
            if (a.toLowerCase().search(value) > -1){
                $(this).show();
            }
            else{
                $(this).hide();
            }
        });
    });
});


