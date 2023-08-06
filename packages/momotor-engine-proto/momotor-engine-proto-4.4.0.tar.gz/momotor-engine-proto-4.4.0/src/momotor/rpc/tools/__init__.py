import typing

from momotor.rpc.proto.tool_pb2 import ToolSet as ToolSetMessage

TN = typing.TypeVar('TN')


def toolsets_to_message(toolsets: typing.Iterable[typing.AbstractSet[str]]) -> typing.Iterable[ToolSetMessage]:
    """ Convert an iterable of ToolName objects into a sequence of Tool messages
    """
    for toolset in toolsets:
        yield ToolSetMessage(
            tool=[str(tool) for tool in toolset]
        )


def message_to_toolsets(toolset_message: typing.Optional[typing.Sequence[ToolSetMessage]]) \
        -> typing.Iterable[typing.FrozenSet[str]]:

    """ Convert a sequence of Tool messages back into an iterable of tool sets """
    if toolset_message:
        for msg in toolset_message:
            yield frozenset(msg.tool)
