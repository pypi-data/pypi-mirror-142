from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Holdoff:
	"""Holdoff commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("holdoff", core, parent)

	def set(self, time: float) -> None:
		"""SCPI: TRIGger[:SEQuence]:RFPower:HOLDoff \n
		Snippet: driver.applications.k149Uwb.trigger.sequence.rfPower.holdoff.set(time = 1.0) \n
		This command defines the holding time before the next trigger event. Note that this command is available for any trigger
		source, not just RF Power. Note that this command is maintained for compatibility reasons only. Use the method RsFsw.
		Applications.K10x_Lte.Trigger.Sequence.IfPower.Holdoff.set command for new remote control programs. \n
			:param time: Unit: S
		"""
		param = Conversions.decimal_value_to_str(time)
		self._core.io.write(f'TRIGger:SEQuence:RFPower:HOLDoff {param}')

	def get(self) -> float:
		"""SCPI: TRIGger[:SEQuence]:RFPower:HOLDoff \n
		Snippet: value: float = driver.applications.k149Uwb.trigger.sequence.rfPower.holdoff.get() \n
		This command defines the holding time before the next trigger event. Note that this command is available for any trigger
		source, not just RF Power. Note that this command is maintained for compatibility reasons only. Use the method RsFsw.
		Applications.K10x_Lte.Trigger.Sequence.IfPower.Holdoff.set command for new remote control programs. \n
			:return: time: Unit: S"""
		response = self._core.io.query_str(f'TRIGger:SEQuence:RFPower:HOLDoff?')
		return Conversions.str_to_float(response)
