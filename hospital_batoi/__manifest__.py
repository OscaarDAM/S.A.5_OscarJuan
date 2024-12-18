{
    'name': 'Hospital Batoi',
    'version': '1.0',
    'author': 'Óscar',
    'category': 'Healthcare',
    'summary': 'gestió de pacients i metges del hospital Batio',
    'description': """
    Aquest mòdul permet gestionar pacients y metges, a més de gestionar les atencions.
    """,
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/patient_view.xml',
        'views/doctor_view.xml',
        'views/appointment_view.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
}

