from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Types import DataType
from ....Internal.ArgSingleList import ArgSingleList
from ....Internal.ArgSingle import ArgSingle
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Replace:
	"""Replace commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("replace", core, parent)

	def set(self, current_channel_name: str, channel_type: enums.ChannelType, new_channel_name: str) -> None:
		"""SCPI: INSTrument:CREate:REPLace \n
		Snippet: driver.instrument.create.replace.set(current_channel_name = '1', channel_type = enums.ChannelType.IqAnalyzer=IQ, new_channel_name = '1') \n
		This command replaces a channel with another one. \n
			:param current_channel_name: No help available
			:param channel_type: Channel type of the new channel. For a list of available channel types see method RsFsw.Instrument.ListPy.get_.
			:param new_channel_name: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('current_channel_name', current_channel_name, DataType.String), ArgSingle('channel_type', channel_type, DataType.Enum, enums.ChannelType), ArgSingle('new_channel_name', new_channel_name, DataType.String))
		self._core.io.write_with_opc(f'INSTrument:CREate:REPLace {param}'.rstrip())
		self._core.io.write('INIT:CONT OFF')
