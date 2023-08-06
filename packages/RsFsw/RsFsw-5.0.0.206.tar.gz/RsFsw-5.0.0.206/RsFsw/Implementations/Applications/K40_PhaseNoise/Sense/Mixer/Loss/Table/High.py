from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class High:
	"""High commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("high", core, parent)

	def set(self, arg_0: str) -> None:
		"""SCPI: [SENSe]:MIXer:LOSS:TABLe:HIGH \n
		Snippet: driver.applications.k40PhaseNoise.sense.mixer.loss.table.high.set(arg_0 = '1') \n
		No command help available \n
			:param arg_0: No help available
		"""
		param = Conversions.value_to_quoted_str(arg_0)
		self._core.io.write(f'SENSe:MIXer:LOSS:TABLe:HIGH {param}')

	def get(self) -> str:
		"""SCPI: [SENSe]:MIXer:LOSS:TABLe:HIGH \n
		Snippet: value: str = driver.applications.k40PhaseNoise.sense.mixer.loss.table.high.get() \n
		No command help available \n
			:return: arg_0: No help available"""
		response = self._core.io.query_str(f'SENSe:MIXer:LOSS:TABLe:HIGH?')
		return trim_str_response(response)
