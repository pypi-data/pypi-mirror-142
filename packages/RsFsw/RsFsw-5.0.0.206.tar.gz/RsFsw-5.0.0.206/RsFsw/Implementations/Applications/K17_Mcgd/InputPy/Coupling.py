from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Coupling:
	"""Coupling commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("coupling", core, parent)

	def set(self, coupling_type: enums.CouplingTypeA, inputIx=repcap.InputIx.Default) -> None:
		"""SCPI: INPut<Undef>:COUPling \n
		Snippet: driver.applications.k17Mcgd.inputPy.coupling.set(coupling_type = enums.CouplingTypeA.AC, inputIx = repcap.InputIx.Default) \n
		This command selects the coupling type of the RF input. \n
			:param coupling_type: AC | DC AC AC coupling DC DC coupling
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
		"""
		param = Conversions.enum_scalar_to_str(coupling_type, enums.CouplingTypeA)
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		self._core.io.write(f'INPut{inputIx_cmd_val}:COUPling {param}')

	# noinspection PyTypeChecker
	def get(self, inputIx=repcap.InputIx.Default) -> enums.CouplingTypeA:
		"""SCPI: INPut<Undef>:COUPling \n
		Snippet: value: enums.CouplingTypeA = driver.applications.k17Mcgd.inputPy.coupling.get(inputIx = repcap.InputIx.Default) \n
		This command selects the coupling type of the RF input. \n
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
			:return: coupling_type: AC | DC AC AC coupling DC DC coupling"""
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		response = self._core.io.query_str(f'INPut{inputIx_cmd_val}:COUPling?')
		return Conversions.str_to_scalar_enum(response, enums.CouplingTypeA)
