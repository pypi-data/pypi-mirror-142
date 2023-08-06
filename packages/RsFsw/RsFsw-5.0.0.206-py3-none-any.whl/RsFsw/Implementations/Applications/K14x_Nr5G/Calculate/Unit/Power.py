from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Power:
	"""Power commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("power", core, parent)

	def set(self, arg_0: enums.PowerUnitNr5G, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:UNIT:POWer \n
		Snippet: driver.applications.k14Xnr5G.calculate.unit.power.set(arg_0 = enums.PowerUnitNr5G.A, window = repcap.Window.Default) \n
		No command help available \n
			:param arg_0: No help available
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.enum_scalar_to_str(arg_0, enums.PowerUnitNr5G)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:UNIT:POWer {param}')

	# noinspection PyTypeChecker
	def get(self, window=repcap.Window.Default) -> enums.PowerUnitNr5G:
		"""SCPI: CALCulate<n>:UNIT:POWer \n
		Snippet: value: enums.PowerUnitNr5G = driver.applications.k14Xnr5G.calculate.unit.power.get(window = repcap.Window.Default) \n
		No command help available \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: arg_0: No help available"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:UNIT:POWer?')
		return Conversions.str_to_scalar_enum(response, enums.PowerUnitNr5G)
