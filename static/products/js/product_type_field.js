document.addEventListener('DOMContentLoaded', function(e){
    var choices_group = document.querySelector('#choices-group');

    function updateChoicesGroup(val) {
        if (choices_group && ['4'].indexOf(val) != -1){
            choices_group.style['display'] = 'block';
        }
        else {
            choices_group.style['display'] = 'none';
        }
    }

    var type_select = document.querySelector('select[name=type]');

    if (type_select) {
        updateChoicesGroup(type_select.value);

        type_select.addEventListener('change', function(e){
           updateChoicesGroup(e.target.value);
        });
    }
});