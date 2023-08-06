from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Source:
	"""Source commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("source", core, parent)

	@property
	def stat(self):
		"""stat commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_stat'):
			from .Stat import Stat
			self._stat = Stat(self._core, self._cmd_group)
		return self._stat

	def set(self, coupling: enums.CouplingRosc) -> None:
		"""SCPI: CONFigure:WLAN:ANTMatrix:SOURce:ROSCillator:SOURce \n
		Snippet: driver.applications.k91Wlan.configure.wlan.antMatrix.source.roscillator.source.set(coupling = enums.CouplingRosc.AUTO) \n
		This remote control command determines whether the reference frequency for the primary and secondary devices in a
		simultaneous MIMO setup are coupled or not. \n
			:param coupling: AUTO | EXTernal | OFF Coupling mode AUTO Secondaries set to the same external reference source as primary. Use an R&S Z11 trigger box to send to the same trigger to all devices (see TRIG:SEQ:SOUR TUN. EXTernal Secondaries' reference source is set to external. Configure a trigger output from the primary (see method RsFsw.Applications.K10x_Lte.Output.Trigger.Otype.set) . OFF Secondaries' reference source is set to internal.
		"""
		param = Conversions.enum_scalar_to_str(coupling, enums.CouplingRosc)
		self._core.io.write(f'CONFigure:WLAN:ANTMatrix:SOURce:ROSCillator:SOURce {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.CouplingRosc:
		"""SCPI: CONFigure:WLAN:ANTMatrix:SOURce:ROSCillator:SOURce \n
		Snippet: value: enums.CouplingRosc = driver.applications.k91Wlan.configure.wlan.antMatrix.source.roscillator.source.get() \n
		This remote control command determines whether the reference frequency for the primary and secondary devices in a
		simultaneous MIMO setup are coupled or not. \n
			:return: coupling: AUTO | EXTernal | OFF Coupling mode AUTO Secondaries set to the same external reference source as primary. Use an R&S Z11 trigger box to send to the same trigger to all devices (see TRIG:SEQ:SOUR TUN. EXTernal Secondaries' reference source is set to external. Configure a trigger output from the primary (see method RsFsw.Applications.K10x_Lte.Output.Trigger.Otype.set) . OFF Secondaries' reference source is set to internal."""
		response = self._core.io.query_str(f'CONFigure:WLAN:ANTMatrix:SOURce:ROSCillator:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.CouplingRosc)

	def clone(self) -> 'Source':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Source(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
