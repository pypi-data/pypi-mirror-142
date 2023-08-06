from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Holdoff:
	"""Holdoff commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("holdoff", core, parent)

	def set(self, delay: float) -> None:
		"""SCPI: [SENSe]:SWEep:EGATe:HOLDoff \n
		Snippet: driver.applications.k14Xnr5G.sense.sweep.egate.holdoff.set(delay = 1.0) \n
		No command help available \n
			:param delay: No help available
		"""
		param = Conversions.decimal_value_to_str(delay)
		self._core.io.write(f'SENSe:SWEep:EGATe:HOLDoff {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:SWEep:EGATe:HOLDoff \n
		Snippet: value: float = driver.applications.k14Xnr5G.sense.sweep.egate.holdoff.get() \n
		No command help available \n
			:return: delay: No help available"""
		response = self._core.io.query_str(f'SENSe:SWEep:EGATe:HOLDoff?')
		return Conversions.str_to_float(response)
