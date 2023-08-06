from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SelectName:
	"""SelectName commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("selectName", core, parent)

	def set(self, channel_name: str) -> None:
		"""SCPI: INSTrument[:SELect] \n
		Snippet: driver.instrument.selectName.set(channel_name = '1') \n
		This command activates a new channel with the defined channel type, or selects an existing channel with the specified
		name. Also see
			INTRO_CMD_HELP: See also \n
			- method RsFsw.Instrument.Create.New.set
			- 'Programming example: performing a sequence of measurements' \n
			:param channel_name: String containing the name of the channel.
		"""
		param = Conversions.value_to_quoted_str(channel_name)
		self._core.io.write_with_opc(f'INSTrument:SELect {param}')
