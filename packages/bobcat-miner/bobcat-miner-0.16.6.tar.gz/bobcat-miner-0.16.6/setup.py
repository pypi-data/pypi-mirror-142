# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['bobcat_miner']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.8.1,<4.0.0',
 'backoff>=1.11.1,<2.0.0',
 'beautifulsoup4>=4.10.0,<5.0.0',
 'click>=8.0.3,<9.0.0',
 'discord-lumberjack>=1.0.4,<2.0.0',
 'filelock>=3.4.2,<4.0.0',
 'requests>=2.27.0,<3.0.0']

entry_points = \
{'console_scripts': ['bobcat = bobcat_miner.cli:cli']}

setup_kwargs = {
    'name': 'bobcat-miner',
    'version': '0.16.6',
    'description': 'Automate the Bobcat miner from the command line.',
    'long_description': '[![PyPI](https://img.shields.io/pypi/v/bobcat_miner.svg)](https://pypi.org/project/bobcat-miner/)\n[![Dockerhub](https://img.shields.io/docker/v/aidanmelen/bobcat?color=blue&label=docker%20build)](https://hub.docker.com/r/aidanmelen/bobcat)\n[![Release](https://github.com/aidanmelen/bobcat-miner-python/actions/workflows/release.yaml/badge.svg)](https://github.com/aidanmelen/bobcat-miner-python/actions/workflows/release.yaml)\n[![Tests](https://github.com/aidanmelen/bobcat-miner-python/actions/workflows/tests.yaml/badge.svg)](https://github.com/aidanmelen/bobcat-miner-python/actions/workflows/tests.yaml)\n[![Lint](https://github.com/aidanmelen/bobcat-miner-python/actions/workflows/lint.yaml/badge.svg)](https://github.com/aidanmelen/bobcat-miner-python/actions/workflows/lint.yaml)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n\n# bobcat miner python\n\nAutomatically *find*, *diagnose*, and *repair* the Bobcat miner!\n\n**Online**\n```console\n$ bobcat autopilot\n✅ Online Status: Online ⭐\n✅ Sync Status: Synced (gap:-1) 💫\n✅ Relay Status: Not Relayed ✨\n✅ Network Status: Good 📶\n✅ Temperature Status: Good (38°C) ☀️\n```\n\n**Offline**\n```console\n$ bobcat autopilot\n❌ Online Status: Offline\n❌ Bobcat Status: Down\n⚠️ Rebooting Bobcat\n✅ Reconnected to the Bobcat (fancy-awesome-bobcat)\n⚠️ Resetting Bobcat\n✅ Reconnected to the Bobcat (fancy-awesome-bobcat)\n⚠️ Fastsyncing Bobcat\n✅ Reconnected to the Bobcat (fancy-awesome-bobcat)\n✅ Repair Status: Complete\n✅ Relay Status: Not Relayed ✨\n✅ Network Status: Good 📶\n✅ Temperature Status: Good (38°C) ☀️\n```\n\nor run with the official Docker image\n\n```\ndocker run --rm -it aidanmelen/bobcat autopilot\n```\n\nℹ️ Run `bobcat --help` to learn about the available sub-commands and options.\n\n## Install\n\n### Pipx\n\n```\npipx install bobcat-miner\n```\n\nℹ️ Please see this [guide](https://packaging.python.org/en/latest/guides/installing-stand-alone-command-line-tools/) for more information about installing stand alone command line tools with [pipx](https://pypa.github.io/pipx/).\n\n### Docker\n\n```\ndocker pull aidanmelen/bobcat\n```\n\n## Finding your Bobcat\n\nAutopilot will automatically search and find your Bobcat. Setting the log-level to `DEBUG` will show more information about the search process.\n\n```console\n$ bobcat -C DEBUG autopilot\n🐛 Searching for a bobcat in these networks: 192.168.0.0/24, 10.0.0.0/24, 172.16.0.0/24, 192.168.0.1/16, 10.0.0.1/16, 172.16.0.1/16\n🐛 Searching network: 192.168.0.0/24\n🐛 Connected to Bobcat: 192.168.0.10\n🐛 Found Bobcat: 192.168.0.10\n🐛 The Bobcat Autopilot is starting 🚀 🚀 🚀\n...\n```\n\nThe search may take awhile depending on your Bobcat\'s IP address. However; this step can be skipped by specifying either the `--ip-address` or `--hostname` options.\n\n```console\n$ bobcat --ip-address 192.168.0.10 -C DEBUG autopilot\n🐛 Connected to Bobcat: 192.168.0.10\n🐛 The Bobcat Autopilot is starting 🚀 🚀 🚀\n...\n```\n\nℹ️ Please see the offical [bobcat instructions](https://bobcatminer.zendesk.com/hc/en-us/articles/4412905935131-How-to-Access-the-Diagnoser) to manually find the IP address.\n\n## Dry Run\n\nUse the `--dry-run` option to see what repair steps the `bobcat autopilot` would normally run\n\n```console\n$ bobcat --dry-run autopilot\n❌ Online Status: Offline\n❌ Bobcat Status: Down\n⚠️ Dry Run: Reboot Skipped\n⚠️ Dry Run: Reset Skipped\n⚠️ Dry Run: Fastsync Skipped\n✅ Network Status: Good 📶\n✅ Temperature Status: Good (38°C) ☀️\n```\n\n## Verbose\n\nUse the `--verbose` option to see detailed diagnostics\n\n```console\n$ bobcat autopilot --verbose\n...\n❌ Bobcat Status: Down\n**Points to:** Miner\'s Docker Container\n\n**Why does this happen?** \nThis can happen if your miner\'s Docker crashes. Sometimes losing power or internet connection during an OTA can cause a miner\'s Docker to crash. This can typically be fixed with a reboot or a reset, followed by a fast sync if your gap is >400. Fast Sync is recommended if your gap is >400 and your miner has been fully synced before.\n\n**What You Can Try:** \n1. First Try Reboot\n2. Try Reset\n3. Then Fastsync\n4. Make Sure Your Miner is Connected to the Internet. What color is your miner\'s LED?\n\n**What to provide customer support if unable to resolve:**\n1. If Possible, Screenshots of Your Diagnoser.\n2. Indicate Miner\'s LED Color\n3. Open Port 22, if Unable to Access the Diagnoser\n4. Provide Miner\'s IP Address\n5. Confirm Port 22 is Open (Include a Screenshot of this Page)\n\n**Troublesooting Guides:**\n- https://bobcatminer.zendesk.com/hc/en-us/articles/4413666097051-Status-Down-4413666097051-Status-Down-\n...\n```\n\n\n## Monitoring with Discord\n\nMonitor your Bobcat remotely by sending events to a Discord channel. No need for VPN or SSH agent setup!\n\n```console\n$ bobcat --discord-webhook-url https://discord.com/api/webhooks/xxx autopilot\n✅ Online Status: Online ⭐\n✅ Sync Status: Synced (gap:0) 💫\n⚠️ Relay Status: Relayed\n✅ Network Status: Good 📶\n❌ Temperature Status: Hot (78°C) 🌋\n```\n\nand check the Discord channel\n\n<!-- <img src="https://raw.githubusercontent.com/aidanmelen/bobcat-miner-python/main/assets/bobcat-autopilot-discord-app.png" alt="drawing" style="width:500px;"/> -->\n<img src="https://raw.githubusercontent.com/aidanmelen/bobcat-miner-python/main/assets/bobcat-autopilot-discord-app.png" alt="drawing" width="300"/>\n\nℹ️ Please see Discord\'s [Intro to Webhooks](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks) document for more information.\n\n## Bobcat SDK\n\nPlease see the [Bobcat SDK Docs](https://github.com/aidanmelen/bobcat-miner-python/blob/main/docs/bobcat_sdk.md) for more information.\n\n\n## Contributions\n\nPlease see the [Contributions Docs](https://github.com/aidanmelen/bobcat-miner-python/blob/main/docs/contributions.md) for more information. This document includes sections for Development, Test, and Release.\n\n## DIY Troubleshooting\n\nPlease see [No Witness\'s Troubleshooting Guide](https://www.nowitness.org/troubleshooting/) for more information.\n\n## Donations\n\nDonations are welcome and appreciated! :gift:\n\n[![HNT: 14HmckNU4WHDDtGH29FMqVENzZAYh5a9XRiLfY2AN6ghfHMvAuR](https://raw.githubusercontent.com/aidanmelen/bobcat-miner-python/main/assets/wallet.jpg)](https://explorer-v1.helium.com/accounts/14HmckNU4WHDDtGH29FMqVENzZAYh5a9XRiLfY2AN6ghfHMvAuR)\n\nHNT: [14HmckNU4WHDDtGH29FMqVENzZAYh5a9XRiLfY2AN6ghfHMvAuR](https://explorer-v1.helium.com/accounts/14HmckNU4WHDDtGH29FMqVENzZAYh5a9XRiLfY2AN6ghfHMvAuR)\n',
    'author': 'Aidan Melen',
    'author_email': 'aidanmelen@protonmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/aidanmelen/bobcat-miner-python',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
