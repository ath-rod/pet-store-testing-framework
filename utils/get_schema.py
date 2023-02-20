get_pet_schema = {
    'id': {'type': 'integer', 'min': 0},
    'category': {
        'type': 'dict',
        'schema': {'id': {'type': 'integer', 'min': 0},
                   'name': {'type': 'string'}}
    },
    'name': {'type': 'string'},
    'photoUrls': {
        'type': 'list',
        'schema': {'type': 'string'}
    },
    'tags': {
        'type': 'list',
        'schema': {'type': 'dict',
                   'schema': {'id': {'type': 'integer', 'min': 0},
                              'name': {'type': 'string'}}
                   }
    },
    'status': {'type': 'string', 'allowed': ['available', 'pending', 'sold']}
}
