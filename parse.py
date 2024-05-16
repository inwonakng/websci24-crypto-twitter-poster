pos = {
"Overall": "crypto, project, binance, token, signal, blockchain, pump, happen, good, big".split(", "),
"1" : "wallstreetbets, massive, announced, event, really, airdrop, kucoin, join, best, awesome ".split(", "),
"2": " roll, love, security, best, great, kinderinu, world, bridge, join, 10".split(", "),
"3": "roll, best, security, love, amazing, join, great, nft, like, team".split(", "),
"4": "roll, sushi, nice, want, love, great, dodo, let, bridge, security".split(", "),
"5": "best, join, wallstreetbets, love, massive, nft, airdrop, awesome, announced, security".split(", "),
"6": "roll, sushi, security, kinderinu, love, new, bridge, nfts, best, things".split(", "),
}


neg =  {
"Overall": "crypto, security, people, roll, like, hack, ftx, binance, bridge, money".split(", "),
"1": "know, uniswap, want, time, blockchain, social, think, going, need, market".split(", "),
"2": "know, going, shit, token, threat, want, bad, time, scam, think".split(", "),
"3": "know, want, going, time, think, threat, token, need, bad, national".split(", "),
"4": "sushi, bad, shit, malicious, scam, fuck, losers, dumps, hour, trade".split(", "),
"5": "know, want, going, time, blockchain, think, national, need, social, token".split(", "),
"6": "sushi, going, bad, shit, 2022, scam, malicious, know, vulnerability, fuck".split(", "),
}


pos = {
    k: set(v)
    for k,v in pos.items()
}

neg = {
    k: set(v)
    for k,v in neg.items()
}

pos_only = {
    k: v - neg[k]
    for k,v in pos.items()
}

neg_only = {
    k: v - pos[k]
    for k,v in neg.items()
}

print("positive")
for k, v in pos_only:
    print(k, v)

print()
print("negative")
for k, v in pos_only:
    print(k, v)
