from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Attenuation:
	"""Attenuation commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("attenuation", core, parent)

	def set(self, attenuation: float, inputIx=repcap.InputIx.Default) -> None:
		"""SCPI: INPut<ip>:ATTenuation \n
		Snippet: driver.applications.k30NoiseFigure.inputPy.attenuation.set(attenuation = 1.0, inputIx = repcap.InputIx.Default) \n
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
		Snippet: value: float = driver.applications.k30NoiseFigure.inputPy.attenuation.get(inputIx = repcap.InputIx.Default) \n
		This command defines the total attenuation for RF input. If you set the attenuation manually, it is no longer coupled to
		the reference level, but the reference level is coupled to the attenuation. Thus, if the current reference level is not
		compatible with an attenuation that has been set manually, the command also adjusts the reference level. \n
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
			:return: attenuation: Range: see data sheet , Unit: DB"""
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		response = self._core.io.query_str(f'INPut{inputIx_cmd_val}:ATTenuation?')
		return Conversions.str_to_float(response)
