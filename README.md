# algorand-projects
Simple projects to learn about the Algorand blockchain


## Running a node

There are multiple genesis.json files present in the ```node/genesisfiles``` folder. A separate data folder can be created for each network. Copy the genesis.json file under the corresponding network folder in ```node/genesisfiles``` to the newly created data folder.

To switch between networks, simply point to the corresponding data file when starting the node.

1. Mainnet
2. Testnet
3. Betanet
4. Devnet

```
# Create a new data folder, copy the corresponding genesis file to it
cd ~/node
mkdir testnetdata
cp ~/node/genesisfiles/testnet/genesis.json ~/node/testnetdata

# To start the node
./goal node start -d ~/node/testnetdata

# To check the status of the node
./goal node status -d ~/node/testnetdata

# To stop the node
./goal node stop -d ~/node/testnetdata
```
