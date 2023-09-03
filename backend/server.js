// Require the framework and instantiate it
const fastify = require('fastify')({ logger: true })
require("dotenv").config();
const {
  AccountId,
  PrivateKey,
  Client,
  TopicCreateTransaction,
  TopicMessageQuery,
  TopicMessageSubmitTransaction,
  FileContentsQuery,
  AccountBalanceQuery,
  HbarUnit,
  AccountCreateTransaction,
  Hbar,
  TransferTransaction,
} = require("@hashgraph/sdk");

// Refer to Hedera documentation for details

const myAccountId = process.env.MY_ACCOUNT_ID;
const myPrivateKey = process.env.MY_PRIVATE_KEY;

const client = Client.forTestnet();

client.setOperator(myAccountId, myPrivateKey);

async function convertHbarToUSD(hbarAmount) {
  const response = await axios.get(
    'https://mainnet-public.mirrornode.hedera.com/api/v1/network/exchangerate',
  )

  const data = response.data

  const centEquivalentPerHbar =
    data.current_rate.cent_equivalent / data.current_rate.hbar_equivalent

  let cents = hbarAmount * centEquivalentPerHbar

  let dollars = cents / 100

  dollars = dollars.toFixed(2)

  return dollars
}

fastify.get('/', function handler (request, reply) {
  reply.send({ hello: 'world' })
})

fastify.get('/hcs', async function handler (request, reply) {
  const topic = request.query.topic;

  let txResponse = await new TopicCreateTransaction().execute(client);

  let receipt = await txResponse.getReceipt(client);
  let topicId = receipt.topicId;
  console.log(`Your topic ID is: ${topicId}`);

  await new Promise((resolve) => setTimeout(resolve, 5000));

  new TopicMessageQuery()
    .setTopicId(topicId)
    .subscribe(client, null, (message) => {
      let messageAsString = Buffer.from(message.contents, "utf8").toString();
      console.log(
        `${message.consensusTimestamp.toDate()} Received: ${messageAsString}`
      );
    });

  let sendResponse = await new TopicMessageSubmitTransaction({
    topicId: topicId,
    message: topic,
  }).execute(client);
  const getReceipt = await sendResponse.getReceipt(client);

  const transactionStatus = getReceipt.status;
  console.log("The message transaction status: " + transactionStatus.toString());
  return res.json({'result': transactionStatus.toString()})
})

fastify.get('/hts', async function handler (request, reply) {
  const id = request.query.id;
  const query = new FileContentsQuery()
  .setFileId(id);

  const contents = await query.execute(client);

  console.log(contents);
  const filePath = 'output.png';

  fs.writeFileSync(filePath, contents);

  console.log(`Buffer data saved as ${filePath}`);
  return res.json({'bytecontent': content})
})

fastify.get('/createaccount', async function handler (request, reply) {
  const privateKey = PrivateKey.generateED25519()
  const publicKey = privateKey.publicKey

  const transactionId = await new AccountCreateTransaction()
    .setKey(publicKey)
    .setInitialBalance(new Hbar(100)) 
    .execute(client)

  const receipt = await transactionId.getReceipt(client)
  const newAccountId = receipt.accountId

  return res.json({accountId: newAccountId.toString(), privateKey: privateKey.toString(),})
})

fastify.get('/balance', async function handler (request, reply) {
  const balance = await new AccountBalanceQuery()
    .setAccountId(myAccountId)
    .execute(client)

  const usd = await convertHbarToUSD(balance.hbars.to(HbarUnit.Hbar))
  console.log(usd)
  return res.json({'usd': usd, 'hbar': balance.hbars.toString()})
})

fastify.get('/send', async function handler (request, reply) {
  const { recipientAccountId, amount } = request.body;

  const client = Client.forTestnet()
  client.setOperator(myAccountId, myPrivateKey)
  client.setDefaultMaxTransactionFee(new Hbar(100))

  const hbars = await getHbarEquivalent(amount)
  const amountTinybars = Math.round(hbars * 100000000 )
  const amountHbar = Hbar.fromTinybars(amountTinybars)

  try {
    const transactionId = await new TransferTransaction()
      .addHbarTransfer(myAccountId, amountHbar.negated()) 
      .addHbarTransfer(recipientAccountId, amountHbar) 
      .execute(client)

    res.json({transactionId: transactionId.toString()})
  } 
  catch (err) {
    res.json({status: 'ERROR', error: err})
  }
})

// Run the server!
fastify.listen({ port: 3000 }, (err) => {
  if (err) {
    fastify.log.error(err)
    process.exit(1)
  }
})