from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Frequency:
	"""Frequency commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frequency", core, parent)

	def set(self, unit: enums.UnitReference, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:UNIT:FREQuency \n
		Snippet: driver.applications.k9X11Ad.calculate.unit.frequency.set(unit = enums.UnitReference.ABS, window = repcap.Window.Default) \n
		This command selects the global unit for all frequency results. \n
			:param unit: REL | ABS
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.enum_scalar_to_str(unit, enums.UnitReference)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:UNIT:FREQuency {param}')

	# noinspection PyTypeChecker
	def get(self, window=repcap.Window.Default) -> enums.UnitReference:
		"""SCPI: CALCulate<n>:UNIT:FREQuency \n
		Snippet: value: enums.UnitReference = driver.applications.k9X11Ad.calculate.unit.frequency.get(window = repcap.Window.Default) \n
		This command selects the global unit for all frequency results. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: unit: REL | ABS"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:UNIT:FREQuency?')
		return Conversions.str_to_scalar_enum(response, enums.UnitReference)
