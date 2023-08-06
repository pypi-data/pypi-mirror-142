from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Load:
	"""Load commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("load", core, parent)

	def set(self, filename: str) -> None:
		"""SCPI: [SENSe]:DDEMod:EQUalizer:LOAD \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.equalizer.load.set(filename = '1') \n
		This command selects a user-defined equalizer. The equalizer mode is automatically switched to USER (see
		[SENSe:]DDEMod:EQUalizer:MODE) . \n
			:param filename: Path and file name (without extension)
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SENSe:DDEMod:EQUalizer:LOAD {param}')

	def get(self) -> str:
		"""SCPI: [SENSe]:DDEMod:EQUalizer:LOAD \n
		Snippet: value: str = driver.applications.k70Vsa.sense.ddemod.equalizer.load.get() \n
		This command selects a user-defined equalizer. The equalizer mode is automatically switched to USER (see
		[SENSe:]DDEMod:EQUalizer:MODE) . \n
			:return: filename: Path and file name (without extension)"""
		response = self._core.io.query_str(f'SENSe:DDEMod:EQUalizer:LOAD?')
		return trim_str_response(response)
