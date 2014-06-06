ENV_NAME="haggle-test1.appspot.com"
TEMPLATE_VALUES = {
        'discount_trends': {
            'header': 'Discount Trends',
            'url': 'https://'+ENV_NAME+'/api/analytics/',
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
            'url': 'https://'+ENV_NAME+'/api/analytics/',
            'description': 'Returns trends on the profile of users frequenting a specified area',
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
            'url': 'https://'+ENV_NAME+'/api/analytics/',
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
            'url': 'https://'+ENV_NAME+'/api/analytics/',
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
            'url': 'https://'+ENV_NAME+'/api/analytics/',
            'description':'Discover what times an area goes deal crazy. Time Trends helps you plan for all the Haggle Happy Hours in your area. Or, look up time trends in other areas to see how your neighborhood shores up against them.',
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
            'url': 'https://'+ENV_NAME+'/api/analytics/',
            'description': 'Are you attracting big spenders or mass selling those hot cakes? Whatever your strategy is, check out if you are above or below the competition in your area.',
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
            },
            'users_search': {
            'header': 'Users Search',
            'url': 'https://'+ENV_NAME+'/api/analytics/',
            'description': 'Returns a list of users that match your query. If you are a restaurant, check out our <a href="/endpoints/render?property=vendors_deal_history">Vendor deals history</a> search function to analyze your previous customers.',
            'endpoint': 'users_search',
            'params': {
                'property': { 
                    'value': 'discount_trends',
                    'description': 'property_desc'
                    },
                'uid': {
                    'value': 21325632,
                    'description': "A specific user's ID"
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
            'users_history': {
            'header': 'Users History',
            'url': 'https://'+ENV_NAME+'/api/analytics/',
            'description': '(Vendors only) Returns a list of customers with the specified minimum/maximum history score. If no parameters are set, returns a sorted list of previous customers. <br>Check out our <a href="http://google.com">Vendor deals history</a> search function to analyze your previous customers.',
            'endpoint': 'users_search',
            'params': {
                'property': { 
                    'value': 'discount_trends',
                    'description': 'property_desc'
                    },
                'min': {
                    'value': 1,
                    'description': 'Minimum History score.'
                    },
                'max': {
                    'value': 4,
                    'description': 'Maximum History score.'
                    },
                }
            },
            'users_loyalty': {
            'header': 'Users Loyalty',
            'url': 'https://'+ENV_NAME+'/api/analytics/',
            'description': '(Vendors only) Returns a list of customers with the specified minimum/maximum loyalty score. If no parameters are set, returns a sorted list of previous customers. <br>Check out our <a href="http://google.com">Vendor deals history</a> search function to analyze your previous customers.',
            'endpoint': 'users_search',
            'params': {
                'property': { 
                    'value': 'discount_trends',
                    'description': 'property_desc'
                    },
                 'min': {
                    'value': 1,
                    'description': 'Minimum Loyalty score.'
                    },
                'max': {
                    'value': 4,
                    'description': 'Maximum Loyalty score.'
                    },
                }
            },
            'users_social_influence': {
            'header': 'Users Social Influence',
            'url': 'https://'+ENV_NAME+'/api/analytics/',
            'description': '(Vendors only) Returns a list of customers with the specified minimum/maximum Social Influence score. If no parameters are set, returns a sorted list of previous customers. <br>Check out our <a href="http://google.com">Vendor deals history</a> search function to analyze your previous customers.',
            'endpoint': 'users_search',
            'params': {
                'property': { 
                    'value': 'discount_trends',
                    'description': 'property_desc'
                    },
                 'min': {
                    'value': 1,
                    'description': 'Minimum Social Influence score.'
                    },
                'max': {
                    'value': 4,
                    'description': 'Maximum Social Influence score.'
                    },
                }
            },
            'users_purchasing_power': {
            'header': 'Users Purchasing Power',
            'url': 'https://'+ENV_NAME+'/api/analytics/',
            'description': '(Vendors only) Returns a list of customers with the specified minimum/maximum purchasing power score. If no parameters are set, returns a sorted list of previous customers. <br>Check out our <a href="http://google.com">Vendor deals history</a> search function to analyze your previous customers.',
            'endpoint': 'users_search',
            'params': {
                'property': { 
                    'value': 'discount_trends',
                    'description': 'property_desc'
                    },
                 'min': {
                    'value': 1,
                    'description': 'Minimum Purchasing Power score.'
                    },
                'max': {
                    'value': 4,
                    'description': 'Maximum Purchasing Power score.'
                    },
                }
            },
            'vendors_categories': {
            'header': 'Vendors Categories',
            'url': 'https://'+ENV_NAME+'/api/analytics/',
            'description': 'Returns either the entire tree or leaf of our categories tree.',
            'endpoint': 'categories',
            'params': {
                'property': { 
                    'value': 'categories',
                    'description': 'property_desc'
                    },
                'leaf': {
                    'value': 'American',
                    'description': '(Optional) Node which you want to start with. Leave blank for the whole tree.'
                    },
                }
            },
            'users_deals': {
            'header': 'Vendors Deal History',
            'url': 'https://'+ENV_NAME+'/api/analytics/',
            'description': 'Analyze your data. Grab your business by the horns. <br>Returns a list of deals based on your parameters.',
            'endpoint': 'users_search',
            'params': {
                'property': { 
                    'value': 'discount_trends',
                    'description': 'property_desc'
                    },
                'since': {
                    'value': 20130320,
                    'description': 'Since (optional) (YYYYMMDD)'
                    },
                'before': {
                    'value': 20130326,
                    'description': 'Before (optional) (YYYYMMDD)'
                    },
                },
            'other_params': '''Other (optional) parameters: <br><table class="table table-hover">
                    <tr>
                        <th>Variable</th>
                        <th>Description</th>
                        <th>HTML param</th>
                    </tr>
                    <tr>
                        <td>Minimum/Maximum Purchasing Power</td>
                        <td>Filters deals by the Purchasing Power of the customers</td>
                        <td>minpp, maxpp</td>
                    </tr>
                    <tr>
                        <td>Minimum/Maximum Loyalty</td>
                        <td>Filters deals by the Loyaly of the customers</td>
                        <td>minlty, maxlty</td>
                    </tr>
                    <tr>
                        <td>Minimum/Maximum Social Influence</td>
                        <td>Filters deals by the Social Influence of the customers</td>
                        <td>minsoc, maxsoc</td>
                    </tr>
                    <tr>
                        <td>Minimum/Maximum History</td>
                        <td>Filters deals by the History of the customers</td>
                        <td>minhist, maxhist</td>
                    </tr>
                </table>''',
            },
            'vendors_general_overview': {
            'header': 'Overview',
            'url': 'local',
            'description': 'Returns an overview of the harmonized restaurants in our datastore. Use this endpoint to learn the different cuisines, neighborhoods etc... you can query by.',
            'endpoint': '/api/restaurants_overview',
            'params': {}
            },
            'vendors_general_explore': {
            'header': 'Explore',
            'url': 'local',
            'description': 'Returns a list of harmonized restaurants from our datastore. The restaurants returned have their data harmonized across 3 social networks.',
            'endpoint': '/api/restaurants',
            'params': {
                    'dlr_rating': {
                        'value': '',
                        'description': 'Dollar Rating'
                        },
                    'lat': {
                        'value': '',
                        'description': 'Latitude'
                        },
                    'lon': {
                        'value': '',
                        'description': 'Longitude'
                        },
                    'radius': {
                        'value': '',
                        'description': 'Radius (in meters).'
                        },
                    'cuisine': {
                        'value': '',
                        'description': 'Cuisine'
                        },
                    'name': {
                        'value': '',
                        'description': 'Restaurant name'
                        },
                    'neigh': {
                        'value': '',
                        'description': 'Neighborhood'
                        }
                }
            }
        }

client_id = 'MQ2SDSAN0EVC11ZX0QV6O411GQJZP2KZ1T10L'
client_secret = 'WJXHM3SAPVMTGBDV2SHMBS5J54NGLPDA5444G'
redirect_uri = 'http://haggle-dev.appspot.com/api/test'
