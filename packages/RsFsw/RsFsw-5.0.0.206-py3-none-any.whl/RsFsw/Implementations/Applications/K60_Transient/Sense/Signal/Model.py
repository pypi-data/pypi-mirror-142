from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Model:
	"""Model commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("model", core, parent)

	def set(self, signal: enums.SignalModel) -> None:
		"""SCPI: [SENSe]:SIGNal:MODel \n
		Snippet: driver.applications.k60Transient.sense.signal.model.set(signal = enums.SignalModel.CHIRp) \n
		Defines which type of signal to expect (if known) , thus determining the analysis method. This command is only required
		if the additional options R&S FSW-K60C/-K60H are installed. \n
			:param signal: HOP | CHIRp HOP Signals 'hop' between random carrier frequencies in short intervals CHIRp The carrier frequency is either increased or decreased linearly over time NONE No specific signal model is used; this is the default setting if no additional options are installed
		"""
		param = Conversions.enum_scalar_to_str(signal, enums.SignalModel)
		self._core.io.write(f'SENSe:SIGNal:MODel {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.SignalModel:
		"""SCPI: [SENSe]:SIGNal:MODel \n
		Snippet: value: enums.SignalModel = driver.applications.k60Transient.sense.signal.model.get() \n
		Defines which type of signal to expect (if known) , thus determining the analysis method. This command is only required
		if the additional options R&S FSW-K60C/-K60H are installed. \n
			:return: signal: HOP | CHIRp HOP Signals 'hop' between random carrier frequencies in short intervals CHIRp The carrier frequency is either increased or decreased linearly over time NONE No specific signal model is used; this is the default setting if no additional options are installed"""
		response = self._core.io.query_str(f'SENSe:SIGNal:MODel?')
		return Conversions.str_to_scalar_enum(response, enums.SignalModel)
