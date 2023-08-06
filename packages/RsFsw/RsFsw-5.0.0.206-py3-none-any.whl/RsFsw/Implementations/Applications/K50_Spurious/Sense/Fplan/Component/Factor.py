from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Factor:
	"""Factor commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("factor", core, parent)

	def set(self, factor: int, component=repcap.Component.Default) -> None:
		"""SCPI: [SENSe]:FPLan:COMPonent<co>:FACTor \n
		Snippet: driver.applications.k50Spurious.sense.fplan.component.factor.set(factor = 1, component = repcap.Component.Default) \n
		No command help available \n
			:param factor: No help available
			:param component: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Component')
		"""
		param = Conversions.decimal_value_to_str(factor)
		component_cmd_val = self._cmd_group.get_repcap_cmd_value(component, repcap.Component)
		self._core.io.write(f'SENSe:FPLan:COMPonent{component_cmd_val}:FACTor {param}')

	def get(self, component=repcap.Component.Default) -> int:
		"""SCPI: [SENSe]:FPLan:COMPonent<co>:FACTor \n
		Snippet: value: int = driver.applications.k50Spurious.sense.fplan.component.factor.get(component = repcap.Component.Default) \n
		No command help available \n
			:param component: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Component')
			:return: factor: No help available"""
		component_cmd_val = self._cmd_group.get_repcap_cmd_value(component, repcap.Component)
		response = self._core.io.query_str(f'SENSe:FPLan:COMPonent{component_cmd_val}:FACTor?')
		return Conversions.str_to_int(response)
