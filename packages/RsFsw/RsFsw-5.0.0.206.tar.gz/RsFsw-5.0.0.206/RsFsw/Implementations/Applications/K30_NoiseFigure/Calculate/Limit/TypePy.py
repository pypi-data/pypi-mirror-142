from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TypePy:
	"""TypePy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("typePy", core, parent)

	def set(self, result: enums.NoiseFigureLimit, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default) -> None:
		"""SCPI: CALCulate<n>:LIMit<li>:TYPE \n
		Snippet: driver.applications.k30NoiseFigure.calculate.limit.typePy.set(result = enums.NoiseFigureLimit.ENR, window = repcap.Window.Default, limitIx = repcap.LimitIx.Default) \n
		This command configures a limit line for a particular result type. \n
			:param result: NOISe | GAIN | TEMPerature | YFACtor | ENR | PHOT | PCOLd GAIN Assigns the limit line to gain reuslts. NOISe Assigns the limit line to noise figure results. PCOLd Assigns the limit line to power (cold) results. PHOT Assigns the limit line to power (hot) results. TEMPerature Assigns the limit line to noise temperature results. YFACtor Assigns the limit line to y-factor results.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
		"""
		param = Conversions.enum_scalar_to_str(result, enums.NoiseFigureLimit)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		self._core.io.write(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:TYPE {param}')

	# noinspection PyTypeChecker
	def get(self, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default) -> enums.NoiseFigureLimit:
		"""SCPI: CALCulate<n>:LIMit<li>:TYPE \n
		Snippet: value: enums.NoiseFigureLimit = driver.applications.k30NoiseFigure.calculate.limit.typePy.get(window = repcap.Window.Default, limitIx = repcap.LimitIx.Default) \n
		This command configures a limit line for a particular result type. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
			:return: result: NOISe | GAIN | TEMPerature | YFACtor | ENR | PHOT | PCOLd GAIN Assigns the limit line to gain reuslts. NOISe Assigns the limit line to noise figure results. PCOLd Assigns the limit line to power (cold) results. PHOT Assigns the limit line to power (hot) results. TEMPerature Assigns the limit line to noise temperature results. YFACtor Assigns the limit line to y-factor results."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.NoiseFigureLimit)
