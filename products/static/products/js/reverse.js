this.Urls = (function() {
    var Urls = {};
    var self = {
        url_patterns: {}
    };
    var _get_url = function(url_pattern) {
        return function() {
            var _arguments, index, url, url_arg, url_args, _i, _len, _ref, _ref_list, match_ref, provided_keys, build_kwargs;
            _arguments = arguments;
            _ref_list = self.url_patterns[url_pattern];
            if (arguments.length == 1 && typeof(arguments[0]) == "object") {
                var provided_keys_list = Object.keys(arguments[0]);
                provided_keys = {};
                for (_i = 0; _i < provided_keys_list.length; _i++)
                    provided_keys[provided_keys_list[_i]] = 1;
                match_ref = function(ref) {
                    var _i;
                    if (ref[1].length != provided_keys_list.length)
                        return false;
                    for (_i = 0; _i < ref[1].length && ref[1][_i] in provided_keys; _i++);
                    return _i == ref[1].length;
                }
                build_kwargs = function(keys) {
                    return _arguments[0];
                }
            } else {
                match_ref = function(ref) {
                    return ref[1].length == _arguments.length;
                }
                build_kwargs = function(keys) {
                    var kwargs = {};
                    for (var i = 0; i < keys.length; i++) {
                        kwargs[keys[i]] = _arguments[i];
                    }
                    return kwargs;
                }
            }
            for (_i = 0; _i < _ref_list.length && !match_ref(_ref_list[_i]); _i++);
            if (_i == _ref_list.length)
                return null;
            _ref = _ref_list[_i];
            url = _ref[0], url_args = build_kwargs(_ref[1]);
            for (url_arg in url_args) {
                var url_arg_value = url_args[url_arg];
                if (url_arg_value === undefined || url_arg_value === null) {
                    url_arg_value = '';
                } else {
                    url_arg_value = url_arg_value.toString();
                }
                url = url.replace("%(" + url_arg + ")s", url_arg_value);
            }
            return '/' + url;
        };
    };
    var name, pattern, url, url_patterns, _i, _len, _ref;
    url_patterns = [
        ['admin:app_list', [
            ['admin/%(app_label)s/', ['app_label', ]]
        ], ],
        ['admin:auth_group_add', [
            ['admin/auth/group/add/', []]
        ], ],
        ['admin:auth_group_autocomplete', [
            ['admin/auth/group/autocomplete/', []]
        ], ],
        ['admin:auth_group_change', [
            ['admin/auth/group/%(object_id)s/change/', ['object_id', ]]
        ], ],
        ['admin:auth_group_changelist', [
            ['admin/auth/group/', []]
        ], ],
        ['admin:auth_group_delete', [
            ['admin/auth/group/%(object_id)s/delete/', ['object_id', ]]
        ], ],
        ['admin:auth_group_history', [
            ['admin/auth/group/%(object_id)s/history/', ['object_id', ]]
        ], ],
        ['admin:auth_user_add', [
            ['admin/auth/user/add/', []]
        ], ],
        ['admin:auth_user_autocomplete', [
            ['admin/auth/user/autocomplete/', []]
        ], ],
        ['admin:auth_user_change', [
            ['admin/auth/user/%(object_id)s/change/', ['object_id', ]]
        ], ],
        ['admin:auth_user_changelist', [
            ['admin/auth/user/', []]
        ], ],
        ['admin:auth_user_delete', [
            ['admin/auth/user/%(object_id)s/delete/', ['object_id', ]]
        ], ],
        ['admin:auth_user_history', [
            ['admin/auth/user/%(object_id)s/history/', ['object_id', ]]
        ], ],
        ['admin:auth_user_password_change', [
            ['admin/auth/user/%(id)s/password/', ['id', ]]
        ], ],
        ['admin:index', [
            ['admin/', []]
        ], ],
        ['admin:jsi18n', [
            ['admin/jsi18n/', []]
        ], ],
        ['admin:login', [
            ['admin/login/', []]
        ], ],
        ['admin:logout', [
            ['admin/logout/', []]
        ], ],
        ['admin:password_change', [
            ['admin/password_change/', []]
        ], ],
        ['admin:password_change_done', [
            ['admin/password_change/done/', []]
        ], ],
        ['admin:products_category_add', [
            ['admin/products/category/add/', []]
        ], ],
        ['admin:products_category_autocomplete', [
            ['admin/products/category/autocomplete/', []]
        ], ],
        ['admin:products_category_change', [
            ['admin/products/category/%(object_id)s/change/', ['object_id', ]]
        ], ],
        ['admin:products_category_changelist', [
            ['admin/products/category/', []]
        ], ],
        ['admin:products_category_delete', [
            ['admin/products/category/%(object_id)s/delete/', ['object_id', ]]
        ], ],
        ['admin:products_category_history', [
            ['admin/products/category/%(object_id)s/history/', ['object_id', ]]
        ], ],
        ['admin:products_product_add', [
            ['admin/products/product/add/', []]
        ], ],
        ['admin:products_product_autocomplete', [
            ['admin/products/product/autocomplete/', []]
        ], ],
        ['admin:products_product_change', [
            ['admin/products/product/%(object_id)s/change/', ['object_id', ]]
        ], ],
        ['admin:products_product_changelist', [
            ['admin/products/product/', []]
        ], ],
        ['admin:products_product_delete', [
            ['admin/products/product/%(object_id)s/delete/', ['object_id', ]]
        ], ],
        ['admin:products_product_history', [
            ['admin/products/product/%(object_id)s/history/', ['object_id', ]]
        ], ],
        ['admin:products_producttype_add', [
            ['admin/products/producttype/add/', []]
        ], ],
        ['admin:products_producttype_autocomplete', [
            ['admin/products/producttype/autocomplete/', []]
        ], ],
        ['admin:products_producttype_change', [
            ['admin/products/producttype/%(object_id)s/change/', ['object_id', ]]
        ], ],
        ['admin:products_producttype_changelist', [
            ['admin/products/producttype/', []]
        ], ],
        ['admin:products_producttype_delete', [
            ['admin/products/producttype/%(object_id)s/delete/', ['object_id', ]]
        ], ],
        ['admin:products_producttype_history', [
            ['admin/products/producttype/%(object_id)s/history/', ['object_id', ]]
        ], ],
        ['admin:products_producttypefield_add', [
            ['admin/products/producttypefield/add/', []]
        ], ],
        ['admin:products_producttypefield_autocomplete', [
            ['admin/products/producttypefield/autocomplete/', []]
        ], ],
        ['admin:products_producttypefield_change', [
            ['admin/products/producttypefield/%(object_id)s/change/', ['object_id', ]]
        ], ],
        ['admin:products_producttypefield_changelist', [
            ['admin/products/producttypefield/', []]
        ], ],
        ['admin:products_producttypefield_delete', [
            ['admin/products/producttypefield/%(object_id)s/delete/', ['object_id', ]]
        ], ],
        ['admin:products_producttypefield_history', [
            ['admin/products/producttypefield/%(object_id)s/history/', ['object_id', ]]
        ], ],
        ['admin:view_on_site', [
            ['admin/r/%(content_type_id)s/%(object_id)s/', ['content_type_id', 'object_id', ]]
        ], ],
        ['products_api:generate_product_fields_form', [
            ['products/api/product_fields_form/%(id)s', ['id', ]]
        ]]
    ];
    self.url_patterns = {};
    for (_i = 0, _len = url_patterns.length; _i < _len; _i++) {
        _ref = url_patterns[_i], name = _ref[0], pattern = _ref[1];
        self.url_patterns[name] = pattern;
        url = _get_url(name);
        Urls[name] = url;
        Urls[name.replace(/-/g, '_')] = url;
    }
    return Urls;
})();