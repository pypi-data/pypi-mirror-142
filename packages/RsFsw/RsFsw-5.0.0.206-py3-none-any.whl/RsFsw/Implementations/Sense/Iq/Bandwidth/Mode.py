from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mode:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, mode: enums.IqBandwidthMode) -> None:
		"""SCPI: [SENSe]:IQ:BWIDth:MODE \n
		Snippet: driver.sense.iq.bandwidth.mode.set(mode = enums.IqBandwidthMode.AUTO) \n
		This command defines how the resolution bandwidth is determined. \n
			:param mode: AUTO | MANual | FFT AUTO (Default) The RBW is determined automatically depending on the sample rate and record length. MANual The user-defined RBW is used and the (FFT) window length (and possibly the sample rate) are adapted accordingly. The RBW is defined using the [SENSe:]IQ:BWIDth:RESolution command. FFT The RBW is determined by the FFT parameters.
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.IqBandwidthMode)
		self._core.io.write(f'SENSe:IQ:BWIDth:MODE {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.IqBandwidthMode:
		"""SCPI: [SENSe]:IQ:BWIDth:MODE \n
		Snippet: value: enums.IqBandwidthMode = driver.sense.iq.bandwidth.mode.get() \n
		This command defines how the resolution bandwidth is determined. \n
			:return: mode: AUTO | MANual | FFT AUTO (Default) The RBW is determined automatically depending on the sample rate and record length. MANual The user-defined RBW is used and the (FFT) window length (and possibly the sample rate) are adapted accordingly. The RBW is defined using the [SENSe:]IQ:BWIDth:RESolution command. FFT The RBW is determined by the FFT parameters."""
		response = self._core.io.query_str(f'SENSe:IQ:BWIDth:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.IqBandwidthMode)
