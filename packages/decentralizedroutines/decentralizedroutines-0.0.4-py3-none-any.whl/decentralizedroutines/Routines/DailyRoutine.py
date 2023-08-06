# from MarketData.Bloomberg import SelectFuturesChain
# from MarketData.Bloomberg import CreateFutSeries
# from MarketData.Bloomberg import LoadFutChainHistory
# from MarketData.Bloomberg import FillDataFutSeries

# from MarketData.BCB import load_focus

# from MarketData.CME import sync_ftp

# from MarketData.CVM import download_files

# from MarketData.Tesouro import update_inventory

from MarketData.BVMF import download_files
from MarketData.BVMF import COTAHIST
from MarketData.BVMF import IndicadoresEconomicos
from MarketData.BVMF import BVBG028
from MarketData.BVMF import DeltaOpcoes
from MarketData.BVMF import PremioReferencia
from MarketData.BVMF import BVBG086
from MarketData.BVMF import CreateFutSeries

from MarketData.BVMF import ContratosEmAbertoPorParticipante

from Routines import Analysis_DI1
from Routines import Analysis_COPOM
from Routines import Analysis_IDI

print('Daily Routine DONE!')

