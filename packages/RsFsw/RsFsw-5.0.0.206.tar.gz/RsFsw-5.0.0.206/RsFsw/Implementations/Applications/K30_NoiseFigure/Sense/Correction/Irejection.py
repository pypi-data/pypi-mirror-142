from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Irejection:
	"""Irejection commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("irejection", core, parent)

	def set(self, image_rejection: float) -> None:
		"""SCPI: [SENSe]:CORRection:IREJection \n
		Snippet: driver.applications.k30NoiseFigure.sense.correction.irejection.set(image_rejection = 1.0) \n
		This command defines the image frequency rejection for the DUT. \n
			:param image_rejection: Range: 0 to 999.99, Unit: DB
		"""
		param = Conversions.decimal_value_to_str(image_rejection)
		self._core.io.write(f'SENSe:CORRection:IREJection {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:CORRection:IREJection \n
		Snippet: value: float = driver.applications.k30NoiseFigure.sense.correction.irejection.get() \n
		This command defines the image frequency rejection for the DUT. \n
			:return: image_rejection: Range: 0 to 999.99, Unit: DB"""
		response = self._core.io.query_str(f'SENSe:CORRection:IREJection?')
		return Conversions.str_to_float(response)
