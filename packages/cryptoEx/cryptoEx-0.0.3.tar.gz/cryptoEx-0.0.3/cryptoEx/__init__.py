from .binanceBasic import bnGet,bnPPD,bnSign
from .huobiBasic import hbGet,hbPost,hbSign
from .okexBasic import okGet,okPost,okSign
from .krakenBasic import kkGet,kkPost,kkSign

__all__=[
    'bnGet','bnPPD','bnSign',
    'hbGet','hbPost','hbSign',
    'okGet','okPost','okSign',
    'kkGet','kkPost','kkSign'
]


__version__='0.0.3'
__license__='GPL-2.0 License'
__author__='Tiancheng Jiao'
__url__='https://github.com/jtc1246/cryptoEx'
__author_email__='jtc1246@outlook.com'
__description__='A simple API for some cryptocurrency exchanges'