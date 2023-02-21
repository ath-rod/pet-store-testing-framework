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

get_store_order_schema = {
    'id': {'type': 'integer', 'min': 0},
    'petId': {'type': 'integer', 'min': 0},
    'quantity': {'type': 'integer', 'min': 1},
    'shipDate': {'type': 'string', 'regex': '202[0-9]-((0[1-9])|(1[0-2]))-(([0-2][0-9])|(3[0-1]))T'
                                            '(([0-1][0-9])|([2][0-3])):([0-5][0-9]):([0-5][0-9]).[0-9][0-9][0-9]'
                                            '\+0000'},
    'status': {'type': 'string', 'allowed': ["placed", "approved", "delivered"]},
    'complete': {'type': 'boolean'}
}

get_store_inventory_schema = {
    'available': {'type': 'integer', 'min': 0},
    'pending': {'type': 'integer', 'min': 0},
    'sold': {'type': 'integer', 'min': 0}
}
