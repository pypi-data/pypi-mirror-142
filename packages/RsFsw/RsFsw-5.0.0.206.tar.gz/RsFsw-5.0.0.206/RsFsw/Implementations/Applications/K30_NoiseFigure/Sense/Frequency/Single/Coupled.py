from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Coupled:
	"""Coupled commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("coupled", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:FREQuency:SINGle:COUPled \n
		Snippet: driver.applications.k30NoiseFigure.sense.frequency.single.coupled.set(state = False) \n
		Couples or decouples frequency selection to the contents of a sweep list. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Decouples frequency selection ON | 1 Couples frequency selection
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:FREQuency:SINGle:COUPled {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:FREQuency:SINGle:COUPled \n
		Snippet: value: bool = driver.applications.k30NoiseFigure.sense.frequency.single.coupled.get() \n
		Couples or decouples frequency selection to the contents of a sweep list. \n
			:return: state: ON | OFF | 0 | 1 OFF | 0 Decouples frequency selection ON | 1 Couples frequency selection"""
		response = self._core.io.query_str(f'SENSe:FREQuency:SINGle:COUPled?')
		return Conversions.str_to_bool(response)
