from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NrqMaster:
	"""NrqMaster commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nrqMaster", core, parent)

	def set(self, device_name: str) -> None:
		"""SCPI: CONFigure[:NR5G]:NRQMaster \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.nrqMaster.set(device_name = '1') \n
		No command help available \n
			:param device_name: No help available
		"""
		param = Conversions.value_to_quoted_str(device_name)
		self._core.io.write(f'CONFigure:NR5G:NRQMaster {param}')

	def get(self) -> str:
		"""SCPI: CONFigure[:NR5G]:NRQMaster \n
		Snippet: value: str = driver.applications.k14Xnr5G.configure.nr5G.nrqMaster.get() \n
		No command help available \n
			:return: device_name: No help available"""
		response = self._core.io.query_str(f'CONFigure:NR5G:NRQMaster?')
		return trim_str_response(response)
