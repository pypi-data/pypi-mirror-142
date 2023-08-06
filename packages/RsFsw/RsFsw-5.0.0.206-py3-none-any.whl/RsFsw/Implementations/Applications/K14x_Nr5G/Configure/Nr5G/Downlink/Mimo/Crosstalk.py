from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Crosstalk:
	"""Crosstalk commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("crosstalk", core, parent)

	def set(self, crosstalk: bool) -> None:
		"""SCPI: CONFigure[:NR5G]:DL:MIMO:CROSstalk \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.downlink.mimo.crosstalk.set(crosstalk = False) \n
		No command help available \n
			:param crosstalk: No help available
		"""
		param = Conversions.bool_to_str(crosstalk)
		self._core.io.write(f'CONFigure:NR5G:DL:MIMO:CROSstalk {param}')

	def get(self) -> bool:
		"""SCPI: CONFigure[:NR5G]:DL:MIMO:CROSstalk \n
		Snippet: value: bool = driver.applications.k14Xnr5G.configure.nr5G.downlink.mimo.crosstalk.get() \n
		No command help available \n
			:return: crosstalk: No help available"""
		response = self._core.io.query_str(f'CONFigure:NR5G:DL:MIMO:CROSstalk?')
		return Conversions.str_to_bool(response)
