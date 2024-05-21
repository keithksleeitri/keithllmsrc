echo $1
message = $1
curl http://localhost:11434/api/chat -d '{
  "model": "llama3",
  "messages": [
    { "role": "user", "content": ${message} }
  ]
}'
