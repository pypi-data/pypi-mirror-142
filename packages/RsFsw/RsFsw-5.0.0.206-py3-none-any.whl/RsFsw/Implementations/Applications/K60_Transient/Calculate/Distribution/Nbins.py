from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Nbins:
	"""Nbins commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nbins", core, parent)

	def set(self, bins: int, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:DISTribution:NBINs \n
		Snippet: driver.applications.k60Transient.calculate.distribution.nbins.set(bins = 1, window = repcap.Window.Default) \n
		Defines the number of columns on the x-axis, i.e. the number of measurement value ranges for which the occurrences are
		determined. \n
			:param bins: Number of columns Range: 1 to 1000
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.decimal_value_to_str(bins)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write_with_opc(f'CALCulate{window_cmd_val}:DISTribution:NBINs {param}')

	def get(self, window=repcap.Window.Default) -> int:
		"""SCPI: CALCulate<n>:DISTribution:NBINs \n
		Snippet: value: int = driver.applications.k60Transient.calculate.distribution.nbins.get(window = repcap.Window.Default) \n
		Defines the number of columns on the x-axis, i.e. the number of measurement value ranges for which the occurrences are
		determined. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: bins: Number of columns Range: 1 to 1000"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str_with_opc(f'CALCulate{window_cmd_val}:DISTribution:NBINs?')
		return Conversions.str_to_int(response)
