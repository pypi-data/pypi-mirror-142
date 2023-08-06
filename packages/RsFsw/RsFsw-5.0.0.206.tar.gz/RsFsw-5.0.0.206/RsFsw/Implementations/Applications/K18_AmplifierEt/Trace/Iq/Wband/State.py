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
		"""SCPI: TRACe:IQ:WBANd[:STATe] \n
		Snippet: driver.applications.k18AmplifierEt.trace.iq.wband.state.set(state = False) \n
		This command turns the wideband signal path on and off. The wideband signal path is available with the corresponding
		bandwidth extensions available for the R&S FSW. \n
			:param state: ON | 1 Turns on the wideband signal path. By default, the application allows you to use the maximum available bandwidth ('Auto' mode in manual operation) . You have to turn on the wideband signal path when you want to use bandwidths greater than 80 MHz. OFF | 0 Turns off the wideband signal path. The largest available bandwidth is 80 MHz.
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'TRACe:IQ:WBANd:STATe {param}')

	def get(self) -> bool:
		"""SCPI: TRACe:IQ:WBANd[:STATe] \n
		Snippet: value: bool = driver.applications.k18AmplifierEt.trace.iq.wband.state.get() \n
		This command turns the wideband signal path on and off. The wideband signal path is available with the corresponding
		bandwidth extensions available for the R&S FSW. \n
			:return: state: ON | 1 Turns on the wideband signal path. By default, the application allows you to use the maximum available bandwidth ('Auto' mode in manual operation) . You have to turn on the wideband signal path when you want to use bandwidths greater than 80 MHz. OFF | 0 Turns off the wideband signal path. The largest available bandwidth is 80 MHz."""
		response = self._core.io.query_str(f'TRACe:IQ:WBANd:STATe?')
		return Conversions.str_to_bool(response)
