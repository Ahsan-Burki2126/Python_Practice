#After flipping a coin 10 times you got this result,
result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
heads = 0
tails = 0
for r in result:
    if r=="heads":
        heads = heads + 1
    elif r=="tails":
        tails = tails + 1
print(f"Total Number of Heads:{heads}")        
    