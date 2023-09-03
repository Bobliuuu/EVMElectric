console.clear();
require("dotenv").config();
const {
  AccountId,
  PrivateKey,
  Client,
  TopicCreateTransaction,
  TopicMessageQuery,
  TopicMessageSubmitTransaction,
  FileContentsQuery
} = require("@hashgraph/sdk");
const fs = require('fs');

// Grab the OPERATOR_ID and OPERATOR_KEY from the .env file
const myAccountId = process.env.MY_ACCOUNT_ID;
const myPrivateKey = process.env.MY_PRIVATE_KEY;

// Build Hedera testnet and mirror node client
const client = Client.forTestnet();

// Set the operator account ID and operator private key
client.setOperator(myAccountId, myPrivateKey);

async function dostuff(){
    //Create the query
    const query = new FileContentsQuery()
        .setFileId('0.0.1162920');

    //Sign with client operator private key and submit the query to a Hedera network
    const contents = await query.execute(client);

    console.log(contents);
    const filePath = 'output.png';

    // Write the buffer data to the PNG file
    fs.writeFileSync(filePath, contents);

    console.log(`Buffer data saved as ${filePath}`);
}

dostuff();