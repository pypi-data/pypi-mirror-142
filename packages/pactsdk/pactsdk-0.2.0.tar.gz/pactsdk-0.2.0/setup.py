# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pactsdk']

package_data = \
{'': ['*']}

install_requires = \
['py-algorand-sdk>=1.9.0,<2.0.0', 'requests>=2.27.1,<3.0.0']

setup_kwargs = {
    'name': 'pactsdk',
    'version': '0.2.0',
    'description': 'Python SDK for Pact smart contracts',
    'long_description': '# Pact Python SDK\n\nPython SDK for Pact smart contracts.\n\nWhat is covered by the library:\n\n- Fetching pools\n- Opt-in for assets\n- Managing liquidity\n- Inspecting pools state\n- Making swaps\n\nSigning and sending transactions is not covered by the library. The provided examples use algosdk directly to send the transactions.\n\n# Installation\n\n`pip install pactsdk`\n\n# Basic usage\n\n**CAUTION** - The library uses integers for asset amounts e.g. microalgos instead of algos so if you want to send 1 algo, you need to specify it as 1_000_000.\n\nCreate a Pact client.\n\n```py\nfrom algosdk.v2client.algod import AlgodClient\nimport pactsdk\n\nalgod = AlgodClient(token, url)\npact = pactsdk.PactClient(algod)\n```\n\nOptionally you can specify custom Pact API url. By default it directs to production API.\n\n```py\npact = pactsdk.PactClient(algod, pact_api_url="https://api.testnet.pact.fi")\n```\n\nFetching pools by assets pair. It uses Pact API to retrieve the pool. Can return multiple pools with differing fee_bps.\n\n```py\nalgo = pact.fetch_asset(0)\nother_coin = pact.fetch_asset(8949213)\n\npools = pact.fetch_pools_by_assets(algo, other_coin) # The pool will be fetched regardless of assets order.\n```\n\nYou can fetch a pool by providing assets ids instead of Asset objects.\n\n```py\npools = pact.fetch_pools_by_assets(0, 8949213)\n```\n\nYou can also fetch a pool by providing app id. This way the pool is retrieved directly from the chain.\n\n```py\npool = pact.fetch_pool_by_id(456321)\n```\n\nYou can list all pools from the Pact API.\n\n```py\npools = pact.list_pools()\nprint(pools)\n# {\n#   "count": 19,\n#   "next": "http://api.pact.fi/api/pools?page=2",\n#   "previous": None,\n#   "results": [...],\n# }\n\n# The listing uses pagination and filtering.\npools = pact.list_pools(\n  page=2,\n  primary_asset__algoid=9843123,\n)\n```\n\nBefore making the transactions you need to opt-in for the assets. There\'s no need to opt-in for algo.\n\n```py\nimport algosdk\n\nprivate_key = algosdk.mnemonic.to_private_key(\'<mnemonic>\')\naddress = algosdk.account.address_from_private_key(private_key)\n\ndef opt_in(asset):\n  is_opted_in = asset.is_opted_in(address)\n  if not is_opted_in\n    opt_in_tx = asset.prepare_opt_in_tx(address)\n    signed_tx = opt_in_tx.sign(private_key)\n    algod.send_transaction(signed_tx)\n  }\n}\n\nopt_in(pool.primary_asset)\nopt_in(pool.secondary_asset)\nopt_in(pool.liquidity_asset) # Needed if you want to manage the liquidity.\n```\n\nCheck the current pool state.\n\n```py\nprint(pool.state)\n# PoolState(\n#   total_liquidity=900000,\n#   total_primary=956659,\n#   total_secondary=849972,\n#   primary_asset_price=Decimal(0.8884795940873393),\n#   secondary_asset_price=Decimal(1.1255182523659604),\n# )\n```\n\nExplicit pool state update is necessary periodically and after each pool operation.\n\n```py\npool.update_state()\npool.state  # Now holds fresh values.\n```\n\nManaging the liquidity.\n\n```py\n# Add liquidity.\nadd_liq_tx_group = pool.prepare_add_liquidity_tx(\n  address=address,\n  primary_asset_amount=100_000,\n  secondary_asset_amount=50_000,\n);\nsigned_add_liq_tx_group = add_liq_tx_group.sign(private_key)\nalgod.send_transactions(signed_add_liq_tx_group)\n\n# Remove liquidity.\nremove_liq_tx_group = pool.prepare_remove_liquidity_tx(\n  address=address,\n  amount=100_000,\n)\nsigned_remove_liq_tx_group = remove_liq_tx_group.sign(private_key)\nalgod.send_transactions(signed_remove_liq_tx_group)\n```\n\nMaking a swap.\n\n```py\nswap = pool.prepare_swap(\n  asset=algo,\n  amount=200_000,\n  slippage_pct=2,\n)\n\n# You can inspect swap effect before submitting the transaction.\nprint(swap.effect)\n# SwapEffect(\n#     amount_out=200000,\n#     amount_in=146529,\n#     minimum_amount_in=143598,\n#     fee=441,\n#     price=Decimal(0.73485),\n#     primary_asset_price_after_swap=Decimal("0.6081680080300244"),\n#     secondary_asset_price_after_swap=Decimal("1.6442824791774173"),\n#     primary_asset_price_change_pct=Decimal("-31.549580645715963"),\n#     secondary_asset_price_change_pct=Decimal("46.091142966447585"),\n# )\n\n# Let\'s submit the swap.\nswap_tx_group = swap.prepare_tx(address)\nsigned_tx_group = swap_tx_group.sign_txn(private_key)\nalgod.send_transactions(signed_tx_group)\n```\n\nLook for more [examples](examples).\n\n# Development\n\n- `poetry install`\n\nDevelopment requires [Pact contracts V1](https://github.com/pactfi/algorand-testbed) to be checked out.\n\n- `git clone git@github.com:pactfi/algorand-testbed.git`\n- `cd algorand-testbed`\n- `poetry install`\n- `docker compose up -d`\n- `cd ..`\n\n## Building\n\n- `poetry build`\n\nYou can install the package locally with\n`pip install dist/pactsdk-<version>.whl`\n\nValidate the installation `python -c "import pactsdk; print(pactsdk.__version__)"`\n\n## Running tests\n\n- `poetry run pytest`\n',
    'author': 'Mateusz Tomczyk',
    'author_email': 'mateusz@ulam.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/pactfi/pact-py-sdk',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
