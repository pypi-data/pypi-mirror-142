from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Value:
	"""Value commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("value", core, parent)

	def set(self, offset: float) -> None:
		"""SCPI: [SENSe]:DDEMod:STANdard:SYNC:OFFSet[:VALue] \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.standard.sync.offset.value.set(offset = 1.0) \n
		This command defines a number of symbols which are ignored before the comparison with the pattern starts. \n
			:param offset: Range: 0 to 15000, Unit: SYMB
		"""
		param = Conversions.decimal_value_to_str(offset)
		self._core.io.write(f'SENSe:DDEMod:STANdard:SYNC:OFFSet:VALue {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:DDEMod:STANdard:SYNC:OFFSet[:VALue] \n
		Snippet: value: float = driver.applications.k70Vsa.sense.ddemod.standard.sync.offset.value.get() \n
		This command defines a number of symbols which are ignored before the comparison with the pattern starts. \n
			:return: offset: Range: 0 to 15000, Unit: SYMB"""
		response = self._core.io.query_str(f'SENSe:DDEMod:STANdard:SYNC:OFFSet:VALue?')
		return Conversions.str_to_float(response)
