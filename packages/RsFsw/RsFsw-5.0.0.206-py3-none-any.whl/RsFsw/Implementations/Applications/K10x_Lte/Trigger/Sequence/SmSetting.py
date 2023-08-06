from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SmSetting:
	"""SmSetting commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: Instrument, default value after init: Instrument.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("smSetting", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_instrument_get', 'repcap_instrument_set', repcap.Instrument.Nr1)

	def repcap_instrument_set(self, instrument: repcap.Instrument) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Instrument.Default
		Default value after init: Instrument.Nr1"""
		self._cmd_group.set_repcap_enum_value(instrument)

	def repcap_instrument_get(self) -> repcap.Instrument:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def set(self, state: bool, instrument=repcap.Instrument.Default) -> None:
		"""SCPI: TRIGger[:SEQuence]:SMSetting<ant> \n
		Snippet: driver.applications.k10Xlte.trigger.sequence.smSetting.set(state = False, instrument = repcap.Instrument.Default) \n
		This command selects the trigger configuration for secondary analyzers in a MIMO setup. \n
			:param state: ON | 1 Uses the same trigger configuration as the primary analyzer. OFF | 0 Uses a custom trigger configuration for the selected analyzer.
			:param instrument: optional repeated capability selector. Default value: Nr1 (settable in the interface 'SmSetting')
		"""
		param = Conversions.bool_to_str(state)
		instrument_cmd_val = self._cmd_group.get_repcap_cmd_value(instrument, repcap.Instrument)
		self._core.io.write(f'TRIGger:SEQuence:SMSetting{instrument_cmd_val} {param}')

	def get(self, instrument=repcap.Instrument.Default) -> bool:
		"""SCPI: TRIGger[:SEQuence]:SMSetting<ant> \n
		Snippet: value: bool = driver.applications.k10Xlte.trigger.sequence.smSetting.get(instrument = repcap.Instrument.Default) \n
		This command selects the trigger configuration for secondary analyzers in a MIMO setup. \n
			:param instrument: optional repeated capability selector. Default value: Nr1 (settable in the interface 'SmSetting')
			:return: state: ON | 1 Uses the same trigger configuration as the primary analyzer. OFF | 0 Uses a custom trigger configuration for the selected analyzer."""
		instrument_cmd_val = self._cmd_group.get_repcap_cmd_value(instrument, repcap.Instrument)
		response = self._core.io.query_str(f'TRIGger:SEQuence:SMSetting{instrument_cmd_val}?')
		return Conversions.str_to_bool(response)

	def clone(self) -> 'SmSetting':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SmSetting(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
