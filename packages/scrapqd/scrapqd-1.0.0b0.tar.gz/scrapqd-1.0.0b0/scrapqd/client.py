from graphql import graphql_sync

from scrapqd.gql.schema import schema


def execute_sync(query, variables=None):
    """API to execute client query from python

    :param query: graphql query
    :param variables: graphql query variables
    :return: Dict
    """
    if variables is None:
        variables = {}
    result = graphql_sync(schema, query, variable_values=variables)
    return result
