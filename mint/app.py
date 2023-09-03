from flask import Flask, request, jsonify
import requests
import w3storage

app = Flask(__name__)

# Use Verbwire API to mint NFT
@app.route('/mint', methods=['GET'])
def mint():
    url = request.args.get('url')
    chain = request.args.get('chain')
    address = request.args.get('address')

    if not url or not chain or not address:
        return jsonify({'error': 'Missing parameters'}), 400

    response = requests.get(url)

    if response.status_code != 200:
        return jsonify({'error': 'Failed to fetch image'}), 500

    with open("image.jpg", "wb") as file:
        file.write(response.content)

    w3 = w3storage.API(token='redacted')
    some_uploads = w3.user_uploads(size=25)
    cid = w3.post_upload(open("image.jpg", "rb"))
    MURL = f"https://ipfs.io/{cid}"

    mint_url = "https://api.verbwire.com/v1/nft/mint/quickMintFromMetadataUrl"

    payload = {
        "allowPlatformToOperateToken": True,
        "chain": chain,
        "metadataUrl": MURL,
        "recipientAddress": address
    }

    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "X-API-Key": "redact"
    }

    response = requests.post(mint_url, json=payload, headers=headers)

    if response.status_code == 200:
        mint_response = response.json()
        block_explorer = mint_response.get('quick_mint', {}).get('blockExplorer', '')
        return jsonify({'block_explorer': block_explorer}), 200
    else:
        return jsonify({'error': 'Failed to mint NFT'}), 500

if __name__ == '__main__':
    app.run(debug=True)