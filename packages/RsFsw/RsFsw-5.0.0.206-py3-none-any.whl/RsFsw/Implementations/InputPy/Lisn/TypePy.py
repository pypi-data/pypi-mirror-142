from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TypePy:
	"""TypePy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("typePy", core, parent)

	def set(self, type_py: enums.LisnType, inputIx=repcap.InputIx.Default) -> None:
		"""SCPI: INPut<ip>:LISN[:TYPE] \n
		Snippet: driver.inputPy.lisn.typePy.set(type_py = enums.LisnType.ENV216, inputIx = repcap.InputIx.Default) \n
		This command turns automatic control of a LISN on and off. It also selects the type of network. \n
			:param type_py: ENV216 R&S ENV 216: two phases and highpass are controllable. ENV432 R&S ENV 432: four phases are controllable. ENV4200 R&S ENV 4200: four phases are controllable. ESH2Z5 R&S ESH2-Z5: four phases (incl. protective earth) are controllable. ESH3Z5 R&S ESH3-Z5: two phases (incl. protective earth) are controllable. FOURphase R&S ESH2-Z5: four phases (incl. protective earth) are controllable. OFF Turns off remote control of the LISN. TWOPhase R&S ESH3-Z5: two phases (incl. protective earth) are controllable.
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
		"""
		param = Conversions.enum_scalar_to_str(type_py, enums.LisnType)
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		self._core.io.write(f'INPut{inputIx_cmd_val}:LISN:TYPE {param}')

	# noinspection PyTypeChecker
	def get(self, inputIx=repcap.InputIx.Default) -> enums.LisnType:
		"""SCPI: INPut<ip>:LISN[:TYPE] \n
		Snippet: value: enums.LisnType = driver.inputPy.lisn.typePy.get(inputIx = repcap.InputIx.Default) \n
		This command turns automatic control of a LISN on and off. It also selects the type of network. \n
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
			:return: type_py: ENV216 R&S ENV 216: two phases and highpass are controllable. ENV432 R&S ENV 432: four phases are controllable. ENV4200 R&S ENV 4200: four phases are controllable. ESH2Z5 R&S ESH2-Z5: four phases (incl. protective earth) are controllable. ESH3Z5 R&S ESH3-Z5: two phases (incl. protective earth) are controllable. FOURphase R&S ESH2-Z5: four phases (incl. protective earth) are controllable. OFF Turns off remote control of the LISN. TWOPhase R&S ESH3-Z5: two phases (incl. protective earth) are controllable."""
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		response = self._core.io.query_str(f'INPut{inputIx_cmd_val}:LISN:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.LisnType)
