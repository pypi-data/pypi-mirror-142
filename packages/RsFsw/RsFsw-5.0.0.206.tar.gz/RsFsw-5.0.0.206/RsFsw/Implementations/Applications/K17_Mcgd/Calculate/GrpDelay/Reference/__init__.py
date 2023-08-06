from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Reference:
	"""Reference commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("reference", core, parent)

	@property
	def frequency(self):
		"""frequency commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import Frequency
			self._frequency = Frequency(self._core, self._cmd_group)
		return self._frequency

	def set(self, ref_type: enums.GrpdRelRefType, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:GRPDelay:REFerence \n
		Snippet: driver.applications.k17Mcgd.calculate.grpDelay.reference.set(ref_type = enums.GrpdRelRefType.AVERage, window = repcap.Window.Default) \n
		Determines the reference used for relative group delay measurement. \n
			:param ref_type: AVERage (Default:) The average group delay is used as a reference CENTer The group delay measured for the center frequency is used as a reference MANual The group delay measured at the user-defined reference frequency is used as a reference (see method RsFsw.Applications.K17_Mcgd.Calculate.GrpDelay.Reference.Frequency.set)
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.enum_scalar_to_str(ref_type, enums.GrpdRelRefType)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:GRPDelay:REFerence {param}')

	# noinspection PyTypeChecker
	def get(self, window=repcap.Window.Default) -> enums.GrpdRelRefType:
		"""SCPI: CALCulate<n>:GRPDelay:REFerence \n
		Snippet: value: enums.GrpdRelRefType = driver.applications.k17Mcgd.calculate.grpDelay.reference.get(window = repcap.Window.Default) \n
		Determines the reference used for relative group delay measurement. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: ref_type: AVERage (Default:) The average group delay is used as a reference CENTer The group delay measured for the center frequency is used as a reference MANual The group delay measured at the user-defined reference frequency is used as a reference (see method RsFsw.Applications.K17_Mcgd.Calculate.GrpDelay.Reference.Frequency.set)"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:GRPDelay:REFerence?')
		return Conversions.str_to_scalar_enum(response, enums.GrpdRelRefType)

	def clone(self) -> 'Reference':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Reference(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
