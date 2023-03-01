
$(document).ready(function(){
    $('#chkjs').change(function () {
        if (this.checked)
            checkDetails(this);
    });

    function checkDetails(ele) {
        console.log('Value: ' + ele.value + ' ID: ' + ele.id);
    }
    
});


