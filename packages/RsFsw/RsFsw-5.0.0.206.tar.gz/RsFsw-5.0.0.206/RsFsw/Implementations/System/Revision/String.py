from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class String:
	"""String commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("string", core, parent)

	def set(self, name: str) -> None:
		"""SCPI: SYSTem:REVision[:STRing] \n
		Snippet: driver.system.revision.string.set(name = '1') \n
		Sets the response to the REV? query to the defined string (HP emulation only, see method RsFsw.System.Language.set) . \n
			:param name: No help available
		"""
		param = Conversions.value_to_quoted_str(name)
		self._core.io.write(f'SYSTem:REVision:STRing {param}')

	def get(self) -> str:
		"""SCPI: SYSTem:REVision[:STRing] \n
		Snippet: value: str = driver.system.revision.string.get() \n
		Sets the response to the REV? query to the defined string (HP emulation only, see method RsFsw.System.Language.set) . \n
			:return: name: No help available"""
		response = self._core.io.query_str(f'SYSTem:REVision:STRing?')
		return trim_str_response(response)
