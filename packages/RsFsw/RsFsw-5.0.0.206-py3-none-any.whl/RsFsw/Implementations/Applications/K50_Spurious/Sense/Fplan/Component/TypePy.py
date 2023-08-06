from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TypePy:
	"""TypePy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("typePy", core, parent)

	def set(self, type_py: enums.ComponentType, component=repcap.Component.Default) -> None:
		"""SCPI: [SENSe]:FPLan:COMPonent<co>:TYPE \n
		Snippet: driver.applications.k50Spurious.sense.fplan.component.typePy.set(type_py = enums.ComponentType.AMPLifier, component = repcap.Component.Default) \n
		Defines the type of component in the signal path. Depending on the type of component, different parameters are available.
		For details see 'Frequency plan and spur identification'. \n
			:param type_py: MIXer | AMPLifier | MULTiplier | DIVider MIXer Mixes the input signal (RF input or the output of the previous component) with a second input frequency. AMPLifier Amplifies the input signal (RF input or the output of the previous component) . MULTiplier Multiplies the input signal (RF input or the output of the previous component) by a configurable factor n. DIVider Divides the input signal (RF input or the output of the previous component) by a configurable factor n.
			:param component: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Component')
		"""
		param = Conversions.enum_scalar_to_str(type_py, enums.ComponentType)
		component_cmd_val = self._cmd_group.get_repcap_cmd_value(component, repcap.Component)
		self._core.io.write(f'SENSe:FPLan:COMPonent{component_cmd_val}:TYPE {param}')

	# noinspection PyTypeChecker
	def get(self, component=repcap.Component.Default) -> enums.ComponentType:
		"""SCPI: [SENSe]:FPLan:COMPonent<co>:TYPE \n
		Snippet: value: enums.ComponentType = driver.applications.k50Spurious.sense.fplan.component.typePy.get(component = repcap.Component.Default) \n
		Defines the type of component in the signal path. Depending on the type of component, different parameters are available.
		For details see 'Frequency plan and spur identification'. \n
			:param component: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Component')
			:return: type_py: MIXer | AMPLifier | MULTiplier | DIVider MIXer Mixes the input signal (RF input or the output of the previous component) with a second input frequency. AMPLifier Amplifies the input signal (RF input or the output of the previous component) . MULTiplier Multiplies the input signal (RF input or the output of the previous component) by a configurable factor n. DIVider Divides the input signal (RF input or the output of the previous component) by a configurable factor n."""
		component_cmd_val = self._cmd_group.get_repcap_cmd_value(component, repcap.Component)
		response = self._core.io.query_str(f'SENSe:FPLan:COMPonent{component_cmd_val}:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.ComponentType)
