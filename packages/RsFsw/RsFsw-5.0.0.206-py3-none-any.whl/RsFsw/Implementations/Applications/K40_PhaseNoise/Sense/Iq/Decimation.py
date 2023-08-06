from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Decimation:
	"""Decimation commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("decimation", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:IQ:DECimation \n
		Snippet: driver.applications.k40PhaseNoise.sense.iq.decimation.set(state = False) \n
		This command turns decimation of results on and off. \n
			:param state: ON | OFF | 1 | 0
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:IQ:DECimation {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:IQ:DECimation \n
		Snippet: value: bool = driver.applications.k40PhaseNoise.sense.iq.decimation.get() \n
		This command turns decimation of results on and off. \n
			:return: state: ON | OFF | 1 | 0"""
		response = self._core.io.query_str(f'SENSe:IQ:DECimation?')
		return Conversions.str_to_bool(response)
