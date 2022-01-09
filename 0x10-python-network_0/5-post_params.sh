#!/bin/bash
# cURL headers send arg in url
curl -d "email=test@gmail.com&subject=I will always be here for PLD" -X POST $1
