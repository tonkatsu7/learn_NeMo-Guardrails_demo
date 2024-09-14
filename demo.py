from nemoguardrails import RailsConfig, LLMRails

config = RailsConfig.from_path("./config")
rails = LLMRails(config)

response = rails.generate(messages=[{
  "role": "user",
  "content": "Hi there, what can you do for me?"
}])
print(response["content"])

response = rails.generate(messages=[{
  "role": "user",
  "content": "Hi there, what can you do for me?"
}])
print(response["content"])