from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, arg_0: bool) -> None:
		"""SCPI: [SENSe]:SWEep:EGATe:CONTinuous[:STATe] \n
		Snippet: driver.applications.k14Xnr5G.sense.sweep.egate.continuous.state.set(arg_0 = False) \n
		No command help available \n
			:param arg_0: No help available
		"""
		param = Conversions.bool_to_str(arg_0)
		self._core.io.write(f'SENSe:SWEep:EGATe:CONTinuous:STATe {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:SWEep:EGATe:CONTinuous[:STATe] \n
		Snippet: value: bool = driver.applications.k14Xnr5G.sense.sweep.egate.continuous.state.get() \n
		No command help available \n
			:return: arg_0: No help available"""
		response = self._core.io.query_str(f'SENSe:SWEep:EGATe:CONTinuous:STATe?')
		return Conversions.str_to_bool(response)
