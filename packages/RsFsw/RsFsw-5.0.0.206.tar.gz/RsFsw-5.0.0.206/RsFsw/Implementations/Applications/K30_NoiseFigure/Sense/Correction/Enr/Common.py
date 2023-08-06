from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Common:
	"""Common commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("common", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:CORRection:ENR:COMMon \n
		Snippet: driver.applications.k30NoiseFigure.sense.correction.enr.common.set(state = False) \n
		This command turns the use of a common ENR on or off. For more information see 'Common Noise Source'. \n
			:param state: ON | OFF | 1 | 0
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:CORRection:ENR:COMMon {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:CORRection:ENR:COMMon \n
		Snippet: value: bool = driver.applications.k30NoiseFigure.sense.correction.enr.common.get() \n
		This command turns the use of a common ENR on or off. For more information see 'Common Noise Source'. \n
			:return: state: ON | OFF | 1 | 0"""
		response = self._core.io.query_str(f'SENSe:CORRection:ENR:COMMon?')
		return Conversions.str_to_bool(response)
