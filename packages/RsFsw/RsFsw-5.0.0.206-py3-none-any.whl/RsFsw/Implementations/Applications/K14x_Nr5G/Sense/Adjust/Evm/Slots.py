from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Slots:
	"""Slots commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("slots", core, parent)

	def set(self, slots: float) -> None:
		"""SCPI: [SENSe]:ADJust:EVM:SLOTs \n
		Snippet: driver.applications.k14Xnr5G.sense.adjust.evm.slots.set(slots = 1.0) \n
		This command selects the number of slots to be used during the auto EVM routine.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Select manual automatic measurement time mode ([SENSe:]ADJust:CONFigure:LEVel:DURation:MODE) .
			- Define an appropriate automatic measurement time ([SENSe:]ADJust:CONFigure:LEVel:DURation) . \n
			:param slots: No help available
		"""
		param = Conversions.decimal_value_to_str(slots)
		self._core.io.write(f'SENSe:ADJust:EVM:SLOTs {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:ADJust:EVM:SLOTs \n
		Snippet: value: float = driver.applications.k14Xnr5G.sense.adjust.evm.slots.get() \n
		This command selects the number of slots to be used during the auto EVM routine.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Select manual automatic measurement time mode ([SENSe:]ADJust:CONFigure:LEVel:DURation:MODE) .
			- Define an appropriate automatic measurement time ([SENSe:]ADJust:CONFigure:LEVel:DURation) . \n
			:return: slots: No help available"""
		response = self._core.io.query_str(f'SENSe:ADJust:EVM:SLOTs?')
		return Conversions.str_to_float(response)
