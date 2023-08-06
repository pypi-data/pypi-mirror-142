from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Level:
	"""Level commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: Instrument, default value after init: Instrument.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("level", core, parent)
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

	def set(self, instrument=repcap.Instrument.Default) -> None:
		"""SCPI: [SENSe]:ADJust:LEVel<ant> \n
		Snippet: driver.applications.k10Xlte.sense.adjust.level.set(instrument = repcap.Instrument.Default) \n
		This command initiates a single (internal) measurement that evaluates and sets the ideal reference level for the current
		input data and measurement settings. This ensures that the settings of the RF attenuation and the reference level are
		optimally adjusted to the signal level without overloading the R&S FSW or limiting the dynamic range by an S/N ratio that
		is too small. \n
			:param instrument: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Level')
		"""
		instrument_cmd_val = self._cmd_group.get_repcap_cmd_value(instrument, repcap.Instrument)
		self._core.io.write(f'SENSe:ADJust:LEVel{instrument_cmd_val}')

	def set_with_opc(self, instrument=repcap.Instrument.Default, opc_timeout_ms: int = -1) -> None:
		instrument_cmd_val = self._cmd_group.get_repcap_cmd_value(instrument, repcap.Instrument)
		"""SCPI: [SENSe]:ADJust:LEVel<ant> \n
		Snippet: driver.applications.k10Xlte.sense.adjust.level.set_with_opc(instrument = repcap.Instrument.Default) \n
		This command initiates a single (internal) measurement that evaluates and sets the ideal reference level for the current
		input data and measurement settings. This ensures that the settings of the RF attenuation and the reference level are
		optimally adjusted to the signal level without overloading the R&S FSW or limiting the dynamic range by an S/N ratio that
		is too small. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param instrument: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Level')
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SENSe:ADJust:LEVel{instrument_cmd_val}', opc_timeout_ms)

	def clone(self) -> 'Level':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Level(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
