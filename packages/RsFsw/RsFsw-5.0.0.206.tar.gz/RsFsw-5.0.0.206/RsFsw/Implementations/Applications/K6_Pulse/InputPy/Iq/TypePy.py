from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TypePy:
	"""TypePy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("typePy", core, parent)

	def set(self, iq_type: enums.IqType) -> None:
		"""SCPI: INPut:IQ:TYPE \n
		Snippet: driver.applications.k6Pulse.inputPy.iq.typePy.set(iq_type = enums.IqType.Ipart=I) \n
		This command defines the format of the input signal. \n
			:param iq_type: No help available
		"""
		param = Conversions.enum_scalar_to_str(iq_type, enums.IqType)
		self._core.io.write(f'INPut:IQ:TYPE {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.IqType:
		"""SCPI: INPut:IQ:TYPE \n
		Snippet: value: enums.IqType = driver.applications.k6Pulse.inputPy.iq.typePy.get() \n
		This command defines the format of the input signal. \n
			:return: iq_type: No help available"""
		response = self._core.io.query_str(f'INPut:IQ:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.IqType)
