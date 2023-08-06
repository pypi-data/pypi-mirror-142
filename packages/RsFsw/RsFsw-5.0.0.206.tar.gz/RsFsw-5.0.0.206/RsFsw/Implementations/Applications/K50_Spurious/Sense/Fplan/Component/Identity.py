from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Identity:
	"""Identity commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("identity", core, parent)

	def set(self, type_py: enums.MixerIdentifier, component=repcap.Component.Default) -> None:
		"""SCPI: [SENSe]:FPLan:COMPonent<co>:IDENtity \n
		Snippet: driver.applications.k50Spurious.sense.fplan.component.identity.set(type_py = enums.MixerIdentifier.CLOCk, component = repcap.Component.Default) \n
		Selects the identifier for the second input frequency for mixers. \n
			:param type_py: LO | CLOCk
			:param component: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Component')
		"""
		param = Conversions.enum_scalar_to_str(type_py, enums.MixerIdentifier)
		component_cmd_val = self._cmd_group.get_repcap_cmd_value(component, repcap.Component)
		self._core.io.write(f'SENSe:FPLan:COMPonent{component_cmd_val}:IDENtity {param}')

	# noinspection PyTypeChecker
	def get(self, component=repcap.Component.Default) -> enums.MixerIdentifier:
		"""SCPI: [SENSe]:FPLan:COMPonent<co>:IDENtity \n
		Snippet: value: enums.MixerIdentifier = driver.applications.k50Spurious.sense.fplan.component.identity.get(component = repcap.Component.Default) \n
		Selects the identifier for the second input frequency for mixers. \n
			:param component: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Component')
			:return: type_py: LO | CLOCk"""
		component_cmd_val = self._cmd_group.get_repcap_cmd_value(component, repcap.Component)
		response = self._core.io.query_str(f'SENSe:FPLan:COMPonent{component_cmd_val}:IDENtity?')
		return Conversions.str_to_scalar_enum(response, enums.MixerIdentifier)
