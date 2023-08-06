from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rbw:
	"""Rbw commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rbw", core, parent)

	def get(self, window=repcap.Window.Default) -> float:
		"""SCPI: CALCulate<n>:PSPectrum:RBW \n
		Snippet: value: float = driver.applications.k6Pulse.calculate.pspectrum.rbw.get(window = repcap.Window.Default) \n
		Queries the resulting resolution bandwidth for the spectrum. Depends on the block size (see method RsFsw.Applications.
		K6_Pulse.Calculate.Pspectrum.BlockSize.set) . \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: rbw: Unit: Hz"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:PSPectrum:RBW?')
		return Conversions.str_to_float(response)
