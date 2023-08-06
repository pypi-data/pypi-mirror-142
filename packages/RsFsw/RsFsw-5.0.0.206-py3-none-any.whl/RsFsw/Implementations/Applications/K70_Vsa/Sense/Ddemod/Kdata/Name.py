from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Name:
	"""Name commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("name", core, parent)

	def set(self, filename: str) -> None:
		"""SCPI: [SENSe]:DDEMod:KDATa[:NAME] \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.kdata.name.set(filename = '1') \n
		This command selects the Known Data file. Note that known data must be activated ([SENSe:]DDEMod:KDATa:STATe) before you
		can select a file. \n
			:param filename: No help available
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SENSe:DDEMod:KDATa:NAME {param}')

	def get(self) -> str:
		"""SCPI: [SENSe]:DDEMod:KDATa[:NAME] \n
		Snippet: value: str = driver.applications.k70Vsa.sense.ddemod.kdata.name.get() \n
		This command selects the Known Data file. Note that known data must be activated ([SENSe:]DDEMod:KDATa:STATe) before you
		can select a file. \n
			:return: filename: No help available"""
		response = self._core.io.query_str(f'SENSe:DDEMod:KDATa:NAME?')
		return trim_str_response(response)
