from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Utilities import trim_str_response
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Address:
	"""Address commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: Instrument, default value after init: Instrument.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("address", core, parent)
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

	def set(self, address: str, instrument=repcap.Instrument.Default) -> None:
		"""SCPI: CONFigure[:LTE]:ANTMatrix:ADDRess<in> \n
		Snippet: driver.applications.k10Xlte.configure.lte.antMatrix.address.set(address = '1', instrument = repcap.Instrument.Default) \n
		This command defines the network address of an analyzer in the test setup. \n
			:param address: String containing the address of the analyzer. Connections are possible via TCP/IP.
			:param instrument: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Address')
		"""
		param = Conversions.value_to_quoted_str(address)
		instrument_cmd_val = self._cmd_group.get_repcap_cmd_value(instrument, repcap.Instrument)
		self._core.io.write(f'CONFigure:LTE:ANTMatrix:ADDRess{instrument_cmd_val} {param}')

	def get(self, instrument=repcap.Instrument.Default) -> str:
		"""SCPI: CONFigure[:LTE]:ANTMatrix:ADDRess<in> \n
		Snippet: value: str = driver.applications.k10Xlte.configure.lte.antMatrix.address.get(instrument = repcap.Instrument.Default) \n
		This command defines the network address of an analyzer in the test setup. \n
			:param instrument: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Address')
			:return: address: String containing the address of the analyzer. Connections are possible via TCP/IP."""
		instrument_cmd_val = self._cmd_group.get_repcap_cmd_value(instrument, repcap.Instrument)
		response = self._core.io.query_str(f'CONFigure:LTE:ANTMatrix:ADDRess{instrument_cmd_val}?')
		return trim_str_response(response)

	def clone(self) -> 'Address':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Address(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
