from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Normalise:
	"""Normalise commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("normalise", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: CONFigure:WLAN:SMAPping:NORMalise \n
		Snippet: driver.applications.k91Wlan.configure.wlan.smapping.normalise.set(state = False) \n
		This remote control command specifies whether an amplification of the signal power due to the spatial mapping is
		performed according to the matrix entries. If this command it set to ON then the spatial mapping matrix is scaled by a
		constant factor to obtain a passive spatial mapping matrix which does not increase the total transmitted power. If this
		command is set to OFF the normalization step is omitted. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'CONFigure:WLAN:SMAPping:NORMalise {param}')

	def get(self) -> bool:
		"""SCPI: CONFigure:WLAN:SMAPping:NORMalise \n
		Snippet: value: bool = driver.applications.k91Wlan.configure.wlan.smapping.normalise.get() \n
		This remote control command specifies whether an amplification of the signal power due to the spatial mapping is
		performed according to the matrix entries. If this command it set to ON then the spatial mapping matrix is scaled by a
		constant factor to obtain a passive spatial mapping matrix which does not increase the total transmitted power. If this
		command is set to OFF the normalization step is omitted. \n
			:return: state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on"""
		response = self._core.io.query_str(f'CONFigure:WLAN:SMAPping:NORMalise?')
		return Conversions.str_to_bool(response)
