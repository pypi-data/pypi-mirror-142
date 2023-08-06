from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Crdata:
	"""Crdata commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("crdata", core, parent)

	def set(self, state: enums.CorsetDataSelect) -> None:
		"""SCPI: [SENSe]:NR5G:DEMod:CRData \n
		Snippet: driver.applications.k14Xnr5G.sense.nr5G.demod.crdata.set(state = enums.CorsetDataSelect.ALL0) \n
		This command selects the CORESET reference data. \n
			:param state: AUTO Automatic detection of reference values. ALL0 CORESET consists of 0's only. PN23 CORESET based on NR-TM PN23 (pseudo random sequence 23) .
		"""
		param = Conversions.enum_scalar_to_str(state, enums.CorsetDataSelect)
		self._core.io.write(f'SENSe:NR5G:DEMod:CRData {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.CorsetDataSelect:
		"""SCPI: [SENSe]:NR5G:DEMod:CRData \n
		Snippet: value: enums.CorsetDataSelect = driver.applications.k14Xnr5G.sense.nr5G.demod.crdata.get() \n
		This command selects the CORESET reference data. \n
			:return: state: AUTO Automatic detection of reference values. ALL0 CORESET consists of 0's only. PN23 CORESET based on NR-TM PN23 (pseudo random sequence 23) ."""
		response = self._core.io.query_str(f'SENSe:NR5G:DEMod:CRData?')
		return Conversions.str_to_scalar_enum(response, enums.CorsetDataSelect)
