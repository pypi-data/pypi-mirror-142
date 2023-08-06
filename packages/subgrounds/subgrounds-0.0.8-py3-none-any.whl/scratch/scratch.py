import logging
logging.basicConfig(format='%(asctime)s %(message)s', filename='subgrounds.log', encoding='utf-8', level=logging.DEBUG)

logger = logging.getLogger('subgrounds')
logger.setLevel(logging.DEBUG)

from subgrounds.subgrounds import Subgrounds

sg = Subgrounds()
uniswapV2 = sg.load_subgraph("https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v2")

# Not necessary, but nice for brevity
Query = uniswapV2.Query
Burn = uniswapV2.Burn
Mint = uniswapV2.Mint

mints = Query.mints(
  orderBy=Mint.timestamp,
  orderDirection='desc',
  first=10,
  where=[
    Mint.pair == '0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc'
  ]
)

burns = Query.burns(
  orderBy=Burn.timestamp,
  orderDirection='desc',
  first=10,
  where=[
    Burn.pair == '0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc'
  ]
)

from pprint import pp
from pipe import map

fpaths = [
  mints.timestamp,
  mints.pair.id,
  mints.pair.token0.symbol,
  mints.pair.token1.symbol,

  burns.timestamp,
  burns.pair.id,
  burns.pair.token0.symbol,
  burns.pair.token1.symbol,
]

pp(list(fpaths | map(lambda fpath: fpath.data_path)))