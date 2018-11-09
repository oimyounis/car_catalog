document.addEventListener('DOMContentLoaded', function(e){

    // var choices_group = document.querySelector('#choices-group');
    //
    // function updateChoicesGroup(val) {
    //     if (choices_group && ['4'].indexOf(val) != -1){
    //         choices_group.style['display'] = 'block';
    //     }
    //     else {
    //         choices_group.style['display'] = 'none';
    //     }
    // }

    var type_select = document.querySelector('select[name=product_type]');
    if (type_select) {
        // updateChoicesGroup(type_select.value);
        type_select.addEventListener('change', function(e){
            var product_type_id = type_select.value;
            if (product_type_id){
                document.querySelector('form').setAttribute('enctype', 'multipart/form-data');

                fetch('/products/api/product_fields_form/' + product_type_id).then(function(res){return res.text()})
                .then(function(res){
                    var type_filed_wrapper = document.querySelector('div.type-field-wrapper');

                    if (type_filed_wrapper){
                        type_filed_wrapper.remove();
                    }

                    var el = document.createElement('div');
                    el.innerHTML = res;
                    document.querySelector('form > div').insertBefore(el, document.querySelector('form > div > div.submit-row'))
                });
            }
        });
    }
});
// updateChoicesGroup(e.target.value);
