from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Vswr:
	"""Vswr commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("vswr", core, parent)

	def set(self, vswr: float, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:UNCertainty:MATCh:DUT:IN[:VSWR] \n
		Snippet: driver.applications.k30NoiseFigure.calculate.uncertainty.match.dut.inputPy.vswr.set(vswr = 1.0, window = repcap.Window.Default) \n
		This command defines the VSWR at the DUT input. \n
			:param vswr: 1..n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.decimal_value_to_str(vswr)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:UNCertainty:MATCh:DUT:IN:VSWR {param}')

	def get(self, window=repcap.Window.Default) -> float:
		"""SCPI: CALCulate<n>:UNCertainty:MATCh:DUT:IN[:VSWR] \n
		Snippet: value: float = driver.applications.k30NoiseFigure.calculate.uncertainty.match.dut.inputPy.vswr.get(window = repcap.Window.Default) \n
		This command defines the VSWR at the DUT input. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: vswr: No help available"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:UNCertainty:MATCh:DUT:IN:VSWR?')
		return Conversions.str_to_float(response)
