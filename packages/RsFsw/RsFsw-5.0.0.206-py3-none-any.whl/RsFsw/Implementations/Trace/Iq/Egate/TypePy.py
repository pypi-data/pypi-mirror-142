from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TypePy:
	"""TypePy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("typePy", core, parent)

	def set(self, type_py: enums.EgateType) -> None:
		"""SCPI: TRACe:IQ:EGATe:TYPE \n
		Snippet: driver.trace.iq.egate.typePy.set(type_py = enums.EgateType.EDGE) \n
		This command selects the gate mode for gated measurements with the I/Q analyzer. Note: The IF power trigger holdoff time
		is ignored if you are using the 'Level' gate mode in combination with an IF Power trigger. \n
			:param type_py: LEVel EDGE
		"""
		param = Conversions.enum_scalar_to_str(type_py, enums.EgateType)
		self._core.io.write(f'TRACe:IQ:EGATe:TYPE {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.EgateType:
		"""SCPI: TRACe:IQ:EGATe:TYPE \n
		Snippet: value: enums.EgateType = driver.trace.iq.egate.typePy.get() \n
		This command selects the gate mode for gated measurements with the I/Q analyzer. Note: The IF power trigger holdoff time
		is ignored if you are using the 'Level' gate mode in combination with an IF Power trigger. \n
			:return: type_py: LEVel EDGE"""
		response = self._core.io.query_str(f'TRACe:IQ:EGATe:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.EgateType)
