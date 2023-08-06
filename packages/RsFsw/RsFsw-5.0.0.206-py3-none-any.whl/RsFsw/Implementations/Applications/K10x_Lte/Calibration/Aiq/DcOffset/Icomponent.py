from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Icomponent:
	"""Icomponent commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("icomponent", core, parent)

	def set(self, offset: float) -> None:
		"""SCPI: CALibration:AIQ:DCOFfset:I \n
		Snippet: driver.applications.k10Xlte.calibration.aiq.dcOffset.icomponent.set(offset = 1.0) \n
		No command help available \n
			:param offset: No help available
		"""
		param = Conversions.decimal_value_to_str(offset)
		self._core.io.write(f'CALibration:AIQ:DCOFfset:I {param}')

	def get(self) -> float:
		"""SCPI: CALibration:AIQ:DCOFfset:I \n
		Snippet: value: float = driver.applications.k10Xlte.calibration.aiq.dcOffset.icomponent.get() \n
		No command help available \n
			:return: offset: No help available"""
		response = self._core.io.query_str(f'CALibration:AIQ:DCOFfset:I?')
		return Conversions.str_to_float(response)
