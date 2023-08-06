from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:MIXer:RFOVerrange[:STATe] \n
		Snippet: driver.applications.k6Pulse.sense.mixer.rfOverrange.state.set(state = False) \n
		If enabled, the band limits are extended beyond 'RF Start' and 'RF Stop' due to the capabilities of the used harmonics. \n
			:param state: ON | OFF | 1 | 0
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:MIXer:RFOVerrange:STATe {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:MIXer:RFOVerrange[:STATe] \n
		Snippet: value: bool = driver.applications.k6Pulse.sense.mixer.rfOverrange.state.get() \n
		If enabled, the band limits are extended beyond 'RF Start' and 'RF Stop' due to the capabilities of the used harmonics. \n
			:return: state: ON | OFF | 1 | 0"""
		response = self._core.io.query_str(f'SENSe:MIXer:RFOVerrange:STATe?')
		return Conversions.str_to_bool(response)
