# -*- coding: utf-8 -*-
{
    "name": "questions generation",
    "summary": """
        questions generation test""",
    "description": """
        Long description of module's purpose
    """,
    "author": "My Company",
    "website": "http://www.yourcompany.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    "category": "Uncategorized",
    "version": "0.1",
    # any module necessary for this one to work correctly
    "depends": ["base", "website_slides"],
    # always loaded
    "data": [
        "security/ir.model.access.csv",
        "views/qgen_views.xml",
        "views/templates.xml",
        "views/slide_view.xml",
        "views/res_config_settings_view.xml",
    ],
    # only loaded in demonstration mode
    "demo": [
        "demo/demo.xml",
    ],
}
