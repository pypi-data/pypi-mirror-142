from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dcycle:
	"""Dcycle commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dcycle", core, parent)

	def set(self, duty_cycle: float) -> None:
		"""SCPI: CONFigure:REFSignal:GOS:DCYCle \n
		Snippet: driver.applications.k18AmplifierEt.configure.refSignal.gos.dcycle.set(duty_cycle = 1.0) \n
		This command defines the duty cycle of an internally generated pulsed reference signal. \n
			:param duty_cycle: numeric value Unit: %
		"""
		param = Conversions.decimal_value_to_str(duty_cycle)
		self._core.io.write(f'CONFigure:REFSignal:GOS:DCYCle {param}')

	def get(self) -> float:
		"""SCPI: CONFigure:REFSignal:GOS:DCYCle \n
		Snippet: value: float = driver.applications.k18AmplifierEt.configure.refSignal.gos.dcycle.get() \n
		This command defines the duty cycle of an internally generated pulsed reference signal. \n
			:return: duty_cycle: numeric value Unit: %"""
		response = self._core.io.query_str(f'CONFigure:REFSignal:GOS:DCYCle?')
		return Conversions.str_to_float(response)
