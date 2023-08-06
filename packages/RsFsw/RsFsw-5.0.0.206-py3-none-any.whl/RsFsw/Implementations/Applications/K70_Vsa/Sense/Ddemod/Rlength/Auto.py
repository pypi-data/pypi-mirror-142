from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Auto:
	"""Auto commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("auto", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:DDEMod:RLENgth:AUTO \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.rlength.auto.set(state = False) \n
		If enabled, the capture length is automatically adapted as required according to the current result length, burst and
		pattern search settings, and network-specific characteristics (e.g. burst and frame structures) . \n
			:param state: No help available
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:DDEMod:RLENgth:AUTO {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:DDEMod:RLENgth:AUTO \n
		Snippet: value: bool = driver.applications.k70Vsa.sense.ddemod.rlength.auto.get() \n
		If enabled, the capture length is automatically adapted as required according to the current result length, burst and
		pattern search settings, and network-specific characteristics (e.g. burst and frame structures) . \n
			:return: state: No help available"""
		response = self._core.io.query_str(f'SENSe:DDEMod:RLENgth:AUTO?')
		return Conversions.str_to_bool(response)
