TEMPLATE_VALUES = {
        'discount_trends': {
            'header': 'Discount Trends',
            'url': 'https://haggle-test1.appspot.com/api/analytics/',
            'description': 'Returns average maximum and minimum discounts being offered in the given area.',
            'endpoint': 'aggregate_campaigns',
            'params': {
                'property': { 
                    'value': 'discount_trends',
                    'description': 'property_desc'
                    },
                'lat': {
                    'value': 40.745619,
                    'description': 'Latitude of the location.'
                    },
                'lon': {
                    'value': -73.985296,
                    'description': 'Longitude of the location.'
                    },
                'radius': { 
                    'value': 3000,
                    'description': 'Radius (in meters).'
                    }
                }
            },
        'score_preference_trends': {
            'header': 'Score Preference Trends',
            'url': 'https://haggle-test1.appspot.com/api/analytics/',
            'description': 'Returns the score preference trends in the given area.',
            'endpoint': 'aggregate_campaigns',
            'params': {
                'property': { 
                    'value': 'score_preference_trends',
                    'description': 'property_desc'
                    },
                'lat': {
                    'value': 40.745619,
                    'description': 'Latitude of the location.'
                    },
                'lon': {
                    'value': -73.985296,
                    'description': 'Longitude of the location.'
                    },
                'radius': { 
                    'value': 3000,
                    'description': 'Radius (in meters).'
                    }
                }
            },
        'bids_trends': {
            'header': 'Bids Trends',
            'url': 'https://haggle-test1.appspot.com/api/analytics/',
            'description': "Returns Users' bidding trends in the given area.",
            'endpoint': 'aggregate_deals',
            'params': {
                'property': { 
                    'value': 'bids_trends',
                    'description': 'property_desc'
                    },
                'lat': {
                    'value': 40.745619,
                    'description': 'Latitude of the location.'
                    },
                'lon': {
                    'value': -73.985296,
                    'description': 'Longitude of the location.'
                    },
                'radius': { 
                    'value': 3000,
                    'description': 'Radius (in meters).'
                    }
                }
            },
        'user_trends': {
            'header': 'User Trends',
            'url': 'https://haggle-test1.appspot.com/api/analytics/',
            'description': 'Placeholder description for User Trends',
            'endpoint': 'aggregate_deals',
            'params': {
                'property': { 
                    'value': 'user_trends',
                    'description': 'property_desc'
                    },
                'lat': {
                    'value': 40.745619,
                    'description': 'Latitude of the location.'
                    },
                'lon': {
                    'value': -73.985296,
                    'description': 'Longitude of the location.'
                    },
                'radius': { 
                    'value': 3000,
                    'description': 'Radius (in meters).'
                    }
                }
            },
        'time_trends': {
            'header': 'Time Trends',
            'url': 'https://haggle-test1.appspot.com/api/analytics/',
            'description': 'Placeholder description for Time Trends',
            'endpoint': 'aggregate_deals',
            'params': {
                'property': { 
                    'value': 'time_trends',
                    'description': 'property_desc'
                    },
                'lat': {
                    'value': 40.745619,
                    'description': 'Latitude of the location.'
                    },
                'lon': {
                    'value': -73.985296,
                    'description': 'Longitude of the location.'
                    },
                'radius': { 
                    'value': 3000,
                    'description': 'Radius (in meters).'
                    }
                }
            },
        'average_spending': {
            'header': 'Average Spending',
            'url': 'https://haggle-test1.appspot.com/api/analytics/',
            'description': 'Placeholder description for Average Spending',
            'endpoint': 'aggregate_deals',
            'params': {
                'property': { 
                    'value': 'average_spending',
                    'description': 'property_desc'
                    },
                'lat': {
                    'value': 40.745619,
                    'description': 'Latitude of the location.'
                    },
                'lon': {
                    'value': -73.985296,
                    'description': 'Longitude of the location.'
                    },
                'radius': { 
                    'value': 3000,
                    'description': 'Radius (in meters).'
                    }
                }
            }
        }

client_id = 'MQ2SDSAN0EVC11ZX0QV6O411GQJZP2KZ1T10L'
client_secret = 'WJXHM3SAPVMTGBDV2SHMBS5J54NGLPDA5444G'
redirect_uri = 'http://haggle-dev.appspot.com/api/test'
