from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Level:
	"""Level commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("level", core, parent)

	def set(self, level: float, externalGen=repcap.ExternalGen.Nr1) -> None:
		"""SCPI: SOURce:EXTernal<gen>:POWer[:LEVel] \n
		Snippet: driver.source.external.power.level.set(level = 1.0, externalGen = repcap.ExternalGen.Nr1) \n
		This command sets the output power of the selected generator. This command is only valid if External Generator Control
		(R&S FSW-B10) is installed and active. \n
			:param level: numeric value Unit: DBM
			:param externalGen: optional repeated capability selector. Default value: Nr1
		"""
		param = Conversions.decimal_value_to_str(level)
		externalGen_cmd_val = self._cmd_group.get_repcap_cmd_value(externalGen, repcap.ExternalGen)
		self._core.io.write(f'SOURce:EXTernal{externalGen_cmd_val}:POWer:LEVel {param}')

	def get(self, externalGen=repcap.ExternalGen.Nr1) -> float:
		"""SCPI: SOURce:EXTernal<gen>:POWer[:LEVel] \n
		Snippet: value: float = driver.source.external.power.level.get(externalGen = repcap.ExternalGen.Nr1) \n
		This command sets the output power of the selected generator. This command is only valid if External Generator Control
		(R&S FSW-B10) is installed and active. \n
			:param externalGen: optional repeated capability selector. Default value: Nr1
			:return: level: numeric value Unit: DBM"""
		externalGen_cmd_val = self._cmd_group.get_repcap_cmd_value(externalGen, repcap.ExternalGen)
		response = self._core.io.query_str(f'SOURce:EXTernal{externalGen_cmd_val}:POWer:LEVel?')
		return Conversions.str_to_float(response)
