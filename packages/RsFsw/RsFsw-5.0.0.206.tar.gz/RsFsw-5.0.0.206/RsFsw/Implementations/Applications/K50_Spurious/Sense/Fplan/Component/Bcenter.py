from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Bcenter:
	"""Bcenter commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bcenter", core, parent)

	def set(self, center_freq: float, component=repcap.Component.Default) -> None:
		"""SCPI: [SENSe]:FPLan:COMPonent<co>:BCENter \n
		Snippet: driver.applications.k50Spurious.sense.fplan.component.bcenter.set(center_freq = 1.0, component = repcap.Component.Default) \n
		Defines the center of the search span that is evaluated for spur identification within the frequency plan. By default,
		the defined center frequency is used. \n
			:param center_freq: Unit: HZ
			:param component: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Component')
		"""
		param = Conversions.decimal_value_to_str(center_freq)
		component_cmd_val = self._cmd_group.get_repcap_cmd_value(component, repcap.Component)
		self._core.io.write(f'SENSe:FPLan:COMPonent{component_cmd_val}:BCENter {param}')

	def get(self, component=repcap.Component.Default) -> float:
		"""SCPI: [SENSe]:FPLan:COMPonent<co>:BCENter \n
		Snippet: value: float = driver.applications.k50Spurious.sense.fplan.component.bcenter.get(component = repcap.Component.Default) \n
		Defines the center of the search span that is evaluated for spur identification within the frequency plan. By default,
		the defined center frequency is used. \n
			:param component: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Component')
			:return: center_freq: Unit: HZ"""
		component_cmd_val = self._cmd_group.get_repcap_cmd_value(component, repcap.Component)
		response = self._core.io.query_str(f'SENSe:FPLan:COMPonent{component_cmd_val}:BCENter?')
		return Conversions.str_to_float(response)
