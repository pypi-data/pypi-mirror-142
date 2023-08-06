from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Holdoff:
	"""Holdoff commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("holdoff", core, parent)

	def set(self, period: float) -> None:
		"""SCPI: TRIGger[:SEQuence]:BBPower:HOLDoff \n
		Snippet: driver.trigger.sequence.bbPower.holdoff.set(period = 1.0) \n
		This command defines the holding time before the baseband power trigger event. The command requires the optional Digital
		Baseband Interface or the optional Analog Baseband Interface. Note that this command is maintained for compatibility
		reasons only. Use the method RsFsw.Applications.K10x_Lte.Trigger.Sequence.IfPower.Holdoff.set command for new remote
		control programs. \n
			:param period: Range: 150 ns to 1000 s, Unit: S
		"""
		param = Conversions.decimal_value_to_str(period)
		self._core.io.write(f'TRIGger:SEQuence:BBPower:HOLDoff {param}')

	def get(self) -> float:
		"""SCPI: TRIGger[:SEQuence]:BBPower:HOLDoff \n
		Snippet: value: float = driver.trigger.sequence.bbPower.holdoff.get() \n
		This command defines the holding time before the baseband power trigger event. The command requires the optional Digital
		Baseband Interface or the optional Analog Baseband Interface. Note that this command is maintained for compatibility
		reasons only. Use the method RsFsw.Applications.K10x_Lte.Trigger.Sequence.IfPower.Holdoff.set command for new remote
		control programs. \n
			:return: period: Range: 150 ns to 1000 s, Unit: S"""
		response = self._core.io.query_str(f'TRIGger:SEQuence:BBPower:HOLDoff?')
		return Conversions.str_to_float(response)
