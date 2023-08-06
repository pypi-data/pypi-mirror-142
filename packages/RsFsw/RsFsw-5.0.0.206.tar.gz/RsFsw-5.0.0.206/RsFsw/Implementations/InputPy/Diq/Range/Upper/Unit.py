from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Unit:
	"""Unit commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("unit", core, parent)

	def set(self, level: enums.DiqUnit, inputIx=repcap.InputIx.Default) -> None:
		"""SCPI: INPut<ip>:DIQ:RANGe[:UPPer]:UNIT \n
		Snippet: driver.inputPy.diq.range.upper.unit.set(level = enums.DiqUnit.AMPere, inputIx = repcap.InputIx.Default) \n
		Defines the unit of the full scale level. The availability of units depends on the measurement application you are using.
		This command is only available if the optional Digital Baseband Interface is installed. \n
			:param level: DBM | DBPW | WATT | DBUV | DBMV | VOLT | DBUA | AMPere
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
		"""
		param = Conversions.enum_scalar_to_str(level, enums.DiqUnit)
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		self._core.io.write(f'INPut{inputIx_cmd_val}:DIQ:RANGe:UPPer:UNIT {param}')

	# noinspection PyTypeChecker
	def get(self, inputIx=repcap.InputIx.Default) -> enums.DiqUnit:
		"""SCPI: INPut<ip>:DIQ:RANGe[:UPPer]:UNIT \n
		Snippet: value: enums.DiqUnit = driver.inputPy.diq.range.upper.unit.get(inputIx = repcap.InputIx.Default) \n
		Defines the unit of the full scale level. The availability of units depends on the measurement application you are using.
		This command is only available if the optional Digital Baseband Interface is installed. \n
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
			:return: level: DBM | DBPW | WATT | DBUV | DBMV | VOLT | DBUA | AMPere"""
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		response = self._core.io.query_str(f'INPut{inputIx_cmd_val}:DIQ:RANGe:UPPer:UNIT?')
		return Conversions.str_to_scalar_enum(response, enums.DiqUnit)
