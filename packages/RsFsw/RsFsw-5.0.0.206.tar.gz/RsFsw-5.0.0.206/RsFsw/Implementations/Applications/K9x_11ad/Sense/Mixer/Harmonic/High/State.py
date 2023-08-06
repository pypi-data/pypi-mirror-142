from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, freq_high: bool) -> None:
		"""SCPI: [SENSe]:MIXer:HARMonic:HIGH:STATe \n
		Snippet: driver.applications.k9X11Ad.sense.mixer.harmonic.high.state.set(freq_high = False) \n
		This command specifies whether a second (high) harmonic is to be used to cover the band's frequency range. \n
			:param freq_high: No help available
		"""
		param = Conversions.bool_to_str(freq_high)
		self._core.io.write(f'SENSe:MIXer:HARMonic:HIGH:STATe {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:MIXer:HARMonic:HIGH:STATe \n
		Snippet: value: bool = driver.applications.k9X11Ad.sense.mixer.harmonic.high.state.get() \n
		This command specifies whether a second (high) harmonic is to be used to cover the band's frequency range. \n
			:return: freq_high: No help available"""
		response = self._core.io.query_str(f'SENSe:MIXer:HARMonic:HIGH:STATe?')
		return Conversions.str_to_bool(response)
