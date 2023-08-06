from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Output:
	"""Output commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("output", core, parent)

	def set(self, state: bool, outputSignal=repcap.OutputSignal.Freq100MHz) -> None:
		"""SCPI: [SENSe]:ROSCillator:O<100|640> \n
		Snippet: driver.sense.roscillator.output.set(state = False, outputSignal = repcap.OutputSignal.Freq100MHz) \n
		This command turns the output of a reference signal on the corresponding connector ('Ref Output') on and off.
		[SENSe:]ROSCillator:O100: Provides a 100 MHz reference signal on corresponding connector. [SENSe:]ROSCillator:O640:
		Provides a 640 MHz reference signal on corresponding connector. \n
			:param state: ON | OFF | 1 | 0 OFF | 0 Switches the reference off. ON | 1 Switches the reference on
			:param outputSignal: optional repeated capability selector. Default value: Freq100MHz
		"""
		param = Conversions.bool_to_str(state)
		outputSignal_cmd_val = self._cmd_group.get_repcap_cmd_value(outputSignal, repcap.OutputSignal)
		self._core.io.write(f'SENSe:ROSCillator:O{outputSignal_cmd_val} {param}')

	def get(self, outputSignal=repcap.OutputSignal.Freq100MHz) -> bool:
		"""SCPI: [SENSe]:ROSCillator:O<100|640> \n
		Snippet: value: bool = driver.sense.roscillator.output.get(outputSignal = repcap.OutputSignal.Freq100MHz) \n
		This command turns the output of a reference signal on the corresponding connector ('Ref Output') on and off.
		[SENSe:]ROSCillator:O100: Provides a 100 MHz reference signal on corresponding connector. [SENSe:]ROSCillator:O640:
		Provides a 640 MHz reference signal on corresponding connector. \n
			:param outputSignal: optional repeated capability selector. Default value: Freq100MHz
			:return: state: ON | OFF | 1 | 0 OFF | 0 Switches the reference off. ON | 1 Switches the reference on"""
		outputSignal_cmd_val = self._cmd_group.get_repcap_cmd_value(outputSignal, repcap.OutputSignal)
		response = self._core.io.query_str(f'SENSe:ROSCillator:O{outputSignal_cmd_val}?')
		return Conversions.str_to_bool(response)
