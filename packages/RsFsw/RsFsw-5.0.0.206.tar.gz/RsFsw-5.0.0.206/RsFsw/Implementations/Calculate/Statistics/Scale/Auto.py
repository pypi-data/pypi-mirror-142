from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Auto:
	"""Auto commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("auto", core, parent)

	def set(self, event: enums.EventOnce, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:STATistics:SCALe:AUTO \n
		Snippet: driver.calculate.statistics.scale.auto.set(event = enums.EventOnce.ONCE, window = repcap.Window.Default) \n
		This command initiates an automatic scaling of the diagram (x- and y-axis) . To obtain maximum resolution, the level
		range is set as a function of the measured spacing between peak power and the minimum power for the APD measurement and
		of the spacing between peak power and mean power for the CCDF measurement. In addition, the probability scale for the
		number of test points is adapted. To get valid results, you have to perform a complete sweep with synchronization to the
		end of the auto range process. This is only possible in single sweep mode. \n
			:param event: No help available
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.enum_scalar_to_str(event, enums.EventOnce)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:STATistics:SCALe:AUTO {param}')
