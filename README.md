# EVMElectric

## Inspiration

Electric vehicles are a common argument in the sustainability world. Although they are more environmentally conscious than gasoline vehicles, finding a charging station is often very difficult, and may offset the cost of actually having one in the first place. With our app, we hope to foster the next generation of electric vehicles. 

## What it does

Introducing ElectricEVM, a web application that allows users to crowdsource charging stations using a DAO in order to complete purchases. Users are able to add charging stations, view existing stations on a map or web view, and . 
We used blockchain principles with Hedera, Flow, and Verbwire in our application. We used the Hedera Consensus Service to log payments, the Hedera HBAR wallet using the SDK to validate balances and create crypto payments, and the Hedera File Service (HFS) to upload and download files (from the Fastify API). 
We used Flow's emulator and playground to mint and deploy NFTs (translated from Solidity to Cadence) to the Flow blockchain, using flow wallets, as well as a service to help new users onboard and mint NFTs. Next, Verbwire is used to take this metadata and send it cross chain to other chains, so it can be viewed on Opensea. 

## How we built it

We used Streamlit & Matplotlib for our frontend application, and Node.JS & Typescript for the backend. We used the Verbwire API, Hedera SDK, and Flow Emulator, as well as Hardhat and Alchemy to deploy Solidity scripts. We used Fastify and Flask for the backend endpoints, connecting it together with Axios and `requests`. 

## Challenges we ran into

We had trouble connecting the frontend and backend, as it was our first time getting used to Solidity and Cadence. We also took a lot of time learning about Hedera's services, as well as how to implement heatmaps. We ran into issues using Flow, which we decided to emulate, as well as creating quick micropayments, and validated using HCS. 

## Accomplishments that we're proud of

We're proud of the fact that we created a working demo and backend of an application that uses both blockchain and full stack principles, and it was our first time using Flow. 

## What we learned

We learned so much about Hedera and Flow (which we will continue to use after the hackathon), as well as DAO principles. We learned about connecting full stack applications with tools like HCS and HFS and a very cheap alternative for existing blockchain tools like IPFS and decentralized logging. We learned a lot about how proofs work, and hope to continue using this to improve EVMElectric in the future with zk-proofs and rollups. 

## What's next for EVMElectric

Next, we will add more features, and improve the onboarding process for new users. We hope to onboard the next generation of electric vehicles! 
