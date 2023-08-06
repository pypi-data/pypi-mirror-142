from typing import Any

from graphql import GraphQLScalarType as Scalar
from graphql.language.ast import ValueNode


def serialize_scalar(output_value: Any) -> Any:
    return output_value


def coerce_scalar(input_value: Any) -> Any:
    return input_value


def parse_scalar_literal(value_node: ValueNode, _variables: Any = None) -> Any:
    return value_node.value


GenericScalar = Scalar(
    name="GenericScalar",
    description="The generic scalar type represents any python datatype.",
    serialize=serialize_scalar,
    parse_value=coerce_scalar,
    parse_literal=parse_scalar_literal,
)
