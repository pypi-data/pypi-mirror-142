from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Iff:
	"""Iff commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("iff", core, parent)

	def set(self, size: enums.DutSize) -> None:
		"""SCPI: [SENSe]:POWer:SEM:IFF \n
		Snippet: driver.applications.k14Xnr5G.sense.power.sem.iff.set(size = enums.DutSize.DUT15) \n
		This command selects the size of the DUT for the SEM measurement.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Select FR2 deployment (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Uplink.Cc.DfRange.set) . \n
			:param size: DUT15 DUT size ≤15 cm DUT30 DUT size ≤30 cm
		"""
		param = Conversions.enum_scalar_to_str(size, enums.DutSize)
		self._core.io.write(f'SENSe:POWer:SEM:IFF {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.DutSize:
		"""SCPI: [SENSe]:POWer:SEM:IFF \n
		Snippet: value: enums.DutSize = driver.applications.k14Xnr5G.sense.power.sem.iff.get() \n
		This command selects the size of the DUT for the SEM measurement.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Select FR2 deployment (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Uplink.Cc.DfRange.set) . \n
			:return: size: DUT15 DUT size ≤15 cm DUT30 DUT size ≤30 cm"""
		response = self._core.io.query_str(f'SENSe:POWer:SEM:IFF?')
		return Conversions.str_to_scalar_enum(response, enums.DutSize)
