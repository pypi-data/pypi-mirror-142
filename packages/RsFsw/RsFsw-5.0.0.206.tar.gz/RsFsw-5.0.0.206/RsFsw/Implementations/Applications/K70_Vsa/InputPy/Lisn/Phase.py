from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Phase:
	"""Phase commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("phase", core, parent)

	def set(self, phase: enums.LisnPhase, inputIx=repcap.InputIx.Default) -> None:
		"""SCPI: INPut<ip>:LISN:PHASe \n
		Snippet: driver.applications.k70Vsa.inputPy.lisn.phase.set(phase = enums.LisnPhase.L1, inputIx = repcap.InputIx.Default) \n
		No command help available \n
			:param phase: No help available
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
		"""
		param = Conversions.enum_scalar_to_str(phase, enums.LisnPhase)
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		self._core.io.write(f'INPut{inputIx_cmd_val}:LISN:PHASe {param}')

	# noinspection PyTypeChecker
	def get(self, inputIx=repcap.InputIx.Default) -> enums.LisnPhase:
		"""SCPI: INPut<ip>:LISN:PHASe \n
		Snippet: value: enums.LisnPhase = driver.applications.k70Vsa.inputPy.lisn.phase.get(inputIx = repcap.InputIx.Default) \n
		No command help available \n
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
			:return: phase: No help available"""
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		response = self._core.io.query_str(f'INPut{inputIx_cmd_val}:LISN:PHASe?')
		return Conversions.str_to_scalar_enum(response, enums.LisnPhase)
