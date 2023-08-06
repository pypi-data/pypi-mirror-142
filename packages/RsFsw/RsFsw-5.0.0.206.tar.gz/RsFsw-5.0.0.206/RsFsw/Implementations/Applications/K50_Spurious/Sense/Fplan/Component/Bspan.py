from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Bspan:
	"""Bspan commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bspan", core, parent)

	def set(self, span: float, component=repcap.Component.Default) -> None:
		"""SCPI: [SENSe]:FPLan:COMPonent<co>:BSPan \n
		Snippet: driver.applications.k50Spurious.sense.fplan.component.bspan.set(span = 1.0, component = repcap.Component.Default) \n
		Defines the span that is evaluated for spur identification within the frequency plan. By default, the full measurement
		span is used. \n
			:param span: Unit: HZ
			:param component: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Component')
		"""
		param = Conversions.decimal_value_to_str(span)
		component_cmd_val = self._cmd_group.get_repcap_cmd_value(component, repcap.Component)
		self._core.io.write(f'SENSe:FPLan:COMPonent{component_cmd_val}:BSPan {param}')

	def get(self, component=repcap.Component.Default) -> float:
		"""SCPI: [SENSe]:FPLan:COMPonent<co>:BSPan \n
		Snippet: value: float = driver.applications.k50Spurious.sense.fplan.component.bspan.get(component = repcap.Component.Default) \n
		Defines the span that is evaluated for spur identification within the frequency plan. By default, the full measurement
		span is used. \n
			:param component: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Component')
			:return: span: Unit: HZ"""
		component_cmd_val = self._cmd_group.get_repcap_cmd_value(component, repcap.Component)
		response = self._core.io.query_str(f'SENSe:FPLan:COMPonent{component_cmd_val}:BSPan?')
		return Conversions.str_to_float(response)
