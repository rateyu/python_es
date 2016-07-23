__author__ = 'myu2'
import pyes

conn = pyes.ES('192.168.1.14:9200')
conn.indices.create_index("test-index")

mapping = {
    'parsedtext': {
        'boost': 1.0,
        'index': 'analyzed',
        'store': 'yes',
        'type': 'string',
        "term_vector": "with_positions_offsets"
    },
    'name': {
        'boost': 1.0,
        'index': 'analyzed',
        'store': 'yes',
        'type': 'string',
        "term_vector": "with_positions_offsets"
    },
    'title': {
        'boost': 1.0,
        'index': 'analyzed',
        'store': 'yes',
        'type': 'string',
        "term_vector": "with_positions_offsets"
    },
    'content': {
        'boost': 1.0,
        'index': 'analyzed',
        'store': 'yes',
        'type': 'string',
        "term_vector": "with_positions_offsets"
    },
    'pos': {
        'store': 'yes',
        'type': 'integer'
    },
    'uuid': {
       'boost': 1.0,
        'index': 'not_analyzed',
        'store': 'yes',
        'type': 'string'
    }
}
conn.indices.put_mapping("test-type", {'properties':mapping}, ["test-index"])
