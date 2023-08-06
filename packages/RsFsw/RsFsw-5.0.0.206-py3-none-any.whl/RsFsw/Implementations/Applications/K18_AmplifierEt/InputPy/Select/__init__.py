from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Select:
	"""Select commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("select", core, parent)

	@property
	def bbAnalog(self):
		"""bbAnalog commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_bbAnalog'):
			from .BbAnalog import BbAnalog
			self._bbAnalog = BbAnalog(self._core, self._cmd_group)
		return self._bbAnalog

	def set(self, signal_source: enums.InputSourceB, inputIx=repcap.InputIx.Default) -> None:
		"""SCPI: INPut<ip>:SELect \n
		Snippet: driver.applications.k18AmplifierEt.inputPy.select.set(signal_source = enums.InputSourceB.FIQ, inputIx = repcap.InputIx.Default) \n
		This command selects the signal source for measurements, i.e. it defines which connector is used to input data to the R&S
		FSW. If no additional input options are installed, only RF input or file input is supported. This command only selects
		the RF input or file input. To select the analog baseband input, you have to use method RsFsw.Applications.
		K18_AmplifierEt.InputPy.Select.BbAnalog.State.set. For R&S FSW85 models with two RF input connectors you must select the
		input connector to configure first using method RsFsw.Applications.K10x_Lte.InputPy.TypePy.set. \n
			:param signal_source: No help available
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
		"""
		param = Conversions.enum_scalar_to_str(signal_source, enums.InputSourceB)
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		self._core.io.write(f'INPut{inputIx_cmd_val}:SELect {param}')

	# noinspection PyTypeChecker
	def get(self, inputIx=repcap.InputIx.Default) -> enums.InputSourceB:
		"""SCPI: INPut<ip>:SELect \n
		Snippet: value: enums.InputSourceB = driver.applications.k18AmplifierEt.inputPy.select.get(inputIx = repcap.InputIx.Default) \n
		This command selects the signal source for measurements, i.e. it defines which connector is used to input data to the R&S
		FSW. If no additional input options are installed, only RF input or file input is supported. This command only selects
		the RF input or file input. To select the analog baseband input, you have to use method RsFsw.Applications.
		K18_AmplifierEt.InputPy.Select.BbAnalog.State.set. For R&S FSW85 models with two RF input connectors you must select the
		input connector to configure first using method RsFsw.Applications.K10x_Lte.InputPy.TypePy.set. \n
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
			:return: signal_source: No help available"""
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		response = self._core.io.query_str(f'INPut{inputIx_cmd_val}:SELect?')
		return Conversions.str_to_scalar_enum(response, enums.InputSourceB)

	def clone(self) -> 'Select':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Select(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
