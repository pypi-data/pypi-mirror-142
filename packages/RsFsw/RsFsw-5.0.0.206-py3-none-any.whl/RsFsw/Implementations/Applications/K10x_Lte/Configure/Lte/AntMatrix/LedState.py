from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LedState:
	"""LedState commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: Instrument, default value after init: Instrument.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ledState", core, parent)
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

	# noinspection PyTypeChecker
	def get(self, instrument=repcap.Instrument.Default) -> enums.LedState:
		"""SCPI: CONFigure[:LTE]:ANTMatrix:LEDState<in> \n
		Snippet: value: enums.LedState = driver.applications.k10Xlte.configure.lte.antMatrix.ledState.get(instrument = repcap.Instrument.Default) \n
		This command queries the state of one of the instruments in a MIMO setup. \n
			:param instrument: optional repeated capability selector. Default value: Nr1 (settable in the interface 'LedState')
			:return: color: GREEN Connection to the instrument has been successfully established. GREY Instrument connection has been turned off with method RsFsw.Applications.K10x_Lte.Configure.Lte.AntMatrix.State.set. RED Connection to the instrument could not be established."""
		instrument_cmd_val = self._cmd_group.get_repcap_cmd_value(instrument, repcap.Instrument)
		response = self._core.io.query_str(f'CONFigure:LTE:ANTMatrix:LEDState{instrument_cmd_val}?')
		return Conversions.str_to_scalar_enum(response, enums.LedState)

	def clone(self) -> 'LedState':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = LedState(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
