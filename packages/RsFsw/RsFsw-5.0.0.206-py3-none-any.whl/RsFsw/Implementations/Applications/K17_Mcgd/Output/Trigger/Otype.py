from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Otype:
	"""Otype commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("otype", core, parent)

	def set(self, type_py: enums.TriggerOutType, triggerPort=repcap.TriggerPort.Default) -> None:
		"""SCPI: OUTPut:TRIGger<tp>:OTYPe \n
		Snippet: driver.applications.k17Mcgd.output.trigger.otype.set(type_py = enums.TriggerOutType.DEVice, triggerPort = repcap.TriggerPort.Default) \n
		This command selects the type of signal generated at the trigger output. \n
			:param type_py: No help available
			:param triggerPort: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Trigger')
		"""
		param = Conversions.enum_scalar_to_str(type_py, enums.TriggerOutType)
		triggerPort_cmd_val = self._cmd_group.get_repcap_cmd_value(triggerPort, repcap.TriggerPort)
		self._core.io.write(f'OUTPut:TRIGger{triggerPort_cmd_val}:OTYPe {param}')

	# noinspection PyTypeChecker
	def get(self, triggerPort=repcap.TriggerPort.Default) -> enums.TriggerOutType:
		"""SCPI: OUTPut:TRIGger<tp>:OTYPe \n
		Snippet: value: enums.TriggerOutType = driver.applications.k17Mcgd.output.trigger.otype.get(triggerPort = repcap.TriggerPort.Default) \n
		This command selects the type of signal generated at the trigger output. \n
			:param triggerPort: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Trigger')
			:return: type_py: No help available"""
		triggerPort_cmd_val = self._cmd_group.get_repcap_cmd_value(triggerPort, repcap.TriggerPort)
		response = self._core.io.query_str(f'OUTPut:TRIGger{triggerPort_cmd_val}:OTYPe?')
		return Conversions.str_to_scalar_enum(response, enums.TriggerOutType)
