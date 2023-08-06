from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, filename: str) -> None:
		"""SCPI: MMEMory:LOAD:SEM:STATe \n
		Snippet: driver.applications.k91Wlan.massMemory.load.sem.state.set(filename = '1') \n
		This command loads a spectrum emission mask setup from an xml file. Note that this command is maintained for
		compatibility reasons only. Use the SENS:ESP:PRES command for new remote control programs.
		(See [SENSe:]ESPectrum<sb>:PRESet[:STANdard]) . See the R&S FSW User Manual, 'Remote commands for SEM measurements'
		chapter. \n
			:param filename: string Path and name of the .xml file that contains the SEM setup information.
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write_with_opc(f'MMEMory:LOAD:SEM:STATe 1, {param}')
