deals = []
with open('./data/deals') as f:
    deals = f.readlines()

availed_deals = []
for deal in deals:
    comps = deal.strip().split('::::')
    if comps[-2] == 'DealStatus.AVAILED':
        availed_deals.append(deal.strip())

availed_deals_with_price = []
for deal in availed_deals:
    comps = deal.strip().split('::::')
    price = float(comps[-3])
    if price > 0.0:
        availed_deals_with_price.append(deal.strip())

print len(deals), len(availed_deals), (float(len(availed_deals))/float(len(deals)))*100, (float(len(availed_deals_with_price))/float(len(deals)))*100

for deal in availed_deals_with_price:
    print deal