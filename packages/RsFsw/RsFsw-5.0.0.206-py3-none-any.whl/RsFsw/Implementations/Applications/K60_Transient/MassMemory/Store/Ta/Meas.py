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
		"""SCPI: MMEMory:STORe:TA:MEAS \n
		Snippet: driver.applications.k60Transient.massMemory.store.ta.meas.set(file = '1') \n
		This command stores the current measurement results (all enabled traces of all windows) into the specified .csv file.
		Secure User Mode In secure user mode, settings that are stored on the instrument are stored to volatile memory, which is
		restricted to 256 MB. Thus, a 'memory limit reached' error can occur although the hard disk indicates that storage space
		is still available. To store data permanently, select an external storage location such as a USB memory device.
		For details, see 'Protecting Data Using the Secure User Mode'. \n
			:param file: path and file name
		"""
		param = Conversions.value_to_quoted_str(file)
		self._core.io.write(f'MMEMory:STORe:TA:MEAS {param}')
