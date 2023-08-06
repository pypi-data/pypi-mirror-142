from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Used:
	"""Used commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("used", core, parent)

	def get(self) -> float:
		"""SCPI: [SENSe]:SWEep:TYPE:USED \n
		Snippet: value: float = driver.sense.sweep.typePy.used.get() \n
		This command queries the sweep type if you have turned on automatic selection of the sweep type. \n
			:return: type_py: SWE Normal sweep FFT FFT mode"""
		response = self._core.io.query_str(f'SENSe:SWEep:TYPE:USED?')
		return Conversions.str_to_float(response)
