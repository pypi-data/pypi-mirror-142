from typing import Any

from graphql import GraphQLScalarType as Scalar
from graphql.error import GraphQLError
from graphql.language import print_ast
from graphql.language.ast import ValueNode
from graphql.pyutils import inspect


def serialize_dict(output_value: Any) -> dict:
    if isinstance(output_value, dict):
        return output_value
    raise GraphQLError("Dict cannot represent a non Dict value: " + inspect(output_value))


def coerce_dict(input_value: Any) -> dict:
    if not isinstance(input_value, dict):
        raise GraphQLError("Dict cannot represent a non Dict value: " + inspect(input_value))
    return input_value


def parse_dict_literal(value_node: ValueNode, _variables: Any = None) -> dict:
    if not isinstance(value_node.value, dict):
        raise GraphQLError("Dict cannot represent a non Dict value: " + print_ast(value_node), value_node)
    return value_node.value


Dictionary = Scalar(
    name="Dict",
    description="The generic scalar type represents python dict.",
    serialize=serialize_dict,
    parse_value=coerce_dict,
    parse_literal=parse_dict_literal,
)
