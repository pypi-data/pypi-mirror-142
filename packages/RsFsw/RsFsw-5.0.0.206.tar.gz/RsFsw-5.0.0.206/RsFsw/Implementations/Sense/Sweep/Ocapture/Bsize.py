from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Bsize:
	"""Bsize commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bsize", core, parent)

	def set(self, block_size: float) -> None:
		"""SCPI: [SENSe]:SWEep:OCAPture:BSIZe \n
		Snippet: driver.sense.sweep.ocapture.bsize.set(block_size = 1.0) \n
		No command help available \n
			:param block_size: No help available
		"""
		param = Conversions.decimal_value_to_str(block_size)
		self._core.io.write(f'SENSe:SWEep:OCAPture:BSIZe {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:SWEep:OCAPture:BSIZe \n
		Snippet: value: float = driver.sense.sweep.ocapture.bsize.get() \n
		No command help available \n
			:return: block_size: No help available"""
		response = self._core.io.query_str(f'SENSe:SWEep:OCAPture:BSIZe?')
		return Conversions.str_to_float(response)
