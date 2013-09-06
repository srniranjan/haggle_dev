TEMPLATE_VALUES = {
        'discount_trends': {
            'header': 'Discount Trends',
            'params': { 'endpoint': 'aggregate_campaigns', 'property': 'discount_trends', 'lat': 40.745619, 'lon': -73.985296, 'radius': 3000 }
            },
        'score_preference_trends': {
            'header': 'Score Preference Trends',
            'params': { 'endpoint': 'aggregate_campaigns', 'property': 'score_preference_trends', 'lat': 40.745619, 'lon': -73.985296, 'radius': 3000 }
            },
        'bids_trends': {
            'header': 'Bids Trends',
            'params': { 'endpoint': 'aggregate_deals', 'property': 'bids_trends', 'lat': 40.745619, 'lon': -73.985296, 'radius': 3000 }
            },
        'user_trends': {
            'header': 'User Trends',
            'params': { 'endpoint': 'aggregate_deals', 'property': 'user_trends', 'lat': 40.745619, 'lon': -73.985296, 'radius': 3000 }
            },
        'time_trends': {
            'header': 'Time Trends',
            'params': { 'endpoint': 'aggregate_deals', 'property': 'time_trends', 'lat': 40.745619, 'lon': -73.985296, 'radius': 3000 }
            },
        'average_spending': {
            'header': 'Average Spending',
            'params': { 'endpoint': 'aggregate_deals', 'property': 'average_spending', 'lat': 40.745619, 'lon': -73.985296, 'radius': 3000 }
            }
        }

client_id = 'MQ2SDSAN0EVC11ZX0QV6O411GQJZP2KZ1T10L'
client_secret = 'WJXHM3SAPVMTGBDV2SHMBS5J54NGLPDA5444G'
redirect_uri = 'http://haggle-dev.appspot.com/api/test'
