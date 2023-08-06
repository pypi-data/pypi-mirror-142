from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Capture:
	"""Capture commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("capture", core, parent)

	def set(self, count: int) -> None:
		"""SCPI: DIAGnostic:DSP:DUMP:CAPTure \n
		Snippet: driver.applications.k149Uwb.diagnostic.dsp.dump.capture.set(count = 1) \n
		No command help available \n
			:param count: No help available
		"""
		param = Conversions.decimal_value_to_str(count)
		self._core.io.write(f'DIAGnostic:DSP:DUMP:CAPTure {param}')

	def get(self) -> int:
		"""SCPI: DIAGnostic:DSP:DUMP:CAPTure \n
		Snippet: value: int = driver.applications.k149Uwb.diagnostic.dsp.dump.capture.get() \n
		No command help available \n
			:return: count: No help available"""
		response = self._core.io.query_str(f'DIAGnostic:DSP:DUMP:CAPTure?')
		return Conversions.str_to_int(response)
