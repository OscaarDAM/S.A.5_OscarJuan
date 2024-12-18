{
    'name': "Batoi",
    'summary': "Gestió dels cicles formatius en batoi",
    'description': """
        Gestió de móduls i cicles formatius.
    """,
    'author': "Óscar",
    'website': "https://github.com/OscaarDAM",
    'category': 'Custom',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'security/groups.xml',
        'views/cicle_formatiu_views.xml',
        'views/modul_views.xml',
        'views/alumne_views.xml',
        'views/professor_views.xml',
    ],
    'installable': True,
    'application': True,
}
