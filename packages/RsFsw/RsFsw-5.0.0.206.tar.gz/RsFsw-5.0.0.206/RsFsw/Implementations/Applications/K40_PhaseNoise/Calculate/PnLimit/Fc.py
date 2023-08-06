from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Fc:
	"""Fc commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: CornerFrequency, default value after init: CornerFrequency.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fc", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_cornerFrequency_get', 'repcap_cornerFrequency_set', repcap.CornerFrequency.Nr1)

	def repcap_cornerFrequency_set(self, cornerFrequency: repcap.CornerFrequency) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to CornerFrequency.Default
		Default value after init: CornerFrequency.Nr1"""
		self._cmd_group.set_repcap_enum_value(cornerFrequency)

	def repcap_cornerFrequency_get(self) -> repcap.CornerFrequency:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def set(self, corner_frequency_value: float, window=repcap.Window.Default, cornerFrequency=repcap.CornerFrequency.Default) -> None:
		"""SCPI: CALCulate<n>:PNLimit:FC<res> \n
		Snippet: driver.applications.k40PhaseNoise.calculate.pnLimit.fc.set(corner_frequency_value = 1.0, window = repcap.Window.Default, cornerFrequency = repcap.CornerFrequency.Default) \n
		This command sets the corner frequency of a phase noise limit line. \n
			:param corner_frequency_value: No help available
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param cornerFrequency: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fc')
		"""
		param = Conversions.decimal_value_to_str(corner_frequency_value)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		cornerFrequency_cmd_val = self._cmd_group.get_repcap_cmd_value(cornerFrequency, repcap.CornerFrequency)
		self._core.io.write(f'CALCulate{window_cmd_val}:PNLimit:FC{cornerFrequency_cmd_val} {param}')

	def get(self, window=repcap.Window.Default, cornerFrequency=repcap.CornerFrequency.Default) -> float:
		"""SCPI: CALCulate<n>:PNLimit:FC<res> \n
		Snippet: value: float = driver.applications.k40PhaseNoise.calculate.pnLimit.fc.get(window = repcap.Window.Default, cornerFrequency = repcap.CornerFrequency.Default) \n
		This command sets the corner frequency of a phase noise limit line. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param cornerFrequency: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fc')
			:return: corner_frequency_value: No help available"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		cornerFrequency_cmd_val = self._cmd_group.get_repcap_cmd_value(cornerFrequency, repcap.CornerFrequency)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:PNLimit:FC{cornerFrequency_cmd_val}?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Fc':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Fc(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
