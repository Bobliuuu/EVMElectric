console.clear();
require("dotenv").config();
const {
  AccountId,
  PrivateKey,
  Client,
  TopicCreateTransaction,
  TopicMessageQuery,
  TopicMessageSubmitTransaction,
  AccountBalanceQuery,
  HbarUnit
} = require("@hashgraph/sdk");
const axios = require('axios');

// Grab the OPERATOR_ID and OPERATOR_KEY from the .env file
const myAccountId = process.env.MY_ACCOUNT_ID;
const myPrivateKey = process.env.MY_PRIVATE_KEY;

// Build Hedera testnet and mirror node client
const client = Client.forTestnet();

// Set the operator account ID and operator private key
client.setOperator(myAccountId, myPrivateKey);

async function convertHbarToUSD(hbarAmount) {
    const response = await axios.get(
      'https://mainnet-public.mirrornode.hedera.com/api/v1/network/exchangerate',
    )
  
    const data = response.data
  
    const centEquivalentPerHbar =
      data.current_rate.cent_equivalent / data.current_rate.hbar_equivalent
  
    // Convert hbars to cents
    let cents = hbarAmount * centEquivalentPerHbar
  
    // Convert cents to dollars
    let dollars = cents / 100
  
    // Round to 2 decimal places
    dollars = dollars.toFixed(2)
  
    return dollars
  }

async function doStuff() {
    const balance = await new AccountBalanceQuery()
      .setAccountId(myAccountId)
      .execute(client)
  
    const usd = await convertHbarToUSD(balance.hbars.to(HbarUnit.Hbar))
    console.log(balance.hbars.toString());
    console.log(usd)
}

doStuff();