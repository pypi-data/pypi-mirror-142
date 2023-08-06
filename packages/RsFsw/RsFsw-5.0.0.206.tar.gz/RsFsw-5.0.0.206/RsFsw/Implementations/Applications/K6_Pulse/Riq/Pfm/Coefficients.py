from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Coefficients:
	"""Coefficients commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: Coefficients, default value after init: Coefficients.Order1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("coefficients", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_coefficients_get', 'repcap_coefficients_set', repcap.Coefficients.Order1)

	def repcap_coefficients_set(self, coefficients: repcap.Coefficients) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Coefficients.Default
		Default value after init: Coefficients.Order1"""
		self._cmd_group.set_repcap_enum_value(coefficients)

	def repcap_coefficients_get(self) -> repcap.Coefficients:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def set(self, coefficient: float, coefficients=repcap.Coefficients.Default) -> None:
		"""SCPI: RIQ:PFM:COEFficients<n> \n
		Snippet: driver.applications.k6Pulse.riq.pfm.coefficients.set(coefficient = 1.0, coefficients = repcap.Coefficients.Default) \n
		Sets/queries coefficients for polynomial FM type reference I/Q data. \n
			:param coefficient: No help available
			:param coefficients: optional repeated capability selector. Default value: Order1 (settable in the interface 'Coefficients')
		"""
		param = Conversions.decimal_value_to_str(coefficient)
		coefficients_cmd_val = self._cmd_group.get_repcap_cmd_value(coefficients, repcap.Coefficients)
		self._core.io.write(f'RIQ:PFM:COEFficients{coefficients_cmd_val} {param}')

	def get(self, coefficients=repcap.Coefficients.Default) -> float:
		"""SCPI: RIQ:PFM:COEFficients<n> \n
		Snippet: value: float = driver.applications.k6Pulse.riq.pfm.coefficients.get(coefficients = repcap.Coefficients.Default) \n
		Sets/queries coefficients for polynomial FM type reference I/Q data. \n
			:param coefficients: optional repeated capability selector. Default value: Order1 (settable in the interface 'Coefficients')
			:return: coefficient: No help available"""
		coefficients_cmd_val = self._cmd_group.get_repcap_cmd_value(coefficients, repcap.Coefficients)
		response = self._core.io.query_str(f'RIQ:PFM:COEFficients{coefficients_cmd_val}?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Coefficients':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Coefficients(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
