import tiktoken

encoding = tiktoken.encoding_for_model("gpt-4o")

tokens = encoding.encode("Argentina will win the world cup again!")
print(len(tokens))
print(tokens)