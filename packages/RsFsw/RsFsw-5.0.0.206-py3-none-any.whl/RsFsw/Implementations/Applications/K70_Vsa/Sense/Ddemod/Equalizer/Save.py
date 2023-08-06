from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Save:
	"""Save commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("save", core, parent)

	def set(self, filename: str) -> None:
		"""SCPI: [SENSe]:DDEMod:EQUalizer:SAVE \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.equalizer.save.set(filename = '1') \n
		This command saves the current equalizer results to a file. \n
			:param filename: File name
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SENSe:DDEMod:EQUalizer:SAVE {param}')

	def get(self) -> str:
		"""SCPI: [SENSe]:DDEMod:EQUalizer:SAVE \n
		Snippet: value: str = driver.applications.k70Vsa.sense.ddemod.equalizer.save.get() \n
		This command saves the current equalizer results to a file. \n
			:return: filename: File name"""
		response = self._core.io.query_str(f'SENSe:DDEMod:EQUalizer:SAVE?')
		return trim_str_response(response)
