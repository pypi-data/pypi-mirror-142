from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Types import DataType
from ....Internal.ArgSingleList import ArgSingleList
from ....Internal.ArgSingle import ArgSingle
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class New:
	"""New commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("new", core, parent)

	def set(self, channel_type: enums.ChannelType, channel_name: str) -> None:
		"""SCPI: INSTrument:CREate[:NEW] \n
		Snippet: driver.instrument.create.new.set(channel_type = enums.ChannelType.IqAnalyzer=IQ, channel_name = '1') \n
		This command adds an additional measurement channel. You can configure up to 10 measurement channels at the same time
		(depending on available memory) .
			INTRO_CMD_HELP: See also \n
			- method RsFsw.Instrument.Select.set
			- method RsFsw.Instrument.delete \n
			:param channel_type: (enum or string) Channel type of the new channel. For a list of available channel types see method RsFsw.Instrument.ListPy.get_.
			:param channel_name: String containing the name of the channel. Note that you can not assign an existing channel name to a new channel; this will cause an error.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('channel_type', channel_type, DataType.EnumExt, enums.ChannelType), ArgSingle('channel_name', channel_name, DataType.String))
		self._core.io.write_with_opc(f'INSTrument:CREate:NEW {param}'.rstrip())
		self._core.io.write('INIT:CONT OFF')
