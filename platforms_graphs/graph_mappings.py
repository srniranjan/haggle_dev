from platforms_graphs.graph_view import average_aggregator, median_aggregator, blind_addition_aggregator

view_to_graphmodel_mapping = {'LineGraphView':'platforms_graphs.graph_model.LineGraphModelBuilder',
                         'BarGraphView':'platforms_graphs.graph_model.BarGraphModelBuilder',
                         'AggregateBarGraphView':'platforms_graphs.graph_model.AggregateBarGraphModelBuilder'}

model_list = {'AvailedDeal' : 'platforms_graphs.model.AvailedDeal',
              'Deal' : 'platforms_graphs.model.Deal',
              'UserScore' : 'platforms_graphs.model.UserScore',
              'Restaurant' : 'platforms_graphs.model.Restaurant'}

aggregator_strategy_list = {'Average' : average_aggregator,
                            'Median' : median_aggregator,
                            'Blind Addition' : blind_addition_aggregator}