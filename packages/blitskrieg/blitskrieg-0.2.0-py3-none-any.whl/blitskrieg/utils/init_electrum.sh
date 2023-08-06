#!/bin/bash

wlt='electrum -D /srv/wallet/wlt --regtest'

mkdir -p /srv/wallet/wlt/regtest
cat <<EOF > /srv/wallet/wlt/regtest/config
{
    "lightning_listen": "0.0.0.0:9735",
    "rpchost": "0.0.0.0",
    "rpcpassword": "default_password",
    "rpcport": 7777,
    "rpcuser": "user",
    "log_to_file": "true",
    "use_gossip": "true"
}
EOF

${wlt} -o create
