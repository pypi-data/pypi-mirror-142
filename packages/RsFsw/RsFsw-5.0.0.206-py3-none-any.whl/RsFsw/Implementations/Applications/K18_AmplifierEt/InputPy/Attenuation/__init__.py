from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Attenuation:
	"""Attenuation commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("attenuation", core, parent)

	@property
	def auto(self):
		"""auto commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_auto'):
			from .Auto import Auto
			self._auto = Auto(self._core, self._cmd_group)
		return self._auto

	def set(self, attenuation: float, inputIx=repcap.InputIx.Default) -> None:
		"""SCPI: INPut<ip>:ATTenuation \n
		Snippet: driver.applications.k18AmplifierEt.inputPy.attenuation.set(attenuation = 1.0, inputIx = repcap.InputIx.Default) \n
		This command defines the total attenuation for RF input. If you set the attenuation manually, it is no longer coupled to
		the reference level, but the reference level is coupled to the attenuation. Thus, if the current reference level is not
		compatible with an attenuation that has been set manually, the command also adjusts the reference level. \n
			:param attenuation: Range: see data sheet , Unit: DB
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
		"""
		param = Conversions.decimal_value_to_str(attenuation)
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		self._core.io.write(f'INPut{inputIx_cmd_val}:ATTenuation {param}')

	def get(self, inputIx=repcap.InputIx.Default) -> float:
		"""SCPI: INPut<ip>:ATTenuation \n
		Snippet: value: float = driver.applications.k18AmplifierEt.inputPy.attenuation.get(inputIx = repcap.InputIx.Default) \n
		This command defines the total attenuation for RF input. If you set the attenuation manually, it is no longer coupled to
		the reference level, but the reference level is coupled to the attenuation. Thus, if the current reference level is not
		compatible with an attenuation that has been set manually, the command also adjusts the reference level. \n
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
			:return: attenuation: Range: see data sheet , Unit: DB"""
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		response = self._core.io.query_str(f'INPut{inputIx_cmd_val}:ATTenuation?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Attenuation':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Attenuation(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
