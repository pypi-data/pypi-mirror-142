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
		"""SCPI: TRIGger[:SEQuence]:IFPower:HOLDoff \n
		Snippet: driver.applications.k17Mcgd.trigger.sequence.ifPower.holdoff.set(time = 1.0) \n
		This command defines the holding time before the next trigger event. Note that this command can be used for any trigger
		source, not just IF Power (despite the legacy keyword) . \n
			:param time: Range: 0 s to 10 s, Unit: S
		"""
		param = Conversions.decimal_value_to_str(time)
		self._core.io.write(f'TRIGger:SEQuence:IFPower:HOLDoff {param}')

	def get(self) -> float:
		"""SCPI: TRIGger[:SEQuence]:IFPower:HOLDoff \n
		Snippet: value: float = driver.applications.k17Mcgd.trigger.sequence.ifPower.holdoff.get() \n
		This command defines the holding time before the next trigger event. Note that this command can be used for any trigger
		source, not just IF Power (despite the legacy keyword) . \n
			:return: time: No help available"""
		response = self._core.io.query_str(f'TRIGger:SEQuence:IFPower:HOLDoff?')
		return Conversions.str_to_float(response)
