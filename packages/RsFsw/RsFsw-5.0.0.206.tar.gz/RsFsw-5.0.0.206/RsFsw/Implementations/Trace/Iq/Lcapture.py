from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Lcapture:
	"""Lcapture commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("lcapture", core, parent)

	def set(self, state: enums.AutoMode) -> None:
		"""SCPI: TRACe:IQ:LCAPture \n
		Snippet: driver.trace.iq.lcapture.set(state = enums.AutoMode.AUTO) \n
		No command help available \n
			:param state: No help available
		"""
		param = Conversions.enum_scalar_to_str(state, enums.AutoMode)
		self._core.io.write(f'TRACe:IQ:LCAPture {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.AutoMode:
		"""SCPI: TRACe:IQ:LCAPture \n
		Snippet: value: enums.AutoMode = driver.trace.iq.lcapture.get() \n
		No command help available \n
			:return: state: No help available"""
		response = self._core.io.query_str(f'TRACe:IQ:LCAPture?')
		return Conversions.str_to_scalar_enum(response, enums.AutoMode)
