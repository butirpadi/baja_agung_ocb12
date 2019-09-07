# -*- coding: utf-8 -*-
{
    'name': "Baja Agung 2019",

    'summary': """
        Baja Agung Custom Module 2019""",

    'description': """
        Baja Agung Custom Module 2019
    """,

    'author': "Tepat Guna Karya",
    'website': "http://www.tepatguna.id",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'stock', 'tax_remove_ocb12'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        # 'views/views.xml',
        'views/product_template_view.xml',
        'views/product_category_view.xml',
        'views/sale_view.xml',
        'views/employee_view.xml',
        'views/product_uom_view.xml',
        'views/purchase_view.xml',
        'views/stock_picking_view.xml',
        'views/hide_menu_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable':True,
    'application':True,
}