from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Meas:
	"""Meas commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("meas", core, parent)

	def set(self, file: str) -> None:
		"""SCPI: MMEMory:STORe:SPUR:MEAS \n
		Snippet: driver.applications.k50Spurious.massMemory.store.spur.meas.set(file = '1') \n
		This command stores the current measurement results (all enabled traces and tables of all windows) into the specified csv
		file. The results are output in the same order as they are displayed on the screen: window by window, trace by trace, and
		table row by table row. \n
			:param file: No help available
		"""
		param = Conversions.value_to_quoted_str(file)
		self._core.io.write(f'MMEMory:STORe:SPUR:MEAS {param}')
