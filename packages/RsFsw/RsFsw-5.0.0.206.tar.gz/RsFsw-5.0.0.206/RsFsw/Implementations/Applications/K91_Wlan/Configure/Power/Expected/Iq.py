from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Iq:
	"""Iq commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("iq", core, parent)

	def set(self, value: float) -> None:
		"""SCPI: CONFigure:POWer:EXPected:IQ \n
		Snippet: driver.applications.k91Wlan.configure.power.expected.iq.set(value = 1.0) \n
		This command specifies the mean power level of the source signal as supplied to the instrument's digital I/Q input. This
		value is overwritten if 'Auto Level' mode is turned on. \n
			:param value: Unit: V
		"""
		param = Conversions.decimal_value_to_str(value)
		self._core.io.write(f'CONFigure:POWer:EXPected:IQ {param}')

	def get(self) -> float:
		"""SCPI: CONFigure:POWer:EXPected:IQ \n
		Snippet: value: float = driver.applications.k91Wlan.configure.power.expected.iq.get() \n
		This command specifies the mean power level of the source signal as supplied to the instrument's digital I/Q input. This
		value is overwritten if 'Auto Level' mode is turned on. \n
			:return: value: Unit: V"""
		response = self._core.io.query_str(f'CONFigure:POWer:EXPected:IQ?')
		return Conversions.str_to_float(response)
