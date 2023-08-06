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
		Snippet: driver.applications.k14Xnr5G.trigger.sequence.rfPower.holdoff.set(time = 1.0) \n
		No command help available \n
			:param time: No help available
		"""
		param = Conversions.decimal_value_to_str(time)
		self._core.io.write(f'TRIGger:SEQuence:RFPower:HOLDoff {param}')

	def get(self) -> float:
		"""SCPI: TRIGger[:SEQuence]:RFPower:HOLDoff \n
		Snippet: value: float = driver.applications.k14Xnr5G.trigger.sequence.rfPower.holdoff.get() \n
		No command help available \n
			:return: time: No help available"""
		response = self._core.io.query_str(f'TRIGger:SEQuence:RFPower:HOLDoff?')
		return Conversions.str_to_float(response)
