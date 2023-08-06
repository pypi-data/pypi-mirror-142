from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Time:
	"""Time commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("time", core, parent)

	def set(self, offset: float, antenna=repcap.Antenna.Default) -> None:
		"""SCPI: TRIGger[:SEQuence]:HOLDoff<ant>[:TIME] \n
		Snippet: driver.applications.k14Xnr5G.trigger.sequence.holdoff.time.set(offset = 1.0, antenna = repcap.Antenna.Default) \n
		This command defines the trigger offset. \n
			:param offset: numeric value Unit: s
			:param antenna: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Holdoff')
		"""
		param = Conversions.decimal_value_to_str(offset)
		antenna_cmd_val = self._cmd_group.get_repcap_cmd_value(antenna, repcap.Antenna)
		self._core.io.write(f'TRIGger:SEQuence:HOLDoff{antenna_cmd_val}:TIME {param}')

	def get(self, antenna=repcap.Antenna.Default) -> float:
		"""SCPI: TRIGger[:SEQuence]:HOLDoff<ant>[:TIME] \n
		Snippet: value: float = driver.applications.k14Xnr5G.trigger.sequence.holdoff.time.get(antenna = repcap.Antenna.Default) \n
		This command defines the trigger offset. \n
			:param antenna: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Holdoff')
			:return: offset: numeric value Unit: s"""
		antenna_cmd_val = self._cmd_group.get_repcap_cmd_value(antenna, repcap.Antenna)
		response = self._core.io.query_str(f'TRIGger:SEQuence:HOLDoff{antenna_cmd_val}:TIME?')
		return Conversions.str_to_float(response)
