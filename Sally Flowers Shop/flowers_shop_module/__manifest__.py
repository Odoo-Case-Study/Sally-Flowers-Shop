# -*- coding: utf-8 -*-
{
    'name': "Sally Flower Shop ",
    'sequence': -11,
    'summary': """
        Sally flowers shop.... Case Study""",

    'description': """
        Sally runs a flower shop. She wants to use Odoo in order to run her daily tasks smoothly. This store grows its own flowers in a garden nearby. These flowers have a set of different attributes.
    """,

    'author': "Ghazal Sabha",
    'website': "https://www.sallyflowersshop.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale','product','sale_management','website','stock'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        # 'views/views.xml',
        # 'views/templates.xml',
        'views/flowers_views.xml',
        'views/product_inherit_view.xml',
        'views/product_flower_view.xml',
        'views/sale_order_line_flowers.xml',
        'views/product_flower_website_inherit_view.xml',
        'views/stock_production_lot_view.xml',
        'views/stock_production_lot_watering_times_view.xml',
        'views/actions.xml',
        'data/paperformat.xml',
        'reports/flower_sale_order_views.xml',
        'data/watering_scheduled_action.xml',
        'data/groups.xml',
        'data/warhouse_actions.xml',
        'security/flowers_shop_rules.xml',
        'views/weather_api_system_parameter.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
    'application': True,
    'installable': True,
}
